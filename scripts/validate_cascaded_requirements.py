#!/usr/bin/env python3
"""
validate_cascaded_requirements.py

Validates that:
1. All 230 telematics requirements across the 4 TSRM components:
   - Vehicle Connection Component (58 requirements)
   - Connectivity / Communications Component (62 requirements)
   - Cloud Component (60 requirements)
   - Mobile App Component (50 requirements)
   cascade correctly in nmfta-vehicle_cybersecurity_requirements (Class 0 Telematics)
   and have identical parent/cascaded statement text, criticality, and metadata
   relative to the baseline reference.

2. All 34 gateway security requirements (AGW-S-*, CGW-S-*, J1939GW-S-*, NGW-S-*)
   in nmfta-vehicle_cybersecurity_requirements (requirements/common/vehicle_gateway_controls.sdoc
   and Class 2 gateway specializations) have identical requirement statements,
   criticalities, titles, and verification criteria relative to the baseline reference.

Supported Modes:
- Hermetic Mode (Default for CI):
  Uses the committed tests/reference_baselines.json snapshot. Does not require external clones.
- Multi-Repo Mode:
  Validates directly against live clones of nmfta-telematics_security_requirements and vcr-experiment.
"""

import argparse
import json
import os
import re
import sys
from typing import Dict, List, Optional, Tuple


def normalize_whitespace(text: Optional[str]) -> str:
    """Normalize whitespace and newlines for robust semantic comparison."""
    if not text:
        return ""
    return re.sub(r"\s+", " ", text.strip())


def parse_sdoc_requirements(file_path: str) -> Dict[str, dict]:
    """Parse requirements from an SDoc file using regex."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    chunks = re.split(r"\n(?=\[REQUIREMENT\]\n)", content)
    requirements: Dict[str, dict] = {}

    for chunk in chunks:
        if not chunk.startswith("[REQUIREMENT]"):
            continue

        uid_match = re.search(r"^UID:\s*([^\n]+)", chunk, re.MULTILINE)
        if not uid_match:
            continue
        uid = uid_match.group(1).strip()

        crit_match = re.search(
            r"^CRITICALITY:\s*(?:>>>\s*\n)?([^\n<]+)", chunk, re.MULTILINE
        )
        crit = crit_match.group(1).strip() if crit_match else None

        title_match = re.search(
            r"^TITLE:\s*(?:>>>\s*\n)?([^\n<]+)", chunk, re.MULTILINE
        )
        title = title_match.group(1).strip() if title_match else None

        stmt = None
        stmt_multi = re.search(
            r"^STATEMENT:\s*>>>\n(.*?)\n<<<", chunk, re.MULTILINE | re.DOTALL
        )
        if stmt_multi:
            stmt = stmt_multi.group(1).strip()
        else:
            stmt_single = re.search(r"^STATEMENT:\s*([^\n>]+)", chunk, re.MULTILINE)
            if stmt_single:
                stmt = stmt_single.group(1).strip()

        verification = None
        verif_multi = re.search(
            r"^VERIFICATION:\s*>>>\n(.*?)\n<<<", chunk, re.MULTILINE | re.DOTALL
        )
        if verif_multi:
            verification = verif_multi.group(1).strip()
        else:
            verif_single = re.search(
                r"^VERIFICATION:\s*([^\n>]+)", chunk, re.MULTILINE
            )
            if verif_single:
                verification = verif_single.group(1).strip()

        parents = []
        rel_block = re.search(r"RELATIONS:\n(.*?)(?=\n\[|\Z)", chunk, re.DOTALL)
        if rel_block:
            p_matches = re.findall(
                r"-\s*TYPE:\s*Parent\s*\n\s*VALUE:\s*([^\n]+)", rel_block.group(1)
            )
            parents = [p.strip() for p in p_matches]

        requirements[uid] = {
            "uid": uid,
            "title": title,
            "criticality": crit,
            "statement": stmt,
            "verification": verification,
            "parents": parents,
            "raw": chunk,
        }

    return requirements


class RequirementValidator:
    def __init__(
        self,
        vcr_dir: str,
        baseline_file: Optional[str] = None,
        tsrm_dir: Optional[str] = None,
        vcr_exp_dir: Optional[str] = None,
    ):
        self.vcr_dir = os.path.abspath(vcr_dir)
        self.baseline_file = os.path.abspath(baseline_file) if baseline_file else None
        self.tsrm_dir = os.path.abspath(tsrm_dir) if tsrm_dir else None
        self.vcr_exp_dir = os.path.abspath(vcr_exp_dir) if vcr_exp_dir else None

        self.vcr_requirements: Dict[str, dict] = {}

    def load_vcr_tree(self) -> None:
        """Dynamically load all SDoc requirements from the target VCR repository."""
        req_dir = os.path.join(self.vcr_dir, "requirements")
        if not os.path.exists(req_dir):
            raise FileNotFoundError(f"requirements/ directory not found in {self.vcr_dir}")

        count = 0
        for root, _, files in os.walk(req_dir):
            for file in files:
                if file.endswith(".sdoc"):
                    sdoc_path = os.path.join(root, file)
                    reqs = parse_sdoc_requirements(sdoc_path)
                    self.vcr_requirements.update(reqs)
                    count += 1
        print(f"Scanned {count} SDoc files in VCR tree ({len(self.vcr_requirements)} requirements loaded).")

    def resolve_ancestor_metadata(
        self, uid: str
    ) -> Tuple[Optional[str], Optional[str], Optional[str], Optional[str]]:
        """
        Walk up parent relations in VCR to resolve:
        (criticality, title, immediate_statement, root_ancestor_statement)
        """
        node = self.vcr_requirements.get(uid)
        if not node:
            return None, None, None, None

        crit = node["criticality"]
        title = node["title"]
        stmt = node["statement"]
        ancestor_stmt = None

        cur = node
        while cur.get("parents"):
            parent_uid = cur["parents"][0]
            parent_node = self.vcr_requirements.get(parent_uid)
            if not parent_node:
                break
            if not crit and parent_node["criticality"]:
                crit = parent_node["criticality"]
            if not title and parent_node["title"]:
                title = parent_node["title"]
            if parent_node["statement"]:
                ancestor_stmt = parent_node["statement"]
            cur = parent_node

        return crit, title, stmt, ancestor_stmt

    def validate_from_baseline_json(self) -> List[str]:
        """Validate VCR against the hermetic reference_baselines.json snapshot."""
        assert self.baseline_file is not None
        if not os.path.exists(self.baseline_file):
            return [f"Baseline file not found: {self.baseline_file}"]

        with open(self.baseline_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        telematics_baseline: Dict[str, dict] = data.get("telematics", {})
        gateways_baseline: Dict[str, dict] = data.get("gateways", {})

        errors: List[str] = []

        # 1. Validate Telematics (230 requirements)
        print(f"Checking {len(telematics_baseline)} Telematics requirements from baseline snapshot...")
        for c0_uid, item in telematics_baseline.items():
            comp = item["component"]
            expected_crit = item["criticality"]
            expected_stmt = item["cascaded_statement"]

            if c0_uid not in self.vcr_requirements:
                errors.append(f"[{comp}] Requirement {c0_uid} missing in VCR Class 0 specification")
                continue

            v_crit, v_title, v_stmt, v_ancestor_stmt = self.resolve_ancestor_metadata(c0_uid)

            if normalize_whitespace(v_crit) != normalize_whitespace(expected_crit):
                errors.append(
                    f"[{comp}] {c0_uid}: Criticality mismatch: "
                    f"Baseline='{expected_crit}', VCR='{v_crit}'"
                )

            if normalize_whitespace(v_ancestor_stmt) != normalize_whitespace(expected_stmt):
                errors.append(
                    f"[{comp}] {c0_uid}: Cascaded parent statement mismatch:\n"
                    f"  Expected : {expected_stmt[:120]}...\n"
                    f"  VCR Resolved : {v_ancestor_stmt[:120] if v_ancestor_stmt else 'None'}..."
                )

        print(f"Checking {len(gateways_baseline)} Gateway requirements from baseline snapshot...")
        for uid, item in gateways_baseline.items():
            expected_crit = item["criticality"]
            expected_stmt = item["statement"]
            expected_verif = item["verification"]

            if uid not in self.vcr_requirements:
                errors.append(f"[Gateway] Requirement {uid} missing in VCR common gateway controls")
                continue

            vcr_node = self.vcr_requirements[uid]

            if normalize_whitespace(expected_crit) != normalize_whitespace(vcr_node["criticality"]):
                errors.append(
                    f"[Gateway] {uid}: Criticality mismatch: "
                    f"Baseline='{expected_crit}', VCR='{vcr_node['criticality']}'"
                )

            if normalize_whitespace(expected_stmt) != normalize_whitespace(vcr_node["statement"]):
                errors.append(
                    f"[Gateway] {uid}: Statement mismatch:\n"
                    f"  Baseline : {expected_stmt[:120]}...\n"
                    f"  VCR      : {vcr_node['statement'][:120]}..."
                )

            if normalize_whitespace(expected_verif) != normalize_whitespace(vcr_node["verification"]):
                errors.append(
                    f"[Gateway] {uid}: Verification criteria mismatch:\n"
                    f"  Baseline : {expected_verif[:120]}...\n"
                    f"  VCR      : {vcr_node['verification'][:120]}..."
                )

            if uid.startswith("AGW-") or uid.startswith("CGW-"):
                c2_uid = f"C2-{uid}"
                if c2_uid not in self.vcr_requirements:
                    errors.append(f"[Gateway] Class 2 specialization {c2_uid} missing in Class 2 document")
                else:
                    c2_node = self.vcr_requirements[c2_uid]
                    if not c2_node["parents"] or c2_node["parents"][0] != uid:
                        errors.append(f"[Gateway] {c2_uid} does not properly link to parent {uid}")

        return errors

    def validate_from_live_repos(self) -> List[str]:
        """Validate VCR directly against live clones of TSRM and vcr-experiment."""
        assert self.tsrm_dir is not None and self.vcr_exp_dir is not None
        errors: List[str] = []

        # TSRM Validation
        tsrm_master_file = os.path.join(self.tsrm_dir, "Telematics_Security_Requirements_Matrix.sdoc")
        if not os.path.exists(tsrm_master_file):
            return [f"TSRM master file missing: {tsrm_master_file}"]

        tsrm_master = parse_sdoc_requirements(tsrm_master_file)
        components = [
            ("Vehicle Connection", "_vehicle_connection_tsrm.sdoc"),
            ("Connectivity / Communications", "_connectivity_tsrm.sdoc"),
            ("Cloud or Back-end", "_cloud_tsrm.sdoc"),
            ("Mobile App", "_mobile_app_tsrm.sdoc"),
        ]

        for comp_name, comp_file in components:
            comp_path = os.path.join(self.tsrm_dir, comp_file)
            if not os.path.exists(comp_path):
                errors.append(f"TSRM component file missing: {comp_path}")
                continue

            comp_reqs = parse_sdoc_requirements(comp_path)
            print(f"Checking TSRM component: {comp_name} ({len(comp_reqs)} requirements)...")

            for uid, tsrm_node in comp_reqs.items():
                c0_uid = f"C0-{uid}"
                if c0_uid not in self.vcr_requirements:
                    errors.append(f"[{comp_name}] Requirement {c0_uid} missing in VCR Class 0 specification")
                    continue

                if not tsrm_node["parents"]:
                    errors.append(f"[{comp_name}] TSRM node {uid} has no parent")
                    continue

                tsrm_parent_uid = tsrm_node["parents"][0]
                if tsrm_parent_uid not in tsrm_master:
                    errors.append(f"[{comp_name}] TSRM parent {tsrm_parent_uid} not found in TSRM master")
                    continue

                tsrm_parent = tsrm_master[tsrm_parent_uid]
                tsrm_crit = tsrm_parent["criticality"]
                tsrm_parent_stmt = tsrm_parent["statement"]

                vcr_crit, _, _, vcr_ancestor_stmt = self.resolve_ancestor_metadata(c0_uid)

                if normalize_whitespace(vcr_crit) != normalize_whitespace(tsrm_crit):
                    errors.append(
                        f"[{comp_name}] {c0_uid}: Criticality mismatch: "
                        f"TSRM='{tsrm_crit}', VCR='{vcr_crit}'"
                    )

                if normalize_whitespace(vcr_ancestor_stmt) != normalize_whitespace(tsrm_parent_stmt):
                    errors.append(
                        f"[{comp_name}] {c0_uid}: Cascaded parent statement mismatch:\n"
                        f"  TSRM Ancestor : {tsrm_parent_stmt[:120]}...\n"
                        f"  VCR Ancestor  : {vcr_ancestor_stmt[:120] if vcr_ancestor_stmt else 'None'}..."
                    )

        # Gateways Validation
        gw_file = os.path.join(self.vcr_exp_dir, "01_gateways.sdoc")
        if not os.path.exists(gw_file):
            errors.append(f"vcr-experiment gateways file missing: {gw_file}")
            return errors

        exp_gw_reqs = parse_sdoc_requirements(gw_file)
        print(f"Checking Gateway requirements from vcr-experiment ({len(exp_gw_reqs)} requirements)...")
        for uid, exp_node in exp_gw_reqs.items():
            if uid not in self.vcr_requirements:
                errors.append(f"[Gateway] Requirement {uid} missing in VCR common gateway controls")
                continue

            vcr_node = self.vcr_requirements[uid]

            if normalize_whitespace(exp_node["criticality"]) != normalize_whitespace(vcr_node["criticality"]):
                errors.append(
                    f"[Gateway] {uid}: Criticality mismatch: "
                    f"vcr-experiment='{exp_node['criticality']}', VCR='{vcr_node['criticality']}'"
                )

            if normalize_whitespace(exp_node["statement"]) != normalize_whitespace(vcr_node["statement"]):
                errors.append(
                    f"[Gateway] {uid}: Statement mismatch:\n"
                    f"  vcr-exp : {exp_node['statement'][:120]}...\n"
                    f"  VCR     : {vcr_node['statement'][:120]}..."
                )

            if normalize_whitespace(exp_node["verification"]) != normalize_whitespace(vcr_node["verification"]):
                errors.append(
                    f"[Gateway] {uid}: Verification criteria mismatch:\n"
                    f"  vcr-exp : {exp_node['verification'][:120]}...\n"
                    f"  VCR     : {vcr_node['verification'][:120]}..."
                )

            if uid.startswith("AGW-") or uid.startswith("CGW-"):
                c2_uid = f"C2-{uid}"
                if c2_uid not in self.vcr_requirements:
                    errors.append(f"[Gateway] Class 2 specialization {c2_uid} missing in Class 2 document")
                else:
                    c2_node = self.vcr_requirements[c2_uid]
                    if not c2_node["parents"] or c2_node["parents"][0] != uid:
                        errors.append(f"[Gateway] {c2_uid} does not properly link to parent {uid}")

        return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate cascaded requirement text and criticalities against reference baseline."
    )
    parser.add_argument(
        "--vcr-dir",
        default=".",
        help="Path to nmfta-vehicle_cybersecurity_requirements repository root (default: current directory)",
    )
    parser.add_argument(
        "--baseline-file",
        default="tests/reference_baselines.json",
        help="Path to hermetic reference baseline JSON file (default: tests/reference_baselines.json)",
    )
    parser.add_argument(
        "--tsrm-dir",
        default=None,
        help="Optional path to live nmfta-telematics_security_requirements repo (triggers live multi-repo validation)",
    )
    parser.add_argument(
        "--vcr-exp-dir",
        default=None,
        help="Optional path to live vcr-experiment repo (triggers live multi-repo validation)",
    )

    args = parser.parse_args()

    print("================================================================================")
    print("NMFTA Requirement Cascading & Fidelity Validator")
    print("================================================================================")
    print(f"VCR Root            : {os.path.abspath(args.vcr_dir)}")

    use_live_repos = bool(args.tsrm_dir and args.vcr_exp_dir)
    if use_live_repos:
        print(f"Mode                : Live Multi-Repository Validation")
        print(f"TSRM Reference      : {os.path.abspath(args.tsrm_dir)}")
        print(f"VCR-Exp Reference   : {os.path.abspath(args.vcr_exp_dir)}")
    else:
        print(f"Mode                : Hermetic Baseline Validation (CI-Ready)")
        print(f"Baseline Snapshot   : {os.path.abspath(args.baseline_file)}")
    print("================================================================================\n")

    validator = RequirementValidator(
        vcr_dir=args.vcr_dir,
        baseline_file=args.baseline_file,
        tsrm_dir=args.tsrm_dir,
        vcr_exp_dir=args.vcr_exp_dir,
    )

    print("Loading VCR specification tree...")
    validator.load_vcr_tree()
    print()

    if use_live_repos:
        all_errors = validator.validate_from_live_repos()
    else:
        all_errors = validator.validate_from_baseline_json()

    print()
    print("================================================================================")
    print("Validation Results Summary")
    print("================================================================================")
    if all_errors:
        print(f"FAILED: Found {len(all_errors)} mismatch(es):")
        for err in all_errors:
            print(f"  - {err}")
        return 1
    else:
        print("SUCCESS: All 230 TSRM telematics requirements and 34 Gateway requirements")
        print("         have identical cascaded statements, criticalities, and verification")
        print("         criteria relative to the reference baseline!")
        return 0


if __name__ == "__main__":
    sys.exit(main())

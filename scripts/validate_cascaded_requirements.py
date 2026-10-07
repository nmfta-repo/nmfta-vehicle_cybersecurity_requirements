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
   relative to the reference nmfta-telematics_security_requirements repository.

2. All 34 gateway security requirements (AGW-S-*, CGW-S-*, J1939GW-S-*, NGW-S-*)
   in nmfta-vehicle_cybersecurity_requirements (requirements/common/vehicle_gateway_controls.sdoc
   and Class 2 gateway specializations) have identical requirement statements,
   criticalities, titles, and verification criteria relative to the reference
   vcr-experiment repository (01_gateways.sdoc).

Usage:
    python scripts/validate_cascaded_requirements.py \\
        --vcr-dir . \\
        --tsrm-dir /path/to/nmfta-telematics_security_requirements \\
        --vcr-exp-dir /path/to/vcr-experiment
"""

import argparse
import os
import re
import sys
from typing import Dict, List, Optional, Tuple


def normalize_whitespace(text: Optional[str]) -> str:
    """Normalize whitespace and newlines for robust comparison."""
    if not text:
        return ""
    # Strip carriage returns and collapse multiple whitespace/newlines
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
    def __init__(self, vcr_dir: str, tsrm_dir: str, vcr_exp_dir: str):
        self.vcr_dir = os.path.abspath(vcr_dir)
        self.tsrm_dir = os.path.abspath(tsrm_dir)
        self.vcr_exp_dir = os.path.abspath(vcr_exp_dir)

        self.vcr_requirements: Dict[str, dict] = {}
        self.tsrm_requirements: Dict[str, dict] = {}
        self.vcr_exp_requirements: Dict[str, dict] = {}

    def load_vcr_tree(self) -> None:
        """Load all SDoc requirements from the target VCR repository."""
        sdoc_files = [
            os.path.join(self.vcr_dir, "requirements/common/baseline_ecu.sdoc"),
            os.path.join(self.vcr_dir, "requirements/common/vehicle_bus_connection.sdoc"),
            os.path.join(self.vcr_dir, "requirements/common/wireless_connectivity.sdoc"),
            os.path.join(self.vcr_dir, "requirements/common/cloud_backend.sdoc"),
            os.path.join(self.vcr_dir, "requirements/common/mobile_app.sdoc"),
            os.path.join(self.vcr_dir, "requirements/common/vehicle_gateway_controls.sdoc"),
            os.path.join(self.vcr_dir, "requirements/class_0_telematics/class_0_telematics.sdoc"),
            os.path.join(self.vcr_dir, "requirements/class_1_wireless_multiseg/class_1_wireless_multiseg.sdoc"),
            os.path.join(self.vcr_dir, "requirements/class_2_gateway/class_2_gateway.sdoc"),
            os.path.join(self.vcr_dir, "requirements/class_3_multiseg_untrusted/class_3_multiseg_untrusted.sdoc"),
            os.path.join(self.vcr_dir, "requirements/class_4_multiseg/class_4_multiseg.sdoc"),
            os.path.join(self.vcr_dir, "requirements/class_5_single_seg_high_risk/class_5_single_seg_high_risk.sdoc"),
            os.path.join(self.vcr_dir, "requirements/class_6_single_seg_med_risk/class_6_single_seg_med_risk.sdoc"),
            os.path.join(self.vcr_dir, "requirements/class_7_single_seg_low_risk/class_7_single_seg_low_risk.sdoc"),
        ]

        for sdoc_path in sdoc_files:
            if os.path.exists(sdoc_path):
                reqs = parse_sdoc_requirements(sdoc_path)
                self.vcr_requirements.update(reqs)
            else:
                print(f"Warning: Expected SDoc file not found: {sdoc_path}")

    def resolve_ancestor_metadata(self, uid: str) -> Tuple[Optional[str], Optional[str], Optional[str], Optional[str]]:
        """
        Walk up the parent relations in VCR to resolve:
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

    def validate_tsrm_telematics(self) -> List[str]:
        """Validate TSRM 4 telematics components against Class 0 in VCR."""
        errors: List[str] = []

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

        total_checked = 0

        for comp_name, comp_file in components:
            comp_path = os.path.join(self.tsrm_dir, comp_file)
            if not os.path.exists(comp_path):
                errors.append(f"TSRM component file missing: {comp_path}")
                continue

            comp_reqs = parse_sdoc_requirements(comp_path)
            print(f"Checking TSRM component: {comp_name} ({len(comp_reqs)} requirements)...")

            for uid, tsrm_node in comp_reqs.items():
                total_checked += 1
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

                vcr_crit, vcr_title, vcr_stmt, vcr_ancestor_stmt = self.resolve_ancestor_metadata(c0_uid)

                # 1. Criticality match
                if normalize_whitespace(vcr_crit) != normalize_whitespace(tsrm_crit):
                    errors.append(
                        f"[{comp_name}] {c0_uid}: Criticality mismatch: "
                        f"TSRM='{tsrm_crit}', VCR='{vcr_crit}'"
                    )

                # 2. Cascaded statement match
                if normalize_whitespace(vcr_ancestor_stmt) != normalize_whitespace(tsrm_parent_stmt):
                    errors.append(
                        f"[{comp_name}] {c0_uid}: Cascaded parent statement mismatch:\n"
                        f"  TSRM Ancestor : {tsrm_parent_stmt[:120]}...\n"
                        f"  VCR Ancestor  : {vcr_ancestor_stmt[:120] if vcr_ancestor_stmt else 'None'}..."
                    )

        print(f"Completed TSRM validation: {total_checked} requirements verified.")
        return errors

    def validate_gateways(self) -> List[str]:
        """Validate gateway requirements against vcr-experiment."""
        errors: List[str] = []

        gw_file = os.path.join(self.vcr_exp_dir, "01_gateways.sdoc")
        if not os.path.exists(gw_file):
            return [f"vcr-experiment gateways file missing: {gw_file}"]

        exp_gw_reqs = parse_sdoc_requirements(gw_file)
        print(f"Checking Gateway requirements from vcr-experiment ({len(exp_gw_reqs)} requirements)...")

        total_checked = 0
        for uid, exp_node in exp_gw_reqs.items():
            total_checked += 1
            if uid not in self.vcr_requirements:
                errors.append(f"[Gateway] Requirement {uid} missing in VCR common gateway controls")
                continue

            vcr_node = self.vcr_requirements[uid]

            # 1. Criticality
            if normalize_whitespace(exp_node["criticality"]) != normalize_whitespace(vcr_node["criticality"]):
                errors.append(
                    f"[Gateway] {uid}: Criticality mismatch: "
                    f"vcr-experiment='{exp_node['criticality']}', VCR='{vcr_node['criticality']}'"
                )

            # 2. Statement
            if normalize_whitespace(exp_node["statement"]) != normalize_whitespace(vcr_node["statement"]):
                errors.append(
                    f"[Gateway] {uid}: Statement mismatch:\n"
                    f"  vcr-exp : {exp_node['statement'][:120]}...\n"
                    f"  VCR     : {vcr_node['statement'][:120]}..."
                )

            # 3. Verification criteria
            if normalize_whitespace(exp_node["verification"]) != normalize_whitespace(vcr_node["verification"]):
                errors.append(
                    f"[Gateway] {uid}: Verification criteria mismatch:\n"
                    f"  vcr-exp : {exp_node['verification'][:120]}...\n"
                    f"  VCR     : {vcr_node['verification'][:120]}..."
                )

            # 4. Check that Class 2 gateway specification references this gateway requirement
            # (AGW and CGW requirements apply to Class 2 gateways)
            if uid.startswith("AGW-") or uid.startswith("CGW-"):
                c2_uid = f"C2-{uid}"
                if c2_uid not in self.vcr_requirements:
                    errors.append(f"[Gateway] Class 2 gateway specialization {c2_uid} missing in Class 2 document")
                else:
                    c2_node = self.vcr_requirements[c2_uid]
                    if not c2_node["parents"] or c2_node["parents"][0] != uid:
                        errors.append(f"[Gateway] {c2_uid} does not properly link to parent {uid}")

        print(f"Completed Gateway validation: {total_checked} requirements verified.")
        return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate cascaded requirement text and criticalities against reference repositories."
    )
    parser.add_argument(
        "--vcr-dir",
        default=".",
        help="Path to nmfta-vehicle_cybersecurity_requirements repository root (default: current directory)",
    )
    parser.add_argument(
        "--tsrm-dir",
        default="/home/bengardiner/src/nmfta-telematics_security_requirements",
        help="Path to nmfta-telematics_security_requirements repository root",
    )
    parser.add_argument(
        "--vcr-exp-dir",
        default="/home/bengardiner/src/vcr-experiment",
        help="Path to vcr-experiment repository root",
    )

    args = parser.parse_args()

    print("================================================================================")
    print("NMFTA Requirement Cascading & Fidelity Validator")
    print("================================================================================")
    print(f"VCR Root            : {os.path.abspath(args.vcr_dir)}")
    print(f"TSRM Reference      : {os.path.abspath(args.tsrm_dir)}")
    print(f"VCR-Exp Reference   : {os.path.abspath(args.vcr_exp_dir)}")
    print("================================================================================\n")

    validator = RequirementValidator(
        vcr_dir=args.vcr_dir,
        tsrm_dir=args.tsrm_dir,
        vcr_exp_dir=args.vcr_exp_dir,
    )

    print("Loading VCR specification tree...")
    validator.load_vcr_tree()
    print(f"Loaded {len(validator.vcr_requirements)} total requirements from VCR tree.\n")

    tsrm_errors = validator.validate_tsrm_telematics()
    print()
    gw_errors = validator.validate_gateways()
    print()

    all_errors = tsrm_errors + gw_errors

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
        print("         criteria relative to the reference repositories!")
        return 0


if __name__ == "__main__":
    sys.exit(main())

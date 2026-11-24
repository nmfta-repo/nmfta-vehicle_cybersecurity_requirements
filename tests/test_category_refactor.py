import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIREMENTS = ROOT / "requirements"


def requirement_uids(path):
    return set(re.findall(r"^UID: (.+)$", path.read_text(encoding="utf-8"), re.MULTILINE))


class CategoryRefactorTests(unittest.TestCase):
    def test_terminal_categories_and_class_allocations(self):
        all_requirements = "\n".join(
            path.read_text(encoding="utf-8")
            for path in REQUIREMENTS.rglob("*.sdoc")
        )
        self.assertNotRegex(all_requirements, r"(?m)^UID: (?:C[0-3]-)?VEH-")

        class0 = (REQUIREMENTS / "class_0_telematics/class_0_telematics.sdoc").read_text(
            encoding="utf-8"
        )
        class1 = (REQUIREMENTS / "class_1_wireless_multiseg/class_1_wireless_multiseg.sdoc").read_text(
            encoding="utf-8"
        )
        self.assertIn("UID: C0-COMMS-AC-010", class0)
        self.assertIn("UID: C0-SCP-100", class0)
        self.assertNotIn("UID: C1-COMMS-", class1)
        self.assertNotIn("UID: C0-CLOUD-", class0)
        self.assertNotIn("UID: C0-MOBILE-", class0)
        self.assertFalse((REQUIREMENTS / "common/vehicle_bus_connection.sdoc").exists())

    def test_terminal_requirements_are_in_cascade_baseline(self):
        terminal_uids = (
            requirement_uids(
                REQUIREMENTS / "common/cloud_backend.sdoc"
            )
            | requirement_uids(REQUIREMENTS / "common/mobile_app.sdoc")
        )
        class0_uids = requirement_uids(
            REQUIREMENTS / "class_0_telematics/class_0_telematics.sdoc"
        )
        expected = {
            uid
            for uid in class0_uids
            if uid.startswith("C0-COMMS-")
        } | {"C0-SCP-100"} | terminal_uids

        baseline = json.loads(
            (ROOT / "tests/reference_baselines.json").read_text(encoding="utf-8")
        )["telematics"]
        self.assertEqual(set(baseline), expected)
        self.assertEqual(len(expected), 173)

    def test_new_categories_have_heuristics_and_examples(self):
        cloud = (REQUIREMENTS / "common/cloud_backend.sdoc").read_text(encoding="utf-8")
        mobile = (REQUIREMENTS / "common/mobile_app.sdoc").read_text(encoding="utf-8")

        for document in (cloud, mobile):
            self.assertIn("Applicability heuristic:", document)
            self.assertIn("Examples include", document)

        self.assertIn(
            "Any internet-connected service (and its systems) that interfaces with the truck.",
            cloud,
        )
        self.assertIn("PC-based OEM diagnostic software", mobile)


if __name__ == "__main__":
    unittest.main()

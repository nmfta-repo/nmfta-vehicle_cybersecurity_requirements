# Working Group Guide: Authoring & Using the Requirements Tree

Welcome to the **NMFTA Vehicle Cybersecurity Requirements (VCR)** specification repository! This repository uses [StrictDoc](https://github.com/strictdoc-project/strictdoc) to manage structured cybersecurity requirements for heavy-duty commercial vehicle Electronic Control Units (ECUs) and subsystems.

This guide provides technical contributors and working group members with the information needed to navigate the repository, understand how vehicle classes are structured, author and edit requirements, and test changes locally before submitting Pull Requests (PRs).

---

## 1. Architecture & ECU Classification

Commercial truck architectures partition ECUs into distinct device classes based on network connectivity, gateway capabilities, and risk profile:

| Class | Name | Scope & Examples |
| :--- | :--- | :--- |
| **Class 0** | **Telematics** | WAN-connected devices, ELDs, Fleet Management Information Systems (FMIS), cloud, connectivity, and vehicle bus interfaces. |
| **Class 1** | **Multi-Segment with Wireless** | Units with at least one wireless link (Bluetooth, Wi-Fi, TPMS RF) and vehicle buses (e.g., ABS, Tire Pressure Monitoring, Navigation/Infotainment). |
| **Class 2** | **Vehicle Gateway** | Dedicated network routing and isolation controllers (Central Gateway / CGW, Telematics Interface Gateway). |
| **Class 3** | **Multi-Segment with Untrusted Wired** | Multi-segment controllers connected to untrusted physical lines (OBD/RP1226 ports, trailer bridges) such as MCM, CPC, TCM, SAM CAB. |
| **Class 4** | **Multi-Segment** | Multi-segment controllers where all connected buses are internal and trusted (e.g., Steering Controller FAS, Chassis Controller #2). |
| **Class 5** | **Single-Segment High Risk** | Single-segment controllers identified as high operational risk (e.g., DPF/ACM emission controller, PTO switches, retarders). |
| **Class 6** | **Single-Segment Medium Risk** | Single-segment controllers identified as medium fleet risk (e.g., Suspension ECS/ECAS, Automated Driving FLR/FLC, Key-Lock body controller). |
| **Class 7** | **Single-Segment Low Risk** | Single-segment controllers identified as low fleet risk (e.g., Door Controllers, HVAC, Cab Display, DEF sensors). |

---

## 2. Directory Layout

The repository is organized by class under the `requirements/` directory:

```text
nmfta-vehicle_cybersecurity_requirements/
├── strictdoc_config.py              # Root StrictDoc configuration
├── .github/workflows/publish.yml    # CI workflow for pull requests and main builds
├── scripts/
│   └── export_questionnaires.py     # Exports supplier Excel questionnaires
├── requirements/
│   ├── overview/
│   │   └── 00_overview.sdoc         # Overarching preface, disclaimer, and glossary
│   ├── shared/
│   │   └── grammar.sgra             # Standardized StrictDoc grammar definition
│   ├── class_0_telematics/
│   │   └── class_0_telematics.sdoc  # Master specification for Class 0
│   ├── class_1_wireless_multiseg/
│   │   └── class_1_wireless_multiseg.sdoc
│   ├── class_2_gateway/
│   │   └── class_2_gateway.sdoc     # Master specification for Class 2 (Gateways)
│   ├── class_3_multiseg_untrusted/
│   │   └── class_3_multiseg_untrusted.sdoc
│   ├── class_4_multiseg/
│   │   └── class_4_multiseg.sdoc
│   ├── class_5_single_seg_high_risk/
│   │   └── class_5_single_seg_high_risk.sdoc
│   ├── class_6_single_seg_med_risk/
│   │   └── class_6_single_seg_med_risk.sdoc
│   └── class_7_single_seg_low_risk/
│       └── class_7_single_seg_low_risk.sdoc
└── media/                           # Diagrams and image assets
```

---

## 3. StrictDoc Syntax Cheat Sheet

Each `.sdoc` file adheres to StrictDoc v0.30+ grammar.

### Grammar Import

All document files import the standardized shared grammar at the top of the file:

```sdoc
[DOCUMENT]
TITLE: Class X ... Security Requirements

[GRAMMAR]
IMPORT_FROM_FILE: @vcr_grammar
```

### Free Text / Preamble

Introductory text, rationale, or context sections use `[TEXT]` blocks:

```sdoc
[TEXT]
STATEMENT: >>>
Context and informative descriptions go here using reStructuredText or plain text syntax.
<<<
```

### Sections

Sections must use double brackets (`[[SECTION]]` ... `[[/SECTION]]`):

```sdoc
[[SECTION]]
TITLE: Network Security Controls

[TEXT]
STATEMENT: >>>
This section details ingress and egress network controls.
<<<

...
[[/SECTION]]
```

### Requirement Elements

Requirements are defined with the `[REQUIREMENT]` block:

```sdoc
[REQUIREMENT]
UID: C2-AGW-S-001
TITLE: Conditionally Prevents OTA
CATEGORY: Access Control
CRITICALITY: High
STATEMENT: >>>
The device SHALL prevent Over The Air updates (OTA) (including parameter flash)
from UND to TND, unless explicitly authorized and authenticated.
<<<
COMMENT: >>>
Vendor devices must verify cryptographic signatures prior to staging firmware.
<<<
PUB_REFS: >>>
SAE J3061: Appendix F - VEHICLE LEVEL CONSIDERATIONS, Security Mechanisms, b.
<<<
VERIFICATION: >>>
Bench test attempting unauthorized OTA broadcast on UND and verifying rejection.
<<<
```

### Requirement Relations (Refinement & Traceability)

When a requirement refines or depends on another requirement, specify `RELATIONS`:

```sdoc
[REQUIREMENT]
UID: C2-CGW-S-005b
CRITICALITY: High
STATEMENT: >>>
The Central Gateway SHALL restrict J1939 diagnostic memory access commands.
<<<
RELATIONS:
- TYPE: Parent
  VALUE: C2-AGW-S-007
  ROLE: Refines
```

---

## 4. Local Build & Verification Workflow

Before submitting a Pull Request, verify your changes locally:

### Step 1: Install Dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install strictdoc xlsxwriter
```

### Step 2: Build Documentation (HTML & ReqIF)

```bash
strictdoc export . --formats=html,reqif-sdoc --output-dir docs/
```

- HTML documentation will be generated in `docs/html/index.html`.
- ReqIF interchange format will be generated in `docs/reqif/output.reqif`.

### Step 3: Generate Supplier Questionnaires

```bash
python scripts/export_questionnaires.py . --output-dir docs/html/
```

- Excel workbook `docs/html/vcr_questionnaires.xlsx` will contain separate worksheets for each class, sorted by criticality.

---

## 5. Working Group Contribution Guidelines

1. **UID Discipline**:
   - Every requirement must have a globally unique `UID`.
   - Prefix class-specific requirements with the class identifier (e.g., `C0-*`, `C1-*`, `C2-*`).
2. **Normative Language**:
   - Use standard RFC 2119 keywords (`SHALL`, `SHALL NOT`, `SHOULD`, `MAY`) in the `STATEMENT` field.
3. **Actionable Verification**:
   - Include a concrete, testable procedure in the `VERIFICATION` field so that fleets and test labs can evaluate conformity.
4. **Pull Request Validation**:
   - All PRs trigger the automated GitHub Actions CI workflow (`.github/workflows/publish.yml`), which validates that StrictDoc parsing, HTML generation, ReqIF export, and questionnaire creation succeed with zero errors.

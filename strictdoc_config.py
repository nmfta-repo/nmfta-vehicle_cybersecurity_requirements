from strictdoc.core.project_config import ProjectConfig, ProjectFeature


def create_config() -> ProjectConfig:
    return ProjectConfig(
        project_title="NMFTA Vehicle Cybersecurity Requirements",
        include_doc_paths=[
            "requirements/shared/grammar.sgra",
            "docs/overview.sdoc",
            "requirements/all_common/baseline_ecu.sdoc",
            "requirements/all_common/vehicle_gateway_controls.sdoc",
            "requirements/class_0_telematics/class_0_telematics.sdoc",
            "requirements/class_1_wireless_multiseg/class_1_wireless_multiseg.sdoc",
            "requirements/class_2_gateway/class_2_gateway.sdoc",
            "requirements/class_3_multiseg_untrusted/class_3_multiseg_untrusted.sdoc",
            "requirements/class_4_multiseg/class_4_multiseg.sdoc",
            "requirements/class_5_single_seg_high_risk/class_5_single_seg_high_risk.sdoc",
            "requirements/class_6_single_seg_med_risk/class_6_single_seg_med_risk.sdoc",
            "requirements/class_7_single_seg_low_risk/class_7_single_seg_low_risk.sdoc",
            "requirements/cloud/cloud.sdoc",
            "requirements/mobile/mobile_app.sdoc",
        ],
        grammars={
            "@vcr_grammar": "requirements/shared/grammar.sgra",
        },
        project_features=[
            ProjectFeature.TABLE_SCREEN,
            ProjectFeature.TRACEABILITY_SCREEN,
            ProjectFeature.DEEP_TRACEABILITY_SCREEN,
            ProjectFeature.TRACEABILITY_MATRIX_SCREEN,
            ProjectFeature.SEARCH,
        ],
    )

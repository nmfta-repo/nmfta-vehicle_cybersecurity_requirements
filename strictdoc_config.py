from strictdoc.core.project_config import ProjectConfig, ProjectFeature


def create_config() -> ProjectConfig:
    return ProjectConfig(
        project_title="NMFTA Vehicle Cybersecurity Requirements",
        include_doc_paths=[
            "requirements/**/*.sdoc",
            "requirements/**/*.sgra",
        ],
        grammars={
            "@vcr_grammar": "requirements/shared/grammar.sgra",
        },
        project_features=[
            ProjectFeature.TABLE_SCREEN,
            ProjectFeature.TRACEABILITY_SCREEN,
            ProjectFeature.DEEP_TRACEABILITY_SCREEN,
            ProjectFeature.SEARCH,
        ],
    )

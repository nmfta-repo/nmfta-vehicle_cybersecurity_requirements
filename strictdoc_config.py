from strictdoc.core.project_config import ProjectConfig


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
        project_features=[],
    )

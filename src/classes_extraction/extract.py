import os

from src.classes_extraction.rules import get_rule

def extract(files, project_type, project_path):
    """Extract imports based on project type rules."""
    rule_function = get_rule(project_type)

    all_classes = {}
    for file_path in files:
        dependencies = rule_function(file_path)
        if dependencies:
            all_classes[os.path.relpath(file_path, project_path)] = dependencies

    return all_classes
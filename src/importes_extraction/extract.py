import os

from src.importes_extraction.rules import get_rule

def extract(files, project_type, project_path):
    """Extract imports based on project type rules."""
    rule_function = get_rule(project_type)

    all_dependencies = {}
    for file_path in files:
        dependencies = rule_function(file_path, project_path)
        if dependencies:
            curr_file_path = file_path[: file_path.rfind("\\")+1]
            dependencies = set(os.path.relpath(curr_file_path + d, project_path) for d in dependencies)
            all_dependencies[os.path.relpath(file_path, project_path)] = dependencies

    return all_dependencies
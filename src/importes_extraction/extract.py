import os

from src.importes_extraction.rules import get_rule

def extract(files, project_type, project_path):
    """Extract imports based on project type rules."""
    rule_function = get_rule(project_type)

    all_dependencies = {
        'modules':{},
        'files':{}
    }
    for file_path in files:
        imported_files, imported_modules = rule_function(file_path, project_path)
        if imported_modules:
            all_dependencies['modules'][os.path.relpath(file_path, project_path)] = imported_modules
        if imported_files:
            curr_file_path = file_path[: file_path.rfind("\\")+1]
            imported_files = set(os.path.relpath(curr_file_path + d, project_path) for d in imported_files)
            all_dependencies['files'][os.path.relpath(file_path, project_path)] = imported_files

    return all_dependencies
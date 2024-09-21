import os

def walk_project(project_path):
    """Traverse the project directory and return all files."""
    project_files = []
    for root, dirs, files in os.walk(project_path):
        for file in files:
            project_files.append(os.path.join(root, file))
    return project_files
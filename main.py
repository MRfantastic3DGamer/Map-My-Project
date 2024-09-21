from collections import defaultdict

from src.debugging.debugging import PrettyLog
from src.importes_extraction.extract import extract as get_imports
from src.classes_extraction.extract import extract as get_classes
from src.dependencies_extraction.extract import extract as get_dependencies
from src.parents_extraction.extract import extract as get_parents
from src.walk_project.walk_project import walk_project

def main(project_type, project_path):

    files = walk_project(project_path)

    classes = get_classes(files, project_type, project_path)
    print(classes)
    all_imports = get_imports(files, project_type, project_path)
    imported_files = all_imports['files']
    imported_modules = all_imports['modules']


    all_classes = defaultdict(set)
    class_bodies = defaultdict(str)
    class_dependencies = defaultdict(set)

    for file, found_classes in classes.items():
        for c in found_classes:
            all_classes[file].add(c['class_name'])
            class_bodies[(file, c['class_name'])] = c['body']

    class_parents = get_parents(project_type, classes, all_classes, imported_files)
    class_dependencies = get_dependencies(project_type, classes, all_classes, imported_files)

    print(f'all imports ->')
    PrettyLog(all_imports, '\t')
    print(f'all classes ->')
    PrettyLog(all_classes, '\t')
    print(f'parents for each class ->')
    PrettyLog(class_parents, '\t')
    # print(f'body of the classes ->')
    # PrettyLog(class_bodies, '\t')
    print(f'dependencies for each class ->')
    PrettyLog(class_dependencies, '\t')

if __name__ == '__main__':
    project_type = 'cpp'
    project_path = "D:\\Development\\Projects\\MapMyProject\\Test\\TestFiles"
    main(project_type, project_path)
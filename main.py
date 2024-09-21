from collections import defaultdict

from src.importes_extraction.extract import extract as get_imports
from src.classes_extraction.extract import extract as get_classes
from src.dependencies_extraction.extract import extract as get_dependencies
from src.parents_extraction.extract import extract as get_parents
from src.walk_project.walk_project import walk_project

def main(project_type, project_path):

    # Walk through the project directory
    files = walk_project(project_path)

    classes = get_classes(files, project_type, project_path)
    print(classes)
    all_imports = get_imports(files, project_type, project_path)

    # print(f'all imports ->\n\t', end='')
    # print(*all_imports.items(), sep='\n\t')

    all_classes = defaultdict(set)
    class_bodies = defaultdict(str)
    class_dependencies = defaultdict(set)

    for file, found_classes in classes.items():
        for c in found_classes:
            all_classes[file].add(c['class_name'])
            class_bodies[(file, c['class_name'])] = c['body']

    class_parents = get_parents(project_type, classes, all_classes, all_imports)
    class_dependencies = get_dependencies(project_type, classes, all_classes, all_imports)

    # for file, classes in all_classes.items():
    #     if file in all_imports:
    #         for class_ in classes:
    #             class_key = (file, class_)
    #             imported_files = all_imports[file]
    #             imported_classes = set()
    #             for imported_file in imported_files:
    #                 if imported_file in all_classes:
    #                     imported_classes.add(*all_classes[imported_file])
    #             class_dependencies[class_key] = get_dependencies( imported_classes, class_bodies[class_key])
    #             for p in class_parents[class_key]:
    #                 class_dependencies[class_key].add(p)

    # print(f'all classes -> {all_classes}')
    # print(f'parents for each class -> {class_parents}')
    # print(f'body of the classes -> {class_bodies}')
    print(f'dependencies for each class -> {class_dependencies}')

if __name__ == '__main__':
    project_type = 'cpp'
    project_path = "D:\\Development\\Projects\\MapMyProject\\Test\\TestFiles"
    main(project_type, project_path)
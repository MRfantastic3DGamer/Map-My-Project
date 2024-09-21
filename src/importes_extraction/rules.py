from enum import Enum
import re
from sys import modules

def cpp_rule(file_path, project_path):
    import_regex = '#include.*'
    module_regex1 = '(?<=").*(?=")'
    module_regex2 = '(?<=<).*(?=>)'

    file_module_path = file_path[:file_path.rfind('\\')]

    imported_modules = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            imports = re.findall(import_regex, file.read())
            for im in imports:
                search = re.search(module_regex1, im)
                if search:
                    import_path = file_module_path + '\\' + im[search.start() : search.end()]
                    imported_modules.add(import_path.lstrip(project_path))
                search = re.search(module_regex2, im)
                if search:
                    imported_modules.add(im[search.start() : search.end()])
    except UnicodeDecodeError as e:
        print(f"Error reading file {file_path}: {e}")
    return imported_modules

rules = {
    'cpp': cpp_rule,
}

def get_rule(project_type):
    '''these are only supposed to return the files that are imported into the input file'''
    return rules[project_type]

if __name__ == '__main__':
    test_pera = """
    #import "module1"
    #import "module2"
    """
    test_str = '#import "module"'
    modules = cpp_rule(test_pera, "./")
    print(modules)
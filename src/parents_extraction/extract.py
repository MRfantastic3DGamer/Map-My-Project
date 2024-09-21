from collections import defaultdict

def extract(project_type, classes, all_classes, all_imports):
    class_parents = defaultdict(set)
    print(all_imports)
    for file, found_classes in classes.items():
        for c in found_classes:
            for p in c['parents']:
                for i in all_imports[file]:
                    if p in all_classes[i]:
                        class_parents[(file,c['class_name'])].add((i, p))
    return class_parents
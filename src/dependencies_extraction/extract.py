from collections import defaultdict


def extract(project_type, classes, all_classes, all_imports):
    class_dependencies = defaultdict(set)
    for file, found_classes in classes.items():
        imported_items = set()
        if file in all_imports:
            for i in all_imports[file]:
                if i in all_classes and len(all_classes[i]) > 0:
                    imported_items.add(*set((i, c) for c in all_classes[i]))
        for c in found_classes:
            c_words = set(c['body'].split())
            for i in imported_items:
                if i[1] in c_words:
                    class_dependencies[(file, c['class_name'])].add(i)
    return class_dependencies
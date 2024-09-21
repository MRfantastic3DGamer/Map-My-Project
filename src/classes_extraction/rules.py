import re

def cpp_rule(file_path):
    # Regex pattern to match class definitions
    class_regex = r'class\s.*'
    classes_details = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

            # Find all class definitions
            class_matches = re.findall(class_regex, file_content)

            for match in class_matches:
                match = match.lstrip('class').rstrip('{').strip()

                if ':' in match:
                    class_name_part, parents_part = match.split(':', 1)
                else:
                    class_name_part, parents_part = match, None

                # Get the class name by taking the first word (before any whitespace)
                class_name = class_name_part.split()[0]

                # Process the parents if they exist
                if parents_part:
                    parent_classes = parents_part.split(',')
                    for i, parent in enumerate(parent_classes):
                        parent_classes[i] = parent.strip().split()[1]
                else:
                    parent_classes = []

                # Extract class body by tracking curly braces
                start_index = file_content.index(match) + len(match)
                brace_count = 0
                class_body = []
                inside_class_body = False

                for i in range(start_index, len(file_content)):
                    char = file_content[i]

                    if char == '{':
                        brace_count += 1
                        inside_class_body = True
                    elif char == '}':
                        brace_count -= 1

                    if inside_class_body:
                        class_body.append(char)

                    # When all braces are closed, the class body ends
                    if brace_count == 0 and inside_class_body:
                        break

                # Convert class body list back to string
                class_body = ''.join(class_body).strip()

                # Append class details
                classes_details.append({
                    'class_name': class_name,
                    'parents': parent_classes,
                    'body': class_body
                })

    except UnicodeDecodeError as e:
        print(f"Error reading file {file_path}: {e}")

    return classes_details


rules = {
    'cpp': cpp_rule,
}

def get_rule(project_type):
    return rules[project_type]
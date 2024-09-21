def find_class_end_tab_based(file_content, start_line):
    current_indent = None
    for i, line in enumerate(file_content[start_line:], start=start_line):
        stripped_line = line.strip()

        if not stripped_line or stripped_line.startswith("#"):
            continue  # Skip empty lines and comments

        indent_level = len(line) - len(line.lstrip())

        if current_indent is None:
            current_indent = indent_level  # First line of class body sets the current indent

        if indent_level < current_indent and stripped_line:
            # When indentation decreases and line is non-empty, class ends
            return i - 1

    return len(file_content) - 1  # Return last line if class ends at the file's end

# Usage Example
with open('my_python_file.py', 'r') as f:
    lines = f.readlines()

# Assuming class starts at line 10
last_line = find_class_end_tab_based(lines, 10)
print(f'Last line of class: {last_line}')
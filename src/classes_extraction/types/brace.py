def find_class_end_brace_based(file_content, start_line):
    brace_count = 0
    class_started = False

    for i, line in enumerate(file_content[start_line:], start=start_line):
        stripped_line = line.strip()

        if '{' in stripped_line:
            brace_count += stripped_line.count('{')
            class_started = True

        if '}' in stripped_line:
            brace_count -= stripped_line.count('}')

        if class_started and brace_count == 0:
            return i

    return len(file_content) - 1  # Return last line if class ends at the file's end

# Usage Example
with open('my_cpp_file.cpp', 'r') as f:
    lines = f.readlines()

# Assuming class starts at line 15
last_line = find_class_end_brace_based(lines, 15)
print(f'Last line of class: {last_line}')
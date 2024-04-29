import re
from os.path import exists


def process(minimum_repetition_count, input_file_name, output_file_name, ignore_line_pattern):
    input_lines = get_input_lines(input_file_name)

    output_lines = process_input_lines(input_lines, minimum_repetition_count, ignore_line_pattern)

    write_output_lines(output_file_name, output_lines)


def get_input_lines(input_file_name):
    if not exists(input_file_name):
        print("Input file named \"" + input_file_name + "\" does not exist")
        exit()

    input_file = open(input_file_name, 'r')
    input_lines = input_file.readlines()

    if not input_lines:
        print("Input file named \"" + input_file_name + "\" is empty")
        exit()

    input_lines.sort()
    return input_lines


def process_input_lines(input_lines, minimum_repetition_count, ignore_line_pattern):
    # Set up the output file, create if necessary, overwrite with a fresh output buffer otherwise
    output_lines = []

    # Get the contents of the first line, and set currentTitleCount to 1
    last_line = None
    current_title_count = 0

    for i in range(len(input_lines)):
        current_line = input_lines[i]
        if current_line == last_line:
            current_title_count += 1
        else:
            add_line_to_output(output_lines, current_title_count, minimum_repetition_count,
                               last_line, ignore_line_pattern)
            last_line = current_line
            current_title_count = 1

    add_line_to_output(output_lines, current_title_count, minimum_repetition_count, last_line, ignore_line_pattern)

    return output_lines


def add_line_to_output(output_lines, title_count, title_count_minimum, title, ignore_line_pattern):
    ignore_line_pattern = re.compile(ignore_line_pattern)
    if title_count >= title_count_minimum and not ignore_line_pattern.match(title):
        output_lines.append("{:03d}".format(title_count) + " - " + title)


def write_output_lines(output_file_name, output_lines):
    output_lines.sort()
    output_lines.reverse()

    output_file = open(output_file_name, 'w')
    output_file.writelines(output_lines)
    output_file.close()

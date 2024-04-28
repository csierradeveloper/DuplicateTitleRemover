from os.path import exists


def add_title_to_output(output_lines, title_count, title_count_minimum, title):
    # TODO: delete authors, their lines will be of the form "Marillier, Juliet *"
    # You'd look for a single word, comma space, some text, space, *
    # Use a regex for this
    if title_count >= title_count_minimum:
        output_lines.append("{:03d}".format(title_count) + " - " + title)


def get_input_lines(input_file_name):
    if not exists(input_file_name):
        print("Input file named \"" + input_file_name + "\" does not exist")
        return

    input_file = open(input_file_name, 'r')
    input_lines = input_file.readlines()

    if not input_lines:
        print("Input file named \"" + input_file_name + "\" is empty")

    return input_lines


def write_output_lines(output_file_name, output_lines):
    output_lines.sort()
    output_lines.reverse()

    output_file = open(output_file_name, 'w')
    output_file.writelines(output_lines)
    output_file.close()


def process_input_lines(input_lines, minimum_line_count):
    # Set up the output file, create if necessary, overwrite with a fresh output buffer otherwise
    output_lines = []

    # Get the contents of the first line, and set currentTitleCount to 1
    last_line = input_lines[0]
    current_title_count = 1

    for i in range(1, len(input_lines)):
        current_line = input_lines[i]
        if current_line == last_line:
            current_title_count += 1
        else:
            add_title_to_output(output_lines, current_title_count, minimum_line_count, last_line)
            last_line = current_line
            current_title_count = 1

    add_title_to_output(output_lines, current_title_count, minimum_line_count, last_line)

    return output_lines


def process(minimum_line_count, input_file_name, output_file_name):
    input_lines = get_input_lines(input_file_name)

    output_lines = process_input_lines(input_lines, minimum_line_count)

    write_output_lines(output_file_name, output_lines)

from InputFileProcessor import process


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # TODO: Prompt user for minimum number of duplicate titles to keep
    # Do this in another class, for practice doing that
    minimum_title_count = 4

    input_file_path = "../Input.txt"
    output_file_path = "../Output.txt"

    process(minimum_title_count, input_file_path, output_file_path)

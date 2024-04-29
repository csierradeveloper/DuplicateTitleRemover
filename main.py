from InputFileProcessor import process
from UserInputGetter import get_minimum_repetition_count

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    minimum_repetition_count = get_minimum_repetition_count()

    input_file_path = "Input.txt"
    output_file_path = "Output.txt"

    # This string defines lines that we would remove from the output even if they would otherwise qualify
    ignore_line_pattern = "^.+(, ).+( \*)$"

    process(minimum_repetition_count, input_file_path, output_file_path, ignore_line_pattern)

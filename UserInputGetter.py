def get_minimum_repetition_count():
    minimum_title_count = input("What is the minimum number of times a title must appear?\n")
    if not minimum_title_count.isdigit():
        print("The input must be a positive integer")
        exit()
    return int(minimum_title_count)
#!/usr/bin/env python3


def get_occurrence_to_key_list_dict(input_string, should_include_whitespace):
    key_to_occurrence_dict = {}

    for key in input_string:
        if key in [" ", "\n"]:
            if not should_include_whitespace:
                continue

            if key == " ":
                key = "SPACE"
            elif key == "\n":
                key = "\\n"

        if key in key_to_occurrence_dict:
            key_to_occurrence_dict[key] += 1
        else:
            key_to_occurrence_dict[key] = 1

    occurrence_to_key_list_dict = {}

    for key, occurrence in key_to_occurrence_dict.items():
        if occurrence in occurrence_to_key_list_dict:
            occurrence_to_key_list_dict[occurrence].append(key)
        else:
            occurrence_to_key_list_dict[occurrence] = [key]

    return occurrence_to_key_list_dict


def get_printing_items(sorted_occurrence_key_list_tuple_list):
    total_keys_entered = 0
    longest_occurrence_len = 0
    longest_keys_name_len = 0

    for occurrence, key_list in sorted_occurrence_key_list_tuple_list:
        total_keys_entered += occurrence * len(key_list)
        length_of_occurrence = len(str(occurrence))

        if length_of_occurrence > longest_occurrence_len:
            longest_occurrence_len = length_of_occurrence

        # Store this somewhere so it doesn't have to be computed again
        keys_name = " ".join(key_list)

        length_of_keys_name = len(keys_name)

        if length_of_keys_name > longest_keys_name_len:
            longest_keys_name_len = length_of_keys_name

    return total_keys_entered, longest_occurrence_len, longest_keys_name_len


def print_histogram_and_details(sorted_occurrence_key_list_tuple_list, number_of_characters_for_full_histogram_bar):
    total_keys_entered, longest_occurrence_len, longest_keys_name_len = get_printing_items(sorted_occurrence_key_list_tuple_list)
    repetitions_of_most_used_key = sorted_occurrence_key_list_tuple_list[0][0]

    print()

    for occurrence, key_list in sorted_occurrence_key_list_tuple_list:
        percentage_of_histogram_bar_to_print = occurrence / repetitions_of_most_used_key
        histogram_bar = "*" * int(percentage_of_histogram_bar_to_print * number_of_characters_for_full_histogram_bar)
        keys_name = " ".join(key_list)
        padded_keys_string = str(keys_name).rjust(longest_keys_name_len, " ")
        padded_occurrence_string = str(occurrence).rjust(longest_occurrence_len, " ")

        print(f"{padded_keys_string} | {padded_occurrence_string} | {histogram_bar}")

    print()
    print("Total keys Entered:", total_keys_entered)
    print()


def get_input_string():
    print("1) Input from keyboard")
    print("2) Input from file")
    print()

    try:
        choice = int(input("Choice: "))
    except Exception:
        choice = 0

    print()

    if choice == 1:
        return input("Text: ")
    elif choice == 2:
        file_path = input("File path: ")

        with open(file_path, "r") as file:
            return file.read()


def main():
    print()

    input_string = get_input_string()
    occurrence_to_key_list_dict = get_occurrence_to_key_list_dict(input_string, True)

    if occurrence_to_key_list_dict:
        sorted_occurrence_key_list_tuple_list = sorted(occurrence_to_key_list_dict.items(), key=lambda x: x[0], reverse=True)
        print_histogram_and_details(sorted_occurrence_key_list_tuple_list, 100)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3


def get_occurence_to_key_list_dict(input_string, should_include_spaces=True):
    key_to_occurence_dict = {}

    for key in input_string:
        if key == " ":
            if not should_include_spaces:
                continue

            key = "SPACE"

        if key in key_to_occurence_dict:
            key_to_occurence_dict[key] += 1
        else:
            key_to_occurence_dict[key] = 1

    occurence_to_key_list_dict = {}

    for key, occurence in key_to_occurence_dict.items():
        if occurence in occurence_to_key_list_dict:
            occurence_to_key_list_dict[occurence].append(key)
        else:
            occurence_to_key_list_dict[occurence] = [key]

    return occurence_to_key_list_dict


def get_items_for_printing(sorted_occurence_key_list_tuple_list): # Fix name
    total_keys_entered = 0
    longest_occurence_len = 0
    longest_keys_name_len = 0

    for occurence, key_list in sorted_occurence_key_list_tuple_list:
        total_keys_entered += occurence * len(key_list)
        length_of_occurence = len(str(occurence))

        if length_of_occurence > longest_occurence_len:
            longest_occurence_len = length_of_occurence

        # Store this somewhere so it doesn't have to be computed again
        keys_name = " ".join(key_list)

        length_of_keys_name = len(keys_name)

        if length_of_keys_name > longest_keys_name_len:
            longest_keys_name_len = length_of_keys_name

    return total_keys_entered, longest_occurence_len, longest_keys_name_len


def print_histogram_and_details(sorted_occurence_key_list_tuple_list, number_of_characters_for_full_histogram_bar):
    total_keys_entered, longest_occurence_len, longest_keys_name_len = get_items_for_printing(sorted_occurence_key_list_tuple_list)
    repetitions_of_most_used_key = sorted_occurence_key_list_tuple_list[0][0]

    print()

    for occurence, key_list in sorted_occurence_key_list_tuple_list:
        percentage_of_histogram_bar_to_print = occurence / repetitions_of_most_used_key
        histrogram_bar = "*" * int(percentage_of_histogram_bar_to_print * number_of_characters_for_full_histogram_bar)
        keys_name = " ".join(key_list)
        padded_keys_string = str(keys_name).rjust(longest_keys_name_len, " ")
        padded_occurence_string = str(occurence).rjust(longest_occurence_len, " ")

        print(f"{padded_keys_string} | {padded_occurence_string} | {histrogram_bar}")

    print()
    print("Total key_list Entered:", total_keys_entered)
    print()


def main():
    print()

    input_string = input("Text: ")
    occurence_to_key_list_dict = get_occurence_to_key_list_dict(input_string)

    if occurence_to_key_list_dict:
        sorted_occurence_key_list_tuple_list = sorted(occurence_to_key_list_dict.items(), key=lambda x: x[0], reverse=True)
        print_histogram_and_details(sorted_occurence_key_list_tuple_list, 100)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

from pathlib import Path


def get_character_to_occurrence_dict(input_string, should_include_whitespace):
    character_to_occurrence_dict = {}
    whitespace_character_substitutes = {
        " ": "SPACE",
        "\n": "\\n"
    }

    for character in input_string:
        if character in whitespace_character_substitutes:
            if not should_include_whitespace:
                continue

            character = whitespace_character_substitutes[character]

        if character in character_to_occurrence_dict:
            character_to_occurrence_dict[character] += 1
        else:
            character_to_occurrence_dict[character] = 1

    return character_to_occurrence_dict


def get_occurrence_to_character_list_dict(input_string, should_include_whitespace):
    character_to_occurrence_dict = get_character_to_occurrence_dict(input_string, should_include_whitespace)

    occurrence_to_character_list_dict = {}

    for character, occurrence in character_to_occurrence_dict.items():
        if occurrence in occurrence_to_character_list_dict:
            occurrence_to_character_list_dict[occurrence].append(character)
        else:
            occurrence_to_character_list_dict[occurrence] = [character]

    return occurrence_to_character_list_dict


def get_printing_items(sorted_occurrence_character_list_tuple_list):
    total_characters_entered = 0
    longest_occurrence_len = 0
    longest_character_list_string = 0

    for occurrence, character_list in sorted_occurrence_character_list_tuple_list:
        total_characters_entered += occurrence * len(character_list)
        length_of_occurrence = len(str(occurrence))

        if length_of_occurrence > longest_occurrence_len:
            longest_occurrence_len = length_of_occurrence

        # Store this somewhere so it doesn't have to be computed again
        character_list_string = " ".join(character_list)

        length_of_character_list_string = len(character_list_string)

        if length_of_character_list_string > longest_character_list_string:
            longest_character_list_string = length_of_character_list_string

    return total_characters_entered, longest_occurrence_len, longest_character_list_string


def print_histogram_and_details(sorted_occurrence_character_list_tuple_list, number_of_characters_for_full_histogram_bar):
    total_characters_entered, longest_occurrence_len, longest_character_list_string = get_printing_items(sorted_occurrence_character_list_tuple_list)
    repetitions_of_most_used_character = sorted_occurrence_character_list_tuple_list[0][0]

    print()

    for occurrence, character_list in sorted_occurrence_character_list_tuple_list:
        character_list_string = " ".join(character_list)
        padded_character_list_string = str(character_list_string).rjust(longest_character_list_string, " ")
        padded_occurrence_string = str(occurrence).rjust(longest_occurrence_len, " ")
        percentage_of_histogram_bar_to_print = occurrence / repetitions_of_most_used_character
        histogram_bar = "*" * int(percentage_of_histogram_bar_to_print * number_of_characters_for_full_histogram_bar)

        output = f"{padded_character_list_string} | {padded_occurrence_string} | {histogram_bar}".rstrip()

        print(output)

    print()
    print("Total Characters Entered:", total_characters_entered)
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
        file_path = Path(input("File path (don't use quotes): "))

        with open(file_path, "r") as file:
            return file.read()


def main():
    print()

    input_string = get_input_string()
    occurrence_to_character_list_dict = get_occurrence_to_character_list_dict(input_string, True)

    if occurrence_to_character_list_dict:
        sorted_occurrence_character_list_tuple_list = sorted(occurrence_to_character_list_dict.items(), key=lambda x: x[0], reverse=True)
        print_histogram_and_details(sorted_occurrence_character_list_tuple_list, 100)


if __name__ == "__main__":
    main()

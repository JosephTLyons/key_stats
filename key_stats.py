#!/usr/bin/env python3

key_usage_dict = {}

for character in input():
    if character != "\n":
        if character == " ":
            character = "\" \""

        if character in key_usage_dict:
            key_usage_dict[character] += 1
        else:
            key_usage_dict[character] = 1

sorted_key_usage_dict = sorted(key_usage_dict.items(), key=lambda x: x[1], reverse=True)

print()

total_keys_entered = 0
longest_key_name_len = 0
longest_occurence_len = 0

for x in sorted_key_usage_dict:
    total_keys_entered += x[1]

    length_of_key_name = len(x[0])

    if length_of_key_name > longest_key_name_len:
        longest_key_name_len = length_of_key_name

    length_of_occurence = len(str(x[1]))

    if length_of_occurence > longest_occurence_len:
        longest_occurence_len = length_of_occurence

repetitions_of_most_used_key = sorted_key_usage_dict[0][1]
i = 100;

for x in sorted_key_usage_dict:
    histrogram_text = "*" * int((x[1] / repetitions_of_most_used_key) * i)
    padded_letter = str(x[0]).rjust(longest_key_name_len, " ")
    padded_occurence = str(x[1]).rjust(longest_occurence_len, " ")

    print(padded_letter, "|", padded_occurence, "|", histrogram_text)


print()
print("Total Keys Entered:", total_keys_entered)


# Fix variable names
# Function-ize
# Group characters with same characteristics in one line? (try on separate branch)
    # New dict that maps occurence to alphetized list of characters
    # Key is alphabetized list: [" ", e, r, etc.]
    # Alphabetize groups
    # If this feature isn't done, we should still
# Post on GH

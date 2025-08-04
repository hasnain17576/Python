# string
# This file is part of the Python Standard Library.
# It is subject to the license terms in the LICENSE file found in the root directory of this repository.



name = "string"
print(name)

# multiline string
multiline_string = """This is a
multiline string."""
print(multiline_string)


# single line string
single_line_string = "This is a single line string."
print(single_line_string)
# string with escape characters
string_with_escape = "This is a string with a newline character.\nSee?"
print(string_with_escape)


# string with index
string_with_index = "This is a string with an index."
print(string_with_index[10])
# string with slicing
print(string_with_index[10:16])
# methods in string
print(string_with_index.upper())
print(string_with_index.lower())
print(string_with_index.replace("index", "subscript"))
# string concatenation
another_string = " Concatenated string."
concatenated_string = string_with_index + another_string
print(concatenated_string)
# string formatting
formatted_string = f"{string_with_index} {another_string.strip()}"
print(formatted_string)
# string length
print(len(formatted_string))
# string split
split_string = formatted_string.split()
print(split_string)
# string join
joined_string = " ".join(split_string)
print(joined_string)

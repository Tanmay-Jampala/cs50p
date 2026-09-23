MIN_LENGTH = 2
MAX_LENGTH = 6

def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return (
        has_valid_length(s)
        and starts_with_two_letters(s)
        and has_no_punctuations(s)
        and has_valid_numbers(s)
    )

def has_valid_length(s):
    return MIN_LENGTH <= len(s) <= MAX_LENGTH

def starts_with_two_letters(s):
    return s[:2].isalpha()

def has_no_punctuations(s):
    return s.isalnum()

def has_valid_numbers(s):
    for index, character in enumerate(s):
        if character.isdigit():
            if character == "0":
                return False

            return s[index: ].isdigit()

    return True

main()

VOWELS = "aeiouAEIOU"


def main():
    text = input("Input: ")
    print("Output:", remove_vowels(text))


def remove_vowels(text):
    """Return text with every vowel removed, leaving all else intact."""
    shortened = ""

    for character in text:
        if character not in VOWELS:
            shortened += character

    return shortened


main()
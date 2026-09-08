def main():
    text = input("Input: ")
    print(convert(text))

def convert(word):
    word = word.replace(":)", "🙂")
    word = word.replace(":(", "🙁")
    return word


main()
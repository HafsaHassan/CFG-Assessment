def check_isogram(string_input):
    string_input = string_input.lower()
    letters = set()
    for letter in string_input:
        if letter.isalpha():
            if letter in letters:
                return False
            letters.add(letter)
    return True


print(check_isogram("isogram"))

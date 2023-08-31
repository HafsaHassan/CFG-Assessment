# 2.1 A)

def count_consonants(input_str):
    # To store the unique consonants
    unique_consonants = set()
    # A set of vowels to reference
    vowels = set('aeiouAEIOU')

    # Iterating through each character of input string
    for char in input_str:
        if char.isalpha() and char not in vowels:
            if input_str.count(char) == 1:
                unique_consonants.add(char)

    return len(unique_consonants)


# Test cases:
print("Unique Consonants:", count_consonants("cat"))  # Output 2
print("Unique Consonants:", count_consonants("cataract"))  # Output 1

# 2.1 B)
# Time Complexity:
# Iterating through the input string requires the program to check each character one at a time.
# Therefore, the time complexity for this is O(n). However, checking if the character is a vowel,
# requires checking over a set of vowels, which is small and fixed.
# Therefore, this would be considered O(1). Overall, the time complexity would be O(n).
#
# Space Complexity:
# Since unique consonants are stored in a set, the space complexity for this would be O(n).
# The vowels are sorted in a fixed set, this would be O(1). Overall, the space complexity would be
# O(n).
#
# Assumptions:
# The vowels set is fixed and will have a space complexity of O(1).

# 2.2


def count_squares(x):
    # Base case
    if x == 1:
        return 1
    # Adding squares of numbers starting at 1 until x is reached
    else:
        return x * x + count_squares(x - 1)


# Test cases:
print("Number of squares:", count_squares(2))  # Output 5
print("Number of squares:", count_squares(3))  # Output 14

def is_palindrome(word):
    return recursive_palindrome(word, 0, len(word) - 1)

def recursive_palindrome(word, first_index, last_index):
    if word[first_index] == word[last_index]:
        return True
    elif first_index >= last_index:
        return False
    return recursive_palindrome(word, first_index + 1, last_index - 1)

print(is_palindrome('noon')) #True
print(is_palindrome('dad')) #True
print(is_palindrome('mother')) #True
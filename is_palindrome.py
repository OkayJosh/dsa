def is_palindrome(word):

    # initialized the two pointers
    left, right = 0, len(word) - 1

    while left < right:
        # Move pointer if not pointing to an alpa-numeric character on the left
        while left < right and not word[left].isalnum():
            left +=1

        # Move right pointer if not pointing to alpha-numeric character
        while left < right and not word[right].isalnum():
            right -=1

        # Compare the character at the left and right pointers
        if word[left].lower() != word[right].lower():
            return False

        # Move the pointer towards the center
        left += 1
        right -= 1

    return True

input_string = "A man, a plan, a canal: Panama"
result = is_palindrome(input_string)
print(f"Is the input string a palindrome? {result}")


input_string = "Able was I, ere I saw Elba."
result = is_palindrome(input_string)
print(f"Is the input string a palindrome? {result}")

input_string = "Eva, can I see bees in a cave?"
result = is_palindrome(input_string)
print(f"Is the input string a palindrome? {result}")
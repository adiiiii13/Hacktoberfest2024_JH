def is_palindrome(string):
  """Checks if a given string is a palindrome.

  Args:
    string: The string to check.

  Returns:
    True if the string is a palindrome, False otherwise.
  """

  return string == string[::-1]

# Example usage:
is_palindrome_result = is_palindrome("racecar")
print(is_palindrome_result)  # Output: True

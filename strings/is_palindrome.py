def is_palindrome(s, case_sensitive=False):
    """
    Check if a string is a palindrome.
    
    Args:
        s (str): Input string to check
        case_sensitive (bool, optional): If False, ignores case. Defaults to False.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
        
    Raises:
        ValueError: If input is not a string
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
        
    # Handle empty string or single character
    if len(s) <= 1:
        return True
        
    # Convert to lowercase if case-insensitive
    if not case_sensitive:
        s = s.lower()
    
    # Remove non-alphanumeric characters
    cleaned = ''.join(c for c in s if c.isalnum())
    
    # Check if it reads the same forwards and backwards
    return cleaned == cleaned[::-1]

def is_palindrome_two_pointers(s, case_sensitive=False):
    """
    Check if a string is a palindrome using two pointers.
    
    Args:
        s (str): Input string to check
        case_sensitive (bool, optional): If False, ignores case. Defaults to False.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
        
    Raises:
        ValueError: If input is not a string
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
        
    if not case_sensitive:
        s = s.lower()
    
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1
            
        if s[left] != s[right]:
            return False
            
        left += 1
        right -= 1
        
    return True

if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal: Panama",  # Classic palindrome with punctuation
        "race a car",                       # Not a palindrome
        " ",                                # Whitespace
        "Able was I ere I saw Elba",       # Case-insensitive palindrome
        "12321",                           # Numeric palindrome
        "Was it a car or a cat I saw?",    # Phrase palindrome
        12321,                             # Non-string input (will raise error)
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"Test Case {i}:")
        print(f"Input: {test}")
        
        try:
            print(f"Is palindrome (simple): {is_palindrome(test) if isinstance(test, str) else 'N/A - Not a string'}")
            print(f"Is palindrome (two pointers): {is_palindrome_two_pointers(test) if isinstance(test, str) else 'N/A - Not a string'}")
        except ValueError as e:
            print(f"Error: {e}")
            
        print("-" * 60)

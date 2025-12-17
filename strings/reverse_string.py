def reverse_string(s):
    """
    Reverse a string using string slicing.
    
    Args:
        s (str): Input string to be reversed
        
    Returns:
        str: Reversed string
        
    Raises:
        ValueError: If input is not a string
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[::-1]

def reverse_string_loop(s):
    """
    Reverse a string using a loop.
    
    Args:
        s (str): Input string to be reversed
        
    Returns:
        str: Reversed string
        
    Raises:
        ValueError: If input is not a string
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
        
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

if __name__ == "__main__":
    test_cases = [
        "hello",          # Normal string
        "racecar",        # Palindrome
        "a",              # Single character
        "",               # Empty string
        "Python is fun",  # String with spaces
        123,              # Non-string input (will raise error)
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"Test Case {i}:")
        print(f"Input: {test}")
        
        try:
            print(f"Reversed (slicing): {reverse_string(test) if isinstance(test, str) else 'N/A - Not a string'}")
            print(f"Reversed (loop): {reverse_string_loop(test) if isinstance(test, str) else 'N/A - Not a string'}")
        except ValueError as e:
            print(f"Error: {e}")
            
        print("-" * 40)

def is_balanced(s: str) -> str:
    """
    Перевіряє, чи є послідовність символів-розділювачів симетричною.
    """
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    matching_brackets = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != matching_brackets[char]:
                return "Несиметрично"
            stack.pop()
    
    return "Симетрично" if not stack else "Несиметрично"

def main():
    """
    Головна функція для перевірки симетричності розділювачів у рядку.
    """
    test_strings = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",
        "( 23 ( 2 - 3);",
        "( 11 }",
        "( { [ ] ( ) ( ) { } } } )",  # Додатковий тестовий рядок
        "( { [ ] ( ) ( { } ) } )"     # Додатковий тестовий рядок
    ]
    
    for s in test_strings:
        result = is_balanced(s)
        print(f"'{s}': {result}")

if __name__ == "__main__":
    main()

from collections import deque

def is_palindrome(s: str) -> bool:
    """
    Перевіряє, чи є рядок паліндромом.
    """
    # Видаляємо всі пробіли та приводимо рядок до нижнього регістру
    s = ''.join(s.split()).lower()
    
    # Додаємо всі символи рядка до двосторонньої черги
    d = deque(s)
    
    # Порівнюємо символи з обох кінців черги
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

def main():
    """
    Головна функція для перевірки рядків на паліндром.
    """
    test_strings = [
        "A man a plan a canal Panama",
        "Hello",
        "Radar",
        "Level",
        "Was it a car or a cat I saw",
        "No lemon, no melon"
    ]
    
    for s in test_strings:
        if is_palindrome(s):
            print(f"'{s}' є паліндромом.")
        else:
            print(f"'{s}' не є паліндромом.")

if __name__ == "__main__":
    main()

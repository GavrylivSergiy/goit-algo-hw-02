import queue
import time
import random

# Створити чергу заявок
request_queue = queue.Queue()

def generate_request(request_id):
    """
    Генерує нову заявку і додає її до черги.
    """
    print(f"Генерація заявки: {request_id}")
    request_queue.put(request_id)

def process_request():
    """
    Обробляє заявку з черги, якщо вона не пуста.
    """
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Обробка заявки: {request_id}")
    else:
        print("Черга пуста. Немає заявок для обробки.")

def main():
    """
    Головний цикл програми, що імітує роботу сервісного центру.
    """
    request_id = 1
    try:
        while True:
            if random.choice([True, False]):
                generate_request(request_id)
                request_id += 1

            if random.choice([True, False]):
                process_request()

            # Пауза між операціями
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nПрограма завершена користувачем.")

if __name__ == "__main__":
    main()

import queue as qu
import time
import random
import keyboard
from datetime import datetime

# Списки для випадкової генерації даних
clients = ["Іван Петренко", "Олена Коваль", "Андрій Сидоренко",
            "Марія Іванчук", "Петро Гнатюк", "Наталія Литвин",
            "Сергій Бондар", "Оксана Шевчук"]

services = ["Ремонт телефону", "Консультація", "Налаштування ноутбука",
            "Доставка аксесуарів", "Ремонт принтера",
            "Оновлення програмного забезпечення"]

priorities = ["звичайний", "високий"]

queue = qu.Queue()
request_id = 1


def generate_request():
    request = {
        "id": f"{request_id:06d}",
        "client": random.choice(clients),
        "service": random.choice(services),
        "priority": random.choice(priorities),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return request


def process_request():
    if queue:
        current = queue.get()
        message = f"[ОБРОБКА] Заявка {current['id']} ({current['service']}) від {current['client']}"
    else:
        message = "Черга порожня"
    
    return message


while True:
    request = generate_request()
    queue.put(request)
    print(f"[НОВА ЗАЯВКА] {request}") 
    print(process_request())
    request_id += 1
    time.sleep(3)  # затримка між заявками (3 секунди) 
    
    if keyboard.is_pressed("space"):  # якщо натиснули "пробіл" → вихід, але чогось треба спамити
        print("Програму завершено користувачем.")
        break
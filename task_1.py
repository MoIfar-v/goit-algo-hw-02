import queue as qu
import time
import random
import keyboard
from datetime import datetime
from pynput.keyboard import Listener

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
keyboard_quit = False

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


def keyboard_handler(key):
    global keyboard_quit
    if hasattr(key, 'char') and key.char == 'q':
        keyboard_quit = True

keyboard_listener = Listener(on_press=keyboard_handler)
keyboard_listener.start()

while not keyboard_quit:
    request = generate_request()
    queue.put(request)
    print(f"[НОВА ЗАЯВКА] {request}") 
    print(process_request())
    request_id += 1
    time.sleep(2)  # затримка між заявками (2 секунди)  
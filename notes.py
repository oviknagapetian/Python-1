import json
import os
from datetime import datetime

# Путь к файлу для хранения заметок
NOTES_FILE = "notes.json"

# Проверка существования файла заметок и его загрузка, если он существует
def load_notes():
    try:
        if os.path.exists(NOTES_FILE):
            with open(NOTES_FILE, "r") as file:
                return json.load(file)
        else:
            return []
    except Exception as e:
        print(f"Ошибка при загрузке заметок: {e}")
        return []

# Сохранение заметок в файл
def save_notes(notes):
    try:
        with open(NOTES_FILE, "w") as file:
            json.dump(notes, file, indent=4)
    except Exception as e:
        print(f"Ошибка при сохранении заметок: {e}")

# Создание новой заметки
def create_note():
    title = input("Введите заголовок заметки: ")
    message = input("Введите текст заметки: ")
    timestamp = datetime.now().isoformat()
    note = {"title": title, "message": message, "timestamp": timestamp}
    return note

# Добавление заметки
def add_note():
    try:
        notes = load_notes()
        note = create_note()
        notes.append(note)
        save_notes(notes)
        print("Заметка успешно сохранена.")
    except Exception as e:
        print(f"Ошибка при добавлении заметки: {e}")

# Вывод списка заметок с фильтрацией по дате
def list_notes():
    try:
        notes = load_notes()
        if not notes:
            print("Список заметок пуст.")
            return

        print("Список заметок:")
        for i, note in enumerate(notes, 1):
            print(f"{i}. Заголовок: {note['title']}")
            print(f"   Дата создания: {note['timestamp']}")
            print(f"   Содержание: {note['message']}\n")
    except Exception as e:
        print(f"Ошибка при выводе списка заметок: {e}")

# Редактирование заметки
def edit_note():
    try:
        notes = load_notes()
        if not notes:
            print("Список заметок пуст.")
            return

        list_notes()
        choice = int(input("Выберите номер заметки для редактирования: ")) - 1

        if 0 <= choice < len(notes):
            new_title = input("Введите новый заголовок: ")
            new_message = input("Введите новый текст: ")
            notes[choice]["title"] = new_title
            notes[choice]["message"] = new_message
            notes[choice]["timestamp"] = datetime.now().isoformat()
            save_notes(notes)
            print("Заметка успешно отредактирована.")
        else:
            print("Неверный выбор заметки.")
    except Exception as e:
        print(f"Ошибка при редактировании заметки: {e}")

# Удаление заметки
def delete_note():
    try:
        notes = load_notes()
        if not notes:
            print("Список заметок пуст.")
            return

        list_notes()
        choice = int(input("Выберите номер заметки для удаления: ")) - 1

        if 0 <= choice < len(notes):
            deleted_note = notes.pop(choice)
            save_notes(notes)
            print("Заметка успешно удалена.")
        else:
            print("Неверный выбор заметки.")
    except Exception as e:
        print(f"Ошибка при удалении заметки: {e}")

# Основной цикл приложения
def main():
    try:
        while True:
            print("\nМеню:")
            print("1. Создать новую заметку")
            print("2. Список заметок")
            print("3. Редактировать заметку")
            print("4. Удалить заметку")
            print("5. Выход")
            choice = input("Выберите опцию: ")

            if choice == "1":
                add_note()
            elif choice == "2":
                list_notes()
            elif choice == "3":
                edit_note()
            elif choice == "4":
                delete_note()
            elif choice == "5":
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Пожалуйста, выберите корректную опцию.")
    except KeyboardInterrupt:
        print("\nВыход из программы.")

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox
import json
import os

class TrainingPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Training Planner")

        # Поля ввода
        self.date_label = tk.Label(root, text="Дата (YYYY-MM-DD):")
        self.date_label.pack()
        self.date_entry = tk.Entry(root)
        self.date_entry.pack()

        self.type_label = tk.Label(root, text="Тип тренировки:")
        self.type_label.pack()
        self.type_entry = tk.Entry(root)
        self.type_entry.pack()

        self.duration_label = tk.Label(root, text="Длительность (минуты):")
        self.duration_label.pack()
        self.duration_entry = tk.Entry(root)
        self.duration_entry.pack()

        # Кнопка добавления тренировки
        self.add_button = tk.Button(root, text="Добавить тренировку", command=self.add_training)
        self.add_button.pack()

        # Таблица для отображения тренировок
        self.training_list = tk.Listbox(root)
        self.training_list.pack()

    def add_training(self):
        date = self.date_entry.get()
        training_type = self.type_entry.get()
        duration = self.duration_entry.get()

        # Проверка корректности ввода
        if not self.validate_input(date, training_type, duration):
            return

        training_data = {
            "date": date,
            "type": training_type,
            "duration": int(duration)
        }

        # Добавление в таблицу
        self.training_list.insert(tk.END, f"{training_data['date']} - {training_data['type']} - {training_data['duration']} мин")
        
        # Сохранение в JSON
        self.save_to_json(training_data)

    def validate_input(self, date, training_type, duration):
        if not self.is_valid_date(date):
            messagebox.showerror("Ошибка", "Неверный формат даты. Используйте YYYY-MM-DD.")
            return False
        
        if not duration.isdigit() or int(duration) <= 0:
            messagebox.showerror("Ошибка", "Длительность должна быть положительным числом.")
            return False
        
        return True

    def is_valid_date(self, date):
        try:
            year, month, day = map(int, date.split('-'))
            return year > 0 and 1 <= month <= 12 and 1 <= day <= 31  # Простая проверка
        except ValueError:
            return False

    def save_to_json(self, training_data):
        if os.path.exists('trainings.json'):
            with open('trainings.json', 'r') as file:
                data = json.load(file)
        else:
            data = []

        data.append(training_data)

        with open('trainings.json', 'w') as file:
            json.dump(data, file)

if __name__ == "__main__":
    root = tk.Tk()
    app = TrainingPlanner(root)
    root.mainloop()

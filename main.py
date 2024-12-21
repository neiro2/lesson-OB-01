#Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, deadline):
        self.description = description  # Описание задачи
        self.deadline = deadline        # Срок выполнения
        self.completed = False          # Статус выполнения: по умолчанию задача не выполнена

    def mark_as_completed(self):
        """Отметить задачу как выполненную."""
        self.completed = True

    def __str__(self):
        """Возвращает строковое представление задачи."""
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Описание: {self.description}, Срок: {self.deadline}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []  # Список задач

    def add_task(self, description, deadline):
        """Добавить новую задачу."""
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_completed(self, index):
        """Отметить задачу по заданному индексу как выполненную."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
        else:
            print("Некорректный индекс задачи.")

    def get_pending_tasks(self):
        """Получить список невыполненных задач."""
        return [task for task in self.tasks if not task.completed]

    def show_tasks(self):
        """Вывод всех задач."""
        for index, task in enumerate(self.tasks):
            print(f"Задача {index + 1}: {task}")

# Пример использования
task_manager = TaskManager()
task_manager.add_task("Купить продукты", "2023-11-01")
task_manager.add_task("Закончить проект", "2023-11-05")

# Отметить первую задачу как выполненную
task_manager.mark_task_completed(0)

# Вывести список всех задач
print("Все задачи:")
task_manager.show_tasks()

# Вывести список невыполненных задач
print("\nНевыполненные задачи:")
for task in task_manager.get_pending_tasks():
    print(task)

from .task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        for current_task in self.tasks:
            if current_task.name == new_task.name:
                return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for current_task in self.tasks:
            if current_task.name == task_name:
                current_task.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_tasks = 0
        for t in self.tasks:
            if t.completed:
                self.tasks.remove(t)
                removed_tasks += 1
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        res = f"Section {self.name}:"
        for t in self.tasks:
            res += f'\n{Task.details(t)}'
        return res


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added: ", task)

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task completed: ", task)
        else:
            print("Task not found: ", task)

    def display_tasks(self):
        if self.tasks:
            print("Todo List:")
            for task in self.tasks:
                print("-", task)
        else:
            print("No tasks in the list.")

# Usage example
todo_list = TodoList()

todo_list.add_task("Buy groceries")
todo_list.add_task("Finish homework")
todo_list.add_task("Call mom")

todo_list.display_tasks()

todo_list.complete_task("Finish homework")
todo_list.complete_task("Go for a run")

todo_list.display_tasks()

class User():
    def __init__(self, name):
        self.name = name
        self.tasks = []
        
        
    def add_task(self, task):
        self.tasks.append(task)
        
        
    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            
            
    def display_tasks(self):
        print("Username: ", self.name)
        for task in self.tasks:
            print("Title", task.title)
            print("Description", task.description)
            print("Completed", task.is_completed)
            print()
            


class Task():
    def __init__(self, title):
        self.name = title
        self.description = ""
        self.is_completed = False
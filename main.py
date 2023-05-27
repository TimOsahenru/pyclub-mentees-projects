class Task():
    def __init__(self, title):
        self.title = title
        self.description = ""
        self.is_completed = False
        
        
        
class User():
    def __init__(self, username):
        self.username = username
        self.tasks = []
        
        
    def add_tasks(self, task):
        self.tasks.append(task)
        
        
    def update_tasks(self, task, new_task):
        if task in self.tasks:
            index_task = self.tasks.index(task)
            self.tasks[index_task] = new_task
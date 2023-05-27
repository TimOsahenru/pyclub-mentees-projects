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
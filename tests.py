import unittest
from main import Task, User


class TestTask(unittest.TestCase):
    def test_task(self):
        task = Task("title")
        self.assertEqual(task.title, "title")
        
        
    def test_description(self):
        task = Task("title")
        self.assertEqual(task.description, "")
        self.assertEqual(len(task.description), 0)
        
        
    def test_complete_status(self):
        task = Task("title")
        self.assertFalse(task.is_completed)
        
        
        
class TestUser(unittest.TestCase):
    
    def test_username(self):
        user = User("tim")
        self.assertEqual(user.username, "tim")
        
        
    def test_tasks(self):
        user = User("tim")
        self.assertEqual(user.tasks, [])
        self.assertEqual(len(user.tasks), 0)
        
        
        
        
if __name__ == "__main__":
    unittest.main()
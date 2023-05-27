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
        
        
    def test_add_tasks(self):
        user = User("tim")
        task_1 = Task("task 1")
        task_2 = Task("task 2")
        
        user.add_tasks(task_1)
        user.add_tasks(task_2)
        
        self.assertEqual(len(user.tasks), 2)
        self.assertIn(task_1, user.tasks)
        self.assertIn(task_2, user.tasks)
        
        
          
    def test_update_task(self):
        user = User("tim")
        task_1 = Task("task 1")
        task_2 = Task("task 2")
        
        user.add_tasks(task_1)
        user.add_tasks(task_2)
        
        new_task = Task("task 3")
        
        user.update_tasks(task_1, new_task)
        
        self.assertNotIn(task_1, user.tasks)
        self.assertIn(new_task, user.tasks)
        self.assertEqual(len(user.tasks), 2)
        
        
    def test_delete(self):
        user = User("tim")
        task_1 = Task("task 1")
        task_2 = Task("task 2")
        
        user.add_tasks(task_1)
        user.add_tasks(task_2)
        
        user.delete_tasks(task_1)
        
        self.assertEqual(len(user.tasks), 1)
        self.assertIn(task_2, user.tasks)
        
        
        
if __name__ == "__main__":
    unittest.main()
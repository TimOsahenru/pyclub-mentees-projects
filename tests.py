import unittest
from main import Task


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
        
        
        
if __name__ == "__main__":
    unittest.main()
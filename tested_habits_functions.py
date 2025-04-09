import unittest
import os
import json
from habits import Habit, save_habits, load_habits
from analytics import view_analytics, view_streaks
from io import StringIO
import sys

class TestHabitFunctions(unittest.TestCase):

    def setUp(self):
        self.test_file = "habits.json"
        self.habit1 = Habit("Run", "Run 5km", "daily", 2, 5, 10, 0)
        self.habit2 = Habit("Read", "Read 10 pages", "weekly", 1, 3, 7, 1)
        save_habits([self.habit1, self.habit2])

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_creation(self):
        habits = load_habits()
        self.assertEqual(habits[0].name, "Run")
        self.assertEqual(habits[1].description, "Read 10 pages")

    def test_mark_complete(self):
        habits = load_habits()
        habits[0].mark_complete()
        self.assertEqual(habits[0].current_streak, 3)
        self.assertEqual(habits[0].completed_goals, 11)

    def test_reset_streak(self):
        habits = load_habits()
        habits[1].reset_streak()
        self.assertEqual(habits[1].current_streak, 0)

    def test_save_and_load(self):
        habits = load_habits()
        save_habits(habits)
        reloaded = load_habits()
        self.assertEqual(reloaded[1].name, "Read")

    def test_delete_habit(self):
        habits = load_habits()
        habits.pop(0)
        save_habits(habits)
        reloaded = load_habits()
        self.assertEqual(len(reloaded), 1)
        self.assertEqual(reloaded[0].name, "Read")

    def test_view_analytics_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        view_analytics()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("Total Current Streaks", output)
        self.assertIn("Total Completed Goals", output)

    def test_view_streaks_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        view_streaks()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("Run", output)
        self.assertIn("Read", output)

if __name__ == '__main__':
    unittest.main()

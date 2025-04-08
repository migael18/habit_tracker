import json
from habits import Habit, load_habits, save_habits

# Define some mock data to simulate habits
mock_habits_data = [
    {
        "name": "Drink Water",
        "description": "Drink 2 liters of water every day",
        "frequency": "daily",
        "current_streak": 5,
        "longest_streak": 7,
        "completed_goals": 10,
        "pending_goals": 2
    },
    {
        "name": "Exercise",
        "description": "Exercise for 30 minutes daily",
        "frequency": "daily",
        "current_streak": 3,
        "longest_streak": 4,
        "completed_goals": 6,
        "pending_goals": 1
    },
    {
        "name": "Read Book",
        "description": "Read at least 10 pages daily",
        "frequency": "daily",
        "current_streak": 10,
        "longest_streak": 12,
        "completed_goals": 15,
        "pending_goals": 0
    },
    {
        "name": "Meditate",
        "description": "Meditate for 10 minutes daily",
        "frequency": "daily",
        "current_streak": 7,
        "longest_streak": 7,
        "completed_goals": 14,
        "pending_goals": 0
    }
]

# Function to save mock habits to a JSON file
def save_mock_habits():
    with open('habits.json', 'w') as f:
        json.dump(mock_habits_data, f, indent=4)

# Load habits function (adjust this if needed)
def load_mock_habits():
    try:
        with open('habits.json', 'r') as f:
            data = json.load(f)
            return [Habit.from_dict(habit) for habit in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Testing function
def test_habits():
    # Save mock habits to file
    save_mock_habits()

    # Load the habits and perform the test
    habits = load_mock_habits()

    print("\n--- Testing Habit Data ---")
    for habit in habits:
        print(f"{habit.name} - Streak: {habit.current_streak}, Longest Streak: {habit.longest_streak}, Completed Goals: {habit.completed_goals}, Pending Goals: {habit.pending_goals}")

    # Test Analytics Calculation
    total_streaks = sum(habit.current_streak for habit in habits)
    total_completed_goals = sum(habit.completed_goals for habit in habits)
    total_pending_goals = sum(habit.pending_goals for habit in habits)
    longest_streak = max((habit.longest_streak for habit in habits), default=0)

    print("\n--- Habit Analytics ---")
    print(f"Total Current Streaks: {total_streaks}")
    print(f"Total Completed Goals: {total_completed_goals}")
    print(f"Total Pending Goals: {total_pending_goals}")
    print(f"Longest Streak: {longest_streak}")

# Run the test
if __name__ == "__main__":
    test_habits()

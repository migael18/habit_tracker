import json


class Habit:
    def __init__(self, name, description, frequency, current_streak=0, longest_streak=0, completed_goals=0, pending_goals=0):
        self.name = name
        self.description = description
        self.frequency = frequency
        self.current_streak = current_streak
        self.longest_streak = longest_streak
        self.completed_goals = completed_goals
        self.pending_goals = pending_goals

    def mark_complete(self):
        self.current_streak += 1
        if self.current_streak > self.longest_streak:
            self.longest_streak = self.current_streak
        self.completed_goals += 1
        self.pending_goals = max(0, self.pending_goals - 1)

    def reset_streak(self):
        self.current_streak = 0

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "frequency": self.frequency,
            "current_streak": self.current_streak,
            "longest_streak": self.longest_streak,
            "completed_goals": self.completed_goals,
            "pending_goals": self.pending_goals
        }

    @staticmethod
    def from_dict(data):
        return Habit(
            name=data["name"],
            description=data["description"],
            frequency=data["frequency"],
            current_streak=data.get("current_streak", 0),
            longest_streak=data.get("longest_streak", 0),
            completed_goals=data.get("completed_goals", 0),
            pending_goals=data.get("pending_goals", 0)
        )


def load_habits():
    try:
        with open("habits.json", "r") as file:
            data = json.load(file)
            return [Habit.from_dict(habit) for habit in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_habits(habits):
    with open("habits.json", "w") as file:
        json.dump([habit.to_dict() for habit in habits], file, indent=4)

def add_habit():
    name = input("Enter habit name: ")
    description = input("Enter habit description: ")
    frequency = input("Enter frequency (daily/weekly): ").strip().lower()


    if frequency not in ["daily", "weekly"]:
        print("Invalid frequency! Choose either 'daily' or 'weekly'.")
        return

    habits = load_habits()
    new_habit = Habit(name, description, frequency)
    habits.append(new_habit)
    save_habits(habits)
    print(f"Habit '{name}' added successfully!")


def list_habits():
    habits = load_habits()
    if not habits:
        print("No habits found.")
        return
    print("\n--- Habit List ---")
    for i, habit in enumerate(habits, start=1):
        print(f"{i}. {habit.name} - {habit.frequency} - Current Streak: {habit.current_streak}")


def mark_complete():
    habits = load_habits()
    if not habits:
        print("No habits to mark as complete.")
        return

    list_habits()
    try:
        choice = int(input("Select the number of the habit to mark as complete: ")) - 1
        if 0 <= choice < len(habits):
            habits[choice].mark_complete()
            save_habits(habits)
            print(f"Habit '{habits[choice].name}' marked as complete!")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_habit():
    habits = load_habits()
    if not habits:
        print("No habits to delete.")
        return

    list_habits()
    try:
        choice = int(input("Select the number of the habit to delete: ")) - 1
        if 0 <= choice < len(habits):
            deleted_habit = habits.pop(choice)
            save_habits(habits)
            print(f"Habit '{deleted_habit.name}' deleted successfully!")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")

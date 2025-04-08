import click
from habits import add_habit, list_habits, mark_complete, delete_habit
from analytics import view_streaks, view_analytics


def main_menu():
    while True:
        print("\n📌 Welcome to the Habit Tracker! Choose an option:\n")
        print("1️⃣ Add a Habit")
        print("2️⃣ List Habits")
        print("3️⃣ Mark Habit as Complete")
        print("4️⃣ View Streaks")
        print("5️⃣ View Analytics")
        print("6️⃣ Delete a Habit")
        print("7️⃣ Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            add_habit()
        elif choice == "2":
            list_habits()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            view_streaks()
        elif choice == "5":
            view_analytics()
        elif choice == "6":
            delete_habit()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()

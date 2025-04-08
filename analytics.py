from habits import load_habits

# View Analytics


def view_analytics():
    habits = load_habits()
    total_streaks = sum(habit.current_streak for habit in habits)
    total_completed_goals = sum(habit.completed_goals for habit in habits)
    total_pending_goals = sum(habit.pending_goals for habit in habits)    
    longest_streak = max((habit.longest_streak for habit in habits), default=0)

    print("\n--- Habit Analytics ---")
    print(f"Total Current Streaks: {total_streaks}")
    print(f"Total Completed Goals: {total_completed_goals}")
    print(f"Total Pending Goals: {total_pending_goals}")
    print(f"Longest Streak: {longest_streak}")

# View Current Streaks


def view_streaks():
    habits = load_habits()
    print("\n--- Current Streaks ---")
    for habit in habits:
        print(f"{habit.name}: {habit.current_streak} days")

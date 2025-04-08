
import json
import click
import os

# File to store habits
HABITS_FILE = "habits.json"

# Function to load habits from file


def load_habits():
    if os.path.exists(HABITS_FILE):
        with open(HABITS_FILE, "r") as file:
            return json.load(file)
    return []


# Function to save habits to file
def save_habits(habits):
    with open(HABITS_FILE, "w") as file:
        json.dump(habits, file, indent=4)


@click.group()
def cli():
    """Habit Tracking App"""
    pass


@click.command()
@click.argument("name")
@click.argument("frequency")
def add_habit(name, frequency):
    """Add a new habit"""
    habits = load_habits()
    # Ensure each habit starts with an empty "completed" list
    habits.append({"name": name, "frequency": frequency, "completed": []})
    save_habits(habits)
    click.echo(f"Habit '{name}' added with frequency '{frequency}' and completion tracking.")


@click.command()
@click.argument("name")
def complete_habit(name):
    """Mark a habit as completed"""
    habits = load_habits()
    for habit in habits:
        if habit["name"] == name:
            habit["completed"].append("today") # Placeholder for actual date tracking
            save_habits(habits)
            click.echo(f"Habit '{name}' marked as completed.")
            return
    click.echo(f"Habit '{name}' not found.")


@click.command()
def list_habits():
    """Show all habits"""
    habits = load_habits()
    if not habits:
        click.echo("No habits found.")
    else:
        for habit in habits:
            completed_count = len(habit["completed"]) # Count completed instances
            click.echo(f"{habit['name']} - {habit['frequency']} - Completed: {completed_count} times")


# Add commands to CLI
cli.add_command(add_habit)
cli.add_command(complete_habit)
cli.add_command(list_habits)

if __name__ == "__main__":
    cli()

import os

FILENAME = "notes_v2.txt"

ADD = "1"
VIEW = "2"
DELETE = "3"
EXIT = "4"

def ensure_file_exists():
    """Ensure notes file exists before any operation"""
    if not os.path.exists(FILENAME):
        open(FILENAME, "w").close()

def get_user_choice(prompt, valid_choices):
    """Get validated user input"""
    choice = input(prompt)
    while choice not in valid_choices:
        print("Invalid choice. Please try again.")
        choice = input(prompt)
    return choice

def add_note(note):
    """Add note to file"""
    with open(FILENAME, "a") as file:
        file.write(note + "\n")
    print("Note added successfully.")

def view_notes():
    """Display all saved notes"""
    with open(FILENAME, "r") as file:
        notes = file.readlines()
        if notes:
            print("\nYour notes:")
            for idx, line in enumerate(notes, 1):
                print(f"{idx}. {line.strip()}")
        else:
            print("No notes found.")

def delete_note(line_number):
    """Delete note by line number"""
    with open(FILENAME, "r") as file:
        notes = file.readlines()
    if 1 <= line_number <= len(notes):
        deleted = notes.pop(line_number - 1)
        with open(FILENAME, "w") as file:
            file.writelines(notes)
        print(f"Deleted note: {deleted.strip()}")
    else:
        print("Invalid line number.")

# Ensure file exists at start
ensure_file_exists()

while True:
    print("\n==== Personal Notes App ====")
    print(f"{ADD}. Add Note")
    print(f"{VIEW}. View Notes")
    print(f"{DELETE}. Delete Note")
    print(f"{EXIT}. Exit")

    choice = get_user_choice("Enter choice (1-4): ", [ADD, VIEW, DELETE, EXIT])

    if choice == ADD:
        note = input("Enter note: ")
        add_note(note)
    elif choice == VIEW:
        view_notes()
    elif choice == DELETE:
        try:
            line_number = int(input("Enter note number to delete: "))
            delete_note(line_number)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == EXIT:
        print("Goodbye!")
        break

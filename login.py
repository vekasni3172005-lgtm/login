# Student Registration System (Main Branch)

students = []

def register_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    students.append({
        "roll_no": roll_no,
        "name": name
    })
    print("Student registered successfully!\n")

def view_students():
    if not students:
        print("No students registered.\n")
        return

    print("\nRegistered Students:")
    for s in students:
        print(f"Roll No: {s['roll_no']}, Name: {s['name']}")
    print()

def menu():
    while True:
        print("==== Student Registration System ====")
        print("1. Register Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Try again.\n")
           
            # Simple Login Feature

def login(username, password):
    if username == "admin" and password == "admin123":
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False


if __name__ == "__main__":
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    login(user, pwd)


menu()
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def show_details(self):
        print("Name:",self.name)
        print("Marks:",self.marks)
    def update_marks(self,new_marks):
        self.marks = new_marks
        print("Marks updated successfully.")
student = None
while True:
    print("\nSTUDENT OOP MANAGER")
    print("1. Add Student")
    print("2. Show Details")
    print("3. Update Marks")
    print("4. Exit")
    choice = int(input("Enter choice:"))
    if choice == 1:
        name = int(input("Enter name:"))
        marks = int(input("Enter marks:"))
        student = Student(name,marks)
        print("Student added successfully.")
    elif choice == 2:
        if student is None:
            print("No student added yet.")
        else:
            student.show_details()
    elif choice == 3:
        if student is None:
            print("No student added yet.")
        else:
            new_marks = int(input("Enter new marks:"))
            student.update_marks(new_marks)
    elif choice == 4:
        print("Program closed.")
        break
    else:
        print("Invalid choice.")
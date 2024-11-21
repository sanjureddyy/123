class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def calculate_average(self):
        total_grades = 0
        count = 0
        for subject, grades in self.grades.items():
            total_grades += sum(grades)
            count += len(grades)
        return total_grades / count if count != 0 else 0

    def get_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def display_grades(self):
        print(f"Grades for {self.name}:")
        for subject, grades in self.grades.items():
            print(f"{subject}: {grades}")
        average = self.calculate_average()
        letter_grade = self.get_letter_grade(average)
        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")

def main():
    student = Student(input("Enter student name: "))
    while True:
        print("\n1. Add Grade")
        print("2. Display Grades")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            student.add_grade(subject, grade)
        elif choice == '2':
            student.display_grades()
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

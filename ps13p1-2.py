# Problem 1: Employee Class with Bonus Calculation
class Employee:
    def __init__(self, first_name, last_name, salary):
        # Initialize employee details
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    # Method to compute bonus based on a given bonus rate
    def compute_bonus(self, bonus_rate):
        bonus = self.salary * bonus_rate  # Calculate bonus
        return bonus


# Problem 2: Student Class with Tuition Calculation
class Student:
    def __init__(self, first_name, last_name, district_code, enrolled_credits):
        # Initialize student's details
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.enrolled_credits = enrolled_credits

    # Method to compute tuition based on district code and enrolled credits
    def compute_tuition(self):
        # Tuition rate depends on the district code
        if self.district_code == "I":
            tuition = self.enrolled_credits * 250  # In-district rate
        else:
            tuition = self.enrolled_credits * 500  # Out-of-district rate
        return tuition


# Test Problem 1: Employee Class
# Create an Employee object
employee = Employee("John", "Doe", 50000)

# Ask the user for the bonus rate (as a decimal)
bonus_rate = float(input("Enter the bonus rate (as a decimal, e.g., 0.10 for 10%): "))

# Calculate the bonus using the compute_bonus method
bonus = employee.compute_bonus(bonus_rate)

# Display the employee's bonus
print(f"\nEmployee {employee.first_name} {employee.last_name} with salary ${employee.salary} gets a bonus of: ${bonus:.2f}")


# Test Problem 2: Student Class
# Create a Student object
student = Student("Alice", "Smith", "I", 15)

# Calculate the tuition using the compute_tuition method
tuition = student.compute_tuition()

# Display the tuition owed
print(f"\nStudent {student.first_name} {student.last_name}, District Code: {student.district_code}, "
      f"Enrolled Credits: {student.enrolled_credits} - Tuition Owed: ${tuition:.2f}")

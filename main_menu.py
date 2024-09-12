from crud_operations import(
    register, Login, update_detail, delete_employee, read_all, read_employee
)

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Login")
        print("2. Register")
        print("3. Read All Employee Name and ID")
        print("4. Read Specific Employee")
        print("5. Exit")

        choice = input("Enter your Choice:")

        if choice == "1":
            Employee_ID = input("Enter your Employee ID: ")
            password = input("Enter your Password: ")
            employee = Login(Employee_ID, password)
            if employee:
                print(f"Welcome {employee[1]}")
                login_menu(Employee_ID)
            else:
                print("Incorrect details")
        
        elif choice == "2":
            name = input("Enter Employee Name: ")
            address = input("Enter Employee Address: ")
            contact = input("Enter Employee Contact: ")
            password = input("Enter Password: ")
            register(name, address, contact, password)
        elif choice == "3":
            employees = read_all()
            print("\nRegistered Employees:")
            for emp in employees:
                print(f"ID: {emp[0]}, Name: {emp[1]}")
        elif choice == "4":
            Employee_ID = int(input("Enter your Employee ID: "))
            employee = read_employee(Employee_ID)
            if employee:
                print(f"Employee ID: {employee[0]}")
                print(f"Employee Name: {employee[1]}")
                print(f"Address: {employee[2]}")
                print(f"Contact: {employee[3]}")
                print(f"Password: {employee[4]}")
                # print(f"Employee Details: ID: {employee[0]}, Name: {employee[1]}, Address: {employee[2]}, Contact: {employee[3]}, password: {employee[4]}")
                # print(f"Employee Details: ID: {employee[0]}, Name: {employee[1]}, Address: {employee[2]}, Contact: {employee[3]}")

            else:
                print("Employee not found!")
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def login_menu(Employee_ID):
    while True:
        print("\nLogin Menu:")
        print("1. Update Employee Details")
        print("2. Delete Your Details")
        print("3. Logout")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("\nWhich detail would you like to update?")
            print("1. Name")
            print("2. Address")
            print("3. Contact")
            print("4. Password")
            update_choice = input("Enter your choice: ")
            
            if update_choice == "1":
                new_value = input("Enter new name: ")
                update_detail(Employee_ID, "Employee_Name", new_value)
            elif update_choice == "2":
                new_value = input("Enter new address: ")
                update_detail(Employee_ID, "Address", new_value)
            elif update_choice == "3":
                new_value = input("Enter new contact: ")
                update_detail(Employee_ID, "Contact", new_value)
            elif update_choice == "4":
                new_value = input("Enter new password: ")
                update_detail(Employee_ID, "PASSWORD", new_value)
            else:
                print("Invalid choice.")

        elif choice == "2":
            confirm = input("Are you sure you want to delete your details? (y/n): ")
            if confirm.lower() == 'y':
                delete_employee(Employee_ID)
                break
        
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
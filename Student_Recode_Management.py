import mysql.connector
import time

class StudentManagementSystem:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="<>",  
            database="data2"   
        )
        self.cursor = self.db.cursor()
        self.create_Table()  

    def create_Table(self):
        create = """
            CREATE TABLE IF NOT EXISTS students (
                Roll_no INT PRIMARY KEY,
                Name VARCHAR(50),
                Age INT,
                Course VARCHAR(50)
            )
        """
        self.cursor.execute(create)
        self.db.commit()
        print(" Table 'students' created (if not exists).")

    def add_student(self):
        try:
            Roll_no = int(input('Enter Roll No: '))
            Name = input("Enter Name: ")
            Age = int(input("Enter Age: "))
            Course = input("Enter Course: ")

            query = "INSERT INTO students (Roll_no, Name, Age, Course) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (Roll_no, Name, Age, Course))
            self.db.commit()
            print(" Student Added Successfully")
        except Exception as e:
            print(f" Error: {e}")

    def display_students(self):
        self.cursor.execute("SELECT * FROM students")
        rows = self.cursor.fetchall()
        print("\n------------ STUDENT RECORDS ------------")
        for i in rows:
            print(f"Roll_no: {i[0]} | Name: {i[1]} | Age: {i[2]} | Course: {i[3]}")
        print("-----------------------------------------")
        time.sleep(2)

    def search_student(self):
        Roll_no = int(input("Enter Roll No to Search: "))
        self.cursor.execute("SELECT * FROM students WHERE Roll_no = %s", (Roll_no,))
        row = self.cursor.fetchone()
        if row:
            print(f" Found: Roll_no: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")
        else:
            print(" No Record Found")

    def update_student(self):
        print("\n---- UPDATE MENU ----")
        print("1. Update Course")
        print("2. Update Age")
        print("3. Update Roll No")
        print("4. Update Name")
        print("5. Exit")
        choice = int(input("Enter Choice: "))

        if choice == 1:
            Roll_no = int(input("Enter Roll No: "))
            Course = input("Enter New Course: ")
            self.cursor.execute("UPDATE students SET Course = %s WHERE Roll_no = %s", (Course, Roll_no))
        elif choice == 2:
            Roll_no = int(input("Enter Roll No: "))
            Age = int(input("Enter New Age: "))
            self.cursor.execute("UPDATE students SET Age = %s WHERE Roll_no = %s", (Age, Roll_no))
        elif choice == 3:
            old_roll = int(input("Enter Current Roll No: "))
            new_roll = int(input("Enter New Roll No: "))
            self.cursor.execute("UPDATE students SET Roll_no = %s WHERE Roll_no = %s", (new_roll, old_roll))
        elif choice == 4:
            Roll_no = int(input("Enter Roll No: "))
            Name = input("Enter New Name: ")
            self.cursor.execute("UPDATE students SET Name = %s WHERE Roll_no = %s", (Name, Roll_no))
        elif choice == 5:
            return
        else:
            print(" Invalid Choice")
            return

        self.db.commit()
        print(" Student Updated Successfully")

    def delete_student(self):
        Roll_no = int(input("Enter Roll No to Delete: "))
        self.cursor.execute("DELETE FROM students WHERE Roll_no = %s", (Roll_no,))
        self.db.commit()
        print(" Student Deleted Successfully")

    def admin_login(self):
        print("\n========== ADMIN LOGIN ==========")
        admin_name = input("Enter Admin Name: ")
        if admin_name.lower() == "sumit":
            password = input("Enter Admin Password: ")
            if password == "1234":
                print(" Login Successful\n")
                self.menu()
            else:
                print(" Incorrect Password")
        else:
            print(" Invalid Admin Name")

    def menu(self):
        while True:
            print("\n====== STUDENT RECORD MENU ======")
            print("1. Add Student")
            print("2. Display All Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Exit")
            choice = int(input("Enter your Choice: "))
            if choice == 1:
                self.add_student()
            elif choice == 2:
                self.display_students()
            elif choice == 3:
                self.search_student()
            elif choice == 4:
                self.update_student()
            elif choice == 5:
                self.delete_student()
            elif choice == 6:
                print(" Thank you. Exiting...")
                break
            else:
                print(" Invalid Choice")


app = StudentManagementSystem()
app.admin_login()

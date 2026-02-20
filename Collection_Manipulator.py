print("Welcome to student Data Organizer.")
print("This program allows you to add or update student details.")

students = []

while True:
    print("\nSelect an option:")
    print("1.Add student \n2.Display All students \n3.Update student Information \n4.Delete student \n5.Display subjects offered \n6.Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            n = int(input("How many students you want to add?: "))

            for i in range(n):
                name = input("Enter student Name: ")
                stu_id = int(input("Enter Student Id: "))
                age = int(input("Enter student Age: "))
                dob = input("Enter student Date Of Birth(YYYY-MM-DD): ")
                grade = input("Enter student Grade: ")
                sub = input("Enter student Subjects(Comma Separated): ")

                sub_list = sub.split(",")
                sub_set = set()

                for i in sub_list:
                    sub_set.add(i.strip())

                stu_tuple = (stu_id, dob)

                stu_dict = {"id_info": stu_tuple, "name" : name, "age" : age, "grade" : grade, "subjects" : sub_set}

                students.append(stu_dict)

            print("\nStudents added successfully!")

        case 2:
            print(f"\n{'-'*20} Display all Students {'-'*20}")
            for i in students:
                sid = i["id_info"][0]
                dob = i["id_info"][1]
                name = i["name"]
                age = i["age"]
                grade = i["grade"]
                subjects = ",".join(i["subjects"])

                print(f"Student Id: {sid} | Name: {name} | Age: {age} | Grade: {grade} | Subjects: {subjects}")
        
        case 3:
            update_id = int(input("Enter student id: "))
            found = False

            for i in students:
                if i["id_info"][0] == update_id:
                    found = True

                    print("1.Update Age \n2.Update Grade \n3.Update subjects")

                    option = int(input("Eneter your choice: "))

                    match option:
                        case 1:
                            new_age = int(input("Enter new age: "))
                            i["age"] = new_age
                            print("Age updated successfully!")

                        case 2:
                            new_grade = input("Enter new grade: ")
                            i["grade"] = new_grade
                            print("Grade updated successfully!")

                        case 3:
                            new_sub = input("Enter new subjects(Comma Separated): ")
                            new_set = set()

                            for i in new_sub.split(","):
                                new_set.add(i.strip())

                            i["subjects"] = new_set
                            print("Subjects updated successfully!")
                        case _:
                            print("Invalid Input!!")

            if not found:
                print("Student not found...")

        case 4:
            del_id = int(input("Enter student id: "))
            found = False

            for i in range(len(students)):
                if students[i]["id_info"][0] == del_id:
                    del students[i]
                    found = True
                    print("Student deleted successfully!")
                    break

            if not found:
                print("Student not found...")

        case 5:
            all_sub = set()

            for i in students:
                all_sub = all_sub.union(i["subjects"])
            
            print("\nUnique Subject Offered:")
            for i in all_sub:
                print(i)

        case 6:
            print("Thank you for using Student Data Organizer!")
            break

        case _:
            print("Invalid Input!")      
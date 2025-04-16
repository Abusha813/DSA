# Sample list of student dictionaries
students = [
    {'id':'DBU1500010', 'name': 'Dawit',   'dept': 'DS', 'cgpa': 3.34},
    {'id':'DBU1500002', 'name': 'Abrham',  'dept': 'CS', 'cgpa': 3.12},
    {'id':'DBU1500012', 'name': 'Soliana', 'dept': 'DS', 'cgpa': 2.74},
    {'id':'DBU1500005', 'name': 'Rahel',   'dept': 'CS', 'cgpa': 3.10},
    {'id':'DBU1500008', 'name': 'Yared',   'dept': 'SE', 'cgpa': 2.98},
    {'id':'DBU1500004', 'name': 'Marta',   'dept': 'CS', 'cgpa': 3.65},
    {'id':'DBU1500007', 'name': 'Lidya',   'dept': 'DS', 'cgpa': 2.45},
    {'id':'DBU1500011', 'name': 'Nahom',   'dept': 'CS', 'cgpa': 3.40},
    {'id':'DBU1500001', 'name': 'Blen',    'dept': 'SE', 'cgpa': 3.21},
    {'id':'DBU1500009', 'name': 'Samuel',  'dept': 'DS', 'cgpa': 3.50},
]

# Define sorting functions
def bubble_sort_by_id(student_list):
    n = len(student_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if student_list[j]['id'] > student_list[j + 1]['id']:
                student_list[j], student_list[j + 1] = student_list[j + 1], student_list[j]
    return student_list

def insertion_sort_by_name(student_list):
    for i in range(1, len(student_list)):
        key = student_list[i]
        j = i - 1
        while j >= 0 and student_list[j]['name'].lower() > key['name'].lower():
            student_list[j + 1] = student_list[j]
            j -= 1
        student_list[j + 1] = key
    return student_list

def selection_sort_by_cgpa_desc(student_list):
    n = len(student_list)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if student_list[j]['cgpa'] > student_list[max_idx]['cgpa']:
                max_idx = j
        student_list[i], student_list[max_idx] = student_list[max_idx], student_list[i]
    return student_list

# Loop until user chooses to exit
print("\nWelcome to the Student Management System")
print("""
         1. Sort by ID
         2. Sort by Name
         3. Sort by CGPA
         4. Exit
    """)    
choice = input("Enter your choice (1-4): ")

if choice == "1":
        sorted_by_id = bubble_sort_by_id(students.copy())
        print("\nStudents sorted by ID (Bubble Sort):")
        for student in sorted_by_id:
            print(student)

elif choice == "2":
        sorted_by_name = insertion_sort_by_name(students.copy())
        print("\nStudents sorted by Name (Insertion Sort):")
        for student in sorted_by_name:
            print(student)

elif choice == "3":
        sorted_by_cgpa = selection_sort_by_cgpa_desc(students.copy())
        print("\nStudents sorted by CGPA Descending (Selection Sort):")
        for student in sorted_by_cgpa:
            print(student)

elif choice == "4":
        print("Exiting the program. Goodbye!")
      

else:
        print("Invalid choice. Please try again.")

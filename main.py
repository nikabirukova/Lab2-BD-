import time


class Searcher:
    def __init__(self, students_ll, teachers_ll):
        self.students_ll = students_ll
        self.teachers_ll = teachers_ll

    def find_classroom_by_student_surname(self, surname):
        start_time = time.time()
        surname = surname.upper()

        current_node = self.students_ll.head
        while current_node:
            if current_node.data['st_last_name'] == surname:
                print(
                    f"{current_node.data['st_last_name']} {current_node.data['st_first_name']} - {current_node.data['classroom']}")

            current_node = current_node.next

        end_time = time.time()
        print(f"\nRequest took: {(end_time - start_time) * 1000}ms")
        print("\n\n")

    def find_bus_route_by_student_surname(self, surname):
        start_time = time.time()
        surname = surname.upper()

        current_node = self.students_ll.head
        while current_node:
            if current_node.data['st_last_name'] == surname:
                print(
                    f"{current_node.data['st_last_name']} {current_node.data['st_first_name']} - {current_node.data['bus']}")

            current_node = current_node.next

        end_time = time.time()
        print(f"\nRequest took: {(end_time - start_time) * 1000}ms")
        print("\n\n")

    def find_teachers_by_classroom(self, classroom):
        start_time = time.time()

        current_node = self.teachers_ll.head
        while current_node:
            if current_node.data['classroom'] == classroom:
                print(
                    f"{current_node.data['t_last_name']} {current_node.data['t_first_name']} - {current_node.data['classroom']}")
            current_node = current_node.next

        end_time = time.time()
        print(f"\nRequest took: {(end_time - start_time) * 1000}ms")
        print("\n\n")

    def find_students_by_bus_route(self, bus_route):
        start_time = time.time()

        current_node = self.students_ll.head
        while current_node:
            if current_node.data['bus'] == bus_route:
                print(
                    f"{current_node.data['st_last_name']} {current_node.data['st_first_name']} - {current_node.data['bus']}")

            current_node = current_node.next

        end_time = time.time()
        print(f"\nRequest took: {(end_time - start_time) * 1000}ms")
        print("\n\n")

    def find_students_by_grade(self, grade):
        start_time = time.time()

        current_node = self.students_ll.head
        while current_node:
            if current_node.data['grade'] == grade:
                print(
                    f"{current_node.data['st_last_name']} {current_node.data['st_first_name']} - {current_node.data['grade']}")

            current_node = current_node.next

        end_time = time.time()
        print(f"\nRequest took: {(end_time - start_time) * 1000}ms")
        print("\n\n")


class StudentNode:
    def __init__(self, st_last_name, st_first_name, grade, classroom, bus):
        self.next = None
        self.data = {
            'st_last_name': st_last_name,
            'st_first_name': st_first_name,
            'grade': grade,
            'classroom': classroom,
            'bus': bus
        }


class TeacherNode:
    def __init__(self, t_last_name, t_first_name, classroom):
        self.next = None
        self.data = {
            't_last_name': t_last_name,
            't_first_name': t_first_name,
            'classroom': classroom
        }


class StudentsLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, st_last_name, st_first_name, grade, classroom, bus):
        new_node = StudentNode(st_last_name.strip(), st_first_name.strip(), grade.strip(), classroom.strip(),
                               bus.strip())

        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node

        new_node.next = None
        self.tail = new_node
        self.length += 1

        return self


class TeachersLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, t_last_name, t_first_name, classroom):
        new_node = TeacherNode(t_last_name.strip(), t_first_name.strip(), classroom.strip())

        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node

        new_node.next = None
        self.tail = new_node
        self.length += 1

        return self


def get_user_input(prompt):
    return input(prompt)


def validate_user_input(input_str, min_val, max_val):
    try:
        value = int(input_str)
        return min_val <= value <= max_val
    except ValueError:
        return False


def main():
    STUDENTS_FILE_PATH = "./list.txt"
    TEACHERS_FILE_PATH = "./teachers.txt"

    try:
        with open(STUDENTS_FILE_PATH, 'r', encoding='utf-8') as f:
            students_lines = [line.strip() for line in f.readlines()]

        with open(TEACHERS_FILE_PATH, 'r', encoding='utf-8') as f:
            teachers_lines = [line.strip() for line in f.readlines()]

        students_ll = StudentsLinkedList()
        teachers_ll = TeachersLinkedList()

        searcher = Searcher(students_ll, teachers_ll)

        for line in students_lines:
            if line:
                line_content = line.split(",")
                students_ll.append(line_content[0], line_content[1], line_content[2], line_content[3], line_content[4])

        for line in teachers_lines:
            if line:
                line_content = line.split(",")
                teachers_ll.append(line_content[0], line_content[1], line_content[2])

        while True:
            user_input = get_user_input(
                "1. Find a student's classroom by surname\n2. Find a student's bus route by surname\n3. Find teachers by classroom\n4. Find students by their bus route\n5. Find students by their grade\n6. exit\n\n[option]: ")
            if not validate_user_input(user_input, 1, 6):
                print("Invalid user input")
                continue

            user_details_input = None
            if user_input == '1':
                user_details_input = get_user_input("[student's surname]: ")
                print("\n")
                searcher.find_classroom_by_student_surname(user_details_input)
            elif user_input == '2':
                user_details_input = get_user_input("[student's surname]: ")
                print("\n")
                searcher.find_bus_route_by_student_surname(user_details_input)
            elif user_input == '3':
                user_details_input = get_user_input("[classroom]: ")
                print("\n")
                searcher.find_teachers_by_classroom(user_details_input)
            elif user_input == '4':
                user_details_input = get_user_input("[bus route]: ")
                print("\n")
                searcher.find_students_by_bus_route(user_details_input)
            elif user_input == '5':
                user_details_input = get_user_input("[grade]: ")
                print("\n")
                searcher.find_students_by_grade(user_details_input)
            elif user_input == '6':
                break

    except Exception as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()

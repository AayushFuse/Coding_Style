"""
Create a Python program that manages student records.
The program should have the following functionalities:
- Create a function that can add new students to the records with their
student_id, name, age, and grade.
The records should be saved to “json” file and each time new record is added,
it should be saved to same “json” file
- Allow searching for a student by student_id or name.
The data should return age and grade from the saved file.
- Allow updating a student's information by using student_id or name(age or grade)
** Ensure to follow PEP8 Coding Guidelines for following criterias:
- Proper Indentation
- Maximum Line Length
- Prescriptive Naming conventions (Package and Module Names,
Class Names, Exception Names, Global Variable Names,
Function and Variable Names, Method Names and Instance Variables, Constants)
- Source File Encoding while accessing the JSON file
- Add NumPy Docstring  to each function
"""

import json


class Student:
    """
    Represents a student.

    Attributes:
        id (int): The student's ID.
        name (str): The student's name.
        age (int): The student's age.
        grade (int): The student's grade.

    Methods:
        __init__: Initializes a new Student object with the provided attributes.
        __str__: Returns a string representation of the Student object.
        to_dict: Converts the Student object into a dictionary.
    """

    def __init__(self, sid, name, age, grade) -> None:
        self.id = sid
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nAge: {self.age}\nGrade: {self.grade}"

    def to_dict(self):
        """Returns Dictionary"""
        return {"id": self.id, "name": self.name, "age": self.age, "grade": self.grade}


def get_students():
    """
    Retrieves the list of students from a JSON file.

    Reads the contents of the "files/students.json" file and attempts to load
    the data as JSON. If successful, returns the list of students. If
    an error occurs during reading or parsing, returns an empty list.

    Returns:
        list: A list of dictionaries representing student records.
              Each dictionary contains keys for 'id', 'name', 'age',
              and 'grade'.
    """
    with open("files/students.json", "r", encoding="utf-8") as json_file:
        try:
            return json.load(json_file)
        except Exception:
            return []


def write_file(students):
    """
    Writes the given list of students to a JSON file named 'files/students.json'.

    Args:
        students (list): A list of student data to be written to the file.

    Returns:
        None
    """
    with open("files/students.json", "w", encoding="utf-8") as json_file:
        json.dump(students, json_file)


def add_student(sid, name, age, grade):
    """Add student to the file"""
    student = Student(sid, name, age, grade)
    students = get_students()
    students.append(student.to_dict())
    write_file(students)


def search_student(sid):
    """
    Searches for a student with the given ID in the list of students.

    Args:
        sid (int): The ID of the student to search for.

    Returns:
        filter object: A filter object containing students matching the given ID.
    """
    students = get_students()
    val = filter(lambda x: x["id"] == sid, students)

    return val


def update_student(sid, age, grade):
    """
    Updates the age and grade of a student with the given ID in the 'files/students.json' file.

    Args:
        sid (int): The ID of the student to update.
        age (int): The new age of the student.
        grade (str): The new grade of the student.

    Returns:
        None
    """
    with open("files/students.json", "r+", encoding="utf-8") as file:
        students = json.load(file)

        for student in students:
            if student["id"] == sid:
                student["age"] = age
                student["grade"] = grade
            file.seek(0)
            json.dump(students, file, indent=4)


if __name__ == "__main__":
    add_student(1, "Aayush", 23, "A+")
    add_student(2, "Abhishek", 27, "A")
    update_student(1, 20, "A++")
    print(next(search_student(2)))

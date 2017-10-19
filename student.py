#!/usr/bin/python
# -*- encoding: utf-8 -*-

# Write a class Student, with the following methods:
# • constructor
# • get_details(self)
# • enroll(self, course)
# • get_no_of_students(self)
# • get_course_participants(self, course)
# • __str__()
# Take care of class vs. Instance variables.

class Student(object):
    '''A student class'''

    def __init__(self):
        self.items = list()

    def push(self, x):
        self.items.append(x)

    def get_details(self):
        for i in self.items:
            print ("Name: {}, ID: {}, Course: {} ".format(i["Name"], i["ID"], i["Course"]))

    # def enroll(self, course):
    #      if self.items.__contains__(self):
    #         return True

    def get_no_of_students(self):
        print(len(self.items))

    def get_course_participants(self, course):
        for i in self.items:
            if i["Course"] == course:
                print("Found student:  Name: {}, ID: {}, Course: {} ".format(i["Name"], i["ID"], i["Course"]))



if __name__ == "__main__":

    s1 = Student()
    s1.push({"Name":"Sally","ID":2,"Course":"EWP"})
    s1.push({"Name":"Minnie","ID":3,"Course":"OOS"})
    s1.push({"Name":"Winnie","ID":4,"Course":"SWT"})

#
    s1.get_details()
    s1.get_no_of_students()
    s1.get_course_participants("OOS")

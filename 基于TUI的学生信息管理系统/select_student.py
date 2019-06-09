# -*- coding: utf-8 -*-

import io_print
import print_student
 
 #通过交互，获取到用户想要查询的学生的学号，然后传入select类中进行查找。
def index(file_path):               
    while True:
        print(u"\nPlease input the id of the student whom you want to select")
        print(u"If you want to break, please input quit!")
        keyword = input(u"Please input the id or 'quit':")
        if keyword == "quit":
            break
        else:
            selectline = Select()
            selectline.selectinfo(keyword, file_path)
             
#通过获取到用户想要查找的记录的学号，同时获取到学生信息列表，然后将其传入到printstudent块中进行处理。
class Select:                        
    def selectinfo(self, number, file_path):
        student = io_print.Io()
        information = []
        information = student.read(information, file_path)
        has_id = False              
        for i in information:
            if i[0] == number:
                has_id = True
                print_student.one_student(information[information.index(i)])
        if has_id == False:
            print("\nThere is no student whose id is ", number)

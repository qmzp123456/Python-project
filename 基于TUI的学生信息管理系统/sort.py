# -*- coding: utf-8 -*-

import io_print
import print_student
 
#通过交互获取到用户想要通过什么方式进行排序，可选择的有学号，年龄，成绩。
def index(file_path):                
    while True:
        print(u"\nPlease input what keyword that you want to sort, you can choose 'number'or'age'or'score'")
        print(u"If you want to break, please input quit!")
        keyword = input(u"Please input what you want:")
        if keyword == "quit":
            break
        elif keyword == "number" or keyword == "age" or keyword == "score":
            student = io_print.Io()
            information = []
            information = student.read(information, file_path)
            if keyword == "number":
                sorted_information = sorted(information, key = lambda student:student[0])
            elif keyword == "age":
                sorted_information = sorted(information, key = lambda student:student[2])
            else:  #keyword == "score"
                sorted_information = sorted(information, key = lambda student:student[3])
            print_student.all_student(sorted_information)
        else:
            print(u"\nPlease input correct keyword")
            

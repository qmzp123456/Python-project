# -*- coding: utf-8 -*-

import io_print

#这个函数是用来被main调用，实现添加记录的功能，通过这个函数来与用户交互，将获取到的数据通过io写入到文件中。
def index(file_path):                
    while True:
        print(u"\nPlease input a student information like:number, name, age, score, address")
        print(u"If you want to break,please input quit!")
        keyword = input(u"please input what you want:")
        if keyword == "quit":
            break
        else:
            addline = Add()
            addline.addinfo(keyword.split(", "), file_path)
            
#add类用来实现将获取到的一条记录传到io中，写入文件。
class Add:                           
    def __init__(self):
        print(u"We will input this student's information")
    def addinfo(self,student_info, file_path):
        student = io_print.Io()      # student作为io模块中Io类的对象
        student.add(student_info, file_path)

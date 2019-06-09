# -*- coding: utf-8 -*-

import io_print
import print_student
#通过与用户交互，获取到用户想要删除的记录的学号，然后交给delete类来实现删除记录的功能。
def index(file_path):                 
    while True:
        print(u"\nPlease input the id of the student whom you want to delete!")
        print(u"If you want to break, please input quit!")
        keyword = input(u"Please input id or 'quit':")
        if keyword == "quit":
            break
        else:
            deleteline = Delete()
            deleteline.deleteinfo(keyword, file_path)
      
#delete类通过io获取到所有学生信息，然后将用户想要删除的学生学号进行匹配，假如匹配到，则删除该条记录。
class Delete:                        
    def deleteinfo(self, number, file_path):
        student = io_print.Io()           # student作为io模块中io类的对象
        information = []
        information = student.read(information, file_path)      #执行完这一步后，information是一个大列表，其中列表的每个元素是每个学生信息组成的小列表
        has_id = False              #has_number为 False时，代表现有的学生列表中没有该学号的学生信息
                                    #为True时，代表有该学号的学生信息
        for i in information:
            if i[0] == number:
                has_id = True
                print("\nThe information of stdent", number, "is")
                print_student.one_student(information[information.index(i)])
                information.remove(i)           #删除该学号对应的小列表
                student.write(information, file_path)   #将删除后的列表再重新写入文件
        if has_id == False:
            print("\nThere is no student whose id is ", number)


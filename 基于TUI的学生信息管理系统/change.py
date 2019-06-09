# -*- coding: utf-8 -*-

import io_print
import print_student
#通过交互获取到用户想要修改的学生的学号，然后传递给change类。
def index(file_path):                
    while True:
        print(u"\nPlease input the id of the student whose information you want to change!")
        print(u"If you want to break, please input quit!")
        keyword = input(u"Please input the id or 'quit':")
        if keyword == "quit":
            break
        else:
            changeline = Change()
            changeline.changeinfo(keyword, file_path)
             
#通过从io中获取学生信息，存储到list中，然后遍历list，获取到匹配学号的记录，
#然后获取到用户想要修改后的数据，将其写入到list中，最后再将这个新的List存入到文件中
class Change:  
    def changeinfo(self, number, file_path):
        student = io_print.Io()
        information = []
        information = student.read(information, file_path)
        has_id = False
        for i in information:
            if i[0] == number:
                has_id = True
                keyword = input(u"Please input the student's information that you want to change like:number, name, age, score, address:")
                keyword = keyword + '\n'
                information[information.index(i)] = keyword.split(", ")     
                #用information[information.index(i)]  是因为 i此时为大列表中的小列表，
                #而information.index(i)返回的是小列表i在大列表中对应的索引位置
                student.write(information, file_path)
                break
        if has_id == False:
            print("\nThere is no student whose id is ", number)

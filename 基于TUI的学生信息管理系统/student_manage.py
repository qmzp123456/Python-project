
# -*- coding: utf-8 -*-

"""
Spyder Editor

This is a temporary script file.
"""

import sys; sys.path

import add
import delete
import change
import select_student
import sort

file_path= 'student.txt'       #首先定义数据的存储路径，这里定义为当前程序锁在目录的根目录中
 
 #在main函数中使用while循环来获取用户的输入信息
def main():                   
    while True:
        print(u"\nWelcome to student information management system!")
        print(u"You can use input:add;delete;change;select;sort;quit")
        keyword=input("Please input what you want to operate:")
        if keyword=="quit":             #因为python中没有switch-case语句
           sys.exit(u"Goodbye")
        elif keyword=="add":
            add.index(file_path)
        elif keyword=="delete":
            delete.index(file_path)
        elif keyword=="change":
            change.index(file_path)
        elif keyword=="select":
            select_student.index(file_path)
        elif keyword=="sort":
            sort.index(file_path)
        else:
            print(u"please input correct option!")
if __name__ == '__main__':
    main()
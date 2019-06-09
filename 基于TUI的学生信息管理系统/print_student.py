# -*- coding: utf-8 -*-

#对查询和排序传过来的列表进行排序
#%+20s，其中的+20是占位20的宽度，数据向右对齐。
def all_student(information):                
    for i in information:
        print("number: %+20s" %str(i[0]))
        print("name:   %+20s" %str(i[1]))
        print("age:    %+20s" %str(i[2]))
        print("score:  %+20s" %str(i[3]))
        print("address: %+20s" %str(i[4]))
         
def one_student(l):
    print("number: %+20s" %str(l[0]))
    print("name:   %+20s" %str(l[1]))
    print("age:    %+20s" %str(l[2]))
    print("score:  %+20s" %str(l[3]))
    print("address: %+20s" %str(l[4]))
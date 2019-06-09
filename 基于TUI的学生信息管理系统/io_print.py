# -*- coding: utf-8 -*-
import sys; sys.path

class Io:
    #读取学生信息
    def read(self, information, file_path):
        f = open(file_path, 'r')
        for line in f:
            information.append(line.split(', '))    #用“， ”作为分隔符，分割出一个学生的各种信息，每个信息作为该小列表的一个元素
                                                    #并将所有学生的信息作为一个外层的大列表
        f.close()
        return  information
    
    #写入学生信息
    def write(self, information, file_path):
        f = open(file_path, 'w')
        for line in information:
            f.write(', '.join(line))
        f.close()
    
    #追加学生信息
    def add(self, information, file_path):
        f = open(file_path,'a')
        print(', '.join(information), file = f) 
        f.close()


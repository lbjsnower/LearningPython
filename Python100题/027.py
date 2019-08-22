#!/usr/bin/Anaconda3/python
# -*- coding: utf-8 -*- 
# @Time  : 2019/8/22 0:20 
"""
【程序 27】
题目：利用递归函数调用方式，将所输入的 5 个字符，以相反顺序打印出来。
难点
"""
str_ocr = "qwert"
def fun(s,length):
    """
    相反顺序打印出来
    :param s: 字符
    :param length:字符长度
    :return:
    """
    if length == 0:
        return ''
    print(s[length-1],end="")
    return fun(s,length-1)


print(fun(str_ocr, len(str_ocr)))
# -*- coding: utf-8 -*-
"""
spyder editor

"""

if __name__ == '__main__':
    
    def ordenar(lista):
        for x in lista[0:]:
            if lista[x][1] < lista[x-1][1]:
                print(lista)

    
    
    students = []
    students.clear()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    
    ordenar(students)
    
    
    print("=====|BEFORE|======")
    print(students)
    sorted(students)
    print("=====|AFTER|======")
    print(students)
    

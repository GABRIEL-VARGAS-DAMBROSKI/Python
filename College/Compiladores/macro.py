# -*- coding: utf-8 -*-
"""
@author: Gabriel Vargas Dambroski
@RA: 100909
"""

import re

def PreProcessador(arquivo):
    arqResult = open('result_01.txt', 'a')
    
    for x in arquivo:
        if 'include' in x:
            arqResult.write('b = 230\n')
        else:
            arqResult.write(x)

def ValidadorMontagem(linha):
    linhaSplit = linha.split()
    indice = 0
    for x in linhaSplit:
        if re.search('\d', x):
            #print('X: ', x)
            x = ('#' + x)
            #print('Result X: ', x)
            #print('indice: ', indice)
            linhaSplit[indice]=x
        indice+=1 
            
    #print(linhaSplit)
            
    if '+' in linhaSplit:
        saida = "MOV {movFrom}, R1\nADD {addFrom}, R1\nMOV R1, {result}\n".format(movFrom = linhaSplit[-1],
                                                                                       addFrom = linhaSplit[2], 
                                                                                       result = linhaSplit[0])
    elif '=' in linhaSplit:
        saida = "MOV {de},{para}".format(de = linhaSplit[-1], para = linhaSplit[0]+'\n')
    return saida


def Montagem(arquivo):
    arqResult = open("result_02.txt", "a")
    for x in arquivo:
        if '=' in x:
            arqResult.write(ValidadorMontagem(x))
                

if __name__ == '__main__':
    entrada = open("input.txt", "r")
    PreProcessador(entrada)
    entrada.close()
    
    result = open("result_01.txt", "r")
    Montagem(result)
    result.close()
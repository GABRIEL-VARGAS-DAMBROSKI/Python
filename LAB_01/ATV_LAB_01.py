# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 23:02:00 2019

@author: Dambroski
"""

import numpy as np
import cv2

BeanGray = cv2.imread('MrBeanOrigianal.jpg', 0)
BeanColor = cv2.imread('MrBeanOrigianal.jpg', 1)

'''
    # ATIVIDADES LAB 01 - 10/09/2019
    
    # Ativiade 01
        - Salvar BeanRed
        - Salvar BeanGreen
        - Salvar Beanblue
    
    # Atividade 02
        - Salvar BeanSepia
        
    # Atividade 03
        - Utilizar imagem como marca d'água
                -> https://unasp.mrooms.net/pluginfile.php/524232/mod_assign/intro/marca.png
    
    # Atividade 04
        - Binarização da imagem do FOTÓGRAFO
    
    # Atividade 05
        - Aplicar o filtro de threshold adaptativo e eliminar as componentes conexas menores
    
'''
#############################
'''
# TAMANHO DA IMAGEM
print(BeanColor.shape)
'''
############################

# Atividade 01
for x in range(340):
    for y in range(515):
        BeanColor[x, y, 0] = BeanColor[x, y, 0]
        BeanColor[x, y, 1] = BeanColor[x, y, 1]
        BeanColor[x, y, 2] = 255


BeanVar = BeanColor

cv2.imshow('BeanVar.jpg', BeanVar)
cv2.imwrite('BeanRed.jpg', BeanVar)






'''
cv2.imshow('BeanColor.jpg', BeanColor)
cv2.imshow('BeanGray.jpg', BeanGray)
'''
cv2.waitKey(0)
cv2.destroyAllWindows()
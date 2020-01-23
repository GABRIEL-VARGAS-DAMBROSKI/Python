# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    runnerUp = sorted(arr)
    
    print(runnerUp)   
    
    size = len(runnerUp)

    print("tamanho", size)
    print("ultima linha:", runnerUp[size-1])
    print("penultima linha:", runnerUp[size-2])
    
    if size == 1:
        print(runnerUp[0])
    elif(runnerUp[size-1] == runnerUp[0]):
        print(runnerUp[0])
    elif size == 2:
        print(runnerUp[1] if runnerUp[0] > runnerUp[1] else runnerUp[0])
    elif runnerUp[size-2] < runnerUp[size-1]:
        print(runnerUp[size-2])    
    else:    
        x = 2
        while True:
            print("O 'x' ta valendo:",x)
            if runnerUp[size-1] != runnerUp[size-x]:
                #x = x-1
                print(runnerUp[size-x])
                break
            else:
                x = x+1
                #print(runnerUp[size-x])
            
            if x == 0:
                print("entrei na ultima condicao")
                if runnerUp[0] < runnerUp[1]:
                    print(runnerUp[0])
                    break
                else:
                    print(runnerUp[0])
                    break
        

    

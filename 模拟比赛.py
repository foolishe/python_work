import os
from random import random
def main():
    printintro()
    proa,prob,n=getinputs()
    winsa,winsb=simngames(n,proa,prob)
    printsummary(winsa,winsb)
def printintro():
    print('这个程序模拟两个选手A和B的某种竞技比赛')
    print('程序运行需要A和B的能力值（以0到1之间的小数表示）')
def getinputs():
    a=eval(input('请输入选手A的能力值（0——1）：'))
    b=eval(input('请输入选手B的能力值（0-1）：'))
    n=eval(input('模拟比赛的场次：'))
    return a,b,n
def printsummary(winsa,winsb):
    n=winsa+winsb
    print('竞技分析开始，共模拟{}场比赛'.format(n))
    print('选手A获胜{}场比赛，占比{:0.2%}'.format(winsa,winsa/n))
    print('选手B获胜{}场比赛，占比{:0.2%}'.format(winsb,winsb/n))
def simonegame(proa,prob):
    scorea,scoreb=0,0
    serving='a'
    while scorea<15 and scoreb<15:
        if serving=='a':
            if random()<proa:
                scorea+=1
            else:serving='b'
        else:
            if random()<prob:
                scoreb+=1
            else:serving='a'    
    return scorea,scoreb
def simngames(n,proa,prob):
    winsa,winsb=0,0
    for i in range(n):
        scorea,scoreb=simonegame(proa,prob)
        if scorea<scoreb:winsb+=1
        else:winsa+=1
    return winsa,winsb
main()
    
    


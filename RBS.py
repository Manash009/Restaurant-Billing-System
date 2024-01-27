import pandas as pd
import pandas as pd 
def CR():
           print('\n By Manash rai')
           print('\n Thank you for visiting us ')
def veg_nonveg():
           df=pd.read_csv('D:\\ip project\\resturant billing system\\veg_non.csv',index_col='Keys')
           print(df)
def menu1():
           df1=pd.read_csv('D:\\ip project\\resturant billing system\\menu1.csv',index_col='Keys')
           print(df1)
def menu11():
           df2=pd.read_csv('D:\\ip project\\resturant billing system\\menu11.csv',index_col='Keys')
           print(df2)
def menuVB():
           df3=pd.read_csv('D:\\ip project\\resturant billing system\\menuVB.csv',index_col='Keys')
           print(df3)
def menuNB():
           df4=pd.read_csv('D:\\ip project\\resturant billing system\\menuNB.csv',index_col='Keys')
           print(df4)
           
def menuVP():
           df5=pd.read_csv('D:\\ip project\\resturant billing system\\menuVP.csv',index_col='Keys')
           print(df5)
           
def menuNP():
           df6=pd.read_csv('D:\\ip project\\resturant billing system\\menuNP.csv',index_col='Keys')
           print(df6)
           
def menuVM():
           df7=pd.read_csv('D:\\ip project\\resturant billing system\\menuVM.csv',index_col='Keys')
           print(df7)

def menuNM():
           df8=pd.read_csv('D:\\ip project\\resturant billing system\\menuNM.csv',index_col='Keys')
           print(df8)
def menuVC():
           df9=pd.read_csv('D:\\ip project\\resturant billing system\\menuVC.csv',index_col='Keys')
           print(df9)

def menuNC():
           df10=pd.read_csv('D:\\ip project\\resturant billing system\\menuNC.csv',index_col='Keys')
           print(df10)
def menuVS():
           df11=pd.read_csv('D:\\ip project\\resturant billing system\\menuVS.csv',index_col='Keys')
           print(df11)
def menuNS():
           df12=pd.read_csv('D:\\ip project\\resturant billing system\\menuNS.csv',index_col='Keys')
           print(df12)

def menu12():
           df13=pd.read_csv('D:\\ip project\\resturant billing system\\menu12.csv',index_col='Keys')
           print(df13)

def menuSV():
           df14=pd.read_csv('D:\\ip project\\resturant billing system\\menuSV.csv',index_col='Keys')
           print(df14)

def menuSN():
           df15=pd.read_csv('D:\\ip project\\resturant billing system\\menuSN.csv',index_col='Keys')
           print(df15)
def menuSl():
           df6=pd.read_csv('D:\\ip project\\resturant billing system\\menuSl.csv',index_col='Keys')
           print(df6)

def menuR():
           df16=pd.read_csv('D:\\ip project\\resturant billing system\\menuR.csv',index_col='Keys')
           print(df16)

def menuVMa():
           df17=pd.read_csv('D:\\ip project\\resturant billing system\\menuVMa.csv',index_col='Keys')
           print(df17)

def menuNMa():
           df18=pd.read_csv('D:\\ip project\\resturant billing system\\menuNMa.csv',index_col='Keys')
           print(df18)
def menuRo():
           df19=pd.read_csv('D:\\ip project\\resturant billing system\\menuRo.csv',index_col='Keys')
           print(df19)

def menu13():
           df20=pd.read_csv('D:\\ip project\\resturant billing system\\menu13.csv',index_col='Keys')
           print(df20)
def menuC():
           df21=pd.read_csv('D:\\ip project\\resturant billing system\\menuC.csv',index_col='Keys')
           print(df21)
def menuI():
           df22=pd.read_csv('D:\\ip project\\resturant billing system\\menuI.csv',index_col='Keys')
           print(df22)
def menuIS():
           df23=pd.read_csv('D:\\ip project\\resturant billing system\\menuIS.csv',index_col='Keys')
           print(df23)

print('*******************************************************Restaurant************************************************')
cost=0
n=[]
o=[]
p=[]
a=0
while a==0:
           menu1()
           c=int(input('what would you like to have , Sir '))
           if c==1:
                      menu11()
                      b=int(input('what would you like to have , Sir '))
                      if b==1:
                                 d=0
                                 while d==0:   
                                            veg_nonveg()
                                            e=input('what would you prefer , Sir (use capital letters )')
                                            if e=='V':
                                                       menuVB()
                                                       f=input('what would you like to have , Sir (use capital letters )')
                                                       if f=='B':
                                                                  g=int(input('How many would you like to have:'))
                                                                  n.append('Blackbean Burger ')
                                                                  o.append(g)
                                                                  p.append(80)
                                                                  h=g*80
                                                                  print('Total price :',h)
                                                                  cost=cost+h
                                                                  m=int(input('do you want somethink else 0-yes/1-no'))
                                                                  d=d+m
                                                       elif f=='F':
                                                                  g=int(input('How many would you like to have:'))
                                                                  n.append('Falafel Burger  ')
                                                                  o.append(g)
                                                                  p.append(90)
                                                                  h=g*90
                                                                  print('Total price :',h)
                                                                  cost=cost+h
                                                                  m=int(input('do you want somethink else 0-yes/1-no'))
                                                                  d=d+m
                                                       elif f=='Q':
                                                                   g=int(input('How many would you like to have:'))
                                                                   n.append('Quinoa Veggies Burger ')
                                                                   o.append(g)
                                                                   p.append(100)
                                                                   h=g*100
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                       elif f=='A':
                                                                   g=int(input('How many would you like to have:'))
                                                                   n.append('Aloo Tikki Burger  ')
                                                                   o.append(g)
                                                                   p.append(120)
                                                                   h=g*120
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                       elif f=='T':
                                                                   g=int(input('How many would you like to have:'))
                                                                   n.append('Tofu Burger ')
                                                                   o.append(g)
                                                                   p.append(130)
                                                                   h=g*130
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                       else :
                                                                  print('invalid ')
                                            elif e=='N':
                                                        menuNB()
                                                        f=input('what would you like to have , Sir (use capital letters )')
                                                        if f=='P':
                                                                   g=int(input('How many would you like to have:'))
                                                                   n.append('Chill Burger with Pepper Relish ')
                                                                   o.append(g)
                                                                   p.append(130)
                                                                   h=g*130
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='C':
                                                                    g=int(input('How many would you like to have:'))
                                                                    n.append('Chicken Burger')
                                                                    o.append(g)
                                                                    p.append(140)
                                                                    h=g*140
                                                                    print('Total price :',h)
                                                                    cost=cost+h
                                                                    m=int(input('do you want somethink else 0-yes/1-no'))
                                                                    d=d+m
                                                        elif f=='F':
                                                                    g=int(input('How many would you like to have:'))
                                                                    n.append('Fish and Chicken Burger ')
                                                                    o.append(g)
                                                                    p.append(150)
                                                                    h=g*150
                                                                    print('Total price :',h)
                                                                    cost=cost+h
                                                                    m=int(input('do you want somethink else 0-yes/1-no'))
                                                                    d=d+m
                                                        elif f=='B':
                                                                    g=int(input('How many would you like to have:'))
                                                                    n.append('Butter Chicken Burger ')
                                                                    o.append(g)
                                                                    p.append(160)
                                                                    h=g*160
                                                                    print('Total price :',h)
                                                                    cost=cost+h
                                                                    m=int(input('do you want somethink else 0-yes/1-no'))
                                                                    d=d+m
                                                        elif f=='D':
                                                                    g=int(input('How many would you like to have:'))
                                                                    n.append('Double Chicken Burger ')
                                                                    o.append(g)
                                                                    p.append(170)
                                                                    h=g*170
                                                                    print('Total price :',h)
                                                                    cost=cost+h
                                                                    m=int(input('do you want somethink else 0-yes/1-no'))
                                                                    d=d+m
                                                        else :
                                                                   print('invalid ')
                                            else:
                                                       print('invalid ')
                                            
                      
                      if b==2:
                                 d=0
                                 while d==0:
                                             veg_nonveg()
                                             e=input('what would you prefer , Sir (use capital letters )')
                                             if e=='V':
                                                        menuVP()
                                                        f=input('what would you like to have , Sir (use capital letters )')
                                                        if f=='P':
                                                                   g=int(input('How many would you like to have:'))
                                                                   n.append('Panner Special Pizza ')
                                                                   o.append(g)
                                                                   p.append(280)
                                                                   h=g*280
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='T':
                                                                    g=int(input('How many would you like to have:'))
                                                                    n.append('Taco Style Pizza ')
                                                                    o.append(g)
                                                                    p.append(290)
                                                                    h=g*290
                                                                    print('Total price :',h)
                                                                    cost=cost+h
                                                                    m=int(input('do you want somethink else 0-yes/1-no'))
                                                                    d=d+m
                                                        elif f=='M':
                                                                    g=int(input('How many would you like to have:'))
                                                                    n.append('Mediterraner Special Pizza ')
                                                                    o.append(g)
                                                                    p.append(300)
                                                                    h=g*300
                                                                    print('Total price :',h)
                                                                    cost=cost+h
                                                                    m=int(input('do you want somethink else 0-yes/1-no'))
                                                                    d=d+m
                                                        elif f=='F':
                                                                    g=int(input('How many would you like to have:'))
                                                                    n.append('Four Cheese Pizza ')
                                                                    o.append(g)
                                                                    p.append(320)
                                                                    h=g*320
                                                                    print('Total price :',h)
                                                                    cost=cost+h
                                                                    m=int(input('do you want somethink else 0-yes/1-no'))
                                                                    d=d+m
                                                        elif f=='C':
                                                                    g=int(input('How many would you like to have:'))
                                                                    n.append('Capsicum Pizza ')
                                                                    o.append(g)
                                                                    p.append(330)
                                                                    h=g*330
                                                                    print('Total price :',h)
                                                                    cost=cost+h
                                                                    m=int(input('do you want somethink else 0-yes/1-no'))
                                                                    d=d+m
                                                        else :
                                                                   print('invalid ')
                                             elif e=='N':
                                                         menuNP()
                                                         f=input('what would you like to have , Sir (use capital letters )')
                                                         if f=='B':
                                                                    g=int(input('How many would you like to have:'))
                                                                    n.append('Barbeque Chicken Pizza')
                                                                    o.append(g)
                                                                    p.append(230)
                                                                    h=g*230
                                                                    print('Total price :',h)
                                                                    cost=cost+h
                                                                    m=int(input('do you want somethink else 0-yes/1-no'))
                                                                    d=d+m
                                                         elif f=='C':
                                                                    g=int(input('How many would you like to have:'))
                                                                    n.append('CLassic Chicken Pizza ')
                                                                    o.append(g)
                                                                    p.append(240)
                                                                    h=g*240
                                                                    print('Total price :',h)
                                                                    cost=cost+h
                                                                    m=int(input('do you want somethink else 0-yes/1-no'))
                                                                    d=d+m
                                                         elif f=='M':
                                                                     g=int(input('How many would you like to have:'))
                                                                     n.append('Chicken Mexican Pizza ')
                                                                     o.append(g)
                                                                     p.append(250)
                                                                     h=g*250
                                                                     print('Total price :',h)
                                                                     cost=cost+h
                                                                     m=int(input('do you want somethink else 0-yes/1-no'))
                                                                     d=d+m
                                                         elif f=='P':
                                                                     g=int(input('How many would you like to have:'))
                                                                     n.append('Pepperoni Pizza ')
                                                                     o.append(g)
                                                                     p.append(260)
                                                                     h=g*260
                                                                     print('Total price :',h)
                                                                     cost=cost+h
                                                                     m=int(input('do you want somethink else 0-yes/1-no'))
                                                                     d=d+m
                                                         elif f=='H':
                                                                     g=int(input('How many would you like to have:'))
                                                                     n.append('Hot N Spicy Chicken Pizza ')
                                                                     o.append(g)
                                                                     p.append(270)
                                                                     h=g*270
                                                                     print('Total price :',h)
                                                                     cost=cost+h
                                                                     m=int(input('do you want somethink else 0-yes/1-no'))
                                                                     d=d+m
                                                         else :
                                                                    print('invalid ')
                                             else:
                                                        print('invalid ')
                      if b==3:
                                 d=0
                                 while d==0:
                                             veg_nonveg()
                                             e=input('what would you prefer , Sir (use capital letters )')
                                             if e=='V':
                                                        menuVM()
                                                        f=input('what would you like to have , Sir (use capital letters )')
                                                        if f=='S':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Steamed Veg Momos ')
                                                                   o.append(g)
                                                                   p.append(80)
                                                                   h=g*80
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='Y':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Soya Momos ')
                                                                   o.append(g)
                                                                   p.append(90)
                                                                   h=g*90
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='M':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Mushroom Momos ')
                                                                   o.append(g)
                                                                   p.append(100)
                                                                   h=g*100
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='F':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Fried Momos ')
                                                                   o.append(g)
                                                                   p.append(120)
                                                                   h=g*120
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='C':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Cheese Momos  ')
                                                                   o.append(g)
                                                                   p.append(130)
                                                                   h=g*130
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        else :
                                                                   print('invalid ')
                                             elif e=='N':
                                                        menuNM()
                                                        f=input('what would you like to have , Sir (use capital letters )')
                                                        if f=='C':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Steamed Chicken Momos ')
                                                                   o.append(g)
                                                                   p.append(130)
                                                                   h=g*130
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='F':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Fish Momos  ')
                                                                   o.append(g)
                                                                   p.append(140)
                                                                   h=g*140
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='P':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Prawns Momos ')
                                                                   o.append(g)
                                                                   p.append(150)
                                                                   h=g*150 
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='S':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Steamed Pork Momos ')
                                                                   o.append(g)
                                                                   p.append(160)
                                                                   h=g*160
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='M':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Meat Momos')
                                                                   o.append(g)
                                                                   p.append(170)
                                                                   h=g*170
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        else :
                                                                   print('invalid ')

                                             else:
                                                        print ('Invalid entery')
                      if b==4:
                                 d=0
                                 while d==0:
                                             veg_nonveg()
                                             e=input('what would you prefer , Sir (use capital letters )')
                                             if e=='V':
                                                        menuVC()
                                                        f=input('what would you like to have , Sir (use capital letters )')
                                                        if f=='W':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('White Chowmein ')
                                                                   o.append(g)
                                                                   p.append(80)
                                                                   h=g*80
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='Y':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Plain Chowmein')
                                                                   o.append(g)
                                                                   p.append(90)
                                                                   h=g*90
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='M':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Manchurian Chowmein ')
                                                                   o.append(g)
                                                                   p.append(100)
                                                                   h=g*100
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='F':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Paneer Chowmein ')
                                                                   o.append(g)
                                                                   p.append(120)
                                                                   h=g*120
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='C':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Crips Chowmein  ')
                                                                   o.append(g)
                                                                   p.append(110)
                                                                   h=g*110
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        else :
                                                                   print('invalid ')
                                             elif e=='N':
                                                        menuNC()
                                                        f=input('what would you like to have , Sir (use capital letters )')
                                                        if f=='C':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Chicken Chowmein ')
                                                                   o.append(g)
                                                                   p.append(130)
                                                                   h=g*130
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='P':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Prawn Chowmein  ')
                                                                   o.append(g)
                                                                   p.append(140)
                                                                   h=g*140
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='R':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Pork Chowmein ')
                                                                   o.append(g)
                                                                   p.append(150)
                                                                   h=g*150
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='E':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Egg Chowmein ')
                                                                   o.append(g)
                                                                   p.append(100)
                                                                   h=g*100
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='H':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Chicken Hakka Noodle')
                                                                   o.append(g)
                                                                   p.append(150)
                                                                   h=g*150
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        else :
                                                                   print('invalid ')

                                             else:
                                                        print ('Invalid entery')
                      if b==5:
                                 d=0
                                 while d==0:
                                             veg_nonveg()
                                             e=input('what would you prefer , Sir (use capital letters )')
                                             if e=='V':
                                                        menuVS()
                                                        f=input('what would you like to have , Sir (use capital letters )')
                                                        if f=='M':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Veg Mix Spring Roll ')
                                                                   o.append(g)
                                                                   p.append(80)
                                                                   h=g*80
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='N':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Noodle Spring Roll  ')
                                                                   o.append(g)
                                                                   p.append(90)
                                                                   h=g*90
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='P':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Paneer Spring Roll ')
                                                                   o.append(g)
                                                                   p.append(100)
                                                                   h=g*100
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='C':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Chinese Spring Roll ')
                                                                   o.append(g)
                                                                   p.append(90)
                                                                   h=g*90
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='V':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Chilli Veggie Spring Roll ')
                                                                   o.append(g)
                                                                   p.append(90)
                                                                   h=g*90
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        else :
                                                                   print('invalid ')
                                             elif e=='N':
                                                        menuNS()
                                                        f=input('what would you like to have , Sir (use capital letters )')
                                                        if f=='E':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Egg Sping Roll ')
                                                                   o.append(g)
                                                                   p.append(100)
                                                                   h=g*100
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='C':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Chicken Sping Roll ')
                                                                   o.append(g)
                                                                   p.append(110)
                                                                   h=g*110
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='P':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Prawn Spring Roll ')
                                                                   o.append(g)
                                                                   p.append(120)
                                                                   h=g*120
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='N':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Chicken and Prawn Spring Roll ')
                                                                   o.append(g)
                                                                   p.append(80)
                                                                   h=g*80
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        elif f=='R':
                                                                   g=int(input('How many would plates you like to have:'))
                                                                   n.append('Pork Spring Roll ')
                                                                   o.append(g)
                                                                   p.append(130)
                                                                   h=g*130
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                        else :
                                                                   print('invalid ')

                                             else:
                                                        print ('Invalid entery')
                                             k=int(input('do you want somethink else 0-yes/1-no'))
                                             a=a+k 
           elif c==2:
                      menu12()
                      b=int(input('what would you like to have , Sir '))
                      if b==1:
                                 
                                 d=0
                                 while d==0:
                                            
                                            veg_nonveg()
                                            e=input('what would you prefer , Sir (use capital letters )')
                                            if e=='V':
                                                       
                                                       menuSV()
                                                       f=input('what would you like to have , Sir (use capital letters )')
                                                       if f=='T':
                                                                  g=int(input('How many would you like to have:'))
                                                                  n.append('Tomato Soup ')
                                                                  o.append(g)
                                                                  p.append(79)
                                                                  h=g*79
                                                                  print('Total price :',h)
                                                                  cost=cost+h
                                                                  m=int(input('do you want somethink else 0-yes/1-no'))
                                                                  d=d+m
                                                       elif f=='M':
                                                                  g=int(input('How many would you like to have:'))
                                                                  n.append('Mushroom Soup ')
                                                                  o.append(g)
                                                                  p.append(89)
                                                                  h=g*89
                                                                  print('Total price :',h)
                                                                  cost=cost+h
                                                                  m=int(input('do you want somethink else 0-yes/1-no'))
                                                                  d=d+m
                                                       elif f=='O':
                                                                   g=int(input('How many would you like to have:'))
                                                                   n.append('Carrot Mushroom Soup ')
                                                                   o.append(g)
                                                                   p.append(89)
                                                                   h=g*89
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                       elif f=='S':
                                                                   g=int(input('How many would you like to have:'))
                                                                   n.append('Sweet Corn Soup ')
                                                                   o.append(g)
                                                                   p.append(89)
                                                                   h=g*89
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                       elif f=='C':
                                                                   g=int(input('How many would you like to have:'))
                                                                   n.append('Manchow Soup ')
                                                                   o.append(g)
                                                                   p.append(89)
                                                                   h=g*89
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                       else :
                                                                  print('invalid ')
                                            elif e=='N':
                                                       menuSN()
                                                       f=input('what would you like to have , Sir (use capital letters )')
                                                       if f=='T':
                                                                  g=int(input('How many would you like to have:'))
                                                                  n.append('Chicken Hot N Sour Soup ')
                                                                  o.append(g)
                                                                  p.append(98)
                                                                  h=g*98
                                                                  print('Total price :',h)
                                                                  cost=cost+h
                                                                  m=int(input('do you want somethink else 0-yes/1-no'))
                                                                  d=d+m
                                                       elif f=='M':
                                                                  g=int(input('How many would you like to have:'))
                                                                  n.append('Chicken Mushroom Soup ')
                                                                  o.append(g)
                                                                  p.append(98)
                                                                  h=g*98
                                                                  print('Total price :',h)
                                                                  cost=cost+h
                                                                  m=int(input('do you want somethink else 0-yes/1-no'))
                                                                  d=d+m
                                                       elif f=='O':
                                                                   g=int(input('How many would you like to have:'))
                                                                   n.append('Chicken Manchow Soup ')
                                                                   o.append(g)
                                                                   p.append(98)
                                                                   h=g*88
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                       elif f=='S':
                                                                   g=int(input('How many would you like to have:'))
                                                                   n.append('Chicken Talumin Soup ')
                                                                   o.append(g)
                                                                   p.append(89)
                                                                   h=g*89
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                       elif f=='C':
                                                                   g=int(input('How many would you like to have:'))
                                                                   n.append('Chicken Sweet Corn Soup ')
                                                                   o.append(g)
                                                                   p.append(80)
                                                                   h=g*98
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                       else :
                                                                  print('invalid ')
                      
                      elif b==2:
                                 d=0
                                 while d==0:
                                            menuSl()
                                            f=input('what would you like to have , Sir (use capital letters )')
                                            if f=='P':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Punjabi Salad  ')
                                                       o.append(g)
                                                       p.append(25)
                                                       h=g*25
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='O':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Onion Salad ')
                                                       o.append(g)
                                                       p.append(30)
                                                       h=g*30
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='C':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Chumbar Salad ')
                                                       o.append(g)
                                                       p.append(32)
                                                       h=g*32
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='M':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Mix Salad ')
                                                       o.append(g)
                                                       p.append(30)
                                                       h=g*30
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='A':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Apple Cabbage Salad ')
                                                       o.append(g)
                                                       p.append(35)
                                                       h=g*30
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            else :
                                                       print('invalid ')
                      elif b==3:
                                 d=0
                                 while d==0:
                                            menuR()
                                            f=input('what would you like to have , Sir (use capital letters )')
                                            if f=='M':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Mixed Raita ')
                                                       o.append(g)
                                                       p.append(20)
                                                       h=g*20
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='P':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Pineapple Raita ')
                                                       o.append(g)
                                                       p.append(22)
                                                       h=g*22
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='B':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Boondi Raita ')
                                                       o.append(g)
                                                       p.append(25)
                                                       h=g*25
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='C':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Plain curd')
                                                       o.append(g)
                                                       p.append(20)
                                                       h=g*20
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='F':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Fruity Raita ')
                                                       o.append(g)
                                                       p.append(30)
                                                       h=g*30
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            else :
                                                       print('invalid ')
                      elif b==4:
                                 d=0
                                 while d==0:
                                            
                                            veg_nonveg()
                                            e=input('what would you prefer , Sir (use capital letters )')
                                            if e=='V':
                                                       menuVMa()
                                                       f=input('what would you like to have , Sir (use capital letters )')
                                                       if f=='P':
                                                                  g=int(input('How many would you like to have:'))
                                                                  n.append('Palak paneer ')
                                                                  o.append(g)
                                                                  p.append(180)
                                                                  h=g*180
                                                                  print('Total price :',h)
                                                                  cost=cost+h
                                                                  m=int(input('do you want somethink else 0-yes/1-no'))
                                                                  d=d+m
                                                       elif f=='D':
                                                                  g=int(input('How many would you like to have:'))
                                                                  n.append('Dal Fry Kolhapuri ')
                                                                  o.append(g)
                                                                  p.append(150)
                                                                  h=g*150
                                                                  print('Total price :',h)
                                                                  cost=cost+h
                                                                  m=int(input('do you want somethink else 0-yes/1-no'))
                                                                  d=d+m
                                                       elif f=='S':
                                                                  g=int(input('How many would you like to have:'))
                                                                  n.append('Veg Seek Masala')
                                                                  o.append(g)
                                                                  p.append(190)
                                                                  h=g*190
                                                                  print('Total price :',h)
                                                                  cost=cost+h
                                                                  m=int(input('do you want somethink else 0-yes/1-no'))
                                                                  d=d+m
                                                       elif f=='H':
                                                                  g=int(input('How many would you like to have:'))
                                                                  n.append('Mushroom Mutter Hara Payaz  ')
                                                                  o.append(g)
                                                                  p.append(200)
                                                                  h=g*200
                                                                  print('Total price :',h)
                                                                  cost=cost+h
                                                                  m=int(input('do you want somethink else 0-yes/1-no'))
                                                                  d=d+m
                                                       elif f=='M':
                                                                  g=int(input('How many would you like to have:'))
                                                                  n.append('Mix Veg  ')
                                                                  o.append(g)
                                                                  p.append(170)
                                                                  h=g*170
                                                                  print('Total price :',h)
                                                                  cost=cost+h
                                                                  m=int(input('do you want somethink else 0-yes/1-no'))
                                                                  d=d+m
                                                       elif f=='R':
                                                                  g=int(input('How many would you like to have:'))
                                                                  n.append('Mushroom Kadai ')
                                                                  o.append(g)
                                                                  p.append(180)
                                                                  h=g*180
                                                                  print('Total price :',h)
                                                                  cost=cost+h
                                                                  m=int(input('do you want somethink else 0-yes/1-no'))
                                                                  d=d+m
                                                       elif f=='L':
                                                                  g=int(input('How many would you like to have:'))
                                                                  n.append('Paneer Malai Kofta ')
                                                                  o.append(g)
                                                                  p.append(230)
                                                                  h=g*230
                                                                  print('Total price :',h)
                                                                  cost=cost+h
                                                                  m=int(input('do you want somethink else 0-yes/1-no'))
                                                                  d=d+m
                                                       elif f=='B':
                                                                   g=int(input('How many would you like to have:'))
                                                                   n.append('Paneer Butter Masala ')
                                                                   o.append(g)
                                                                   p.append(200)
                                                                   h=g*200
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                       elif f=='K':
                                                                   g=int(input('How many would you like to have:'))
                                                                   n.append('Kadai Paneer')
                                                                   o.append(g)
                                                                   p.append(190)
                                                                   h=g*190
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                       elif f=='C':
                                                                   g=int(input('How many would you like to have:'))
                                                                   n.append('Paneer Chatpata  ')
                                                                   o.append(g)
                                                                   p.append(190)
                                                                   h=g*190
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                       else :
                                                                  print('invalid ')
                                            elif e=='N':
                                                       menuNMa()
                                                       f=input('what would you like to have , Sir (use capital letters )')
                                                       if f=='C':
                                                                  g=int(input('How many would you like to have:'))
                                                                  n.append('Murg Cheez Masala')
                                                                  o.append(g)
                                                                  p.append(300)
                                                                  h=g*300
                                                                  print('Total price :',h)
                                                                  cost=cost+h
                                                                  m=int(input('do you want somethink else 0-yes/1-no'))
                                                                  d=d+m
                                                       elif f=='H':
                                                                  g=int(input('How many would you like to have:'))
                                                                  n.append('Murg Hydrabadi ')
                                                                  o.append(g)
                                                                  p.append(280)
                                                                  h=g*280
                                                                  print('Total price :',h)
                                                                  cost=cost+h
                                                                  m=int(input('do you want somethink else 0-yes/1-no'))
                                                                  d=d+m
                                                                  
                                                       elif f=='L':
                                                                  g=int(input('How many would you like to have:'))
                                                                  n.append('Murg Laziz  ')
                                                                  o.append(g)
                                                                  p.append(290)
                                                                  h=g*290
                                                                  print('Total price :',h)
                                                                  cost=cost+h
                                                                  m=int(input('do you want somethink else 0-yes/1-no'))
                                                                  d=d+m
                                                       elif f=='B':
                                                                  g=int(input('How many would you like to have:'))
                                                                  n.append('Butter Chicken  ')
                                                                  o.append(g)
                                                                  p.append(280)
                                                                  h=g*280
                                                                  print('Total price :',h)
                                                                  cost=cost+h
                                                                  m=int(input('do you want somethink else 0-yes/1-no'))
                                                                  d=d+m
                                                       elif f=='T':
                                                                  g=int(input('How many would you like to have:'))
                                                                  n.append('Murg Tikka  ')
                                                                  o.append(g)
                                                                  p.append(290)
                                                                  h=g*290
                                                                  print('Total price :',h)
                                                                  cost=cost+h
                                                                  m=int(input('do you want somethink else 0-yes/1-no'))
                                                                  d=d+m
                                                       elif f=='A':
                                                                  g=int(input('How many would you like to have:'))
                                                                  n.append('Prawans Adaraki Masala ')
                                                                  o.append(g)
                                                                  p.append(350)
                                                                  h=g*350
                                                                  print('Total price :',h)
                                                                  cost=cost+h
                                                                  m=int(input('do you want somethink else 0-yes/1-no'))
                                                                  d=d+m
                                                       elif f=='K':
                                                                  g=int(input('How many would you like to have:'))
                                                                  n.append('Prawans Kholapuri Masala ')
                                                                  o.append(g)
                                                                  p.append(380)
                                                                  h=g*380
                                                                  print('Total price :',h)
                                                                  cost=cost+h
                                                                  m=int(input('do you want somethink else 0-yes/1-no'))
                                                                  d=d+m
                                                       elif f=='M':
                                                                   g=int(input('How many would you like to have:'))
                                                                   n.append('Murg Handi ')
                                                                   o.append(g)
                                                                   p.append(290)
                                                                   h=g*290
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                       elif f=='S':
                                                                   g=int(input('How many would you like to have:'))
                                                                   n.append('Murg Musselum  ')
                                                                   o.append(g)
                                                                   p.append(380)
                                                                   h=g*380
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                       elif f=='U':
                                                                   g=int(input('How many would you like to have:'))
                                                                   n.append('Murg Masala ')
                                                                   o.append(g)
                                                                   p.append(280)
                                                                   h=g*280
                                                                   print('Total price :',h)
                                                                   cost=cost+h
                                                                   m=int(input('do you want somethink else 0-yes/1-no'))
                                                                   d=d+m
                                                       else :
                                                                  print('invalid ')
                      elif b==5:
                                 d=0
                                 while d==0:
                                            menuRo()
                                            f=input('what would you like to have , Sir (use capital letters )')
                                            if f=='B':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Butter Roti ')
                                                       o.append(g)
                                                       p.append(10)
                                                       h=g*10
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='N':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Butter Naan  ')
                                                       o.append(g)
                                                       p.append(30)
                                                       h=g*30
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='G':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Garlic Naan ')
                                                       o.append(g)
                                                       p.append(40)
                                                       h=g*40
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='K':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Kashmiri Naan ')
                                                       o.append(g)
                                                       p.append(50)
                                                       h=g*50
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='R':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Rumali Naan ')
                                                       o.append(g)
                                                       p.append(10)
                                                       h=g*10
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='M':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Missi Roti ')
                                                       o.append(g)
                                                       p.append(30)
                                                       h=g*30
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='S':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Khasta Roti ')
                                                       o.append(g)
                                                       p.append(30)
                                                       h=g*30
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='C':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Chur Chur Naan ')
                                                       o.append(g)
                                                       p.append(40)
                                                       h=g*40
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='L':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Plain Naan  ')
                                                       o.append(g)
                                                       p.append(25)
                                                       h=g*25
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='P':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Paneer Paratha ')
                                                       o.append(g)
                                                       p.append(50)
                                                       h=g*50
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            else :
                                                       print('invalid ')
                                 else:
                                            
                                            print('invalid')
                                 k=int(input('do you want somethink else 0-yes/1-no'))
                                 a=a+k
           elif  c==3:
                      menu13()
                      b=int(input('what would you like to have , Sir '))
                      if b==1:
                                 d=0
                                 while d==0:
                                            menuC()
                                            f=input('what would you like to have , Sir (use capital letters )')
                                            if f=='R':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Red Valvet Cake ')
                                                       o.append(g)
                                                       p.append(300)
                                                       h=g*300
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='B':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Black Forest Cake  ')
                                                       o.append(g)
                                                       p.append(290)
                                                       h=g*290
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='C':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Chocolate Cake ')
                                                       o.append(g)
                                                       p.append(280)
                                                       h=g*280
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='P':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Pineapple Cake   ')
                                                       o.append(g)
                                                       p.append(270)
                                                       h=g*270
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='E':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Cheese Cake  ')
                                                       o.append(g)
                                                       p.append(275)
                                                       h=g*275
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='S':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Butterscotch Cake ')
                                                       o.append(g)
                                                       p.append(375)
                                                       h=g*375
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='T':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Chocolate truffle Cake ')
                                                       o.append(g)
                                                       p.append(300)
                                                       h=g*300
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='R':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Strawberry Cake ')
                                                       o.append(g)
                                                       p.append(250)
                                                       h=g*250
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='F':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Chiffon Cake ')
                                                       o.append(g)
                                                       p.append(230)
                                                       h=g*230
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='U':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Cup Cake')
                                                       o.append(g)
                                                       p.append(200)
                                                       h=g*200
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            else :
                                                       print('invalid ')  
                      elif b==2:
                                 d=0
                                 while d==0:
                                            menuI()
                                            f=input('what would you like to have , Sir (use capital letters )')
                                            if f=='V':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Vanilla Ice Cream ')
                                                       o.append(g)
                                                       p.append(190)
                                                       h=g*190
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='C':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Chocolate Ice Cream ')
                                                       o.append(g)
                                                       p.append(180)
                                                       h=g*180
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='S':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Strawberry Ice Cream ')
                                                       o.append(g)
                                                       p.append(160)
                                                       h=g*160
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='M':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Matcha Ice Cream ')
                                                       o.append(g)
                                                       p.append(150)
                                                       h=g*150
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='T':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Taro Ice Cream ')
                                                       o.append(g)
                                                       p.append(200)
                                                       h=g*200
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='B':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Blue Berry Ice Cream ')
                                                       o.append(g)
                                                       p.append(210)
                                                       h=g*210
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='N':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('MacaDimia Nut Ice Cream ')
                                                       o.append(g)
                                                       p.append(220)
                                                       h=g*220
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='L':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Malai Kulfi ')
                                                       o.append(g)
                                                       p.append(150)
                                                       h=g*150
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='O':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Mango Kulfi ')
                                                       o.append(g)
                                                       p.append(170)
                                                       h=g*170
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='K':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Black sasame Ice Cream ')
                                                       o.append(g)
                                                       p.append(200)
                                                       h=g*200
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            else :
                                                       print('invalid ')
                      elif b==3:
                                 d=0
                                 while d==0:
                                            menuIS()
                                            f=input('what would you like to have , Sir (use capital letters )')
                                            if f=='R':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Rasmalai ')
                                                       o.append(g)
                                                       p.append(200)
                                                       h=g*200
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='G':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Gulab Jamun ')
                                                       o.append(g)
                                                       p.append(300)
                                                       h=g*300
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='H':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Gajar Ka Halawa ')
                                                       o.append(g)
                                                       p.append(400)
                                                       h=g*400
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='R':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Rice Kheer ')
                                                       o.append(g)
                                                       p.append(150)
                                                       h=g*150
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            elif f=='M':
                                                       g=int(input('How many would you like to have:'))
                                                       n.append('Mango Lassi ')
                                                       o.append(g)
                                                       p.append(100)
                                                       h=g*100
                                                       print('Total price :',h)
                                                       cost=cost+h
                                                       m=int(input('do you want somethink else 0-yes/1-no'))
                                                       d=d+m
                                            else :
                                                       print('invalid ')

                      else:
                                print('invalid')
           print('1:Starter Food ')
           print('2:Main course Dishes')
           print('3:Dessert Food ')
           k=int(input('do you like to have something else(1-no/0-yes)'))
           a=a+k
#bill           
           elif b==0:
                      while v==1:
                                 v=v-1
                                 pas=int(input('Enter Password'))
                                 if pas==1234:
                                            while u==1:
                                                       print('Welcome to staff Panel')
                                                       print('1:Monthly Sales Data')
                                                       print('2:Employee Details')
                                                       print('3:Recent Sales')
                                                       print('4:Back')
                                                       sales=pd.read_csv('D:\\ip project\\resturant billing system\\sales.csv')
                                                       c1=int(input('Enter your choice:'))
                                                       if c1==1:
                                                                  c2=int(input('Enter your choice:'))
                                                                  if c2==1:
                                                                             
                                                                             tsales=sales['TotalSales']
                                                                             tsales=list(tsales)
                                                                             ts=tsales[0:12]
                                                                             psales=sales['TotalPurchase']
                                                                             psales=list(psales)
                                                                             ps=psales[0:12]
                                                                             months=['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec']
                                                                             g=plt.plot(month,ts)
                                                                             plt.show()
                                                                             a=int(input('See more........yes-1/no-0'))
                                                                  elif c1==2:
                                                                             print(sales)
                                                                             a=int(input('See more........yes-1/no-0'))
                                                                  else:
                                                                             print('Invalid Entry')
                                                                             a=int(input('See more........yes-1/no-0'))
                                                       elif c1==2:
                                                                  b=pd.read_csv('D:\\ip project\\resturant billing system\\bill.csv')
                                                                  print(b)
                                                                  a=int(input('See more........yes-1/no-0'))
                                                       elif c1==3:
                                                                  e=pd.read_csv('D:\\ip project\\resturant billing system\\bill.csv')
                                                                  print()
                                                                  print('-----------------')
                                                                  print()
                                                                  a=int(input('See more........yes-1/no-0'))
                                                       else:
                                                                  print('Invalid Entry')
                                                                  a=int(input('See more........yes-1/no-0'))
                                             else:
                                                       f=int(input('incorrect password......... /ntry again-1 or back10'))
                                                       if f==1:
                                                                  v=f
                                                       elif f==0:
                                                                  w=f
                                                       else:
                                                                  print('invalid Entry')
CR()                         
           
                                 
                                 
                                            
                      
                      
                                            

























                                                        

#CARPENTER'S PROJECT
n=int(input('Number of Pieces of wood:'))
x=int(input('x:'))#dimension of piece of wood
y=int(input('y:'))#dimension of piece of wood
z=int(input('z:'))#dimension of piece of wood


m=int(input('Number of boxes:'))#no of boxes expected


choice=int(input("user choice:"))#enter a choice for dimensions
if(choice==1):
    p=int(input())#dimensions of box m
    q=int(input())#dimensions of box m
    r=int(input())#dimensions of box m
else:
    p=5#random value
    q=5#random value
    r=5#random value

if(p>x or q>y or r>z):
    print('No box can be formed')
else:
    tot_vol = x*y*(n*z)#volume of Pieces of wood         
    req_vol=p*q*r #volume of each box                     
    boxes=tot_vol//req_vol #it will provide no of boxes    
    remainingWood=tot_vol%req_vol #remaining wood after creating box if possible   
    print('Total no. of boxes:',end="")
    print(boxes)
    print('Leftover amount of wood:',end="")
    print(remainingWood)
    if(boxes>m):#if we got more boxes as expected before creation of boxes,then additional boxes can be calculated
        MoreBox=boxes-m   
        print('Additional boxes formed:',end="")
        print(MoreBox)

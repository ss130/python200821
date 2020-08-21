import random
import turtle

def t():
     b=turtle.Turtle()
     b.color('white')
     b.shape('turtle')
     a=turtle.Turtle()
     a.color('white')
     a.shape('turtle')
     screen=turtle.Screen()
     screen.bgcolor('black')
     turtle.done
     
     for i in range(1,180):
         b.right(2)
         b.forward(2)
         a.right(3)
         a.forward(2)
     for i in range(1,360):
         a.right(1)
         a.forward(2)
     

while True:
    print('歡迎來到猜數字')
    print('1.開始游戲')
   
    option=input('輸入選項:')
    
    if option=='1':
        
        num=random.randint(1,9)
        i=0
        while i<5:
            ans=int(input("請輸入數字:"))
            if ans == num:
                print("恭喜答對!!!")
                print('==按下方視窗看獎勵==')
                t()
                break
            elif ans <= num:
                print("bigger")
            elif ans >= num:
                print("smaller")             
i=i+1
    
       
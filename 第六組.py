print('烏龜小隊')
print('1.電腦猜數字')
print('2.猜數字看烏龜')
print('3.turtle畫麥塊')
m = input('要哪一個就打幾號:')
if m=='1':
    from time import sleep
    print('歡迎到電腦猜數字')
    print('1.1~32')
    print('2.1~64')
    print('3.1~128')
    n = input('你要多大的數字，就選幾號。')
    if n == '1':
        Q1 = []
        Q2 = []
        Q3 = []
        Q4 = []
        Q5 = []
        for binNum in range(1,32):
            binStr = format(binNum,'05b')
        
            if binStr[-1] == '1':
                Q1.append(binNum)
        
            if binStr[-2] == '1':
                Q2.append(binNum)
        
            if binStr[-3] == '1':
                Q3.append(binNum)
    
            if binStr[-4] == '1':
                Q4.append(binNum)
        
            if binStr[-5] == '1':
                Q5.append(binNum)
        ans = 0
        print('想一個數字')
        sleep(5)
        print(Q1)
        a = input("y/n: ")
        if a == 'y':
            ans = ans +1
        print(Q2)
        b = input("y/n: ")
        if b == 'y':
            ans = ans +2
        print(Q3)
        c = input("y/n: ")
        if c == 'y':
                ans = ans + 4
        print(Q4)
        d = input("y/n: ")
        if d == 'y':
                ans = ans+8
        print(Q5)
        e = input("y/n: ")
        if e == 'y':
                ans = ans+ 16
        print("The Number in Your Mind is {}".format(ans))
    elif n =='2':
        Q1 = []
        Q2 = []
        Q3 = []
        Q4 = []
        Q5 = []
        Q6 = []
        for i in range(32,63):
            Q6.append(i)
        
        for binNum in range(1,64):
            binStr = format(binNum,'05b')
        
            if binStr[-1] == '1':
                Q1.append(binNum)
        
            if binStr[-2] == '1':
                Q2.append(binNum)
        
            if binStr[-3] == '1':
                Q3.append(binNum)
    
            if binStr[-4] == '1':
                Q4.append(binNum)
        
            if binStr[-5] == '1':
                Q5.append(binNum)
        
        ans = 0
        print(Q1)
        a = input("y/n: ")
        if a == 'y':
            ans = ans +1
        print(Q2)
        b = input("y/n: ")
        if b == 'y':
            ans = ans +2
        print(Q3)
        c = input("y/n: ")
        if c == 'y':
            ans = ans + 4
        print(Q4)
        d = input("y/n: ")
        if d == 'y':
            ans = ans+8
        print(Q5)
        e = input("y/n: ")
        if e == 'y':
            ans = ans+ 16
        print(Q6)
        f = input("y/n: ")
        if f == 'y':
            ans = ans+ 32
        print("The Number in Your Mind is {}".format(ans))
    else:
        Q1 = []
        Q2 = []
        Q3 = []
        Q4 = []
        Q5 = []
        Q6 = []
        Q7 = []
        for i in range(32,63):
            Q6.append(i)
        for j in range(64,128):
            Q7.append(j)
        for k in range(96,128):
            Q6.append(k)
        for binNum in range(1,128):
            binStr = format(binNum,'05b')
            
            if binStr[-1] == '1':
                Q1.append(binNum)
            
            if binStr[-2] == '1':
                Q2.append(binNum)
            
            if binStr[-3] == '1':
                Q3.append(binNum)
        
            if binStr[-4] == '1':
                Q4.append(binNum)
            
            if binStr[-5] == '1':
                Q5.append(binNum)
        ans = 0
        print(Q1)
        a = input("y/n: ")
        if a == 'y':
            ans = ans +1
        print(Q2)
        b = input("y/n: ")
        if b == 'y':
            ans = ans +2
        print(Q3)
        c = input("y/n: ")
        if c == 'y':
            ans = ans + 4
        print(Q4)
        d = input("y/n: ")
        if d == 'y':
            ans = ans+8
        print(Q5)
        e = input("y/n: ")
        if e == 'y':
            ans = ans+ 16
        print(Q6)
        e = input("y/n: ")
        if e == 'y':
            ans = ans+ 32
        print(Q7)
        e = input("y/n: ")
        if e == 'y':
            ans = ans+ 64
        print("The Number in Your Mind is {}".format(ans))
elif m=='2':
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
         
         
         for i in range(1,180):
             b.right(2)
             b.forward(2)
             a.right(3)
             a.forward(2)
         for i in range(1,360):
             a.right(1)
             a.forward(2)
         turtle.done()
    
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
        
           


else:
    import turtle
    screen = turtle.Screen()
    
    a = turtle.Turtle()
    a.pensize(5)
    
    a.forward(50)
    a.left(90)
    a.forward(70)
    a.left(90)
    a.forward(50)
    a.left(90)
    a.forward(70)
    
    a.right(90)
    a.forward(50)
    a.right(90)
    a.forward(70)
    a.right(90)
    a.forward(100)
    
    a.left(90)
    a.forward(130)
    a.left(90)
    a.forward(100)
    a.left(90)
    a.forward(130)
    a.left(90)
    
    a.forward(150)
    a.left(90)
    a.forward(130)
    a.left(90)
    a.forward(50)
    a.left(90)
    a.forward(130)
    
    a.right(90)
    a.forward(150)
    a.right(90)
    a.forward(130)
    a.right(90)
    a.forward(45)
    
    a.forward(100)
    a.left(90)
    a.forward(100)
    a.left(90)
    a.forward(100)
    a.left(90)
    a.forward(100)
    
    a.right(180)
    a.forward(60)
    a.right(90)
    a.forward(40)
    a.left(90)
    a.forward(20)
    a.left(90)
    a.forward(40)
    a.right(90)
    a.forward(20)
    a.right(90)
    a.forward(100)
    a.right(90)
    a.forward(20)
    a.right(90)
    a.forward(40)
    a.left(90)
    a.forward(20)
    a.left(90)
    a.forward(40)
    
    
    
    
    
   
    turtle.done()
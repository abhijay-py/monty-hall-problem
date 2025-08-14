import random
z = [1,2,1]
t = ["a","b"]
u = ["b","c"]
v = ["a","c"]
f = 1
g = 1
Prob_Num = 0
Prob_Den = 0
TotalProb = 0
while f == 1:
     a = random.choice(z)
     a = int(a)
     if a == 1:
         y = [2,1]
         b = random.choice(y)
         b = int(b)
         if b == 2:
             c = 1
         else:
             c = 2
     else:
         b = 1
         c = 1
     d = input("Which door do you choose? a, b, or c: ")
     d = str(d)
     if d == "a":
         d = a
         if a == 2:
             rand_1 = random.choice(u)
             print(f"Door {rand_1} is empty.")
             h = input("Do you want to stay or change? Press 1 to stay and press 0 to switch doors: ")
             h = int(h)
             if rand_1 == "b" and h == 0:
                 d = c
             elif h == 0:
                 d = b
         elif b == 2:
             print("Door c is empty.")
             h = input("Do you want to stay or change? Press 1 to stay and press 0 to switch doors: ")
             h = int(h)
             if h == 0:
                 d = b
         else:
             print("Door b is empty.")
             h = input("Do you want to stay or change? Press 1 to stay and press 0 to switch doors: ")
             h = int(h)
             if h == 0:
                 d = c
     elif d == "b":
         d = b
         if b == 2:
             rand_1 = random.choice(v)
             print(f"Door {rand_1} is empty.")
             h = input("Do you want to stay or change? Press 1 to stay and press 0 to switch doors: ")
             h = int(h)
             if rand_1 == "c" and h == 0:
                 d = a
             elif h == 0:
                 d = c
         elif a == 2:
             print("Door c is empty.")
             h = input("Do you want to stay or change? Press 1 to stay and press 0 to switch doors: ")
             h = int(h)
             if h == 0:
                 d = a
         else:
             print("Door a is empty.")
             h = input("Do you want to stay or change? Press 1 to stay and press 0 to switch doors: ")
             h = int(h)
             if h == 0:
                 d = c
     elif d == "c":
         d = c
         if c == 2:
             rand_1 = random.choice(t)
             print("Door "+rand_1+" is empty.")
             h = input("Do you want to stay or change? Press 1 to stay and press 0 to switch doors: ")
             h = int(h)
             if rand_1 == "b" and h == 0:
                 d = a
             elif h == 0:
                 d = b
         elif b == 2:
             print("Door a is empty.")
             h = input("Do you want to stay or change? Press 1 to stay and press 0 to switch doors: ")
             h = int(h)
             if h == 0:
                 d = b
         else:
             print("Door b is empty.")
             h = input("Do you want to stay or change? Press 1 to stay and press 0 to switch doors: ")
             h = int(h)
             if h == 0:
                 d = a
     if d == 2:
         Prob_Num = Prob_Num+1
         print("There was a car behind your door!")
     else :
         print("There was nothing behind your door!")
     Prob_Den = Prob_Den+1
     Prob_Den = float(Prob_Den)
     Prob_Num = float(Prob_Num)
     TotalProb = Prob_Num/Prob_Den
     TotalProb = float(TotalProb)
     TotalProb = str(TotalProb)
     print(f"Total Probability so far: {TotalProb}")
     TotalProb = float(TotalProb)
     g = input("Do you want to continue? Press 1 to continue and 0 to end: ")
     g = float(g)
     if g == 0:
         f = 0
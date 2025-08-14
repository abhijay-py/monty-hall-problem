import random
z = [1,2,1]
t = ["a","b"]
u = ["b","c"]
v = ["a","c"]
f = 1
g = 1
Choice = ["a","b","c"]
Prob_Num = 0
Prob_Den = 0
TotalProb = 0
times = 0
Prob_Num2 = 0
Prob_Den2 = 0
TotalProb2 = 0
Switch = 0
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
     d = random.choice(Choice)
     d = str(d)
     if d == "a":
         d = a
         if a == 2:
             rand_1 = random.choice(u)
             h = Switch
             h = int(h)
             if rand_1 == "b" and h == 0:
                 d = c
             elif h == 0:
                 d = b
         elif b == 2:
             h = Switch
             h = int(h)
             if h == 0:
                 d = b
         else:
             h = Switch
             h = int(h)
             if h == 0:
                 d = c
     elif d == "b":
         d = b
         if b == 2:
             rand_1 = random.choice(v)
             h = Switch
             h = int(h)
             if rand_1 == "c" and h == 0:
                 d = a
             elif h == 0:
                 d = c
         elif a == 2:
             h = Switch
             h = int(h)
             if h == 0:
                 d = a
         else:
             h = Switch
             h = int(h)
             if h == 0:
                 d = c
     elif d == "c":
         d = c
         if c == 2:
             rand_1 = random.choice(t)
             h = Switch
             h = int(h)
             if rand_1 == "b" and h == 0:
                 d = a
             elif h == 0:
                 d = b
         elif b == 2:
             
             h = Switch
             h = int(h)
             if h == 0:
                 d = b
         else:
             h = Switch
             h = int(h)
             if h == 0:
                 d = a
     if d == 2 and Switch == 0:
         Prob_Num = Prob_Num+1
     if Switch == 0:
         Prob_Den = Prob_Den+1
         Prob_Den = float(Prob_Den)
         Prob_Num = float(Prob_Num)
         TotalProb = Prob_Num/Prob_Den
         TotalProb = float(TotalProb)
         times = times+1
     if d == 2 and Switch == 1:
         Prob_Num2 = Prob_Num2 +1
     if Switch == 1:
         Prob_Den2 = Prob_Den2+1
         Prob_Den2 = float(Prob_Den2)
         Prob_Num2 = float(Prob_Num2)
         TotalProb2 = Prob_Num2/Prob_Den2
         TotalProb2 = float(TotalProb2)
         times = times+1
     if times == 1000000:
         TotalProb = str(TotalProb)
         print "The final Probability for switching is "+TotalProb+"!"
         TotalProb2 = str(TotalProb2)
         print "The final Probability for staying is "+TotalProb2+"!"
         f = 0
     if times == 500000:
         Switch = 1
 
     
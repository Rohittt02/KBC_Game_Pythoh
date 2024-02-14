import random
a=[").what is capital of india",
").he is my friend",
").wich companey has shut down its smart phone business",
").who is father of nation of india",
").wich animal is called king of junggle",
").wich is the longest river in india",
").what is taught in navgurukul",
").national language of india",
").national fruit of india",
").national sweet of india",
"(switch Qustion).what is my name "]

b=[["1>.himachal","2>.punjab","3>.dillhi","4>.hariyana","5>.life-line"],
["1>.Shrwan","2>.Tausif","3>.Choopa","4>.Ajay meena","5>.life-line"],
["1>.vivo","2>.lg","3>.oppo","4>.sumsung","5>.life-line"],
["1>.gandhi","2>.nehru","3>.bhim","4>.kabir","5>.life-line"],
["1>.lion","2>.rabbit","3>.tiger","4>.cammal","5>.life-line"],
["1>.ganga","2>.nil","3>.satlaj","4>.bhagirathi","5>.life-line"],
["1>.python","2>.coding","3>.manejment","4>.html","5>.life-line"],["1>.english","2>.hindi","3>.urdu","4>.tamil","5>.life-line"],
["1>.mango","2>.littchi","3>.banana","4>.guava","5>.life-line"],
["1>.rasgulle","2>.peda","3>jalebi","4>laddu","5>.life-line"],
["1>.monu","2>.Rohit","3>.Sharwan","4>.choopa"]]

c=[3,4,2,1,1,1,2,2,1,3,2]
life=["1).50-50","2).phone of friend","3).audiance poll","4).switch question"]

life1=[["3>.delhi","1>.himachal"],["3>.bhumesh","4>.akash"],["2>.lg","3>.oppo"],
["1>.gandhi","2>.nehru"],["1>.lion","2>.rabbit"],
["1>.ganga","3>.satlaj"],["2>.coding","3>.manejment"],["2>.hindi","3>.urdu"],["1>.mango","4>.guava"],
["3>jalebi","4>laddu"]]
d=50000
l1=0
l2=0
l3=0
l4=0
m=1
while m>0:
    m2=random.randint(1,101)
    m3=random.randint(1,101)
    m4=random.randint(1,101)
    m5=random.randint(1,101)
    if m2+m3+m4+m5==100:
        break
    else:1
    m=m+1
lis=[0,1,2,3,4,5,6,7,8,9]

for i1 in range (len(a)):
    d=d*2
    print('\033[37m',"*).this question for amount=",d,'\033[0m')
    i=random.choice(lis)
    print('\033[33m',str(i1+1)+a[i],'\033[0m')
    print()
    lis.remove(i)
    for j in  (b[i]):
        print(j)
    print('\033[41m',"chose_option :-enter",'\033[0m')
    n=int(input())
    if n==5:
        if l1==1:
            print('\033[42m',"allready used by-50-50",'\033[0m')
        if l2==1:
            print('\033[42m',"allready used by phone a friend",'\033[0m')
        if l3==1:
            print('\033[42m',"allready used by audiance-poll",'\033[0m')
        if l4==1:
            print('\033[42m',"allready used by switch question",'\033[0m')
        for a1 in (life):
            print('\033[28m',a1,'\033[0m')
        l=int(input("enter your choice: "))
        #..50-50_life_line
        if l==1 and l1<1:
            for j in life1[i]:
                print(j)
            v = int(input("enter your answer: "))
            l1+=1
            life.remove("1).50-50")
            n=v
        #..phone of friend..
        elif l == 2 and l2<1:
            print('\033[45m','Your friend suggest',c[i],'\033[0m')
            v=int(input('enter your answer'))
            l2+=1
            life.remove("2).phone of friend")
            n=v
            print()
        #audiance poll
        elif l==3 and l3<1:
            print('\033[39m',str(m2)+'% audiance want option 1>','\033[0m')
            print('\033[39m',str(m3)+'% audiance want option 2>','\033[0m')
            print('\033[39m',str(m4)+'% audiance want option 3>','\033[0m')
            print('\033[39m',str(m5)+'% audiance want option 4>','\033[0m')
            v=int(input('enter your answear'))
            l3+=1
            life.remove("3).audiance poll")
            n=v
            print()
        #..switch-question..
        elif l==4 and l4<1:
            i=10
            print(a[i])
            print()
            for j in  (b[i]):
                print(j)
            print("chose_option :-enter")
            l4+=1
            life.remove("4).switch question")
            n=int(input())

    if c[i]==n:
        print("congratulations. you_win . your answer is right",d)

        print()
    else:

        print()
        n=input("you want to game continue yes or no :-")
        if n=="yes":
            continue

        else:
            break







                
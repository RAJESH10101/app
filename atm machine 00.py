
l={100:0,200:0,500:0,2000:0}
q=0;c=0
password="1234"
mininstatement = []




def deposite():
    print("deposite")
    pp=int(input("enter the amount"))
    x=q+pp
    print("amount deposite successfully")
    print("u current acount balance is",x)

def transection():
    print("transection")
    print("your account balance is",q)
    jl=int(input("enter the amount"))
    if jl<q:
        print("amont transfer successfully")
        o=q-jl
        print(" current balance is",o)


def mini_statement():
    print("last trasection is ",(mininstatement))
    


def pinchange():
    global password
    print("pinchange")
    s=input("enter the old pin:")
    if s==password:
        print("enter the new pin")
        x=input("enter the new pin:")
        password=x
        print("pin change successfully")
    else:
        print("wrong")
def withdrawel():
    global q
    print("withdrawel")
    v=int(input("enterr the amount:"))
    if v<q and v%100==0:
         print("take the cash")
         q=q-v
         print("u current amount is",q)
         mininstatement.append(q)
        
    else:
        print("invalid amount")
       
def user():
    global q,c
    print("user")
    while c<3:
        w=input("pin:")
        if w==password:
            print("successfully login")
            while True:
                print("1.withdrawel\n 2.pinchange\n 3.mini_statement\n 4.transection\n 5.deposite\n  6.exit")
                k=int(input("choice the option"))
                if k==1:
                    withdrawel()
                elif k==2:
                    pinchange()
                elif k==3:
                    mini_statement()
                elif k==4:
                    transection()
                elif k==5:
                    deposite()
                else:
                    break
        else:
            c=c+1
            print("wrong pin")
    else:
         print("account is blocked")
def view():
    print("amount",l)
def load():
    global q

    print("enter the demonitions of 2000,500,200,100")
    for i in l:
        e=int(input())
        l[i]+=e
        q=q+e*i
    print("successfully added")
def admin():

    print("admin")
    a=input("user name:")
    b=input("pin:")
    if a=="rajesh" and b=="0000":
        print("login successfully")
        while True:
            print("1.load\n 2.check\n 3.exit\n")
            c=int(input("choice the option"))
            if c==1:
                load()
            elif c==2:
              print(l)
              print(q)
            elif c==3:
                break;
    else:
         print("wrong password")
while True:
    print("welcome to SBI bank")
    print("1.admin\n2.user\n3.exit")
    a=int(input("choice the option"))
    if a==1:
       admin()
    elif a==2:
       user()
    elif a==3:
       break;
    else:
       print("invalid")

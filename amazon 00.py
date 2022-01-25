



product=[{"name":"iphone","prize":"65000","stock":"10"},
         {"name":"tv","prize":"30000","stock":"5"}]


        
        
cart = dict()
cart1 = list()
existinguser = dict()        
merchants = dict()        
users = dict()

def cart():
    print("cart")
    while True:
     print("1.place order\n 2.cancel")
     s=int(input("select the option"))
     if s==1:
        print("order placed successfully")
        print("it can delivered within 5 days")
        break
     else:
         print(" order cancelled")
         break



def buyer():
    print("buyer")
    print("1.search the product\n 2.go to cart")
    h=int(input("choice the option"))
    if h==1:
     print("search the product")
     search=input("search the product")
     d=0
     for i in product:
        if(search==product[d]["name"]):
            print("Name of the product",product[d]["name"])
            print("prize of the product",product[d]["prize"])
            while True:
             print("add cart","or","not")
             print("1.add\n 2.not add")
             j=int(input("select the choice"))
             if j==1:
                  print("add duccessfully")
                  cart1.append(product[d])
                  return cart() 
             else:
                print("not added") 
                return
        d+=1
    else:
        return cart()
            


def removeproduct():
    print("remove product")
    remove=input("product name")
    del existinguser[remove]

def addproduct():
    print("add product")
    while True:
     name=input("product name:")
     prize=int(input("prize:"))
     existinguser.update({name:prize})
     print("added successfully")
     return merchant()

def existing_merchant():
    print("existing merchant")
    while True:
     n=input("user name:")
     m=input("passsword:")
     if n=="ram" and m=="1010":
          print("login successfully")
          while True:
            print("1.add product\n 2.remove product")
            exist=int(input("choice the option"))
            if exist==1:
             return addproduct()
            else:
                return removeproduct()
     else:
        print("no user found")
        break
          

def approve_merchant():
    print(" welcome to approve marchent")
    while True:
        if len(merchants) != 0:
          print("request is found")
          while True:
           print("1.yes\n 2.no")
           approve=int(input("select the option"))
           if approve==1:
              print("approve successfully")
              return merchant()            
           else:
              print("not approved")
              return merchant()
        else:
            print("no request found")
            break
            
    
def add_merchant():
    print("add merchant")
    while True:
     name=input("enter the merchant name:")
     password=input("password:")
     users.update({name:password})
     print("add successfully")
     break
def remove_merchant():
    remove=input("enter the merchant name:")
    del users[remove]
    print("remove successfully")
def new_merchant():
    print("new_merchant")
    while True:
        name=input("enter the merchant name:")
        password=int(input("enter password"))
        merchants.update({name:password})
        print("account registered.. wait for admin approval")
        break

            
def merchant():
    print("merchant")
    while True:
        print("1.new merchnat\n 2.existing merchant\n 3.exit")
        x=int(input("choice the option"))
        if x==1:
            new_merchant()
        elif x==2:
            existing_merchant()
        else:
            break
def admin():
    print("admin")
    n=input("user name:")
    m=input("password:")
    if n=="rajesh" and m=="0000":
        print("successfully login")
        while True:
            print("1.remove merchant\n 2.approve merchant\n 3.exit")
            d=int(input("select the option"))
            if d==1:
                remove_merchant()
            elif d==2:
                approve_merchant()
            else:
                break
    else:
        print("wrong password")
while True:
 print("welcome to amazon")
 print("1.admin\n 2.merchant\n 3.buyer\n 4.exit")
 a=int(input("enter the choice"))
 if a==1:
    admin()
 elif a==2:
     merchant()
 elif a==3:
     buyer()
 else:
    break;
      



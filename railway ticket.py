



station = {1:'coimbatore',2:'tirupur',3:'erode',4:'salem'}



wait = list[]
ticket = dict()
newuser = dict()
def wait():
    




def cancel_ticket():
    print("cancel ticket")
    print(ticket)
    while True:
     print("r u cancel the ticket")
     print("1.yes\n 2.no")
     er=int(input("select the option"))
     if er==1:
           print("ticket cancel successfully")
           break
     else:
        break
def ticket_conformation():
    print("are u book the ticket")
    while True:
     print("1.yes\n 2.no")
     we=int(input("select the option"))
     if we==1:
           print("ticket booked successfully")
           break
     else:
        break



def ticket_booking():
        seats = 10
        station = 5
        seat_array = [[0 for j in range(station)] for i in range(seats)]
        wait = []
        for i in seat_array:
              print(*i)   
        n=int(input("enter the no of bookings:"))
        for pas in range(n):
           st,ed = map(int,input().split())
           for i in range(seats):
               if sum(seat_array[i][st-1:ed-1])==0:
                   print("seat allocated is",i+1)
                   print("seat are booked successfully")
                   for j in range(st-1,ed):
                      seat_array[i][j]=pas+1
                      break
                   
                   return ticket_conformation()
                    
           else:
               wait.append([pas+1,st,ed])
               print("no seats are avalable")
        for i in seat_array:
            print(*i)
             
    
        
        
        
        
        

def existing_user():
    print("existing user")
    x=input("user name:")
    y=int(input("user password:"))
    if x==n and y==m:
        print("login successfully")
        while True:
         print("1.ticket booking\n 2.canel ticket\n 3.exit")
         o=int(input("select thr option"))
         if o==1:
              ticket_booking()
         elif o==2:
            cancel_ticket()
         else:
            break
    else:
        print("no user found")
    
    



while True:
    print("welcome to railway service")
    print("1.new user\n 2.existing user\n 3.exit")
    a=int(input("select the option"))
    if a==1:
        print("new user")
        n=input("user name:")
        m=int(input("user password:"))
        newuser.update({n:m})
        print("id created successfully")
    elif a==2:
        existing_user()
    else:
        break
        

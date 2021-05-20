flag=0
while(True):
    register=input("Do you want to register(yes/no): ")
    if(register.lower()=="no"):
        break
    elif(register.lower()!="no" and register.lower()!="yes"):
        continue
    elif(register.lower()=="yes"):
        username=input("Enter Username: ")
        while(True):
            password=input("Enter Password: ")
            if len(password) < 8:
                flag=-1
                print('Invalid Password: length should be greater than 8')
               
            elif not any(char.isdigit() for char in password):
                flag=-1
                print('Invalid Password: Password should have at least one numeral')
                
            elif not any(char.isupper() for char in password):
                flag=-1
                print('Invalid Password: Password should have at least one uppercase letter')
                
            elif not any(char.islower() for char in password):
                flag=-1
                print('Invalid Password: Password should have at least one lowercase letter')
                
            else:
                flag=0
                print("Valid Password ")
                break        
        if(flag==-1):
            continue
        while(True):
            login=input("Do you want to login(yes/no): ")
            if(login.lower()=="no"):
                break
            elif(login.lower()!="no" and login.lower()!="yes"):
                continue
            elif(login.lower()=="yes"):
                while(True):
                    name=input("Enter Username: ")
                    passwrd=input("Enter Password: ")
                    if(name!=username or password!=passwrd):
                        print("Details not matched")
                        continue
                    elif(name==username and password==passwrd):
                        print("login completed")
                    while(True):
                        choose=input("Choose anyone from three options: Calculator, Table, Pattern: ")
                        if(choose.lower()=="calculator"):
                            a = float(input("Give first number: "))
                            b = float(input("Give second number: "))
                            c = input("Choose one Operator- Add, Subtract, Multiply, Divide: ")
                            if(c.lower()=="add"):
                                print(a+b)
                            elif(c.lower()=="subtract"):
                                print(a-b)
                            elif(c.lower()=="multiply"):
                                print(a*b)
                            elif(c.lower()=="divide"):
                                print(a/b)
                        elif(choose.lower()=="table"):
                            n=int(input("Table of: "))
                            for i in range(1,11):
                                print(n*i)
                        elif(choose.lower()=="pattern"):
                            n=int(input("Pattern till: "))
                            num=1
                            for i in range(n):
                                num=1
                                for j in range(i+1):
                                    print(num, end=" ")
                                    num+=1
                                print("\r")
                        
                        ask=input("Do you want to Continue(YES/NO): ")
                        if(ask.lower()=="yes"):
                            continue
                        elif(ask.lower()=="no"):
                            break
                        
                                
                       
                    break            
            break                    
    break                
               
           
            
            
    
          
    

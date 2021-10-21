# Curl Expression goes one line
# curl -X POST http://xxxxxx.com/login.php  
#  -H "Content-Type: application/x-www-form-urlencoded"    
# -d "referer=//&username=Jorge&email=jgonzalez@mgz.co.cr&password=a123456&confirmpassword=a123456&datacheck=1" 

# Developed by T Ramirez ++
# 20-10-2021

import random
import requests
import threading
import time
from datetime import datetime
 

def injectDummyRequests(threaId): 

    email ="" 
    domain =""
    user =""
    raiz =""
    passwd="";
    string = "abcdefghijkalmnopqrstvwxyzabcdefghijkalmnopqrstvwxyzabcdefghijkalmnopqrstvwxyz"
    lista= random.sample(range(25),10)
        
    for i in lista:
        user=user+string[i]        
    
    userCompleto = user +" " +user[::-1]
    
    lista= random.sample(range(30),4)    
    for i in lista:
        domain=domain+string[i]
        
    lista= random.sample(range(30),3)
    for i in lista:
        raiz=raiz+string[i]
        
    email= user+"@"+domain+"."+raiz     
    passwd= raiz[::-1]+domain[::-1]    
    url = "http://xxxx.com/login.php"
    
    # Taken 20-10-2021 https://www.geeksforgeeks.org/python-requests-post-request-with-headers-and-body/
    myHeaders = { "Content-Type" : "application/x-www-form-urlencoded" }
       
    data = {"referer":"/",
            "username":userCompleto,
            "email":email,
            "password":passwd,
            "confirmpassword":passwd,
            "datacheck":1 }    
    
    #print(data)
    #time.sleep(3)
    delay()
    try:
        response = requests.post(url, data, headers=myHeaders,  timeout=4)
        today = datetime.today()
        # Everthing goes ok
        if response.status_code == 200:
            print(f"Ok Threat {threaId}  "+ today.strftime("%d/%m/%Y %H:%M:%S"))
        else:
            print("Error Code Response = "+str(response.status_code));  
            #print(response.data)
    except:
         print(f"Catch error in Threat {threaId} ") 
    

def delay():
    numeric = random.sample(range(5),1)[0] 
       
    if numeric == 0:
        numeric = 1
    #print(numeric)
    
    time.sleep(numeric)   

    
def main():    
    for i in range(1,500):
        thread1 = threading.Thread(target = injectDummyRequests, args = (i,))
        thread1.start()
          
    
if __name__ == "__main__":
    main()
    
    
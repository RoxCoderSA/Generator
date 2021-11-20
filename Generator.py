# Genarate Password
import string
import random

print("""
   _____                           _             
  / ____|                         | |            
 | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|  @Roxcoder
                                                                                                                           
""")



stop = False  #value for stop condetion

while stop != True: #while loop infinty loop to do genarator password

    lenNumber = int(input("Please enter the length you want : ")) #enter the length of password from user
#defined funtion and give the password initial value is empty as string
    def Genarator():
        password = ''
#for loop to genarate password with length that a sign by user
        for genrator in range(lenNumber):
            x = random.randint(0, 64) #call the function radomint to random number
            password += string.printable[x] #call the function printtable to print letters and special charcters +
            # randomint numbers
        print("\n") #newline for space
        print(password) #print the password that come from printtable and randomint
        print("\n")#newline for space

    if lenNumber == 0:#condetion for stop final result is 0
        stop = True #change the value stop to true to stop condetion
        break #going out from function
    else: #call the functin infitly
        Genarator() #call the function first time
#call the function last time
Genarator()
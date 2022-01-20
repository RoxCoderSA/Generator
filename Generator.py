# Genarate Password
import string # importing string library 
import random # importing random library 
import argparse # importing argparse  library

print("""
   _____                           _             
  / ____|                         | |            
 | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|  @RoxCoderSA
                                                                                                                           
""")

#Assgin argument from argparser library to parser 
parser=argparse.ArgumentParser(description="this script help users to create generate password")
#Adding new argument name length to make the user enter the length he want 
parser.add_argument( "-l" , "--length" , help='enter the length password' , type=int) 
#Take all argument from argparse and assgin to args value 
args=parser.parse_args()


#Identify function call arg_Generator 
def arg_Generator():
    #Creating variable name counter 
    counter = 1
    #Creating varible string name arg_password 
    arg_password = ''
#Creating while loop starting from 1 to the length the user want 
    while(counter <= args.length):
        #Call the function radomint to random number
        z = random.randint(0,64)
        #Call the function printtable to print letters and special charcters + randomint numbers
        arg_password += string.printable[z]
        #Increase varible counter as 1
        counter+=1
        #Printing  while loop rsults
    print(arg_password)
    #Printing new line 
    print("\n")
#Check if the user run script with argument or not 
if args.length:
    #Call the function if the user run the script with argument 
    arg_Generator()
    #Stoping script when length equal 0

#####################################################################################################################################################################

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
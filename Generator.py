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
    print('\n')
    #asking the user if want save password
    savepass = input('Do you want save password [y/n/x] : ').lower()
    # If the value equal yes it create text file call list.txt 
    if savepass == 'y':
       file = open('list.txt', 'a')
       #Asking the user give the name for password to remember what this password for 
       namepass = input('Give a name password for : ')
       #Saving the password and the name value in list.txt file 
       file.writelines(arg_password + ' ======> ' + namepass + '\n')
       #close the text file after writing the password and name password
       file.close()
       #Exiting from script after saving the password
       exit(0)
       #If the user does not want the password the function recall a same length the user request in frist time 
    elif savepass == 'n':
        arg_Generator()
        #If the user enter the letter x it well be exit from script 
    elif savepass == 'x':
        print('You enter x value for exit')
        exit(0)
        #If the user entered any wrong value the script tell the user the value is incorrect and exiting from script 
    else:
        print('You entered wrong value try again')
        exit(0)
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
        #asking the user if want save password
        savepassword = input('Do you want save password [y/n/x] : ').lower()
        # If the value equal yes it create text file call list.txt
        if savepassword == 'y':
            file = open('list.txt','a')
            #Asking the user give the name for password to remember what this password for
            namepassword = input('Give a name password for : ')
            #Saving the password and the name value in list.txt file
            file.writelines(password + ' ------> ' + namepassword + '\n')
            #close the text file after writing the password and name password
            file.close()
            #Exiting from script after saving the password
            exit(0)
            #If the user does not want the password the function recall a same length the user request in frist time 
        elif savepassword == 'n':
            Genarator()
            #If the user enter the letter x it well be exit from script 
        elif savepassword == 'x':
            print('You enter x value for exit')
            exit(0)
            #If the user entered any wrong value the script tell the user the value is incorrect and exiting from script
        else:
            print('You entered wrong value try again')
            exit(0)
    if lenNumber == 0:#condetion for stop final result is 0
        stop = True #change the value stop to true to stop condetion
        break #going out from function
    else: #call the functin infitly
        Genarator() #call the function first time
#call the function last time
Genarator()
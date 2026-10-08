import os

   # function
def mainMenu():
    print(":::main menu:::")
    print("[ 1]. registera new user")
    print("[ 2]. list all users")
    print("[ 3]. serch  user")
    print("[ 4]. delete user ")
    print("[ 5]. update user")
    print("[ 6]. show active users")
    print("[ 7]. show inactive users")
    print("[ 8]. exit")
ids= []
#main
mainMenu()
os.system('clear')
mainMenu()
#main
while True:
    os.system('clear')
    mainMenu()
    opt= input("press any option [1,8 ]: ")
match opt:
         
        case "1":
            os.system('clear')
            print(":::register form:::")
            ids= input("ident.number: ")
            fisrtNames= input("first name: ")
            lastNames= input("last name: ")
            mobile_phones= input("mobile phone: ")
            emails= input("E-mail: ")
            genders= input("gender [M/F/O ]: ")

            ids.append(id)
            firstNames.append(fisrtName)
            lastNames.append(lastName)
            mobile_phones.append(mobile_phone)
            emails.append(email)
            statuses.append("true")
            genders.append(gender)
            created_at.append(date.today())
            print("user has been created successfully!!")
            any_key= input("press any key to main menu")

           case "2":
            print(":::list all register users:::") 
            any_key= input("press any key ")

            case "8":
            any_key= input("bye,bye.pres")
            
import os
from sys import platform
from gpiozero import OutputDevice

## Alustetaan ledit
rele1 = OutputDevice(21, initial_value=True) 
rele2 = OutputDevice(20, initial_value=True) 
rele3 = OutputDevice(16, initial_value=True) 
rele4 = OutputDevice(26, initial_value=True) 
rele5 = OutputDevice(19, initial_value=True) 
rele6 = OutputDevice(13, initial_value=True) 
rele7 = OutputDevice(6, initial_value=True) 
rele8 = OutputDevice(5, initial_value=True) 

options = {1 : rele1,
2 : rele2,
3 : rele3,
4 : rele4,
5 : rele5,
6 : rele6,
7 : rele7,
8 : rele8
}

## Text menu in Python
## Tulostetaan menu
def print_menu():
    clear_screen()
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Releen tila on " + releen_tila(1)
    print "2. Releen tila on " + releen_tila(2)
    print "3. Releen tila on " + releen_tila(3)
    print "4. Releen tila on " + releen_tila(4)
    print "5. Releen tila on " + releen_tila(5)
    print "6. Releen tila on " + releen_tila(6)
    print "7. Releen tila on " + releen_tila(7)
    print "8. Releen tila on " + releen_tila(8)
    print "9. Exit"
    print 67 * "-"
    print releet

def clear_screen():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "darwin":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')
    elif platform == "cygwin":
        os.system('cls')
    return

def releen_tila(relenro):
    if releet[int(relenro-1)] == 1:
        options[relenro].off()
        return "paalla"
    else:
        options[relenro].on()
        return "sammuksissa"

def vaihda_releen_tila(relenro):
    if releet[relenro-1] == 1:
        releet[relenro-1] = 0
    else:
        releet[relenro-1] = 1

releet = list((0, 0, 0, 0, 0, 0, 0, 0))
loop=True

while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-9]: ")

    if choice==1:     
        print "Laitetta 1 on ohjailtu"
        ## You can add your code or functions here
        vaihda_releen_tila(1)
    elif choice==2:
        print "Laitetta 2 on ohjailtu"
        ## You can add your code or functions here
        vaihda_releen_tila(2)
    elif choice==3:
        print "Laitetta 3 on ohjailtu"
        ## You can add your code or functions here
        vaihda_releen_tila(3)
    elif choice==4:
        print "Laitetta 4 on ohjailtu"
        ## You can add your code or functions here
        vaihda_releen_tila(4)
    elif choice==5:
        print "Laitetta 5 on ohjailtu"
        ## You can add your code or functions here
        vaihda_releen_tila(5)
    elif choice==6:
        print "Laitetta 6 on ohjailtu"
        ## You can add your code or functions here
        vaihda_releen_tila(6)
    elif choice==7:
        print "Laitetta 7 on ohjailtu"
        ## You can add your code or functions here
        vaihda_releen_tila(7)
    elif choice==8:
        print "Laitetta 8 on ohjailtu"
        ## You can add your code or functions here
        vaihda_releen_tila(8)
    elif choice==9:
        print "Poistuit valikosta, heippa!"
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-9 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")

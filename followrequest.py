#coded by RaymonDev

from instapy import InstaPy
import os
import time

def title():
    print("\n")
    print("███████╗ ██████╗ ██╗     ██╗      ██████╗ ██╗    ██╗ ██████╗ ██╗   ██╗███████╗███████╗████████╗")
    print("██╔════╝██╔═══██╗██║     ██║     ██╔═══██╗██║    ██║██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝")
    print("█████╗  ██║   ██║██║     ██║     ██║   ██║██║ █╗ ██║██║   ██║██║   ██║█████╗  ███████╗   ██║")
    print("██╔══╝  ██║   ██║██║     ██║     ██║   ██║██║███╗██║██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║")
    print("██║     ╚██████╔╝███████╗███████╗╚██████╔╝╚███╔███╔╝╚██████╔╝╚██████╔╝███████╗███████║   ██║")
    print("╚═╝      ╚═════╝ ╚══════╝╚══════╝ ╚═════╝  ╚══╝╚══╝  ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝ ")
    print("\nCoded by: RamonG")
    print("Powered by InstaPy")
    print("-----------------------------------------------------------------------------------------------")

def clean():
    os.system("cls")

if __name__ == '__main__':
    title()
    print("\nType the username and password:")
    user = input("\nUsername: ")
    passw = input("Password: ")

    clean()
    title()
    print("\nWhat would you like to do? ")
    print("\n")
    print("[1] Accept petitions")
    print("[2] Reject petitions")
    number = int(input("\nNumber: "))

    if number == 1:
        clean()
        title()
        print("\nWith this command you can choose how many accounts you want to accept")
        naccounts  = int(input("How many accounts do you want to accept?: "))
        ndelay = int(input("How much delay do you want in between accounts? (1 second is recomended): "))

        print("\n")
        print("\n")

        session = InstaPy(username=user, password=passw, want_check_browser=True)
        session.login()

        session.accept_follow_requests(amount=naccounts, sleep_delay=ndelay)
        session.end()
        print("Operacion finalizada")
        os.system("pause")



    if number == 2:
        clean()
        title()
        print("\nWith this command you can reject the accounts")
        naccounts = int(input("How many accounts do you want to reject: "))
        ndelay = int(input("How much delay do you want in between accounts? (1 second is recomended): "))

        print("\n")
        print("\n")

        session = InstaPy(username=user, password=passw, want_check_browser=True)
        session.login()

        session.remove_follow_requests(amount=naccounts, sleep_delay=ndelay)
        session.end()
        print("Process finished")

        os.system("pause")
    if number > 2 or number < 1:
        clean()
        title()
        print("\nThis number is not correct")
        time.sleep(5)
        quit()
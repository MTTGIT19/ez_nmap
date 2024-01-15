# modules
import os
import sys
from pyfiglet import Figlet
from termcolor import colored, cprint

# brings user to main menu
def main():
   menu()

# Main menu options -- Provides navigation to all other functions.
def menu():

    f = Figlet(font='slant')
    print (f.renderText("Easy N.Mapper"))
    cprint(colored("************ Written by MTTGIT19 **************", "blue", attrs=["bold"]))
    print()

    choice = input("""
        A: Run an network scan using Nmap.
        B: Run a vulnerability scan.
        C: Help Menu.
        D: Find my IP address.
        Q: Quit!

        Please enter your choice:  """)
                                                                                                                                                                                                                                                                                                                                
    if choice == "A" or choice =="a":
        nmap_menu()
    elif choice == "B" or choice =="b":
        vuln_menu()                                                                                                                                  
    elif choice == "C" or choice =="c":
        help_menu()
    elif choice == "D" or choice =="d":
        ip_menu()
    elif choice=="Q" or choice=="q":
        sys.exit
# Catches exceptions, blocks rogue input. Returns user to main menu
# These exceptions are reused throughout the program.
# If this program expands, I would likely make these a seperate function.
    else:
        cprint(colored("You must only select either A, B, C, or Q.", "red"))
        cprint(colored("Please try again...", "green"))

        menu()


# Abbreviated menu -- Prevents users from being spammed with intro banner. Better UI design. 
def short_menu():
    cprint(colored("***************************** MAIN MENU ******************************", "blue", attrs=["bold"]))

    choice = input("""
        A: Run an network scan using Nmap.
        B: Run a vulnerability scan.
        C: Help Menu.
        D: Find my IP Address.
        Q: Quit!

        Please enter your choice:  """)
                                                                                                                                                                                                                                                                                                                                
    if choice == "A" or choice =="a":
        nmap_menu()
    elif choice == "B" or choice =="b":
        vuln_menu()                                                                                                                                  
    elif choice == "C" or choice =="c":
        help_menu()
    elif choice == "D" or choice =="d":
        ip_menu()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        cprint(colored("You must only select either A, B, C, or Q.", "red"))
        cprint(colored("Please try again...", "green"))

        menu()

# Menu for option A: Nmap scans
# Options A and B output only to command line. C and D create .txt files.
# Scans utilize the OS module. 
def nmap_menu():
    cprint(colored("*************** Nmap Scan options ***************", "blue", attrs=["bold"]))

    choice = input("""
            Print outputs to command line:
        A. Quick scan my Network.
        B. Scan my network for active services.

            Writes output to  .TXT file.
        C. Quick scan my network + save to file
        D. Scan my network for active services + save to file

        E. Back to main menu.

        Please enter your choice: """)

    if choice == "A" or choice =="a":
        os.system("nmap 127.0.0.1")
        short_menu()
    elif choice == "B" or choice =="b":
        os.system("nmap -A -sV 127.0.0.1") 
        short_menu()                                                                                                                  
    elif choice == "C" or choice =="c":
        os.system("nmap 127.0.0.1 -oN nmap_quickscan")
        cprint(colored("*** File Saved! ***", "green"))
        print("*** Returning to Menu *** ")
        short_menu()
    elif choice == "D" or choice =="d":
        os.system("nmap -A -sV 127.0.0.1 -oN nmap_servicescan")  
        cprint(colored("*** File Saved! ***", "green"))
        print("*** Returning to Menu *** ")
        short_menu()
    elif choice == "E" or choice =="e":
        menu()
    else:
        cprint(colored("You must only select either A, B, C, D, or E.", "red"))
        cprint(colored("Please try again...", "green"))

        menu()


# Menu for option B: Vulnerability scans. 
# Uses both Nikto and NMAP 
def vuln_menu():

    cprint(colored("*************** Vulnerability Scan options ***************", "blue", attrs=["bold"]))

    choice = input("""
            Prints output to command line:
        A. Conduct host vulnerability scan using Nikto
        B. Conduct host vulnerability scan using Nmap

            Writes output to .TXT file:
        C. Conduct host vulnerability scan using Nikto + save to file
        D. Conduct host vulnerability scan using Nmap + save to file

        E. Back to main menu.

        Please enter your choice: """)

    if choice == "A" or choice =="a":
        os.system("nikto -h 127.0.0.1")
        short_menu()
    elif choice == "B" or choice =="b":
        os.system("nmap -sC 127.0.0.1")
        short_menu()                                                                                                                       
    elif choice == "C" or choice =="c":
        os.system("nikto -h 127.0.0.1 -o nikto_scan.txt")
        cprint(colored("*** File Saved! ***", "green"))
        print("*** Returning to Menu *** ")
        short_menu()
    elif choice == "D" or choice =="d":
        "nmap -sC 127.0.0.1 -oN nmap_vulnscan"
        cprint(colored("*** File Saved! ***", "green"))
        print("*** Returning to Menu *** ")
        short_menu()
    elif choice=="E" or choice=="e":
        menu()
    else:
        cprint(colored("You must only select either A, B, C, or Q.", "red"))
        cprint(colored("Please try again...", "green"))

        menu()

# Print statement of basic instructions and information about the program
def help_menu():
    cprint(colored("""   
        ****************************** HELP MENU ******************************
        Welcome! This program is designed to help new users use basic network scanning tools.
                        Discover more about your own network!

            **These tools are for use on internal, user owned networks only!**
            **This program is NOT designed for penetration testing**

        Tools this program uses include Nmap (www.nmap.org) and Nikto (www.CIRT.net/Nikto2). 

        Simply follow the on-screen prompts, and enter a letter of your choice.
        Capital or lower case letters are accepted.
        ***********************************************************************
        """, "yellow", attrs=["bold"]))

    short_menu()


# Menu for option D: Find my IP Address
# Uses OS to run ifconfig 
# Also prints basic information about the users system/OS.
# Includes option to save IPCONFIG to file
def ip_menu():
    cprint(colored("""
    ********************** Find my IP Address **********************
    Below is some helpful information about your system.
    Note the 'inet' flag is typically followed by your IP address. 
    """, "blue"))

    print(os.uname(),"\n")
    os.system('ifconfig')

    option = input(" Would you like this information saved to a file? (Y/N)?")
    
    if option == "Y" or option == 'y':
        os.system('ifconfig > ip_config.txt')
        cprint(colored("*** File Saved! ***", "green"))
        print("*** Returning to Menu *** ")
        short_menu()

    elif option == "N" or option == 'n':
        short_menu()

    else:
        cprint(colored("You must only select either A, B, C, or Q.", "red"))
        cprint(colored("Please try again...", "green"))
        menu()


if __name__== "__main__":
    main()

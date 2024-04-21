"""This exercise tests out the default values of parameters. Create a program which has a main
function and a subfunction called tester. The main function prompts user for an input "Write something (quit ends): "
and sends this input to the subfunction as a parameter.Define the subfunction tester so that it has one parameter
called "givenstring", which has the default value "Too short".If the user input is less than 10 characters, the program
uses the default value and if 10 or more, it prints the usergiven input. If the user inputs "quit", the program is
terminated. When working correctly, the program will print out something like this:"""

def pester(user_ask):
    while user_ask != " ":

        if  user_ask == "quit":
            break
        if len(user_ask) < 10:
            print(givenstring)
        else:
            print(user_ask)
        user_ask = input("Write something (quit ends): ")

givenstring = "Too short"
user_ask = input("Write something (quit ends): ")
pester(user_ask)

















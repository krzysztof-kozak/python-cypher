from userInput import get_user_input
from cypher import cypher
from logo import logo
from replit import clear

go_again = True

while go_again:
    clear()
    print(logo)
    text, shift, direction = get_user_input()
    cypher(direction, text, shift)

    decision = input("Go again? Type y or n\n")

    if decision.lower() != "y":
        go_again = False

from userInput import get_user_input
from cypher import cypher

text, shift, direction = get_user_input()
cypher(direction, text, shift)

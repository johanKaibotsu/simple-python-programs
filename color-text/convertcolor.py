import random
from termcolor import colored
colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
text = input("Enter a Sentence: ")
for i in text:
    j = random.randint(0,5)
    print(colored(i,colors[j]), end='')
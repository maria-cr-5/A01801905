import random


options = ["Rock","Paper","Scissors"]
rockOptions=[0,  -1  ,1]
paperOptions=[1,  0,  -1]
scissorsOptions=[-1,  1,  0]

print("Lets play rock paper scisoors")
print("Select one of the following options")
print("Rock  [1]")
print("Paper  [2]")
print("Scissors  [3]")
print("What do you choose?:")

playerChoice = int(input())
computerChoice = random.randint(1,3)

# If player chooses 1, they picked rock!
if playerChoice ==!
  rockOptions

from random import randint
from os import listdir, system, name
from os.path import isfile, join

def fileToTitle(s): # removes the extension, replaces '_' with whitespace, then capitalizes each word
    return s.split('.')[0].translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\\|`~-=_+"}).title()

# Gets all the text files in the folder in a list to be then selected later
questionFiles = [f for f in listdir('.') if str(f).endswith("txt")]
qFLen = len(questionFiles)

# Selecting a text file to play
print(">> Please select a question list:\n")
for i in range(0, qFLen): # Displays the names off all the text files
    s = fileToTitle(questionFiles[i])
    print(f"\033[1m\033[96m{str(i+1)}. {s}\033[0m") # puts the file names in bold blue

sel = 0
while 1 > sel or qFLen < sel: # Select a valid index number between 1 and the list length
    try:
        sel = int(input(f"\n<< Please enter your list (1 - {str(qFLen)}): "))
    except ValueError:
        print("!! That wasn't an integer :(")

selFile = questionFiles[sel-1] # selFile is the selected file by the user
selFile_f = fileToTitle(selFile)

with open(selFile, encoding="utf8") as f: # Reads the selected file into a list
    qList = f.read().splitlines()

qLen = len(qList) # Length of the list (i.e., question count)
max = qLen - 1 # to shuffle indexes
rIndex= [(i) for i in range(0, qLen)] #Generate a list starting from 0 to the question count

for i in range(0, qLen): # Shuffles the indexes by randomly switching r and max, then lowers max by one
    r = randint(0, max)
    rIndex[r], rIndex[max] = rIndex[max], rIndex[r]
    max-=1

for i in range(0, qLen): # Main loop of the program
    if name == 'posix': # Clears the screen for the next question
        # for linux
        system('clear')
    else:
    # for windows platfrom
        system('cls')
    print(f"{selFile_f}") # file name as title
    print("----------------------------\n")
    print(f"\033[1m\033[96m{qList[rIndex[i]]}\033[0m\n") # puts the question in bold blue text
    t = input(">> Press ENTER for a new question... ") # input() to wait
    if(t == "exit"):
        break
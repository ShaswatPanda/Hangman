import random

print("\n WELCOME TO HANGMAN! \n")

from hangman_art import logo
print(logo)

from hangman_words import word_list


wordList = ['shaswat', 'panda', 'cake']
chosenWord = random.choice(word_list)
print("\nHint: Chosen word is ", chosenWord)

chosenWordList = list(chosenWord)
#print(chosenWordList)
wordLength = len(chosenWordList)
guessList = []
for letter in chosenWord:
  guessList += "_"
print(guessList, "\n")

gameOver = False
lives = 5



while gameOver==False:
  print("LIVES LEFT: ", lives)
  guess = input("Guess a letter: ")
  

  if guess not in chosenWordList:
    print("WRONG")
    lives-=1
  else:
    for i in range(wordLength):
      if chosenWordList[i] == guess:
        print("RIGHT")

        guessList[i] = chosenWordList[i]
        chosenWordList[i] = ""

        #print("Chosen word: ", chosenWordList)
  print(guessList)    
  print("\n")

  if lives<=0:
    gameOver = True
    print("\nG A M E  O V E R !\n")

  if "_" not in guessList:
    gameOver = True
    print("\nY O U  H A V E  W O N !\n")

  from hangman_art import stages
  print(stages[lives])
  
  
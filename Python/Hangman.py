word = input("Player one, what is the word? ")
print("\n"*50) #clearing screen
letters = list(word)
guess_arr = []
wrong_counter = 1
#array to build the "hangman"
hangman = ["---|\n",
           "   o\n",
           "   |\n",
           "  /","|","\\", "\n",
           "   |\n",
           "  /"," ","\\","\n"]

#building array with blanks for each letter
for i in letters:
    guess_arr.append("_")

while True:
    #printing out hangman
    current_hangman = ""
    for i in range(0,wrong_counter):
        current_hangman += hangman[i]
    print(current_hangman)
    #printing out current letters
    current_letters = ""
    for i in guess_arr:
        current_letters += i + " "
    print(current_letters)
    #taking guess
    guess = input("Player two, what is your guess? ")
    #checking guess
    if guess not in letters:
        print("Wrong!")
        wrong_counter += 1
        #making sure a space or new line isn't included in wrong guesses
        if hangman[wrong_counter] == "\n" or hangman[wrong_counter] == " ":
            wrong_counter += 1
    else:
        print("Correct!")
        #looping through to check for multiples of letters
        for i in letters:
            if guess in letters:
                letter_pos = letters.index(guess)
                guess_arr[letter_pos] = guess
                letters[letter_pos] = " "
            else:
                break
            
    #checking if the user has guessed the word
    if guess_arr == list(word):
        print("The word was " + word)
        print("You win!")
        break
    #checking if the user lost
    if wrong_counter == len(hangman):
        current_hangman = ""
        for i in range(0,wrong_counter):
            current_hangman += hangman[i]
        print(current_hangman)
        print("The word was " + word)
        print("You lost!")
        break

    


        

        

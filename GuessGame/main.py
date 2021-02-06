guessValue = 55
attemptCounter = 0
totalAttemptCounter = 5

while 1:
    if attemptCounter <= totalAttemptCounter and totalAttemptCounter - attemptCounter != 0:
        userInput = input("Enter a number : ")
        attemptCounter += 1

        if userInput.isalnum():
            userInput = int(userInput)

            if userInput == guessValue:
                print("Congratulation! ", f'Take : {attemptCounter} attempt')
                break
            elif userInput < guessValue:
                print("Lower ", f' {totalAttemptCounter - attemptCounter} attempt left')
            elif userInput > guessValue:
                print("Grater ", f' {totalAttemptCounter - attemptCounter} attempt left')

        else:
            print("Invalid input type! ", f' {totalAttemptCounter - attemptCounter} attempt left')
    else:
        print("Game Over !", f' {attemptCounter} attempt tried')
        break

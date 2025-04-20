# ***************
# Parker Haynie 
# Assignment 5.1: Final Project: Application and Presentation Video
# ***************

# Creates a string list called usersName to hold the usersNameInut variable in the printWelcomeMessage function
usersName: list[str] = []

# A function that prints out the title of the application
def printApplicationTitle():
    # Prints the title
    print("\n\t      *** Trivia Games ***\n")

# A function that prints out the description for the application
def printApplicationDescription():
    # Prints the applications description
    print("In this application you can test your knowledge of ")
    print("different topics through multiple trivia games.")

# A function that prints out the instructions on how the application is used
def printApplicationInstructions():
    # Prints the applications instructions
    print("\nFirst, you determine what topic of trivia quiz you")
    print("want to be quized on. Once chosen, you will be asked")
    print("five questions that relate to that topic. Answer all")
    print("five questions correctly and you win and then you")
    print("can start another quiz with a different topic.")

# A function that asks for the users name and then prints out a welcome message
def printWelcomeMessage():
    # User enters their input for usersName variable
    usersNameInput = input("\nBefore you start a quiz, please enter your name below\n")
    # Appends the usersNameInput into the usersName string list
    usersName.append(usersNameInput)
    # Prints the welcome message containing the users name
    print("\nWelcome, {}, please enjoy my trivia game!".format(usersName[0]))

# A function that provides a divider between the different text elements for a better user experience
def printDivider():
    # Prints a divider to make the user experience nicer
    print("\n------------------------------------------------------------------------------")

# A function that contains all of the logic for the trivia quizes
def startQuiz():
    # The beginning of the while loop. Everything inside of this will loop until the user enters something other than yes.
    while True:
        # Calls the printDivider function
        printDivider()
        # Print the trivia topic selection
        print("\nWhich trivia topic do you want to be quized on?")
        print("\n1. Movies")
        print("2. Food")
        print("3. Animals")

        # User enters their input for their trivia topic (1, 2, or 3)
        triviaTopicChoice = input("\nPlease choose your topic (1, 2, 3)\n")

        # If statement for topic 1 "Movies" -------------------------------------------------
        if triviaTopicChoice == '1':
            # Calls the printDivider function
            printDivider()
            # States the topic selected
            print("\nTopic Chosen: Movies")
            # Prints question 1
            print("\nQuestion 1: In 2004 comedy 'Napoleon Dynamite' who is Napoleon's best friend?")
            # Prints the possible answers for question 1
            print("\n1. Kip")
            print("2. Pedro")
            print("3. Deb")
            print("4. Rex")
            # Prints text that tells the user what inputs are avaible
            print("\nPlease enter your answer to proceed (1, 2, 3, 4)")

            # User enters their input for question 1 (1, 2, 3, or 4)
            choice1 = input()

            # If statement for printing question 2
            if choice1 == '2':
                # States that the user provided the correct answer for question 1
                print("\n*** Correct! ***")
                # Calls the printDivider function
                printDivider()
                # Prints qustion 2
                print("\nQuestion 2: Evan Goldberg and which other actor wrote and directed 2007 comedy 'Superbad'?")
                # Prints the possible answers for question 2
                print("\n1. Jonah Hill")
                print("2. James Franco")
                print("3. Danny McBride")
                print("4. Seth Rogen")

                # User enters their input for question 2 (1, 2, 3, or 4)
                choice2 = input()

                # If statement for printing question 3
                if choice2 == '4':
                    # States that the user provided the correct answer for question 2
                    print("\n*** Correct! ***")
                    # Calls the printDivider function
                    printDivider()
                    # Prints qustion 3
                    print("\nQuestion 3: In gritty 2009 film 'Gran Torino' lead character Walt was a veteran of which war?")
                    # Prints the possible answers for question 3
                    print("\n1. Korean War")
                    print("2. World War 2")
                    print("3. Vietnam War")
                    print("4. American Civil War")

                    # User enters their input for question 3 (1, 2, 3, or 4)
                    choice3 = input()

                    # If statement for winning the trivia quiz
                    if choice3 == '1':
                        # States that the user provided the correct answer for question 2
                        print("\n*** Correct! ***")
                        # Calls the printDivider function
                        printDivider()
                        # Prints qustion 3
                        print("\nQuestion 4: In what year did famous fictional boxer Rocky return in 'Rocky Balboa'?")
                        # Prints the possible answers for question 3
                        print("\n1. 2004")
                        print("2. 2006")
                        print("3. 2009")
                        print("4. 2002")

                        # User enters their input for question 4 (1, 2, 3, or 4)
                        choice4 = input()

                        if choice4 == '2':
                            # States that the user provided the correct answer for question 2
                            print("\n*** Correct! ***")
                            # Calls the printDivider function
                            printDivider()
                            # Prints qustion 3
                            print("\nQuestion 5: In 'Superman Returns' what is Superman's nickname?")
                            # Prints the possible answers for question 3
                            print("\n1. Man of Gold")
                            print("2. Man of Silver")
                            print("3. Man of Iron")
                            print("4. Man of Steel")

                            # User enters their input for question 5 (1, 2, 3, or 4)
                            choice5 = input()

                            if choice5 == '4':
                                # Prints the congratulations message if the user wins
                                print("\nCongrats, you win!")

                            # Else statement for if the user answers question 5 incorrectly
                            else:
                                print("\nSorry, thats incorrect.")

                        # Else statement for if the user answers question 4 incorrectly
                        else:
                            print("\nSorry, thats incorrect.")

                    # Else statement for if the user answers question 3 incorrectly
                    else:
                        print("\nSorry, thats incorrect.")

                # Else statement for if the user answers question 2 incorrectly
                else:
                    print("\nSorry, thats incorrect.")

            # Else statement for if the user answers question 1 incorrectly    
            else:
                print("\nSorry, thats incorrect.")
                
        # Elif statement for topic 2 "Food" -------------------------------------------------
        elif triviaTopicChoice == '2':
            # Calls the printDivider function
            printDivider()
            # States the topic selected
            print("\nTopic Chosen: Food")
            # Prints question 1
            print("\nQuestion 1: Which fruit resembles 60% of human DNA?")
            # Prints the possible answers for question 1
            print("\n1. Bananas")
            print("2. Strawberry")
            print("3. Orange")
            print("4. Apple")

            # User enters their input for question 1 (1, 2, 3, or 4)
            choice1 = input()

            # If statement for printing question 2
            if choice1 == '1':
                # States that the user provided the correct answer for question 1
                print("\n*** Correct! ***")
                # Calls the printDivider function
                printDivider()
                # Prints question 2
                print("\nQuestion 2: Which foo never rots and doesn't require preservatives to keep fresh?")
                # Prints the possible answers for question 2
                print("\n1. Peanuts")
                print("2. Oats")
                print("3. Honey")
                print("4. Tea")

                # User enters their input for question 2 (1, 2, 3, or 4)
                choice2 = input()

                # If statement for printing question 2
                if choice2 == '3':
                    # States that the user provided the correct answer for question 2
                    print("\n*** Correct! ***")
                    # Calls the printDivider function
                    printDivider()
                    # Prints question 3
                    print("\nQuestion 3: Which food contains the most calories per gram?")
                    # Prints the possible answers for question 3
                    print("\n1. Pistachio")
                    print("2. Avocado")
                    print("3. Chia seeds")
                    print("4. Chocolate")

                    # User enters their input for question 3 (1, 2, 3, or 4)
                    choice3 = input()

                    # If statement for winning the trivia quiz
                    if choice3 == '2':
                        # States that the user provided the correct answer for question 2
                        print("\n*** Correct! ***")
                        # Calls the printDivider function
                        printDivider()
                        # Prints question 3
                        print("\nQuestion 4: Which was the first country to set the minimum drinking age to 21?")
                        # Prints the possible answers for question 3
                        print("\n1. England")
                        print("2. Scotland")
                        print("3. Netherlands")
                        print("4. Germany")

                        # User enters their input for question 4 (1, 2, 3, or 4)
                        choice4 = input()

                        if choice4 == '1':
                            # States that the user provided the correct answer for question 2
                            print("\n*** Correct! ***")
                            # Calls the printDivider function
                            printDivider()
                            # Prints question 3
                            print("\nQuestion 5: Which shellfish comes in varieties such as Olympia, European flat, and Kumamoto?")
                            # Prints the possible answers for question 3
                            print("\n1. Mussels")
                            print("2. Clams")
                            print("3. Oysters")
                            print("4. Scallops")

                            # User enters their input for question 5 (1, 2, 3, or 4)
                            choice5 = input()

                            if choice5 == '3':
                                # Prints the congratulations message if the user wins
                                print("\nCongrats, you win!")

                            # Else statement for if the user answers question 5 incorrectly
                            else:
                                print("\nSorry, thats incorrect.")

                        # Else statement for if the user answers question 4 incorrectly
                        else:
                            print("\nSorry, thats incorrect.")

                    # Else statement for if the user answers question 3 incorrectly
                    else:
                        print("\nSorry, thats incorrect.")

                # Else statement for if the user answers question 2 incorrectly
                else:
                    print("\nSorry, thats incorrect.") 
                
            # Else statement for if the user answers question 1 incorrectly
            else:
                print("\nSorry, thats incorrect.")

        # Elif statement for topic 3 "Animals" ----------------------------------------------
        elif triviaTopicChoice == '3':
            # Calls the printDivider function
            printDivider()
            # States the topic selected
            print("\nTopic Chosen: Animals")
            # Prints question 1
            print("\nQuestion 1: Which of these mammals lay eggs?")
            # Prints the possible answers for question 1
            print("\n1. Kiwi")
            print("2. Bongo")
            print("3. Echidna")
            print("4. Southern Right Whale")

            # User enters their input for question 1 (1, 2, 3, or 4)
            choice1 = input()

            # If statement for printing question 2
            if choice1 == '3':
                # States that the user provided the correct answer for question 1
                print("\n*** Correct! ***")
                # Calls the printDivider function
                printDivider()
                # Prints question 2
                print("\nQuestion 2: Which is the biggest species of shark?")
                # Prints the possible answers for question 2
                print("\n1. Great White Shark")
                print("2. Hammerhead Shark")
                print("3. Whale Shark")
                print("4. Basking Shark")

                # User enters their input for question 2 (1, 2, 3, or 4)
                choice2 = input()

                # If statement for printing question 3
                if choice2 == '3':
                    # States that the user provided the correct answer for question 2
                    print("\n*** Correct! ***")
                    # Calls the printDivider function
                    printDivider()
                    # Prints question 3
                    print("\nQuestion 3: What is the most posionous snake on the planet?")
                    # Prints the possible answers for question 3
                    print("\n1. Black Mamba")
                    print("2. Western Diamondback Rattlesnake")
                    print("3. Cobra")
                    print("4. Inland Taipan")

                    # User enters their input for question 3 (1, 2, 3, or 4)
                    choice3 = input()

                    # If statement for winning the trivia quiz
                    if choice3 == '4':
                        # States that the user provided the correct answer for question 2
                        print("\n*** Correct! ***")
                        # Calls the printDivider function
                        printDivider()
                        # Prints question 3
                        print("\nQuestion 4: What is the fastest flying bird in the world?")
                        # Prints the possible answers for question 3
                        print("\n1. Harpy Eagle")
                        print("2. Peregrine Falcon")
                        print("3. Horned Sungem")
                        print("4. Spine-Tailed Swift")

                        # User enters their input for question 4 (1, 2, 3, or 4)
                        choice4 = input()

                        if choice4 == '2':
                            # States that the user provided the correct answer for question 2
                            print("\n*** Correct! ***")
                            # Calls the printDivider function
                            printDivider()
                            # Prints question 3
                            print("\nQuestion 5: What is the smallest mammal in the world?")
                            # Prints the possible answers for question 3
                            print("\n1. Bumblebee Bat")
                            print("2. Pygmy Marmoset")
                            print("3. Numbat")
                            print("4. Western Harvest Mouse")

                            # User enters their input for question 5 (1, 2, 3, or 4)
                            choice5 = input()

                            if choice5 == '1':
                                # Prints the congratulations message if the user wins
                                print("\nCongrats, you win!")

                            # Else statement for if the user answers question 5 incorrectly
                            else:
                                print("\nSorry, thats incorrect.")

                        # Else statement for if the user answers question 4 incorrectly
                        else:
                            print("\nSorry, thats incorrect.")

                    # Else statement for if the user answers question 3 incorrectly
                    else:
                        print("\nSorry, thats incorrect.")

                # Else statement for if the user answers question 2 incorrectly
                else:
                    print("\nSorry, thats incorrect.")

            # Else statement for if the user answers question 1 incorrectly            
            else:
                print("\nSorry, thats incorrect.")
        
        # Else statement for if the user enters an invalid input for the topic selection
        else:
            print("\nInvalid Input: Please try again and enter either 1, 2, or 3")

        # Allows the user to determine whether or not they want to continue using the application
        goAgain = input("\nDo you want to go again? (yes/no)\n")

        # If statement for when the user enters no or any other input besides yes
        if goAgain.lower() != 'yes':
            # Calls the printDivider function
            printDivider()
            # Calls the printGoodbyeMessage to the user
            printGoodbyeMessage()
            # Breaks out of the loop
            break

# Prints the goodbye message containing the users name
def printGoodbyeMessage():
    # Prints the message saying goodbye to the user
    print("\n\t*** Thank you, {}, for playing my trivia games! ***\n".format(usersName[0]))

# Calls the function that prints the applications title
printApplicationTitle()

# Calls the function that prints the applications description
printApplicationDescription()

# Calls the function that prints the applications instructions
printApplicationInstructions()

# Calls the function that asks the user for their name and displays a welcome message
printWelcomeMessage()

# Calls a function that contains all of the logic for the trivia quizes
startQuiz()
#Emma #1 
#Start Screen and End Screen
import random
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
p1 = ["dog", "cat", "ran", "sat", "bat"]
p2 = ["roof", "ooof", "corn", "ball", "foot", "cook", "jazz"]
p3 = ["chick", "board", "trees", "bagel", "drum"]

def show_start_screen():
    print("""

       ,-'''''-.:-^-._                                _,-^-;,-'''''-.
      /      '  ( `  _\    Welcome to Hippo Run      /_  ` )  `      \      
      \      \   _ .,-'                              `-., _,  ;      /
       )_\-._-._((_(                                   )_))_,-_,-/_(
                                   """ + name )
    print(" ")
def instructions(name):
    print("Hello " + name + """. The goal of this game is to guess the word before the Hippo gets away.
 Since we all like hippos please for all of human kinds sake dont let the
 hippo get away.""")
    print(" ")
    print(" ")
    print(" ")
    

    
def end(name):
    print("Thank you for playing, " + name + ". Come back soon! Game made bt Emma #1")
    print("""

                     .^.,*.
                    (   )  )
                   .~       "-._   _.-'-*'-*'-*'-*'-'-.--._
                 /'             `"'                        `.
               _/'                                           `.
          __,""                                                ).--.
       .-'       `._.'                                          .--.\
      '                                                         )   \`:
     ;                                                          ;    "
    :                                                           )
    | 8                                                        ;
     =                  )                                     .
      \                .                                    .'
       `.            ~  \                                .-'
         `-._ _ _ . '    `.          ._        _        |
                           |        /  `"-*--*' |       |  
                           |        |           |       :
 ~~~~~~~---   ~-~-~-~   -~-~-~-~-~-~~~~~~  ~~~~  ~-~-~-~-~-~-~-
------~~~~~~~~~----------~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
 ~~~~~~~~~   ~~~~~~~~~       ~~~~~~~   ~~~~~~~~~  ~~~~~~~~~~~~~~~
 """)
#How the game works
def difficulty(p1, p2, p3):
    print("You only 6 guesses in each difficulty so choose wisely.")
    print("Difficulty 1: 3 letter words")
    print("Difficulty 2: 4 letter words")
    print("Difficulty 3: 5 letter words")

    while True:
        diff = input("Please enter your difficulty:")
        if diff == "1":
                return p1
        elif diff == "2":
                return p2
        elif diff == "3":
                return p3
        else:
                print("Please enter 1, 2, or 3")
        


def get_puzzle( p1, p2, p3):
    return random.choice(difficulty(p1, p2, p3))
    print(" ")
    print(" ")
    print(" ")    
def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess(guesses):

    while True:
        
        guess = input("Enter a letter: ")
        if len(guess) > 1 :
            print ("Please enter only 1 letter at a time")
        elif guess not in alpha:
            print ("Please enter an actual number.")
        elif guess in guesses:
            print("You already guessed that latter")
        else:
            return guess
    print("")
def display_board(strikes, solved, guesses):
    print("***********")
    print(solved)
    print("***********")

    print("Letters already guessed: ? , ! " + guesses)
    print("Strikes: " + str(strikes))
    gap = "             " * strikes
    if strikes <= 5:
        print("""_\|/^ """ + gap + """,-'''''-.:-^-._ """ )
        print("""(_oo """ + gap + """/      '  ( `  _\ """ )
        print(""" | """ + gap + """ \      \   _ .,-' """)
        print("""/|\ """ + gap + """ )_\-._-._((_(""")
    else:
        print(" ")
    print(" ")
    print(" ")
    print(" ")
def show_result(strikes, limit, puzzle):
    if strikes < limit:
        print("You win!")
    else:
        print("You lose.")
        print("The word was " + puzzle + ".")



def play_again(name):
    while True:
        decision = input("Would you like to play again, " + name + "? (y/n) ")

        if decision.lower() == 'y' or decision.lower() == 'yes':
            print()
            return True
        elif decision.lower() == 'n' or decision.lower() == 'no':
            print()
            return False
        else:
            print("Please enter 'y' or 'n'.")
            
def play(p1, p2, p3):
    puzzle = get_puzzle(p1, p2, p3)
    guesses = ""
    solved = get_solved(puzzle, guesses)
    strikes = 0
    limit = 6
    
    print(solved)


    
    while solved != puzzle and strikes < limit:
        letter = get_guess(guesses)
        if letter not in puzzle:
            strikes += 1
            
      
        guesses += letter + ","
        solved = get_solved(puzzle, guesses)
        display_board(strikes, solved, guesses)
            

    show_result(strikes, limit, puzzle)
    
# Game is running here
name = input("Enter name: ")
show_start_screen()
instructions(name)

playing = True
while playing:
    play(p1, p2, p3)
    playing = play_again(name)
end(name)

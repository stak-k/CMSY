#Serra Tak
#7: Lists

def main():

    print("Welcome to the Soccer Calculator \n ") #open text

    #open the file and read data from file 
    infile = open('/Users/serratak/Documents/soccer.txt', 'r')

    #read lines one by one from file
    fname = infile.readline()[:-1]#remove newline
    lname = infile.readline()[:-1]#remove newline
    tmname = infile.readline()[:-1]#remove newline
    leauge = infile.readline()[:-1]#remove newline

    infile.close()#close file after rading

    #display info from file
    print(f'First Name: {fname}')
    print(f'Last Name : {lname}')
    print(f'Team Name : {tmname}')
    print(f'Leauge    : {leauge} \n')


    # Prompt to begin entering soccer performance data for the player
    print(f"Enter info for {fname} {lname}:\n")
        

    again = 'y' #loop condition to cont.

    while again == 'y' or again =='Y': #variable to contron loop/rep

        #call geting valid inputs functions
        games_played = total_games_played()
        shots_taken = total_shots_taken()
        goals_scored = total_goals_scored()

        #create list to keep averages
        avg = [0, 0, 0]


        #calculations for list
        avg[0] = goals_scored / games_played
        avg[1] = shots_taken / games_played
        avg[2] = shots_taken / goals_scored

    #call  display function 
        display(avg)


    #permision input to run the program again
        again = input('Would you like to enter another (y/n)')

    close()#call closing message 

   
def total_games_played():

  #gets the total game number
    games_played= int(input('Please enter the games: '))

    while games_played <= 0: #input criteria
        print('Error: the games cannot be <=0, please reenter.')#error msg
        games_played= int(input('Please enter the games: '))
    return games_played #returns the input and make ready to reuse for next step

def total_shots_taken():
   #gets the total shot number
    shots_taken= int(input('Please enter the shots: '))
    
    while shots_taken <=0:#input criteria
        print('Error: the shots cannot be <=0, please reenter.') #error msg
        shots_taken= int(input('Please enter the shots: '))
    return shots_taken #returns the input and make ready to reuse for next step

def total_goals_scored(): 
   #gets the total goal number
    goals_scored = int(input('Please enter the golas: '))
    
    while goals_scored <= 0:#input criteria
        print('Error: the goals cannot be <=0, please reenter.') #error msg
        goals_scored = int(input('Please enter the golas: '))
    return goals_scored #returns the input and make ready to reuse for next step
 

 #result display function    
def display(avg): 

    print(f'\nThe average goals per game is: {avg[0]:^30.2f}')

    print(f'The average shots on goal per game is: {avg[1]:^15.2f}')

    print(f'The average shots per goal is: {avg[2]:^30.2f}\n')
    
def close(): #closing message function
    print("\nThank you for using this program!") 


main()
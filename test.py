#serra Tak
#04/07/2025
#Lab 5 Part1.5
#Soccer Calculator with Functions
def main():

    print("Welcome to the CMSY 156 Soccer Calculator \n ") #open text

    again = 'y' #loop condition to cont.

    while again == 'y' or again =='Y': #variable to contron loop/rep

        #call geting valid inputs functions
        games_played = total_games_played()
        shots_taken = total_shots_taken()
        goals_scored = total_goals_scored()

    #average calculation
        avg_goal_per_game = goals_scored / games_played
        avg_shots_per_game = shots_taken / games_played
        avg_shots_per_goal = shots_taken / goals_scored

    #call result display function 
        result(avg_goal_per_game, avg_shots_per_game, avg_shots_per_goal)


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
def result(avg_goal_per_game, avg_shots_per_game, avg_shots_per_goal): 

    print(f'\nThe average goals per game is: {avg_goal_per_game:^30.2f}')

    print(f'The average shots on goal per game is: {avg_shots_per_game:^15.2f}')

    print(f'The average shots per goal is: {avg_shots_per_goal:^30.2f}\n')
    
def close(): #closing message function
    print("Thank you for using this program!") 
    
main()



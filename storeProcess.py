#Serra Tak
#Store and process test scores using lists and functions


def main():
    scores = input_scores()
    while True:
        display_menu() # Get initial test scores from user
        choice = input("Enter your choice: ") # Get user menu selection
        if choice == '1': score_metrics(scores) # Display min, max, average
        elif choice == '2': mine_scores(scores) # Display high and low scores
        elif choice == '3': update_score(scores) # Update a test score
        elif choice == '4': display_scores(scores) # Display scores in reverse
        elif choice == '5':
            print("Bye!"); # Exit the program
            break
        else: print("Invalid.") # Handle invalid menu choice

def input_scores():# Function to input scores from user
    while True:
        try:
            total_test = int(input('How many scores will you be entering: '))
            if total_test > 0: break
            print("Error: Number of scores must be greater than zero.")
        except: print("Error: Please enter a valid integer")
    scores = []
    while len(scores) < total_test:
        try:
            Scores_list = int(input(f"Enter test score {len(scores)+1} (0 - 100): "))
            if 0 <= Scores_list <= 100:
                scores.append(Scores_list)
            else:
                print("Error: Score must be between 0 and 100.")
        except:
            print("Error: Please enter a valid integer.")
    return scores

def display_menu(): # Function to display menu options
    menu = ['\n1. Score Metrics (min/max/avg)', '2. Mine Scores (low/high scores)',
            '3. Update Score', '4. Display Scores (reverse order)', '5. Quit' ]
    for d in menu:
        print(d)
    
def score_metrics(Scores_list): # Function to display metrics about scores
    print(f"\n\nNumber of Scores: {len(Scores_list)}")
    print(f"\nHighest Score: {max(Scores_list):^10.2f}")
    print(f"Lowest Score: {min(Scores_list):^12.2f}")
    print(f"Average Score: {sum(Scores_list)/len(Scores_list):^10.2f}")

def mine_scores(Scores_list): # Function to separate high and low scores
    avg = sum(Scores_list) / len(Scores_list) # Calculate average
    high = sorted([scr for scr in Scores_list if scr >= avg]) # High scores (>= average)
    low = sorted([scr for scr in Scores_list if scr < avg]) # Low scores (< average)
    
    print("\nTop Scores",)
    for scr in high:
        print(f'{scr:.2f}')
        
    print("\nBottom Scores:")
    for scr in low:
        print(f'{scr:.2f}')
        
def update_score(Scores_list): # Function to update a specific test score
    print('\nUpdate test score')

    # Display scores with numbering
    index = 1
    for scr in Scores_list:
        print(f'{index}. {scr:.2f}')
        index += 1

    # Get valid score number to update   
    while True:
        try:
            selection = int(input("Select score number to update: "))
            if 1 <= selection <= len(Scores_list):
                break
            else:
                print(f"Error: Enter a number between 1 and {len(Scores_list)}.")
        except:
            print("Error: Please enter a valid integer.")

    # Get valid new score
    while True:
        try:
            new_score = int(input("Enter new score: "))
            if 0 <= new_score <= 100:
                break
            else:
                print("Error: Score must be between 0 and 100.")
        except:
            print("Error: Please enter a valid integer.")

    # Update the selected score      
    Scores_list[selection - 1] = new_score

     # Display updated scores
    index = 1
    for scr in Scores_list:
        print(f"{index}. {scr:.2f}")
        index += 1

# Function to display scores in reverse order
def display_scores(Scores_list):
    print("Scores in revers order:") 
    for scr_rvrs in Scores_list[::-1]:
        print(f'{scr_rvrs:^20.2f}')

if __name__ == "__main__": #run the program
    main()
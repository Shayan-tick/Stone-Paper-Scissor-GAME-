import random

plans = ['Stone','Paper','Scissor']
pc_score = 0
u_score = 0
while True:
    print("1. Stone   2. Paper   3. Scissor")
    print("------------    ------------")
    plan = input("Choose between 1,2 or 3:")
    
    random_num = random.choice(plans)
    print(plan, random_num)
    
    if pc_score == 3 or u_score == 3:
        if not u_score>pc_score:
            print("You Lost")
            break
        else:
            print("You Win")
            break
            
    if plan == "1":
        if random_num == "Stone":
            print("Equal")
            
        elif random_num == "Paper":
            print("You lost this round")
            pc_score += 1

        else:
            print("You win this round")
            u_score += 1
            
        print("******************")
        print(pc_score, 'PC Score')
        print("----------")
        print(u_score, 'User Score')
        
    elif plan == "2":
        if random_num == "Stone":
            print("You win this round")
            u_score += 1
        elif random_num == "Paper":
            print("Equal")
        else:
            print("You lost this round")
            pc_score += 1

        print("******************")
        print(pc_score, 'PC Score')
        print("----------")
        print(u_score, 'User Score')
        
    elif plan == "3":
        if random_num == "Stone":
            print("You lost this round")
            pc_score += 1
        elif random_num == "Paper":
            print("You win this round")
            u_score += 1
        else:
            print("Equal")

        print("******************")
        print(pc_score, 'PC Score')
        print("----------")
        print(u_score, 'User Score')
        
    else:
        print("Wrong Input")

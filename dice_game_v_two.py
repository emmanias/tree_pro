import random

#roll dice
def roll_the_die(number_of_dice):
    the_dice =[] #create the dice table
    i = 1 #default initialize to 1 for single dice
    if number_of_dice > 1:
        number_of_dice -= 1  #correct the value
        i = 0  #initialize to 0 for multiple dice

    if number_of_dice > 0:
        while i <= number_of_dice:
            a_dice = random.randint(1,6)
            the_dice.append(a_dice)
            i += 1
    return the_dice


#we will need comprehension too
#What is going on


#the box counter
def count_the_dice(dice_given):
    one_box = 0
    two_box = 0
    three_box = 0
    four_box = 0
    five_box = 0
    six_box = 0



    the_loc = ["one_box",
    "two_box",
    "three_box",
    "four_box",
    "five_box",
    "six_box"]

    for target in dice_given:
        if target == 1:
            one_box = dice_given.count(target)
        elif target == 2:
            two_box = dice_given.count(target)
        elif target == 3:
            three_box = dice_given.count(target)
        elif target == 4:
            four_box = dice_given.count(target)
        elif target == 5:
            five_box = dice_given.count(target)
        elif target == 6:
            six_box = dice_given.count(target)
        else:
            print("something is wrong")

    the_count = [one_box, two_box, three_box, four_box, five_box, six_box]
    the_pair_valued = dict(zip(the_loc, the_count))
    return the_count, the_pair_valued

#inspect them
def score_checker(settled_dice, on_table, compro):
    the_count = compro
    dice_are_there = 0
    one_box = settled_dice['one_box']
    two_box = settled_dice['two_box']
    three_box = settled_dice['three_box']
    four_box = settled_dice['four_box']
    five_box = settled_dice['five_box']
    six_box = settled_dice['six_box']
    score = 0
    used_on_table = 0
    inform = False

    while dice_are_there < on_table:
        if one_box == two_box == three_box == four_box == five_box == six_box == 1:
            print("You win 1000 points for seq")
            score += 1000
            used_on_table = 6
            break
        elif two_box == three_box == four_box == five_box == six_box == 0 and one_box == 6:
            print("You win all")
            score = "You win all"
            used_on_table = -6
            break
        elif (one_box >= 1) and (one_box < 3):
            print("You win 100 points for one dice")
            score += 100
            one_box -= 1
            used_on_table -= 1
        elif (five_box >= 1) and (five_box != 3) and (five_box < 4):
            print("You win 50 points oka")
            score += 50
            five_box -= 1
            inform = True
            used_on_table -= 1
        elif one_box == 3 or ((one_box >= 3) and (one_box != 6)):
            print("You win 1000 points")
            score += 1000
            on_table -= 3
            used_on_table -= 3
            one_box -= 3
        elif two_box == 3:
            print("You win 200 points")
            score += 200
            two_box -= 3
            on_table -= 3
            used_on_table -= 3
            break
        elif three_box == 3:
            print("You win 300 points")
            score += 300
            on_table -= 3
            used_on_table -= 3
            break
        elif four_box == 3:
            print("You win 400 points")
            score += 400
            on_table -= 3
            used_on_table -= 3
            break
        elif five_box == 3:
            print("You win 500 points")
            score += 500
            on_table -= 3
            used_on_table -= 3
            break
        elif six_box == 3:
            print("You win 600 points")
            score += 600
            on_table -= 3
            used_on_table -= 3
            break
        else:
            spoted = 0
            for look_out in the_count:
                if look_out == 2:
                    spoted += 1
            if spoted == 3:
                print("You win 1000 points for 3 pairs")
                score += 1000
                if inform == True:
                    score -= 100
                the_count.clear()
                used_on_table -= 6
                break
        dice_are_there += 1
        bring = on_table - 1
    return score, used_on_table

#helper
def play_game(dice_to_use):
    #So this returns the score and the subtracted dice if set to return once_all
    num_of_dice_to_use = dice_to_use
    dice_result = roll_the_die(num_of_dice_to_use)
    print(dice_result)
    onece_call = score_checker(count_the_dice(dice_result)[1],num_of_dice_to_use,count_the_dice(dice_result)[0])
    #return onece_call[0]
    return onece_call


#the player
def player():
    the_final_score = 0
    used_dice = 6
    rolling = False
    the_final_result = "yu"
    remaining_dice = used_dice
    the_combo_result = play_game(used_dice)
    print(f"The total score is {the_combo_result[0]} removed {the_combo_result[1]}")
    remaining_dice_stp = used_dice + the_combo_result[1]
    the_final_score += the_combo_result[0]
    if remaining_dice_stp != 0:
        rolling = True
        while rolling == True:
            remaining_dice = remaining_dice + the_combo_result[1]
            if the_combo_result[1] > -1 or the_combo_result[1] == 0 or remaining_dice == 0:
                if the_combo_result[1] > -1 or the_combo_result[1] == 0:
                    the_final_score = 0
                    print("You lost")
                    break
                else:
                    break
            else:
                the_choice = str(input(f"Do you want to continue with {remaining_dice} dice \n Press 'Y' for yes and 'N' for no"))
                if the_choice == "Y" or the_choice == "y":
                    the_combo_result = play_game(remaining_dice)
                    the_final_score += the_combo_result[0]
                    print(f"The total score was {the_final_score} removed {the_combo_result[1]}")
                else:
                    print("Your response is No")
                    break
    the_final_result = f"The total score is now here as {the_final_score}"
    return the_final_result, the_final_score

#game manager
def game_man():
    player_name = ""
    print("Hello there this is a 6 dice game\n")
    player_name = input("May I know how to call you")
    print(f"{player_name}, {player()[0]}")
    

#main call
game_man()




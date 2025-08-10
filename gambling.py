# gambling is cool btw

import random
import time

player_money = 10.00

slots = ("⭐", "⭐", "🍒", "🍒", "🍒", "🍓", "🍓", "⚡", "⚡", "💎")

def place_bet(value: float):
    
    global player_money
    
    if value > player_money:
        print("You don't have enough money to place this bet!")
        return False
    else:
        player_money -= value
        return True
# 

def random_slot():
    
    global slots
    
    return random.choice(slots)
#

def setup_slots():
    
    slot1 = random_slot()
    slot2 = random_slot()
    slot3 = random_slot() 
    
    slot_machine = (slot1, slot2, slot3)
    
    return slot_machine    
#    

def print_slot_machine_results(slot_machine: tuple):
    for slot in slot_machine:
        print(slot, end= "     |     ", flush = True)
        time.sleep(1.0)
#    

def check_prize(slots: tuple, player_bet):
    
    global player_money
    
    slot = slots[0]
    
    if slot == "🍒":
        player_money += player_bet * 1.2
    elif slot == "🍓":
        player_money += player_bet * 1.5
    elif slot == "⭐":
        player_money += player_bet * 2.0
    elif slot == "⚡":
        player_money += player_bet * 2.5  
    elif slot == "💎":
        player_money += player_bet * 3.0   
#

def check_win(slot_machine: tuple):
    
    if len(set(slot_machine)) == 1:
        return True
    else:
        return False
# 

def print_start():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("/----------------------------------\\")
    print("|          SLOT MACHINE            |")
    print("|----------------------------------|")
    print("|       PLACE YOUR BET TO WIN      |")
    print("\\----------------------------------/")
    print(f"\nYour current balance is: ${player_money:.2f}\n")
#

def main():
    
    global player_money
    
    user_choice = ""
    
    while True:
        
        print_start()

        if player_money <= 0:
                print("You are out of money! Stop gambling.")
                break
                
        player_bet = float(input("PLACE YOUR BET: $"))

      
        
        if place_bet(player_bet):
            
            slots_result = setup_slots()
            
            print("/-----------------------------------\\")
            print("|  ", end= "")
            print_slot_machine_results(slots_result)  
            print("\n\\-----------------------------------/")
              
            if check_win(slots_result):
                check_prize(slots_result, player_bet)
                print(f"\nYour current balance is: ${player_money:.2f}")
                user_choice = input(("YOU WON! Want to play again? (Y / N): "))
            else:
                print(f"\nYour current balance is: ${player_money:.2f}")
                user_choice = input(("You lost! Want to play again? (Y / N): "))
                if user_choice.lower() not in ("y", "yes"):
                    break
        else:
            continue
    
    print("Thanks for playing!")
#    
    
if __name__ == '__main__':
    main()
            
        
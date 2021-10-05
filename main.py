
import random
from replit import clear

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def play_game():
    print(logo)

    def deal_card():
        """Returns a random card from the deck."""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    user_cards = []
    dealer_cards = []
    for add in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    def score(list):
        current_score = sum(list)
        if current_score == 21 and len(list) == 2:
            return "BlackJack"
        if 11 in list and current_score > 21:
            list.remove(11)
            list.append(1)
        return current_score

    current_score = score(user_cards)
    dealer_score = score(dealer_cards)

    while dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = score(dealer_cards)

    print(f"Your cards : {user_cards} - Your current score is : {current_score}")
    print(f"Dealer first card id: {dealer_cards[0]}")

    hit = True
    while hit:
        hit_or_stand = input("Type 'y' to hit or type 'n' to stand: ")
        if hit_or_stand == "y":
            user_cards.append(deal_card())
            score(user_cards)
            current_score = score(user_cards)
            print(f"Your cards: {user_cards} - Your current score is : {current_score}")
            if current_score > 21:
                print("You lose...")
                hit = False
        else:
            hit = False
            print(f"Your final hand: {user_cards} - Your current score is : {current_score}")
            print(f"Dealer final hand: {dealer_cards}, final score {dealer_score}")
            if current_score > dealer_score or dealer_score > 21:
                print("You win!!")
            elif current_score == dealer_score:
                print("Its a draw..")
            else:
                print("You lose..")
                hit = False


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()

#Blackjack (no split) 

import random

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
ranks = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
values = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return self.rank + " of " + self.suit

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __repr__(self):
        remaining_cards = ""
        for card in self.deck:
            remaining_cards += "\n" + card.__repr__() 
        return "This deck has: " + remaining_cards

    def shuffle(self):
        return random.shuffle(self.deck)

    def deal_card(self):
        chosen_card = self.deck.pop()
        return chosen_card

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win(self):
        self.total += self.bet

    def lose(self):
        self.total -= self.bet

player_chips = Chips()

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips do you wish to bet? "))
            if chips.bet > chips.total:
                print("Sorry, your bet may not exceed your total chips (" + str(chips.total) + ")")
            else:
                break
        except ValueError:
            print("Please enter an integer value!")
    
        
def take_hit(deck, hand):
    hand.add_card(deck.deal_card())
    hand.adjust_for_aces()

def hit_or_stand(deck, hand):
    global playing

    while True:
        temp = input("Do you wish to [h]it or [s]tand? ").lower()

        if temp == "h":
            take_hit(deck, hand)
        elif temp == "s":
            print("Dealer is now playing")
            playing = False
        else:
            print("Please enter h for hit or s for stand")
            continue
        break

def show_some(player, dealer):
    print("Dealer's hand:")
    print("<card hidden>")
    print(dealer.cards[1])

    player_list = ""
    for card in player.cards:
        player_list += "\n" + card.__repr__()
    print("Player's hand:" + player_list)
    

def show_all(player, dealer):

    player_list = ""
    for card in player.cards:
        player_list += "\n" + card.__repr__()
    print("Player's hand:" + player_list)
    print("Players's value: " + str(player.value))
    
    dealer_list = ""
    for card in dealer.cards:
        dealer_list += "\n" + card.__repr__()
    print("Dealer's hand:" + dealer_list)
    print("Dealer's value: " + str(dealer.value))

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win()

def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose()

def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose()

def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win()

def push(player,dealer):
    print("It's a tie!")

while True:
    
    print("Welcome to Eric's blackjack game!")

    new_deck = Deck()
    new_deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(new_deck.deal_card())
    player_hand.add_card(new_deck.deal_card())

    dealer_hand = Hand()
    dealer_hand.add_card(new_deck.deal_card())
    dealer_hand.add_card(new_deck.deal_card())

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)
    
    while playing:

        hit_or_stand(new_deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
        

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            take_hit(new_deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        elif player_hand.value < dealer_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    print("Current player chip count: " + str(player_chips.total))

    invalid_input = True
    
    while invalid_input:
        play_again = input("Would you like to play again? [y]es/[n]o ").lower()
        if play_again == "y" or play_again == "n":
            invalid_input = False
        else:
            invalid_input = True
    
    if play_again == "y":
        playing = True
        continue
    else:
        print("Thank you for playing!")
        break


        

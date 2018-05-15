
#Milestone Project 2 - Blackjack Game
#In this milestone project you will be creating a Complete BlackJack Card Game in Python.

#Here are the requirements:

#You need to create a simple text-based BlackJack game
#The game needs to have one player versus an automated dealer.
#The player can stand or hit.
#The player must be able to pick their betting amount.
#You need to keep track of the player's total money.
#You need to alert the player of wins, losses, or busts, etc...

#Game Play
#To play a hand of Blackjack the following steps must be followed:

#1. Create a deck of 52 cards
#2. Shuffle the deck
#3. Ask the Player for their bet
#4. Make sure that the Player's bet does not exceed their available chips
#5. Deal two cards to the Dealer and two cards to the Player
#6. Show only one of the Dealer's cards, the other remains hidden
#7. Show both of the Player's cards
#8. Ask the Player if they wish to Hit, and take another card
#9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
#10. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
#11. Determine the winner and adjust the Player's chips accordingly
#12. Ask the Player if they'd like to play again

import random
class Deck():

    def __init__(self):
        self.deck = []
        suits = ('Hearts', 'Spades', 'Clubs', 'Diamonds')
        ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        
        for suit in suits:
            for rank in ranks:
                self.deck.append((suit,rank))
        
        random.shuffle(self.deck)


    def __str__(self):
        return("{}".format(self.deck)) 

    def __len__(self):
        return len(self.deck)


class Dealer():
    
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11, 'ace':1}

    def __init__(self):
        mycard = []
        self.mycard = mycard
        self.name = 'Dealer'


    def hit(self, deck):
        self.mycard.append(deck.deck.pop())

   
    def hand(self,hidecard=0):
        sum = 0
        print('\n' + self.name)
        if hidecard == 1:
            for cards in self.mycard:
                sum += Dealer.values[cards[1]]
            print(self.mycard[0])
            print('(HIDDEN CARD)')

        else:
            for cards in self.mycard:
                sum += Dealer.values[cards[1]]
                print(cards)
            if sum == 21:
                print('Blackjack!')
            else:
                print(sum)

        return sum

    def ace_check(self):
        try:
            ace_index = [ace[1] for ace in self.mycard].index('Ace')
        except:
            return False
        else:
            self.mycard[ace_index] = (self.mycard[ace_index][0],'ace')
            return True
        
            


class Player(Dealer):

    def __init__(self,balance=1000):
        self.balance = balance
        mycard =[]
        self.mycard = mycard
        self.name = 'Player'
        self.bet = 0.0

    def betting(self):
        while True:
            try:
                self.bet = (float(input('Place your bet! : ')))
            except:
                print('Please put in a amount!')
                continue
            else:        
                if self.balance - self.bet >= 0:
                    self.balance -= self.bet
                    break
                else:
                    print("You can't bet more than what you have!")
                    continue

    def pay(self,winner=''):
        if winner == 'pB':
            self.balance += self.bet * 2.5
        elif winner == 'p':
            self.balance += self.bet * 2
        elif winner == 't':
            self.balance += self.bet

def hit_or_stay():
    while True:   
        move = input("\nHit? or Stay? Enter 'h' or 's: ")
        
        if move.lower().startswith('h'):
            return True
        elif move.lower().startswith('s'):
            return False
        else:
            print("Invalid input")
            continue
        break

def dealer_hit_or_stay(ptotal,dtotal):
    if dtotal < 17:
        return True
    elif ptotal > 17 and ptotal > dtotal:
        return True
    else: 
        return False

def replay():
    
    return input("Do you want to play again? Enter 'y' or 'n': ").lower().startswith('y')

def check_winner(ptotal,dtotal):

    if ptotal == 21 and (ptotal > dtotal or dtotal > 21):
        print('\nPlayer won with Blackjack!')
        return 'pB'
    elif dtotal == 21 and (dtotal > ptotal or ptotal > 21):
        print('\nDealer won with Blackjack!')
    elif ptotal > 21 and dtotal != 21:
        print('\nDealer won because Player busted!')
    elif dtotal > 21 and ptotal != 21:
        print('\nPlayer won because Dealer busted!')
        return 'p'
    elif dtotal == ptotal and dtotal >= 17:
        print('\nTie!')
        return 't'
    elif ptotal > dtotal:
        print('\nPlayer won with',ptotal)
    else:
        print('\nDealer won with',dtotal)

#TODO: implement betting ability for player

player = Player()
while True:
    #create deck, player, dealer
    new_deck = Deck()
    dealer = Dealer()

    print('Your balance is:',player.balance)
    player.betting()

    #deal two cards to each
    player.hit(new_deck)
    dealer.hit(new_deck)
    player.hit(new_deck)
    dealer.hit(new_deck)

    ptotal = player.hand()
    dtotal = dealer.hand(1)
    winner = ''

    #player turn
    while True and dtotal != 21:
        if  ptotal < 21 and  hit_or_stay():
            player.hit(new_deck)
            ptotal = player.hand()

            #check for player bust
            if ptotal > 21:
                #if there is an Ace count it as 1 and if there are no more Aces then it is a bust
                if player.ace_check():
                    ptotal = player.hand()
                    continue
                break
            else:
                continue
        else:
            dealer.hand()
            break

    #dealer turn
    while True:
        if ptotal > 21 or dtotal == 21:
            player.hand()
            dealer.hand()
            winner = check_winner(ptotal,dtotal) 
            break
        else:
            if dealer_hit_or_stay(ptotal,dtotal):
                dealer.hit(new_deck)
                dtotal = dealer.hand()
                #check for dealer bust
                if dtotal > 21:
                    if dealer.ace_check():
                        dtotal = dealer.hand()
                        continue
                    else:
                        player.hand()
                        dealer.hand()
                        winner = check_winner(ptotal,dtotal)
                        break
                else:        
                    dealer.ace_check()
                    continue
            else:
                player.hand()
                dealer.hand()
                winner = check_winner(ptotal,dtotal)
                break
    
    player.pay(winner)
    player.mycard = []
    
    if player.balance == 0:
        print('You are out of money!')
        if replay():
            player.balance = 1000
        else:
            break

    

    
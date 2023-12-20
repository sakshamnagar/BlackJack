from random import shuffle
# Global Variables
# Card suites,rank and value
suites=("Clubs","Diamonds","Hearts","Spades")
ranks=("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,
        "Queen":10,"King":10,"Ace":11}

class Cards:
    """
    Class to create individual card.

    Attributes:
        suite(str): suite of card.
        rank(str): rank of the card.
        value(int): value of the card in int to compare its value with other cards.
    """
    all=[]
    def __init__(self,rank,suite):
        """Creating attributes"""
        self.suite=suite
        self.rank=rank
        self.value=values[rank]  ##Value of card
    
        
    def __str__(self):
        """Print the cards"""
        return(f"{self.rank} of {self.suite}")
    
class Deck:
    """
        Class to create a deck of cards using the Cards() class.

        Attributes:
            all_cards(list): A deck of card is created using Cards() class.

        Methods:
            deal(): Pops and returns one card from the deck.
            shuffle(): Shuffles the deck.
    """
    def __init__(self):
        """Create a deck of cards."""
        self.all_cards=[]
        for suite in suites:
            for rank in ranks:
                self.all_cards.append(Cards(rank,suite))

    def __str__(self):
        """Prints the deck."""
        return f"{self.all_cards}"
    
    def deal(self):
        """Pops and returns one card from deck."""
        return self.all_cards.pop()
    
    def shuffle(self):
        """Shuffles the deck."""
        shuffle(self.all_cards)

    def __str__(self):
        """Print the deck."""
        s=''
        for i in self.all_cards:
            s=s+"\n"+i.__str__()
        return s



class User():
    """
        Class to create users  """
    def __init__(self,name):
        self.name=name
        self.rank=ranks
        self.all_cards=[]

    def add(self,new_cards):
        self.all_cards.append(new_cards)

    def total_value(self):
        total_value=0
        for i in self.all_cards:
            total_value+=i.value
            if total_value>21 and i.rank=="Ace":
                total_value-=10
        return total_value
       
    
    def hit(self):
        hit=input("Would you like to hit? enter Y for yes and N for no. ")
        while hit.upper() not in ("Y","N"):
            hit=input("Incorrect input! Please enter Y or N again below.\n")
        return hit.upper()
        

       
    

    
class Bank:
    def __init__(self,balance):
        self.balance=balance
    
    def bet(self):
        bet=0
        while True:
            bet=int(input("How much would you like to bet?\n"))
            if bet>self.balance:
                print(f"Betting amount higher than balance! Your balance is {self.balance}")
                bet=int(input("Please enter lower amount.\n"))
            else:
                break
        return bet
    def win(self,bet):
        self.balance+=bet
    def loose(self,bet):
        self.balance-=bet




def print_hand():
    print('\033[4m'"\nDealer Cards:"'\033[0m',"<Card Is Hidden>",dealer.all_cards[-1],'\033[4m'"\nPlayer Card:"'\033[0m',
            *player.all_cards,sep="\n   ")
    print(f"\nYour total card value is {player.total_value()}")
def print_final():
    print('\033[4m'"\nDealer Cards:"'\033[0m',*dealer.all_cards,'\033[4m'"\nPlayer Card:"'\033[0m',
            *player.all_cards,sep="\n   ")
    print(f"\nYour total card value is {player.total_value()}")
    print(f"Dealer total card value is {dealer.total_value()}")


    

##Game Logic 
game_on=True
new_deck=Deck()
bank=Bank(100)
print('\x1B[1m'"Welcome to Blackjack!  "'\033[0m')
print('\x1B[1m'f"Your balance is ${bank.balance}"'\033[0m')
while game_on:
    new_deck.shuffle()
    player=User("Player")
    dealer=User("Dealer")
    for i in range(2):
        player.add(new_deck.deal())
        dealer.add(new_deck.deal())
    start_game=input("Would you like to play Blackjack? Y or N\n")

    if start_game.upper()=="N":
        game_on=False
        break
    bank_bet=bank.bet()
    print(f"\n                                You bet ${bank_bet}. Dealing the cards now.")

    print_hand()
    loop=True
    while loop:
        
        

        
            

        
        while player.total_value()<21:
            if player.hit()=="Y":
                player.all_cards.append(new_deck.deal())
                print_hand()
            else:
                break

        if player.total_value()>21:
            bank.loose(bank_bet)
            print(f"You Bust! Your balance is {bank.balance}")
            break
        else:
            print("Dealers turn")

            while dealer.total_value()<17:
                dealer.add(new_deck.deal())
            print_final()
            
            if player.total_value() > dealer.total_value() or player.total_value()==21:
                bank.win(bank_bet)
                print(f"You win! Your balance is {bank.balance}")
                
            elif player.total_value()<dealer.total_value() and dealer.total_value()<21:
                bank.loose(bank_bet)
                print(f"You loose! Your balance is {bank.balance}")
            
            elif player.total_value()==dealer.total_value():
                print("Its a draw!")   

            else:
                loop==False
                break

            

        


 





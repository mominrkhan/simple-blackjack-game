from dataclasses import dataclass
import random
import logging

# Logging to console + file
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[
        logging.FileHandler("blackjack_log.txt"),
        logging.StreamHandler()
    ]
)

SUIT_SYMBOLS = {
    "spades": "♠",
    "clubs": "♣",
    "hearts": "♥",
    "diamonds": "♦"
}


@dataclass
class Card:
    suit: str
    rank: str
    value: int

    def __str__(self) -> str:
        return f"{self.rank}{SUIT_SYMBOLS[self.suit]}"


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank, value)
                      for suit in SUIT_SYMBOLS
                      for rank, value in [
                          ("A", 11), ("2", 2), ("3", 3), ("4", 4), ("5", 5),
                          ("6", 6), ("7", 7), ("8", 8), ("9", 9), ("10", 10),
                          ("J", 10), ("Q", 10), ("K", 10)
        ]]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, count=1):
        return [self.cards.pop() for _ in range(count)]


class Hand:
    def __init__(self, is_dealer=False):
        self.cards = []
        self.is_dealer = is_dealer

    def add_cards(self, cards):
        self.cards.extend(cards)

    def get_value(self):
        value = sum(card.value for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == "A")
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def is_blackjack(self):
        return len(self.cards) == 2 and self.get_value() == 21

    def display(self, reveal_dealer=False):
        if self.is_dealer:
            logging.info("Dealer's Hand:")
            if not reveal_dealer:
                logging.info("[Hidden] %s", str(self.cards[1]))
            else:
                logging.info(" ".join(str(card)
                             for card in self.cards) + f" = {self.get_value()}")
        else:
            logging.info("Your Hand:")
            logging.info(" ".join(str(card)
                         for card in self.cards) + f" = {self.get_value()}")
        logging.info("")


class BlackjackGame:
    def __init__(self):
        self.balance = 100
        self.stats = {"wins": 0, "losses": 0, "ties": 0}

    def play(self):
        logging.info("🎲 Welcome to Blackjack 🎲")
        while self.balance > 0:
            logging.info(f"\n💰 Current balance: ${self.balance}")
            bet = self.get_bet()
            deck = Deck()
            player = Hand()
            dealer = Hand(is_dealer=True)

            player.add_cards(deck.deal(2))
            dealer.add_cards(deck.deal(2))

            player.display()
            dealer.display()

            if player.is_blackjack():
                logging.info("🎉 Blackjack! You win 1.5x your bet!")
                self.balance += int(1.5 * bet)
                self.stats["wins"] += 1
                continue

            # Player action
            while player.get_value() < 21:
                move = input("Hit (H) or Stand (S)? ").lower()
                if move in ['h', 'hit']:
                    player.add_cards(deck.deal(1))
                    player.display()
                elif move in ['s', 'stand']:
                    break

            player_value = player.get_value()
            if player_value > 21:
                logging.info("❌ You busted! You lose your bet.")
                self.balance -= bet
                self.stats["losses"] += 1
                continue

            # Dealer logic
            while dealer.get_value() < 17:
                dealer.add_cards(deck.deal(1))
            dealer.display(reveal_dealer=True)
            dealer_value = dealer.get_value()

            # Result
            if dealer_value > 21 or player_value > dealer_value:
                logging.info("✅ You win!")
                self.balance += bet
                self.stats["wins"] += 1
            elif dealer_value > player_value:
                logging.info("❌ Dealer wins.")
                self.balance -= bet
                self.stats["losses"] += 1
            else:
                logging.info("⚖️ It's a tie!")
                self.stats["ties"] += 1

            if self.balance == 0:
                logging.info("💀 You're out of money!")
                break

            again = input("Play again? (Y/N): ").lower()
            if again != 'y':
                break

        # End
        logging.info("\n🏁 Final Balance: $%s", self.balance)
        logging.info("📊 Game Stats: Wins: %s | Losses: %s | Ties: %s",
                     self.stats["wins"], self.stats["losses"], self.stats["ties"])
        logging.info("📝 Session saved to blackjack_log.txt")
        logging.info("Thanks for playing!")

    def get_bet(self):
        while True:
            try:
                bet = int(input("Enter your bet: $"))
                if 1 <= bet <= self.balance:
                    return bet
                logging.info("⚠️ Bet must be between $1 and $%s", self.balance)
            except ValueError:
                logging.info("⚠️ Invalid input. Please enter a number.")


if __name__ == "__main__":
    BlackjackGame().play()

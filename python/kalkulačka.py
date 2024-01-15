# Importing necessary libraries
import random

# Defining the basic structure of the game

class FinancialGame:
    def __init__(self):
        self.balance = 1000  # Starting balance
        self.day = 1         # Starting day
        self.end_day = 30    # End day of the game
        self.investments = {'stocks': 0, 'bonds': 0, 'real_estate': 0} # Different types of investments

    def display_status(self):
        """ Display the current status of the player """
        print(f"Day: {self.day}/{self.end_day}")
        print(f"Balance: ${self.balance}")
        print("Investments:")
        for investment, value in self.investments.items():
            print(f"  {investment.capitalize()}: ${value}")

    def make_decision(self):
        """ Where the player makes decisions for the day """
        print("\nWhat would you like to do today?")
        print("1. Invest Money")
        print("2. End Day")
        decision = input("Enter your choice (1 or 2): ")
        if decision == '1':
            self.invest_money()
        # Other decisions can be added here

    def invest_money(self):
        """ Invest money in different assets """
        asset = input("Choose an asset to invest in (stocks, bonds, real_estate): ")
        amount = int(input("How much would you like to invest?: "))
        if asset in self.investments and amount <= self.balance:
            self.investments[asset] += amount
            self.balance -= amount
            print(f"Invested ${amount} in {asset}.")
        else:
            print("Invalid investment choice or insufficient balance.")

    def update_day(self):
        """ Update the game to the next day and apply investment growth/loss """
        self.day += 1
        self.apply_investment_changes()

    def apply_investment_changes(self):
        """ Randomly increase or decrease the value of investments """
        for asset in self.investments:
            change = random.uniform(-0.1, 0.1)  # Investment value can change by -10% to +10%
            self.investments[asset] *= (1 + change)

    def is_game_over(self):
        """ Check if the game has reached its end """
        return self.day > self.end_day

    def play(self):
        """ Main game loop """
        while not self.is_game_over():
            self.display_status()
            self.make_decision()
            self.update_day()

# Creating an instance of the game and starting it
game = FinancialGame()
game.play()

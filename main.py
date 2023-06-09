import random

MAX_LINES = 3       # best practice = use capital letters to declare constant values
MAX_BET = 100
MIN_BET = 1

# slot machine features
ROWS = 3    # lines 
COLS = 3    # wheels      

# dictionary containing symbols and their count in each wheel
symbol_count = {
    "A":2,
    "B":2,
    "C":2,
    "D":2
}

def get_slot_machine_spin(rows, cols, symbols):
    # making a list which will contain all possible symbols
    all_symbols = []    
    for symbol, symbol_count in symbols.items():    # for each entry in my dictionary...
        for i in range(symbol_count):               # ...append the symbol to my list as much times as its count value
            all_symbols.append(symbol)
    
    # Once we got our list of symbols, we need to select what values will go in every single column
    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]    # we make a copy of the all_symbols list...
        # ... because each time we pick a value, we remove it from the list, so that we don't pick it again
        # but we need to keep the original all_symbols list intact, or the next column will be empty
        for row in range(rows):
            value = random.choice(current_symbols)      # pick a value among those available in current_symbols
            current_symbols.remove(value)               # remove this value from my buffer list   
            column.append(value)                        # add this random value to the current column   
        columns.append(column)                          # add the current column to my columns list
    
    return columns                                      # columns is a list of lists

def print_slot_machine(columns):
    # TRANSPOSING our columns (currently layed out as rows) into actual columns
    # we say that we "transpose the matrix"
    for row in range(len(columns[0])):  # number of rows = number of elements in each of our columns
        # loop through of all of my columns and only print the first value
        for index, column in enumerate(columns):    # I use index + enumerate...
            if index != len(columns) - 1:           # ...because the pipe separator should not appear after the last column
                print(column[row], "|")             # using the pipe to separate columns
            else:
                print(column[row])

# First user inputs = deposit + bet
def deposit():
    while True:     # keep asking the user to enter a deposit amount until he gives a valid amount 
        amount = input("How much would you like to deposit? $")
        # I must ensure the user input is valid
        if amount.isdigit():    # check if inpût is a whole number
            amount = int(amount)    # user input is always a string, so I have to convert it
            if amount > 0:
                break           # break the while loop and bring us down to "return amount"
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a positive number!")
    return amount

def get_number_of_lines():
    while True:    
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():    
            lines = int(lines)    
            if 1 <= lines <= MAX_LINES:
                break      
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input(f"Enter the amount of your bet (${MIN_BET}-${MAX_BET}): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Enter a number between ${MIN_BET} and ${MAX_BET}.")
        else: 
            print("Please enter a positive number.")
    return amount
            

# I put my program in the function main() so that if I end my program, I can call this function again to rerun it
def main():                        
    balance = deposit()
    lines = get_number_of_lines()

    # making sure the balance is sufficient to place the bet
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if balance >= total_bet:
            break
        else: 
            print("Your current balance is insufficient to place this bet.")
            print(f"Your current balance: ${balance}. Your bet: ${total_bet}.")

    if lines == 1:
        print(f"Current balance: ${balance}. You are betting ${bet} on {lines} line. Total bet is equal to: ${total_bet}")
    else:
        print(f"Current balance: ${balance}. You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main()
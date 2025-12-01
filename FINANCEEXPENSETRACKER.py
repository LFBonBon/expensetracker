import matplotlib.pyplot as plt

def expense_tracker():
    expenses = {}

    while True:
        category = input("Enter category for expense (type 'quit' to exit):").lower()
        if category == "quit":
            break
        amount = float(input("Enter $ amount:"))
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount
    print("Expenses:")
    for category , amount in expenses.items():
        print(f"{category.capitalize()}: ${amount:.2f}")
    
    if expenses:
        labels = list(expenses.keys())
        values = list(expenses.values())

        plt.pie(values, labels=labels, autopct="%1.1f%%")
        plt.title("Expenses")
        plt.show()
    else:
        print("No info to display.")


expense_tracker()




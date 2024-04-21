class Customer:
    total_customer = 0

    def __init__(self, first_name, last_name, loyalty_points):
        self.first_name = first_name
        self.last_name = last_name
        self.loyalty_points = loyalty_points
        Customer.total_customer += 1

    def increase(self, loyalty_points):
        self.loyalty_points += loyalty_points


new_customer1 = Customer("Mia", "Fluffins", 2)
new_customer2 = Customer("Abdul", "Ammar", 1)

print(f"Dear Customer {new_customer2.first_name} {new_customer2.last_name}, you have {new_customer2.loyalty_points} loyalty points.")
print(f"Dear Customer {new_customer1.first_name} {new_customer1.last_name}, you have {new_customer1.loyalty_points} loyalty points.")
new_customer1.increase(3)
new_customer2.increase(4)
print(f"Dear Customer {new_customer2.first_name} {new_customer2.last_name}, you have {new_customer2.loyalty_points} loyalty points.")
print(f"Dear Customer {new_customer1.first_name} {new_customer1.last_name}, you have {new_customer1.loyalty_points} loyalty points.")
print(f"we have {Customer.total_customer} ")
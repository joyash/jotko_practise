class Restaurant:
    def __init__(self,name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Kotipizza serves wonderful pizza.")

    def open_restaurant(self):
        print("Kotipizza is open. Come on in!")




restaurant = Restaurant('Kotipizza', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
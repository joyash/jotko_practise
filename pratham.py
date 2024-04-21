class Dog:
    created = 0

    def __init__(self, name, birth_year, sound="Woof Woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound
        Dog.created += 1

    def bark(self, times):
        for i in range(times):
            print(f"{self.name} barks {self.sound} {i + 1} time")
        return


class Hotel:
    def __init__(self):
        self.dog_list = []

    def dog_checkin(self, dog):
        self.dog_list.append(dog)
        print(f"{dog.name} check in to hotel.")

    def dog_checkout(self, dog):
        self.dog_list.remove(dog)
        print(f"{dog.name} check out from hotel!")

    def dog_greet(self):
        for dog in self.dog_list:
            dog.bark(1)


dog1 = Dog("Rascal", 2022)
dog2 = Dog("Perkele", 2023, "Hyau Hyau")
print(f"{Dog.created} dogs have been created so far!")
hotel = Hotel()
hotel.dog_checkin(dog1)
hotel.dog_checkin(dog2)
hotel.dog_checkin(dog1)
hotel.dog_greet()

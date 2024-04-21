"""class School:
    def __init__(self, subject:str, score:float, grade_one = "A", grade_two = "B", grade_three = "C"):
        assert score, f"{score} must be an integer"
        assert subject, f"{subject}  subject should be an string"

        self.subject = subject
        self.score = score
        self.grade_one = grade_one
        self.grade_two = grade_two
        self.grade_three = grade_three

    def pass_mark(self):
        if self.score >= 80:
            return self.grade_one
        elif 70<= self.score < 80:
            return self.grade_two
        else:
            return self.grade_three
sofi = School("Math", 89 )
ram = School("physics", 97.3)
pritam = School("english", 33)

print(sofi.pass_mark())
print(ram.pass_mark())
print(pritam.pass_mark())"""


def dictfunction(numbers):
    dict = { }
    for x in range(len(numbers)-1,0,-1):
        if numbers[x] ** 2 % 2 != 0:
            dict[numbers[x]*2] = numbers[x] **2
    return dict

print(dictfunction([2,7,4,5]))

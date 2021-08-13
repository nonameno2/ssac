class Student:
    def __init__(self, name, a1, a2, a3, a4):
        self.name = name
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4

    def sum(self): 
        return self.a1 + self.a2 + self.a3 + self.a4
    
    def average(self):
        return self.sum() / 4

    def result(self):
        return "{} \t {} \t {}".format(self.name, self.sum(), self.average())

students = [
    Student("s1", 45, 49, 86, 94),
    Student("s2", 75, 32, 44, 15),
    Student("s3", 88, 95, 84, 65),
    Student("s4", 87, 97, 86, 78),
    Student("s5", 97, 65, 77, 66)
]

print("name", "total score", "average", sep = "\t")

for i in students:
    print(i.result())
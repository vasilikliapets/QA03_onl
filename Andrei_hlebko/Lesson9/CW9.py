class Worker:
    worker_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Worker.increase_count_worker()

    def get_name(self):
        return self.name

    @staticmethod
    def get_count_worker():
        return Worker.worker_count

    @staticmethod
    def increase_count_worker():
        Worker.worker_count += 1

worker1 = Worker("Andrei",1000)
print(worker1.name)
print(Worker.worker_count)



class Student:

    def __init__(self,name,money):
        self.name = name
        self.money = money

def most_money(list_name):
    max = list_name[0].money
    name = list_name[0].name
    for i in list_name:
        if i.money < max:
            max = i.money
            name = i.name
    return name
    #petya.money, gleb.money, anna.money
    # return max(list_name,key=lambda i: i.money)



petya = Student("Petya",3000)
gleb = Student("Gleb",4000)
anna = Student("Anna",1000)

print(most_money[petya,gleb,anna])
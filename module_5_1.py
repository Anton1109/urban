class House:
   def __init__(self, name, number_of_floors):
       self.name = name
       self.number_of_floors = number_of_floors

   def go_to (self, new_floor):
       for i in range(1, new_floor + 1):
           if 1 <= new_floor <= self.number_of_floors:
               print(i)
           else:
               print('такого этажа не существует')
               break
h1 = House('ЖК Горский', 30)
h2 = House('Домик в деревне', 20)
h1.go_to(5)
h2.go_to(10)
print(h1.name, h1.number_of_floors)
print(h2.name,h2.number_of_floors)












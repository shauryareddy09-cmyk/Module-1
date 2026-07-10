class cars:
 type="vehicle"

 def __init__(self,name,age):
  self.name=name
  self.age=age

ford=cars("ford",110)
tesla=cars("tesla",20)

print("ford is a {}".format(ford.type))
print("tesla is a {}".format(tesla.type))

print("{} is {} years old".format(ford.name,ford.age))
print("{} is {} years old".format(tesla.name,tesla.age))


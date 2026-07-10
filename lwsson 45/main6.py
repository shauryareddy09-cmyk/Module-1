class boeing:
 type="airliner"

 def __init__(self,name,age):
  self.name=name
  self.age=age

airbus=boeing("747",70)
cessna=boeing("787",20)

print("airbus is a {}".format(airbus.type))
print("The 787 is a {}".format(cessna.type))

print("{} is {} years old".format(airbus.name,airbus.age))
print("{} is {} years old".format(cessna.name,cessna.age))


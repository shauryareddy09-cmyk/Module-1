class Student:
 name="Nolan"
 grade="11"

 def introduction(self):
  print("Hello, I am a student")

 def  information(self):
  print("My name is ",self.name)
  print("I study in grade",self.grade)

ob=Student()
ob.introduction()
ob.information()
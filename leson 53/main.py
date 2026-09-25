n=4
guess=input("Total Points= 1 + 2 + 3 + 4=")
input("Formula: one calculation, Press enter to run ")
total=n *(n+1)//2
print("total=",total," steps=1")
input("Loop add one at a time Press enter to run")
total=0
for student in range(n,n+1):
    total+=student
print(" total",total,"steps =", n)
n=int(input("How many charachters to preview?"))
file=open("jetlist.txt","r")
print(file.read(n))
file.close()
print()

file=open("jetlist.txt")
lines=file.readlines()
file.close()
print("Total lines",len(lines))
for i in range(len(lines)):
    print(i + 1,"->",lines[i].strip)
print()

word=input("Skip lines starting with:")
file=open("jetlist.txt","r")
for line in file:
    if line.startswith(word):
        print("skip->",line.strip())
    else:
        print("keep->",line.strip())
file.close()
print()

file=open("jetlist.txt")
lines=file.readlines()
file.close()
out=open("odd-lines.txt")
for i in range(0,len(lines),2):
    out.write(lines[i])
out.close()
print("Odd lines saved to odd-lines.txt")


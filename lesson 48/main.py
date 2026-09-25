file=open("bucketlist.text","w")
file.write("1.Drive a gt3 car")
file.write("10.go skydiving")
file.write("11.Have a nice model airport 1:200 scale")
file.close()

file=open("bucketlist.text","r")
content=file.read()
print("My Bucket List")
print(content)
file.close

file=open("bucketlist.text","r")
lines=file.readlines()
print(f"You have {len(lines)} items in your bucket")
file.close()

file=open("bucketlist.text","a")
file.write("3.Drive a gt3 car")
file.write("4.go skydiving")
file.write("5.Have a nice model airport 1:200 scale")
file.write("6.Go to racing events")
file.write("7.Travel asia and Europe")
file.close()
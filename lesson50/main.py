print("=== Science Notes ===")
with open("sciencenotes.txt", "r") as f:
    for line in f:
        print(line.strip())
print()

print("=== Word Count ===")
with open("mathnotes.txt", "r") as f:
    for line in f:
        words = line.split()
        print(len(words), "words ->", line.strip())
print()

print("=== Merging Notes ===")
if os.path.exists("allnotes.txt"):
    print("allnotes.txt already exists - overwriting")
else:
    print("allnotes.txt not found - creating now")

content = ""
with open("sciencenotes.txt", "r") as f:
    content += "--- science-notes.txt ---\n"
    content += f.read() + "\n"
with open("mathnotes.txt", "r") as f:
    content += "--- mathsnotes.txt ---\n"
    content += f.read() + "\n"
with open("allnotes.txt", "w") as out:
    out.write(content)
print("Saved to allnotes.txt")
print()

if os.path.exists("allnotes.txt"):
    os.remove("allnotes.txt")
    print("allnotes.txt deleted.")
else:
    print("allnotes.txt does not exist.")



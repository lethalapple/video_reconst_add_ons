with open("MyFile.txt", "r") as f:
    contents = f.readlines()

contents.insert(0, "640 480\n")
with open("MyFile.txt", "w") as f:
    contents = "".join(contents)
    f.write(contents)

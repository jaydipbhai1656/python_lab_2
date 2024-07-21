with open("karan.txt","w") as file:
    file.write("Hello World")
with open("karan.txt","r") as file:
    content=file.read()
    print(content)
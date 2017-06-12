import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Write the names into a file
myfile=open("names", "w", encoding='utf-8')
data=["Chav\n", "Aleksandar\n", "Iva\n", "Кирил"]
myfile.writelines(data)
myfile.close()

# Read the names from the file
with open("names", "r") as myfile:
    content = (myfile.readlines())
    print(content)

# Read the names from the file
with open("names", "r", encoding='utf-8') as myfile:
    print(myfile.tell())
    myfile.seek(2)
    print(myfile.tell())
    myfile.seek(3)
    print(myfile.tell())

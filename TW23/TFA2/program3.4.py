fileObj = open("students.txt", "r")
information = fileObj.read()
fileObj.close()
print(information)
newText = input()

file = open("text.txt", "r")
text = file.read()
file.close()
file2 = open("text2.txt", "w")
file2.write(text+newText)
file2.close()


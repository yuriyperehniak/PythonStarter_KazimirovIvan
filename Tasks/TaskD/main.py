#Задача D
file_input = open("input.txt")
text = file_input.readlines()

text[-1] +="\n"
output_text = ""

for i in range(len(text)):
    output_text += text[-(i+1)]

print(output_text)

file_output = open("output.txt", "x")
file_output.write(output_text)
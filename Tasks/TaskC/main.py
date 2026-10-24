#Задача C
file_input = open("input.txt")
text = file_input.read()

output_text = ""

for i in range(len(text)):
    output_text += text[-(i+1)]

file_output = open("output.txt", "x")
file_output.write(output_text)
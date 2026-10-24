#Задача B
file_input = open("input.txt")
text = file_input.read().split()

sum = 0
for line in text:
    sum += int(line)

file_output = open("output.txt", "x")
file_output.write(str(sum))
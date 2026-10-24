filename = input("Filename: ")

schedule = {
    "Activity": input("Activity: "),
    "Time": input("Time: "),
    "Duration": input("Duration: ")
}

try:
    file = open(f"{filename}.txt", "a", encoding="utf-8")
except FileNotFoundError:
    file = open(filename,"x", encoding="utf-8")
except:
    print("File Error")
else:
    for key in schedule:
        if key == "Time":
            file.write(f"{key}: \t\t{schedule[key]}")
        else:
            file.write(f"{key}: \t{schedule[key]}")
        file.write("\n")
finally:
    file.write("--------------------\n")
    file.close()

from rich import print
fruits = ["живой", "груша", "яблуко", "слива", "овощ", 
          "чайник", "шоколадний", "вафля"]

def getFromList(list, index):
    try:
        value = list[index-1]
    except IndexError:
        print("[red]Нема такого індекса[/]")
    except TypeError:
        print("[red]Не правильний тип списку або індексу[/]")
    else:
        print(f"[blue]Елемент:[{value}][/]")
        print(f"[blue]Індекс:[{index}][/]")


while True:
    try:
        inputIndex = int(input())
    except ValueError:
        print("[red]Індекс має бути ЧИСЛОМ![/]")
    else:
        getFromList(fruits, inputIndex) 
    
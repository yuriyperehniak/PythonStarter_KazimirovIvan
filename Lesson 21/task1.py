from rich import print

num1 = int(input())
num2 = input()

try:
    print(num1 / num2)
except ZeroDivisionError:
    print("[red]Не можна ділити на 0[/]")
except TypeError:
    print("[green bold]Неправильний тип даних[/]")

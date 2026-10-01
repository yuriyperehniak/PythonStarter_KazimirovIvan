players = {
    "Андрій": 7,
    "Марта": 10,
    "Назар": 99
}

def greet(name, level):
    print(f"Гравець {name} - {level} рівня")

for name, level in players.items():
    greet(name, level)

u_name, u_level = input().split(" ")
greet(u_name, u_level)

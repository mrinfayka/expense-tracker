#пробная работа
print("Добро пожаловать в трекер расходов!")

expenses = []

while True:
    name = input("На что потратила деньги? (или 'стоп'): ")

    if name.lower() == "стоп":
        break

    amount = float(input("Сколько потратила? "))

    expenses.append((name, amount))
    print("Расход добавлен!\n")

print("\nТвои расходы:")

for name, amount in expenses:
    print(f"{name}: {amount:.2f}")

total = sum(amount for name, amount in expenses)

print(f"\nВсего потрачено: {total:.2f}")
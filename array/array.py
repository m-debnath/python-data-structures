from pprint import PrettyPrinter

pp = PrettyPrinter()

expenses_2022: list[dict[str, int]] = [
    {"January": 2200},
    {"February": 2350},
    {"March": 2130},
    {"April": 2600},
    {"May": 2190},
]

print("1. In February, how many dollars you spent extra compare to January?")
answer = list(expenses_2022[1].values())[0] - list(expenses_2022[0].values())[0]
print(f"Answer: {answer}")
print("")

no_of_months = 3
answer = 0
print(f"2. Find out your total expense first {no_of_months} months of the year.")
for i in range(no_of_months):
    answer += list(expenses_2022[i].values())[0]
print(f"Answer: {answer}")
print("")

search_term = 2000
found = False
print(f"3. Find out if you spent exactly {search_term} dollars in any month.")
for expense in expenses_2022:
    if list(expense.values())[0] == search_term:
        print(f"Answer: {list(expense.keys())[0]}")
        found = True
if not found:
    print("Answer: Not found")
print("")

new_month = "June"
new_expense = 1980
print(
    f"4. {new_month} month just finished and your expense is {new_expense} dollars. Add this item to our monthly expense list."
)
expenses_2022.append({new_month: new_expense})
print("Answer:")
pp.pprint(expenses_2022)
print("")

refund_month = "May"
refund_amount = 200
print(
    f"5. You returned an item that you bought in a month of {refund_month} and got a refund of {refund_amount} $. Make a correction to your monthly expense list based on this."
)
for expense in expenses_2022:
    if list(expense.keys())[0] == refund_month:
        expense[refund_month] -= refund_amount
        break
print("Answer:")
pp.pprint(expenses_2022)
print("")

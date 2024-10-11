num_soups = int(input())
money_in_bank = int(input())

if num_soups < 5:
    print('Not enough soups purchased')
else:
    total_cost = num_soups + 8
    if total_cost <= money_in_bank:
        print('Soups successfully purchased')
    else:
        print('Not enough money to buy all')

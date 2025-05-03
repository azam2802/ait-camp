clients = ["Emil", "Munara", "Timur", "Daiyrbek"]
balances = [2000, 4000, 5000, 600]

# for x, y in enumerate(clients):
#     print(y + ": " + str(balances[x]))

# count = 0
# while count < len(clients):
#     print(clients[count] + ": " + str(balances[count]))
#     count += 1


def transfer(fromClient, toClient, amount):
    if fromClient not in clients or toClient not in clients:
        print("Пользователь не найден")
        return
    if amount <= 0:
        print("Невозможно перевести сумму <= 0")
        return
    if balances[clients.index(fromClient)] < amount:
        print("Недостаточно средств")
        return
    balances[clients.index(fromClient)] -= amount
    balances[clients.index(toClient)] += amount


# transfer("Emil", "Munara", 0)


def transferToMany(fromClient: str, *toClients, amounts: list):
    if fromClient not in clients or all(i not in clients for i in toClients):
        print("Пользователь не найден")
        return
    if sum(amounts) <= 0:
        print("Невозможно перевести сумму <= 0")
        return
    if balances[clients.index(fromClient)] < sum(amounts):
        print("Недостаточно средств")
        return
    print(sum(amounts))
    balances[clients.index(fromClient)] -= sum(amounts)
    for i, v in enumerate(toClients):

        balances[clients.index(v)] += amounts[i]


# transferToMany("Emil", "Daiyrbek", "Timur", 'Daiyrbek', amounts=[1000, 500, 100])

clientsDictonary = {"Munara": 4000, "Timur": 5000, "Daiyrbek": 600, "Emil": 2000}


def transferDictionary(fromClient: str, toClient: str, amount: int):
    if not clientsDictonary.get(fromClient) or not clientsDictonary.get(toClient):
        print("Пользователь не найден")
        return
    if amount <= 0:
        print("Невозможно перевести сумму <= 0")
        return
    if balances[clients.index(fromClient)] < amount:
        print("Недостаточно средств")
        return
    clientsDictonary[fromClient] -= amount
    clientsDictonary[toClient] += amount


def transferToMany(fromClient: str, *toClients, amounts: list):
    if fromClient not in clients or all(i not in clients for i in toClients):
        print("Пользователь не найден")
        return
    
    if balances[clients.index(fromClient)] < sum(amounts):
        print("Недостаточно средств")
        return
    print(sum(amounts))
    balances[clients.index(fromClient)] -= sum(amounts)
    for i, v in enumerate(toClients):

        balances[clients.index(v)] += amounts[i]


transferDictionary("Emil", "Munara", 1000)

print(clientsDictonary)
print(balances)

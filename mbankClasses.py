from datetime import datetime


class Bank:
    def __init__(self, fee: int):
        self.clients = []
        self.fee = fee
        self.balance = 0

    def transfer(self, fromClient, toClient, amount):
        if not isinstance(amount, int) and not isinstance(amount, float):
            try:
                amount = float(amount)
            except:
                return "Введите число."

        if fromClient not in self.clients or toClient not in self.clients:
            return "Пользователь не найден."
        if amount <= 0:
            return "Неправильная сумма перевода."
        if fromClient == toClient:
            return "Невозможно перевести самому себе."
        feeAmount = amount * self.fee / 100
        if amount + feeAmount > fromClient.getBalance():
            return "Недостаточно средств для перевода."

        for i in self.clients:
            if i == fromClient:
                i.minusBalance(amount + feeAmount)
            elif i == toClient:
                i.plusBalance(amount)

        self.balance += feeAmount

        history = History(
            fromClient.getName(),
            toClient.getName(),
            amount,
            datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        )

        fromClient.addHistory(history)
        toClient.addHistory(history)
        return "Транзакция прошла успешно."

    def addClient(self, client):
        self.clients.append(client)
        return f"{client.getName()} успешно добавлен."

    def __str__(self):
        return f"Баланс банка: {self.balance}\nКлиенты:\n{'\n'.join(str(i) for i in self.clients)}"


class Client:
    def __init__(self, name, phone, balance):
        self.name = name
        self.phone = phone
        self.balance = balance
        self.history = []

    def getName(self):
        return self.name

    def getPhone(self):
        return self.phone

    def getBalance(self):
        return self.balance

    def plusBalance(self, amount):
        if amount <= 0:
            return "Неправильная сумма пополнения."
        self.balance += amount
        return "Счет пополнен успешно."

    def minusBalance(self, amount):
        if amount <= 0:
            return
        self.balance -= amount

    def addHistory(self, history):
        self.history.append(history)

    def printHistory(self):
        for i in self.history:
            print(i)

    def __str__(self):
        return f"{self.name}: {self.phone}, {self.balance}"


class History:
    def __init__(self, fromName, toName, amount, date):
        self.fromName = fromName
        self.toName = toName
        self.amount = amount
        self.date = date

    def __str__(self):
        return f"{self.fromName} -> {self.toName}: {self.amount} ({self.date})"


mbank = Bank(5)

client1 = Client("Emil", "+996552531101", 2000)
client2 = Client("Munara", "+996552531102", 4000)

print(mbank.addClient(client1))
print(mbank.addClient(client2))


print(mbank.transfer(client1, client2, "jhgfcxv"))

client1.printHistory()
print(mbank)

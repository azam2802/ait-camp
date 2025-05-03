document.getElementById("confirmButton").addEventListener("click", transferMoney)
document.getElementById("sendButton").addEventListener("click", showPasswordAndConfirm)

function showPasswordAndConfirm() {
    let pincode = document.getElementById("pincodeInput")
    let confirmButton = document.getElementById("confirmButton")
    let fromClient = document.getElementById("senderInput").value
    let toClient = document.getElementById("recieverInput").value
    let amount = document.getElementById("amountInput").value

    if (fromClient == "" || toClient == "" || amount == "") {
        alert("Please fill in all fields")
        return
    }

    pincode.style.visibility = "visible"
    confirmButton.style.visibility = "visible"
}

async function transferMoney() {
    let fromClient = document.getElementById("senderInput").value
    let toClient = document.getElementById("recieverInput").value
    let amount = document.getElementById("amountInput").value
    let pincode = document.getElementById("pincodeInput").value
    let error = document.getElementById("errorMessage")

    await fetch("http://127.0.0.1:5000/transfer", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            from: fromClient,
            to: toClient,
            amount: amount,
            pincode: pincode
        }),
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                error.innerText = data.error
                setTimeout(() => {
                    error.innerText = ""
                }, 3000)
            }
        })
    clearAll()
    getHistory()
    getClients()
}

function getHistory() {
    fetch("http://127.0.0.1:5000/history")
        .then(response => response.json())
        .then(data => {
            let history = document.getElementById("historyList")
            history.innerHTML = ""
            // [{ "from": "Daiyrbek", "to": "Emil", "amount": 1000, "date": "2023-10-01" }]
            for (let transaction of data) {
                let transactionItem = document.createElement("li")
                transactionItem.innerText = `${transaction.from} -> ${transaction.to}: ${transaction.amount} (${transaction.date})`
                history.appendChild(transactionItem)
            }
        })
}

async function getClients() {
    await fetch("http://127.0.0.1:5000/clients")
        .then(response => response.json())
        .then(data => {
            let clientsList = document.getElementById("clientsList")
            // Daiyrbek: 600, Emil: 2000, Munara: 4000, Timur: 5000
            clientsList.innerHTML = ""
            for (let client in data) {
                let clientItem = document.createElement("li")
                clientItem.innerText = `${client}: ${data[client]}`
                clientsList.appendChild(clientItem)
            }
        })
}

function clearAll() {
    let pincode = document.getElementById("pincodeInput")
    let confirmButton = document.getElementById("confirmButton")
    pincode.style.visibility = "hidden"
    confirmButton.style.visibility = "hidden"

    document.getElementById("senderInput").value = ""
    document.getElementById("recieverInput").value = ""
    document.getElementById("amountInput").value = ""
    document.getElementById("pincodeInput").value = ""
}

getClients()
getHistory()
function sendMessage() {
    let input = document.getElementById("userInput");
    let message = input.value;

    if (message === "") return;

    let chat = document.getElementById("messages");

    chat.innerHTML += `<p><b>You:</b> ${message}</p>`;

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        chat.innerHTML += `<p><b>AI:</b> ${data.reply}</p>`;
    });

    input.value = "";
}

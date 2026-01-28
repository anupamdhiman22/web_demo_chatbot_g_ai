// function sendMessage() {
//     let input = document.getElementById("userInput");
//     let message = input.value;

//     if (message === "") return;

//     let chat = document.getElementById("messages");

//     chat.innerHTML += `<p><b>You:</b> ${message}</p>`;

//     fetch("/chat", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json"
//         },
//         body: JSON.stringify({ message: message })
//     })
//     .then(res => res.json())
//     .then(data => {
//         chat.innerHTML += `<p><b>AI:</b> ${data.reply}</p>`;
//     });

//     input.value = "";
// }



function sendMessage() {
    let input = document.getElementById("userInput");
    let message = input.value.trim();

    if (message === "") return;

    let chat = document.getElementById("messages");

    chat.innerHTML += `<div class="message user">${message}</div>`;
    chat.scrollTop = chat.scrollHeight;

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        chat.innerHTML += `<div class="message ai">${data.reply}</div>`;
        chat.scrollTop = chat.scrollHeight;
    });

    input.value = "";
}

// Enter key support
document.getElementById("userInput").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});

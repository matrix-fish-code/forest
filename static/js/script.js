// Alternar menu lateral
document.getElementById("toggleMenu").addEventListener("click", function () {
    const menu = document.getElementById("menu");
    menu.classList.toggle("open");
});

// Selecionar entidade
function selectEntity(name) {
    document.getElementById("entityName").innerText = name;
}

// Ajustar altura do textarea conforme o conteúdo
document.getElementById("messageInput").addEventListener("input", function () {
    this.style.height = "auto";
    this.style.height = this.scrollHeight + "px";
});

// Enviar mensagem para o backend
document.getElementById("sendBtn").addEventListener("click", async function () {
    const input = document.getElementById("messageInput");
    const responseBox = document.getElementById("response");

    if (input.value.trim() === "") return;

    const userMessage = input.value;
    input.value = "";
    input.style.height = "50px"; // Reset altura

    responseBox.innerHTML += `<p><strong>Você:</strong> ${userMessage}</p>`;
    responseBox.scrollTop = responseBox.scrollHeight;

    try {
        const response = await fetch("/chat", { // Substitua pela rota correta do seu backend
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: userMessage })
        });

        const data = await response.json();
        if (data.response) {
            responseBox.innerHTML += `<p><strong>${document.getElementById("entityName").innerText}:</strong> ${data.response}</p>`;
            responseBox.scrollTop = responseBox.scrollHeight;
        } else {
            responseBox.innerHTML += `<p><strong>${document.getElementById("entityName").innerText}:</strong> Erro ao obter resposta.</p>`;
        }
    } catch (error) {
        responseBox.innerHTML += `<p><strong>${document.getElementById("entityName").innerText}:</strong> Erro na conexão com o backend.</p>`;
    }
});

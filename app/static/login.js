document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("login-form");
  const messageBox = document.getElementById("login-message");

  loginForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {
      const response = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });

      const result = await response.json();

      if (response.ok) {
        messageBox.classList.remove("hidden", "negative");
        messageBox.classList.add("positive");
        messageBox.textContent = result.message;
        setTimeout(() => {
          window.location.href = "/dashboard"; // Redirecionar
        }, 1000);
      } else {
        messageBox.classList.remove("hidden", "positive");
        messageBox.classList.add("negative");
        messageBox.textContent = result.error;
      }
    } catch (error) {
      messageBox.classList.remove("hidden", "positive");
      messageBox.classList.add("negative");
      messageBox.textContent = "Erro ao tentar logar. Tente novamente.";
    }
  });
});

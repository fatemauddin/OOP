const API_URL = "http://127.0.0.1:5000/categories";

function addCategory() {
    const input = document.getElementById("categoryInput");
    const name = input.value.trim();

    if (!name) return alert("Category cannot be empty");

    fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name })
    })
    .then(() => {
        input.value = "";
        loadCategories();
    });
}

function loadCategories() {
    fetch(API_URL)
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById("categoryList");
            list.innerHTML = "";

            data.forEach(cat => {
                const li = document.createElement("li");
                li.textContent = cat;
                list.appendChild(li);
            });
        });
}

loadCategories();

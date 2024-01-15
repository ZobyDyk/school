function generateTable() {
    var number = document.getElementById("numberInput").value;
    var tableContainer = document.getElementById("tableContainer");
    tableContainer.innerHTML = ""; // Vymaže předchozí tabulku

    if (number > 0) {
        var table = document.createElement("table");
        for (var i = 0; i < number; i++) {
            var row = table.insertRow();
            for (var j = 0; j < number; j++) {
                var cell = row.insertCell(); // Vytvoří prázdnou buňku
                cell.addEventListener('click', toggleHighlight); // Přidá posluchač událostí pro přepnutí vyznačení buňky
            }
        }
        tableContainer.appendChild(table);
    }
}

function toggleHighlight() {
    this.classList.toggle('highlight');
}

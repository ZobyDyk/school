<?php
$servername = "localhost";
$username = "root";
$password = "admin";
$dbname = "mojeDatabaze";

// Vytvoření připojení
$conn = new mysqli($servername, $username, $password, $dbname);

// Kontrola připojení
if ($conn->connect_error) {
    die("Připojení selhalo: " . $conn->connect_error);
}

$sql = "SELECT Jmeno, Narozen FROM osoby";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // výpis dat z každého řádku
    while($row = $result->fetch_assoc()) {
        echo "Jméno: " . $row["Jmeno"]. " - Narozen: " . $row["Narozen"]. "<br>";
    }
} else {
    echo "0 výsledků";
}
$conn->close();
?>

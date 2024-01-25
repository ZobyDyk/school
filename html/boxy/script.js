document.getElementById('addBox').addEventListener('click', function() {
    const container = document.getElementById('container');
    const boxNumber = container.children.length + 1;
    const box = createBox(boxNumber);
    container.appendChild(box);
    updateClearButtonVisibility();
});

document.getElementById('clearBoxes').addEventListener('click', function() {
    const container = document.getElementById('container');
    Array.from(container.children).forEach(box => {
        box.classList.add('fade-out');
    });

    // Počkat na dokončení animace než odstraníme boxy
    setTimeout(() => {
        container.innerHTML = '';
        updateClearButtonVisibility();
    }, 500); // 500 ms pro animaci
});

function createBox(number) {
    const box = document.createElement('div');
    box.classList.add('box');
    box.innerText = `Box #${number}`;

    box.addEventListener('click', function() {
        changeBoxColor(box);
    });

    return box;
}

function updateClearButtonVisibility() {
    const container = document.getElementById('container');
    const clearButton = document.getElementById('clearBoxes');
    clearButton.style.display = container.children.length > 0 ? 'block' : 'none';
}

function changeBoxColor(box) {
    const colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightpink', 'lightyellow'];
    const currentColor = box.style.backgroundColor;
    let nextColor = colors[Math.floor(Math.random() * colors.length)];

    // Zajistíme, aby se barva skutečně změnila
    while(nextColor === currentColor) {
        nextColor = colors[Math.floor(Math.random() * colors.length)];
    }

    box.style.backgroundColor = nextColor;
}

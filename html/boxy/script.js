document.getElementById('addBox').addEventListener('click', function() {
    const container = document.getElementById('container');
    const boxNumber = container.children.length + 1;
    const box = document.createElement('div');
    box.classList.add('box');
    box.innerText = 'Box #' + boxNumber;
    container.appendChild(box);

    document.getElementById('clearBoxes').style.display = 'block';
});

document.getElementById('clearBoxes').addEventListener('click', function() {
    const container = document.getElementById('container');
    container.innerHTML = '';
    this.style.display = 'none';
});

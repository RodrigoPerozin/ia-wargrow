function toggleTroopsInput() {
    const actionType = document.getElementById('action-type').value;
    const troopsContainer = document.getElementById('troops-container');

    if (actionType === 'troops') {
        troopsContainer.style.display = 'block';
    } else {
        troopsContainer.style.display = 'none';
    }
}

const elementButton = document.getElementById("do-movement");

elementButton.addEventListener('click', doMovement);

async function doMovement() {
    const color = document.getElementById('team-color').value;
    const movementType = document.getElementById('action-type').value;
    const troops = document.getElementById('troops').value;
    const resultElement = document.getElementById('result-play');
    const file = document.getElementById('file-receiver').files[0];

    if (file && color) {
        try {
            const formData = new FormData();
            formData.append('image', file);

            const response = await fetch('http://127.0.0.1:8000/predict-complete', {
                method: 'POST',
                body: formData,
            });

            const headers = {
                'Content-Type': 'application/json'
            };

            const jsonData = await response.json();
            let objResult = null;

            if (movementType === 'attack') {
                const responseNode = await fetch(`http://127.0.0.1:3000/attack?color=${color}`, {
                    method: 'POST',
                    body: jsonData,
                    headers: headers
                });
                objResult = await responseNode.json();
            } else if (movementType === 'move-troops') {
                const responseNode = await fetch(`http://127.0.0.1:3000/move-troop?color=${color}`, {
                    method: 'POST',
                    body: jsonData,
                    headers: headers
                });
                objResult = await responseNode.json();
            } else if (movementType === 'troops' && troops) {
                const responseNode = await fetch(`http://127.0.0.1:3000/movement?color=${color}&troops=${troops}`, {
                    method: 'POST',
                    body: jsonData,
                    headers: headers
                });
                objResult = await responseNode.json();
            }
            console.log(objResult);

            const messagesArray = objResult.message.toString().split('\n');

            // Gerar a lista em HTML
            const htmlList = '<ul>' + messagesArray.map(message => `<li>${message}</li>`).join('') + '</ul>';
    
            // Adicionar a lista ao elemento com o ID "message-list"
            document.getElementById('message-list').innerHTML = htmlList;
        } catch (error) {
            alert(error);
        }
    } else {
        document.getElementById('validations').textContent = 'Informe o campo cor e o print para execução da jogada!';
    }
}

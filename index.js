const elementButton = document.getElementById("do-movement");

elementButton.addEventListener('click', doMovement)

async function doMovement() {

    const color = document.getElementById('team-color').value;
    const troops = document.getElementById('troops').value;
    const firstMove = document.getElementById('first-move').value;
    const file = document.getElementById('file-receiver').files[0]

    if (file && color) {

            try {

                const formData = new FormData();

                formData.append('image', file)

                const response = await fetch('http://127.0.0.1:8000/predict-complete', {
                    method: 'POST',
                    body: formData,
                });

                const headers = {
                    'Content-Type': 'application/json'
                };
                const jsonData = await response.json();

                const responseNode = await fetch('http://127.0.0.1:3000/movement?color=' + color +  '&troops=' + troops, {
                    method: 'POST',
                    body: jsonData,
                    headers: headers
                })

                console.log(response)
                console.log(responseNode)

            } catch (error) {
                alert(error);
            }


    } else {
        document.getElementById('validations').textContent = 'Informe o campo cor e o print para execução da jogada!'
    }

}

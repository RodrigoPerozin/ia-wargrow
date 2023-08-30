const elementButton = document.getElementById("do-movement");

elementButton.addEventListener('click', doMovement)

async function doMovement() {

    const color = document.getElementById('team-color').value;
    const firstMove = document.getElementById('first-move').value;
    const file = document.getElementById('file-receiver').files[0]

    if (file && color) {

            try {

                const formData = new FormData();

                formData.append('file', file)

                const response = await fetch('http://localhost:3000/movement?color=' + color + '&firstMove=' + firstMove, {
                    method: 'POST',
                    body: formData,
                });

            } catch (error) {
                alert(error);
            }


    } else {
        document.getElementById('validations').textContent = 'Informe o campo cor e o print para execução da jogada!'
    }

}

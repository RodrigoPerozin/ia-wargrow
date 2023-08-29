const express = require('express');
const app = express();
const cors = require('cors')
const PORT = 3000;
const warPredictionController = require('../controller/warPredictionController');

app.use(express.json());
app.use(cors())

// movement
app.post('/movement', (req, res) => {

    const data = req.body;
    //fazer logica de chamar a request e python

    const troops = req.query.troops;
    const colorTeam = req.query.colorTeam;

    if (data && data.length) {

        const handledCountries = warPredictionController.handleCountries(data);

        const movements = warPredictionController.doFirstMove(troops, colorTeam, handledCountries)

        if (movements && movements.length) {

            let movementsStr = '';

            for (let movement of movements) {
                movementsStr += "\nMova " + movement.quantityTroops + ' unidades para o pais: ' + movement.country.name + '\n'
            }

            res.status(200).send(movementsStr);

        } else {
            res.status(500).send();
        }

    }

});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

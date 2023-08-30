const express = require('express');
const app = express();
const cors = require('cors')
const PORT = 3000;
const warPredictionController = require('../controller/warPredictionController');

app.use(express.json());
app.use(cors())


app.post('/movement', (req, res) => {

    const data = req.body;
    const troops = req.query.troops;
    const colorTeam = req.query.color;

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

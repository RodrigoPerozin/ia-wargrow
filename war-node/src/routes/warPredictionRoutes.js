const express = require("express");
const app = express();
const cors = require("cors");
const PORT = 3000;
const warPredictionController = require("../controller/warPredictionController");
const attackController = require("../controller/attackController");

app.use(express.json());
app.use(cors());


app.post("/attack", (req, res) => {
    
    const data = req.body;
    
    const colorTeam = req.query.color;
    const objId = req.query.obj;
    
    if (!data || !data.length || !colorTeam) {
        return res.status(400).json({ message: "Dados de ataque inválidos." });
    }

    const bestMove = attackController.doAttack(data, colorTeam);
    const objResult = {};
    let msg = "";

    if (bestMove) {
        msg += `${bestMove.attacker} ataca ${bestMove.defender}`;
    } else {
        msg = "Não ataque!"
    }

    objResult.message = msg
    return res.status(200).json(objResult);

});

app.post("/move-troop", (req, res) => {
    const data = req.body;
    const colorTeam = req.query.color;
    
    if (!data || !data.length || !colorTeam) {
        return res
            .status(400)
            .json({ message: "Dados de movimentação de tropas inválidos." });
    }

    const handledCountries =
        warPredictionController.findBestTransfersToReinforce(data, colorTeam);

    moveTroopArray = [];
    
    handledCountries.forEach((country) => {
        if (!moveTroopArray.includes(country)) {
            moveTroopArray.push(country);
        }
    });

    const moveTroopMessages = moveTroopArray.map((country) => {
        return country;
    });
    const responseObj = {
        message: moveTroopMessages.join("\n"),
    };

    return res.status(200).json(responseObj);
});

/*
app.post("/movement", (req, res) => {
    const data = req.body;
    const troops = req.query.troops;
    const colorTeam = req.query.color;

    if (!data || !data.length) {
        return res
            .status(400)
            .json({ message: "Dados de movimento inválidos." });
    }

    const handledCountries = warPredictionController.handleCountries(data);

    const movements = warPredictionController.doFirstMove(
        troops,
        colorTeam,
        handledCountries
    );

    if (!movements || !movements.length) {
        return res
            .status(500)
            .json({ message: "Falha ao calcular os movimentos." });
    }

    const movementMessagesArray = movements.map((movement) => {
        return `Mova ${movement.quantityTroops} unidades para o país: ${movement.country.name}`;
    });

    movementMessages = [];

    movementMessagesArray.forEach((country) => {
        if (!movementMessages.includes(country)) {
            movementMessages.push(country);
        }
    });

    const responseObj = {
        message: movementMessages.join("\n"),
    };

    return res.status(200).json(responseObj);
});
*/
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

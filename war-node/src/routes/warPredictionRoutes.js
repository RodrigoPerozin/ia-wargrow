const express = require("express");
const app = express();
const cors = require("cors");
const PORT = 3000;
const movementController = require("../controller/movementController");
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

    const bestMove = attackController.doAttack(data, colorTeam, objId);
    const objResult = {};
    let msg = "";

    if (bestMove) {
        msg += `${bestMove.attacker.name} ataca ${bestMove.defender.name}`;
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

    const moveTroopMessages = movementController.findBestTransfersToReinforce(data, colorTeam);

    const responseObj = {
        message: moveTroopMessages.join("\n"),
    };

    return res.status(200).json(responseObj);
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

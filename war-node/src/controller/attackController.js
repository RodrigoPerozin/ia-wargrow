const frontiersConstants = require("../constants/frontiersConstants");

function calculateWinProbability(attackerTroops, defenderTroops) {
    return attackerTroops - 1 - defenderTroops;
}

const attackController = {
    doAttack(data, colorTeam) {
        let possibleMoves = [];
        // let highestProbability = 0;
        for (const territory of data) {
            const attackerTroops = parseInt(territory.troop);

            if (attackerTroops < 2) continue;

            // Verifique se o território pertence ao colorTeam
            if (territory.color_name !== colorTeam) continue;

            // Verifique as fronteiras deste território usando frontiersConstants
            const borders = frontiersConstants.countriesFrontiers.find(
                (country) => country.countryName.toLowerCase() === territory.class_name.toLowerCase()
            );

            if (!borders || !(borders.frontiers.length > 0)) continue;

            for (const destinationTerritoryName of borders.frontiers) {
                // Encontre o território de destino correspondente
                const destinationTerritory = data.find(
                    (t) => t.class_name.toLowerCase() === destinationTerritoryName.toLowerCase()
                );

                if (destinationTerritory && destinationTerritory.color_name !== colorTeam) {
                    const defenderTroops = parseInt(destinationTerritory.troop);
                    // Calcular a probabilidade de vitória
                    const winProbability = calculateWinProbability(attackerTroops, defenderTroops);

                    // Defina um limiar de probabilidade para decidir se você deseja atacar
                    // const probabilityThreshold = 0.5; // Ajuste conforme necessário
                    // Verifique se esta jogada é uma das melhores

                    possibleMoves.push({
                        attacker: territory.class_name,
                        defender: destinationTerritory.class_name,
                        probability: winProbability,
                    });

                    // if (winProbability > probabilityThreshold) {
                    //     if (winProbability > highestProbability) {
                    //         // Esta é a nova melhor jogada, limpa a lista anterior
                    //         highestProbability = winProbability;
                    //         bestMoves = [
                    //             `${territory.class_name} ataque a ${destinationTerritory.class_name}`,
                    //         ];
                    //     } else if (winProbability === highestProbability) {
                    //         // Esta jogada tem a mesma probabilidade que a melhor jogada até agora
                    //         bestMoves.push(
                    //             `${territory.class_name} ataque a ${destinationTerritory.class_name}`
                    //         );
                    //     }
                    // }
                }
            }
        }

        const sortedList = possibleMoves.sort((x) => {
            return x.probability;
        });

        return sortedList[0];
    },
};

module.exports = attackController;

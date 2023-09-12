const frontiersConstants = require("../constants/frontiersConstants");

function calculateWinProbability(attackerTroops, defenderTroops) {
    return (attackerTroops - 1) - defenderTroops;
}

const attackController = {

    doAttack(data, colorTeam) {

        let possibleMoves = [];

        for (const territory of data) {
            const attackerTroops = parseInt(territory.troop);

            if (attackerTroops < 2) continue;

            if (territory.color_name !== colorTeam) continue;

            const borders = frontiersConstants.countriesFrontiers.find(
                (country) => country.countryName.toLowerCase() === territory.class_name.toLowerCase()
            );

            if (!borders || !(borders.frontiers.length > 0)) continue;

            for (const destinationTerritoryName of borders.frontiers) {

                const destinationTerritory = data.find(
                    (t) => t.class_name.toLowerCase() === destinationTerritoryName.toLowerCase()
                );

                if (destinationTerritory && destinationTerritory.color_name !== colorTeam) {
                    const defenderTroops = parseInt(destinationTerritory.troop);

                    const winProbability = calculateWinProbability(attackerTroops, defenderTroops);

                    possibleMoves.push({
                        attacker: territory.class_name,
                        defender: destinationTerritory.class_name,
                        probability: winProbability,
                    });
                }
            }
        }

        if (possibleMoves && possibleMoves.length) {

            const sortedList = possibleMoves.sort((x) => {
                return x.probability;
            });

            return sortedList[0];

        }

        return null;

    },
};

module.exports = attackController;

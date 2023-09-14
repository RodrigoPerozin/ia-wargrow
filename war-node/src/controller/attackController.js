const frontiersConstants = require("../constants/frontiersConstants");
const objConstants = require("../constants/objConstants");
const continentConstants = require("../constants/continentConstants");

function calculateWinProbability(attackerTroops, defenderTroops) {
    if (Number.isNaN(attackerTroops) || Number.isNaN(defenderTroops)) return 0;
    return (attackerTroops - 1) - defenderTroops;
}

function getDrawList(sortedList) {
    let higherScore = sortedList[sortedList.length - 1].probability;
    let newList = [];
    sortedList.forEach((element) => {
        if(element.probability === higherScore) newList.push(element);
    });
    return newList;
}

function getBestMoveByObjective(sortedList, teamColor, objId) {
    const obj = objConstants.find((obj) => obj.id == objId);
    if (!obj) return sortedList[sortedList.length - 1];
    if (obj.type === "REGION") return getBestMoveByRegion(sortedList, obj);
    if (obj.type === "TERRITORY") return getBestMoveByTerritory(sortedList, obj);
    if (obj.type === "COLOR") return getBestMoveByColor(sortedList, teamColor, obj);

}

function getBestMoveByRegion(bestMovesList, obj){
    let newList = bestMovesList.filter((element) => obj.regions.includes(element.defender));
    if(newList.length<=1) return bestMovesList[0];
    return getBestMoveByTerritory(newList);
}

function getBestMoveByTerritory(bestMovesList) {
    let newList = bestMovesList.filter((element) => element.attacker.continent === element.defender.continent);
    if (newList.length <= 1) return bestMovesList[0];
    return newList[0];
}

function getBestMoveByColor(bestMovesList, teamColor, obj) {
    if (teamColor === obj.enemyColor) return bestMovesList[0];
    let newList = bestMovesList.filter((element) => element.defender.color_name === obj.enemyColor);
    if (newList.length <= 1) return bestMovesList[0];
    return getBestMoveByTerritory(newList);
}

function getTerritoryContinent(territoryName) {
    const territoryContinent = continentConstants.find(
        (continent) => continent.countries.includes(territoryName.toLowerCase())
    );

    if (!territoryContinent) return "";

    return territoryContinent.name;
}


const attackController = {

    doAttack(data, colorTeam, objId) {

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

                    let defContinent = getTerritoryContinent(destinationTerritory.class_name);
                    let attContinent = getTerritoryContinent(territory.class_name);

                    possibleMoves.push({
                        attacker: {
                            name: territory.class_name,
                            troops: attackerTroops,
                            continent: attContinent,
                        },
                        defender: {
                            name: destinationTerritory.class_name,
                            troops: defenderTroops,
                            continent: defContinent,
                            color: destinationTerritory.color_name
                        },
                        probability: parseInt(winProbability),
                    });
                }
            }
        }

        if (!possibleMoves || possibleMoves.length<=0) return null;

        const sortedList = possibleMoves.sort((x, y) => x.probability - y.probability);

        const bestMovesList = getDrawList(sortedList)

        if(bestMovesList.length<=1) return sortedList[sortedList.length - 1];

        return getBestMoveByObjective(bestMovesList, colorTeam, objId);

    },
};

module.exports = attackController;

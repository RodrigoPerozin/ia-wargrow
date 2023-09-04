const Country = require('../model/countryModel');
const Movement = require('../model/movementModel')
const frontiersConstants = require('../constants/frontiersConstants')
const objConstants = require('../constants/objConstants')
const continentConstants = require('../constants/continentConstants')

const warPredictionController = {

    handleCountries(unhandledCountries, quantityTroops) {

        const handledCountries = [];

        if (unhandledCountries && unhandledCountries.length) {

            unhandledCountries.forEach(unhandledCountry => {

                unhandledCountry.class_name = unhandledCountry.class_name.replaceAll(' ', '_')

                const country = new Country(unhandledCountry.class_name, unhandledCountry.color_name);

                handledCountries.push(country);

            });

            this.populateFrontiers(handledCountries);

        }

        return handledCountries;

    },
    populateFrontiers(countries) {

        countries.forEach(country => {

            country.frontiers = frontiersConstants.countriesFrontiers
                .filter(frontier => frontier.countryName.toUpperCase() === country.name.toUpperCase())
                .map(f => f.frontiers);

        });

    },
    doFirstMove(quantityTroops, colorTeam, countries) {

        const groupByTeam = this.groupCountriesByColor(countries);

        const team = groupByTeam.filter(objGroup => objGroup.color.toUpperCase() === colorTeam.toUpperCase())[0];

        if (team.countries) {

            const movements = [];

            while (quantityTroops) {

                team.countries.forEach(country => {

                    if (quantityTroops) {

                        if (this.alreadyMoved(movements, country)) {

                            let editMovement = movements.filter(movement => movement.country === country)[0];

                            editMovement.quantityTroops++;

                        } else {
                            movements.push(new Movement(1, country))
                        }

                        quantityTroops--;

                    }

                })

            }
            return movements;
        }

    },
    groupCountriesByColor(countries) {

        const groupByColor = [];

        countries.forEach(country => {

            let objGroup = groupByColor.filter(obj => obj.color.toUpperCase() === country.color.toUpperCase())[0];

            if (objGroup) {

                if (!objGroup.countries) {
                    objGroup.countries = [];
                }

                objGroup.countries.push(country)

            } else {

                objGroup = {};
                objGroup.color = country.color.toUpperCase();
                objGroup.countries = [];

                objGroup.countries.push(country);

                groupByColor.push(objGroup);

            }

        });

        return groupByColor;

    },
    alreadyMoved(movements, country) {
        return movements.filter(movement => movement.country === country).length;
    },    
    doAttack(data, colorTeam, objectiveId) {

        function calculateTroopsToTransfer(attackerTroops, defenderTroops) {
            return Math.max(Math.floor(attackerTroops / 2), 1);
        }

        function calculateWinProbability(attackerTroops, defenderTroops, troopsToTransfer) {
            const attackerTroopsSimulation = Math.min(attackerTroops, 3);
            const defenderTroopsSimulation = Math.min(defenderTroops, 2);
        
            const attackerResults = [];
            const defenderResults = [];
        
            for (let i = 0; i < attackerTroopsSimulation; i++) {
                attackerResults.push(Math.floor(Math.random() * 6) + 1);
            }
        
            for (let i = 0; i < defenderTroopsSimulation; i++) {
                defenderResults.push(Math.floor(Math.random() * 6) + 1);
            }
        
            attackerResults.sort((a, b) => b - a);
            defenderResults.sort((a, b) => b - a);
        
            let attackerWins = 0;
            let defenderWins = 0;
        
            for (let i = 0; i < Math.min(attackerTroopsSimulation, defenderTroopsSimulation); i++) {
                if (attackerResults[i] > defenderResults[i]) {
                    attackerWins++;
                } else {
                    defenderWins++;
                }
            }
        
            const attackerWinProbability = attackerWins / attackerTroopsSimulation;
        
            const troopsToTransferCalculated = Math.min(attackerTroops - 1, troopsToTransfer);
            const troopsPassed = attackerTroops - troopsToTransferCalculated;
        
            return {
                winProbability: attackerWinProbability,
                troopsPassed,
                troopsToTransfer: troopsToTransferCalculated,
            };
        }
        
        const bestMoves = [];
        const objective = objConstants.objConstants.find((obj) => obj.id == objectiveId);
    
        if (!objective) {
            console.error("Objetivo não encontrado.");
            return bestMoves;
        }
    
        for (const territory of data) {
            const attackerTroops = parseInt(territory.troop);
    
            const continent = continentConstants.continentConstants.find((cont) =>
                cont.frontiers.includes(territory.class_name.toLowerCase())
            );
    
            if (attackerTroops >= 2 && territory.color_name === colorTeam && continent) {
                const borders = frontiersConstants.countriesFrontiers.find(
                    (country) => country.countryName.toLowerCase() === territory.class_name.toLowerCase()
                );
    
                if (borders && borders.frontiers.length > 0) {
                    for (const destinationTerritoryName of borders.frontiers) {
                        const destinationTerritory = data.find(
                            (t) => t.class_name.toLowerCase() === destinationTerritoryName.toLowerCase()
                        );
    
                        if (
                            destinationTerritory &&
                            destinationTerritory.color_name !== colorTeam
                        ) {
                            const defenderTroops = parseInt(destinationTerritory.troop);
                            let troopsToTransfer;
    
                            if (objective.regions) {
                                troopsToTransfer = calculateTroopsToTransfer(attackerTroops, defenderTroops);
                            } else if (objective.enemyColor) {
                                troopsToTransfer = attackerTroops - 1;
                            } else if (objective.territoryCount) {
                                const requiredTerritoryCount = objective.territoryCount;
                                if (attackerTroops > requiredTerritoryCount) {
                                    troopsToTransfer = calculateTroopsToTransfer(attackerTroops, defenderTroops);
                                } else {
                                    troopsToTransfer = 0;
                                }
                            }
    
                            const result = calculateWinProbability(
                                attackerTroops,
                                defenderTroops,
                                troopsToTransfer
                            );

                            if (result.winProbability > 0.5) {
                                const moveDescription = `${territory.class_name} ataque ${destinationTerritory.class_name} com probabilidade de ${result.winProbability * 100}% de vitória e transferir ${result.troopsToTransfer} tropas`;
                                bestMoves.push(moveDescription);
                            }
                        }
                    }
                }
            }
        }
    
        return bestMoves;
    },    
    findBestTransfersToReinforce(data, colorTeam) {
        const bestTransfers = [];
        let maxTroopDifference = 0;

        for (const territory of data) {
            if (territory.color_name === colorTeam) {
                // Verifique as fronteiras deste território
                const fronteiras = frontiersConstants.countriesFrontiers.find(
                    (country) => country.countryName.toLowerCase() === territory.class_name.toLowerCase()
                );

                if (fronteiras && fronteiras.frontiers.length > 0) {
                    for (const frontierName of fronteiras.frontiers) {
                        // Encontre o território de fronteira correspondente
                        const frontierTerritory = data.find(
                            (t) => t.class_name.toLowerCase() === frontierName.toLowerCase()
                        );

                        if (
                            frontierTerritory &&
                            frontierTerritory.color_name === colorTeam
                        ) {
                            // Calcule a diferença entre as tropas nos territórios
                            const troopDifference = territory.troop - frontierTerritory.troop;

                            // Verifique se a diferença é maior que a máxima registrada até agora
                            if (troopDifference > maxTroopDifference) {
                                bestTransfers.length = 0; // Limpe o array se encontrar uma diferença maior
                                maxTroopDifference = troopDifference;
                            }

                            // Se a diferença for igual à máxima registrada, adicione ao array
                            if (troopDifference === maxTroopDifference) {
                                const transferMessage = `Mova ${troopDifference} tropas do ${territory.class_name} para o ${frontierTerritory.class_name}`;
                                bestTransfers.push(transferMessage);
                            }
                        }
                    }
                }
            }
        }

        return bestTransfers;
    }
}

module.exports = warPredictionController;

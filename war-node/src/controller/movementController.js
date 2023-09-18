const Country = require('../model/countryModel');
const Movement = require('../model/movementModel')
const frontiersConstants = require('../constants/frontiersConstants')
const objConstants = require('../constants/objConstants')
const continentConstants = require('../constants/continentConstants')

class Transfer {
    constructor(territory_i, territory_f, troops) {
        this.territory_i = territory_i;
        this.territory_f = territory_f;
        this.troops = troops;
    }
}


const movementController = {

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
    findBestTransfersToReinforce(data, colorTeam) {

        const movements = [];

        for (const territory of data) {

            if (territory.color_name === colorTeam && territory.troop > 1) {

                const frontiers = frontiersConstants.countriesFrontiers.filter(
                    (country) => country.countryName.toLowerCase() === territory.class_name.toLowerCase()
                ).map(frontierObj => frontierObj.frontiers)[0];

                if (frontiers && frontiers.length) {

                    const countriesFrontiers = frontiers.map(frontierName => data.find(country => country.class_name.toUpperCase() === frontierName.toUpperCase()));
                    const enemiesFrontiers = countriesFrontiers.filter(country => country && country.color_name && country.color_name.toUpperCase() !== colorTeam.toUpperCase());

                    if (enemiesFrontiers && enemiesFrontiers.length) {
                        continue;
                    } else {

                        const selectedCountry = this.getBestMovementByFriendlyFrontiersCountry(countriesFrontiers, data, colorTeam);

                        if (selectedCountry) {
                            movements.push('Mova todas as tropas possíveis do pais ' + territory.class_name + ' para o país ' + selectedCountry.class_name)
                        } else {
                            movements.push('Mova todas as tropas possíveis do pais ' + territory.class_name + ' para o país ' + countriesFrontiers[0].class_name)
                        }


                    }

                }

            }

        }

        return movements && movements.length >= 1 ? movements : ['Não fazer movimentações!']; // Retorna um array com as mensagens das melhores transferências

    },
    getBestMovementByFriendlyFrontiersCountry(friendlyCountriesFrontiers, allCountries) {

        for (const territory of friendlyCountriesFrontiers) {


            const frontiers = frontiersConstants.countriesFrontiers.filter(
                (country) => country.countryName.toLowerCase() === territory.class_name.toLowerCase()
            ).map(frontierObj => frontierObj.frontiers)[0];

            if (frontiers && frontiers.length) {

                let colorTeam = territory.color_name;
                const countriesFrontiers = frontiers.map(frontierName => allCountries.find(country => country.class_name.toUpperCase() === frontierName.toUpperCase()));
                const enemiesFrontiers = countriesFrontiers.filter(country => country.color_name && country.color_name.toUpperCase() !== colorTeam.toUpperCase());

                if (enemiesFrontiers && enemiesFrontiers.length) {
                    return territory;
                }

            }

        }

    }

}

module.exports = movementController;

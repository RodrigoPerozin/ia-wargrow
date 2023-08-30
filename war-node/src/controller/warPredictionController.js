const Country = require('../model/countryModel');
const Movement = require('../model/movementModel')
const frontiersConstants = require('../constants/frontiersConstants')

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

                            editMovement.quantityTroops ++;

                        } else {
                            movements.push(new Movement(1, country))
                        }

                        quantityTroops --;

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
    }

}

module.exports = warPredictionController;

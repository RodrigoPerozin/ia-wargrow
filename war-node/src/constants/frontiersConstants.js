const frontiersConstants = {
    countriesFrontiers: [
        {
            countryName: 'brasil',
            frontiers: ["argentina", "peru", "venezuela", "argelia"]
        },
        {
            countryName: "argentina",
            frontiers: ["peru", "brasil"]
        },
        {

            countryName: "peru",
            frontiers: ["brasil", "argentina", "venezuela"]
        },

        {
            countryName: "venezuela",
            frontiers: ["brasil", "peru", "mexico"]
        },
        {
            countryName: "mexico",
            frontiers: ["venezuela", "nova york", "california"]
        },
        {
            countryName: "mexico",
            frontiers: ["venezuela", "nova york", "california"]
        },
        {
            countryName: "nova york",
            frontiers: ["mexico", "california", "ottawa", "labrador"]
        },
        {
            countryName: "california",
            frontiers: ["nova york", "ottawa", "vancouver", "mexico"]
        },
        {
            countryName: "ottawa",
            frontiers: ["labrador", "nova york", "california", "vancouver", "mackenzie"]
        },
        {
            countryName: "vancouver",
            frontiers: ["mackenzie", "alaska", "ottawa", "california"]
        },
        {
            countryName: "labrador",
            frontiers: ["ottawa", "nova york", "groenlandia"]
        },
        {
            countryName: "mackenzie",
            frontiers: ["alaska", "vancouver", "ottawa", "groenlandia"]
        },
        {
            countryName: "groenlandia",
            frontiers: ["mackenzie", "islandia"]
        },
        {
            countryName: "alaska",
            frontiers: ["mackenzie", "vancouver", "vladvostok"]
        },
        {
            countryName: "islandia",
            frontiers: ["groenlandia", "inglaterra"]
        },
        {
            countryName: "inglaterra",
            frontiers: ["islandia", "suecia", "alemanha", "franca"]
        },
        {
            countryName: "franca",
            frontiers: ["polinia", "alemanha", "inglaterra", "argelia"]
        },
        {
            countryName: "polinia",
            frontiers: ["alemanha", "moscou", "franca", "oriente medio", "egito"]
        },
        {
            countryName: "alemanha",
            frontiers: ["inglaterra", "polinia", "franca"]
        },
        {
            countryName: "suecia",
            frontiers: ["moscou", "inglaterra"]
        },
        {
            countryName: "moscou",
            frontiers: ["suecia", "omsk", "oriente medio", "polinia", "aral"]
        },
        {
            countryName: "egito",
            frontiers: ["argelia", "sudao", "oriente medio", "polinia", "franca"]
        },
        {
            countryName: "sudao",
            frontiers: ["egito", "argelia", "congo", "madagascar", "africa do sul"]
        },
        {
            countryName: "congo",
            frontiers: ["sudao", "africa do sul", "argelia"]
        },
        {
            countryName: "africa do sul",
            frontiers: ["madagascar", "congo", "sudao"]
        },
        {
            countryName: "madagascar",
            frontiers: ["africa do sul", "sudao"]
        },
        {
            countryName: "vladvostok",
            frontiers: ["siberia", "tchita", "china", "japao", "alaska"]
        },
        {
            countryName: "siberia",
            frontiers: ["vladvostok", "tchita", "dudinka"]
        },
        {
            countryName: "tchita",
            frontiers: ["mongolia", "dudinka", "siberia", "vladvostok", "china"]
        },
        {
            countryName: "dudinka",
            frontiers: ["siberia", "tchita", "omsk", "mongolia"]
        },
        {
            countryName: "omsk",
            frontiers: ["mongolia", "dudinka", "moscou", "aral", "china"]
        },
        {
            countryName: "aral",
            frontiers: ["omsk", "china", "moscou", "oriente medio", "india"]
        },
        {
            countryName: "oriente medio",
            frontiers: ["aral", "india", "egito", "polinia", "moscou"]
        },
        {
            countryName: "mongolia",
            frontiers: ["china", "tchita", "omsk", "dudinka"]
        },
        {
            countryName: "vietna",
            frontiers: ["india", "china", "borneo"]
        },
        {
            countryName: "japao",
            frontiers: ["china", "vladvostok"]
        },
        {
            countryName: "china",
            frontiers: ["vladvostok", "tchita", "mongolia", "aral", "india", "vietna", "japao", "omsk"]
        },
        {
            countryName: "india",
            frontiers: ["oriente medio", "china", "aral", "vietna", "sumatra"]
        },
        {
            countryName: "argelia",
            frontiers: ["egito", "sudao", "congo", "brasil", "franca"]
        },
        {
            countryName: "sumatra",
            frontiers: ["australia", "india"]
        },
        {
            countryName: "borneo",
            frontiers: ["australia", "vietna"]
        }
    ]

}

module.exports = frontiersConstants;













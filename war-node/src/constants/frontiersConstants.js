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
            frontiers: ["venezuela", "nova_york", "california"]
        },
        {
            countryName: "mexico",
            frontiers: ["venezuela", "nova_york", "california"]
        },
        {
            countryName: "nova_york",
            frontiers: ["mexico", "california", "ottawa", "labrador"]
        },
        {
            countryName: "california",
            frontiers: ["nova_york", "ottawa", "vancouver", "mexico"]
        },
        {
            countryName: "ottawa",
            frontiers: ["labrador", "nova_york", "california", "vancouver", "mackenzie"]
        },
        {
            countryName: "vancouver",
            frontiers: ["mackenzie", "alaska", "ottawa", "california"]
        },
        {
            countryName: "labrador",
            frontiers: ["ottawa", "nova_york", "groenlandia"]
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
            frontiers: ["polonia", "alemanha", "inglaterra", "argelia"]
        },
        {
            countryName: "polonia",
            frontiers: ["alemanha", "moscou", "franca", "oriente_medio", "egito"]
        },
        {
            countryName: "alemanha",
            frontiers: ["inglaterra", "polonia", "franca"]
        },
        {
            countryName: "suecia",
            frontiers: ["moscou", "inglaterra"]
        },
        {
            countryName: "moscou",
            frontiers: ["suecia", "omsk", "oriente_medio", "polonia", "aral"]
        },
        {
            countryName: "egito",
            frontiers: ["argelia", "sudao", "oriente_medio", "polonia", "franca"]
        },
        {
            countryName: "sudao",
            frontiers: ["egito", "argelia", "congo", "madagascar"]
        },
        {
            countryName: "congo",
            frontiers: ["sudao", "africa_do_sul", "argelia"]
        },
        {
            countryName: "africa_do_sul",
            frontiers: ["madagascar", "congo", "sudao"]
        },
        {
            countryName: "madagascar",
            frontiers: ["africa_do_sul", "sudao"]
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
            frontiers: ["omsk", "china", "moscou", "oriente_medio", "india"]
        },
        {
            countryName: "oriente_medio",
            frontiers: ["aral", "india", "egito", "polonia", "moscou"]
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
            frontiers: ["oriente_medio", "china", "aral", "vietna", "sumatra"]
        }
    ]

}

module.exports = frontiersConstants;













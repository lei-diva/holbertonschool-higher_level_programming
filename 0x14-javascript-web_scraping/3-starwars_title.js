#!/usr/bin/node
const request = require("request")
request("http://swapi.co/api/films/" + process.argv[2], function(error, response, body){
    const info = JSON.parse(body)
    console.log(info.title)
});
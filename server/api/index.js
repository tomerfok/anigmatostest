const express = require('express');
const bodyParser = require('body-parser')
const request = require('request');

const app = express();
const port = 3000;
const flaskServerURL = 'http://127.0.0.1:8080';

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }))

app.get('/', (req, res) => {
    try {
        res.send("Welcome to my Nodejs Server");
    } catch (err) {
        throw err;
    }
});

app.post('/create', (req, res) => {
    let { username, email } = req.body;
    let customer = { username, email };
    try {
        request.post({ url: `${flaskServerURL}/create`, headers: { "content-type": "application/json"}, body: customer, json: true }, (error, response, body ) => {
            res.send(body);
        });
    } catch (err) {
        throw err;
    }
});

app.listen(port, () => {
  console.log(`App listening on port ${port}`)
})
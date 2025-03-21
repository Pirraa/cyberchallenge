// Importa il modulo node-fetch
import fetch from 'node-fetch';  // usa require('node-fetch') se usi CommonJS

// Definizione delle variabili direttamente nel codice
const login = "true";
const username = "admin2";
const code = "0111100110000000000011001110000000000000110000000000000000000111000000000000000000000000001000011100";
const wsPort = "20002";

// Funzione per inviare la richiesta di login
function sendLoginRequest() {
    const loginData = {
        username: username,
        code: code,
        login: login
    };

    fetch('http://ctf.unife.it:20001/login2', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams(loginData).toString()
    })
    .then(response => {
        console.log('Response Status:', response.status);  // Stampa lo status della risposta
        return response.text();  // Usa .text() invece di .json() per ottenere la risposta raw
    })
    .then(data => {
        console.log('Response Body:', data);  // Stampa il corpo della risposta raw
        try {
            const jsonData =data;  // Tentiamo di fare il parsing solo se la risposta è JSON
            console.log('Login riuscito:', jsonData);
            sendGameRequest();
        } catch (error) {
            console.error('Errore nel parsing della risposta JSON:', error);
        }
    })
    .catch(error => {
        console.error('Errore nel login:', error);
    });
}

// Funzione per inviare una richiesta al gioco
function sendGameRequest() {
    const gameData = {
        username: username,
        ws_port: wsPort
    };

    fetch('http://ctf.unife.it:20001/battleship', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        console.log('Response Status:', response.status);
        return response.text();  // Usa .text() se non è un JSON
    })
    .then(data => {
        console.log('Response Body:', data);  // Stampa la risposta raw (HTML, testo, etc.)
        // Gestisci il dato ricevuto come testo
    })
    .catch(error => {
        console.error('Errore nel gioco:', error);
    });
}

// Esegui la richiesta di login quando la pagina è pronta
sendLoginRequest();

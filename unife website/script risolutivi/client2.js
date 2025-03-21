import fetch from 'node-fetch';
import WebSocket from 'ws';

// Definizione delle variabili
const login = "true";
const username = "admin23";
const code = "1101101100000000000011101110100000000000111101110000000000000000000000000000000000000000000000000000";
const wsPort = "20002";

// Variabile per la connessione WebSocket
let ws;
let opponentGrid = [];
let myGrid = [];
let myHP = 18;
let opponentHP = 18;
let isMyTurn = false;

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
    .then(response => response.text())
    .then(data => {
        console.log('Login riuscito:', data);
        establishWebSocketConnection(); // Dopo il login, stabilisci la connessione WebSocket
    })
    .catch(error => {
        console.error('Errore nel login:', error);
    });
}

// Funzione per stabilire la connessione WebSocket
function establishWebSocketConnection() {
    // Inizializza la connessione WebSocket
    ws = new WebSocket(`ws://ctf.unife.it:${wsPort}`);

    ws.onopen = () => {
        console.log('Connessione WebSocket stabilita');
        sendGridData(); // Una volta connesso, invia la griglia
    };

    ws.onmessage = (event) => {
        const message = JSON.parse(event.data);
        console.log('Messaggio ricevuto dal server:', message);

        // Gestire il messaggio di tipo 'sync' che contiene le informazioni sullo stato del gioco
        if (message.type === 'sync') {
            console.log('Griglia sincronizzata con il server:', message);
            myGrid = message.grid; // Aggiorna la tua griglia
            opponentGrid = message.opp_grid; // Aggiorna la griglia dell'avversario
            myHP = message.hp; // Aggiorna i tuoi punti vita
            opponentHP = message.opp_hp; // Aggiorna i punti vita dell'avversario
            isMyTurn = message.turn; // Aggiorna se è il tuo turno

            // Se è il tuo turno, fai una mossa
            if (isMyTurn) {
                AI_Think(); // L'IA fa la sua mossa
            }
        }
    };

    ws.onerror = (error) => {
        console.error('Errore nella connessione WebSocket:', error);
    };

    ws.onclose = () => {
        console.log('Connessione WebSocket chiusa');
    };
}

// Funzione per inviare la griglia tramite WebSocket
function sendGridData() {
    const gridData = {
        type: "join",  // Tipo di messaggio per unire la partita
        username: username,
        code: code, // La tua griglia di battaglia (codice)
        ws_port: wsPort
    };

    // Invia la griglia al server attraverso WebSocket
    if (ws && ws.readyState === WebSocket.OPEN) {
        ws.send(JSON.stringify(gridData));
        console.log('Griglia inviata al server:', gridData);
    } else {
        console.log('La connessione WebSocket non è ancora aperta');
    }
}

// Funzione che implementa la logica dell'IA per fare una mossa
function AI_Think() {
    let targetCells = []; // Array per memorizzare le celle che contengono navi dell'avversario e non sono state colpite

    // Scorri tutte le celle della griglia dell'avversario
    for (let i = 0; i < opponentGrid.length; i++) {
        if (opponentGrid[i].ship && !opponentGrid[i].hit) {
            targetCells.push(i); // Aggiungi la cella all'array se contiene una nave e non è stata colpita
        }
    }

    if (targetCells.length === 0) {
        console.log("Non ci sono più navi da colpire!");
        return; // Se non ci sono più navi da colpire, termina la funzione
    }

    // Se ci sono celle valide da colpire, scegli una casuale tra quelle disponibili
    let randomIndex = Math.floor(Math.random() * targetCells.length);
    let chosenCell = targetCells[randomIndex];

    // Calcola la posizione della cella (riga, colonna)
    let chosen = [String(chosenCell).substring(0, 1), String(chosenCell).substring(1)];

    // Invia l'attacco al server
    let msg = {
        type: "attack",
        username: username,
        target: "opponent", // Opponent è l'utente avversario
        box: chosen // La cella da colpire
    };
    attack(msg);
    console.log('Attacco inviato:', msg);
}

// Funzione per inviare un attacco al server
function attack(msg) {
    if (ws && ws.readyState === WebSocket.OPEN) {
        ws.send(JSON.stringify(msg));
        console.log(`Attacco inviato a ${msg.target} con la cella ${msg.box}`);
    } else {
        console.log('La connessione WebSocket non è ancora aperta');
    }
}

// Funzione per aggiornare lo stato del gioco
function update(ws) {
    let opp_grid = [];
    try {
        for (let i = 0; i < ws.opponent.grid.length; i++) {
            let square = {
                id: i,
                ship: ws.opponent.grid[i].ship,
                hit: ws.opponent.grid[i].hit,
            };
            opp_grid.push(square);
        }

        let msg = {
            type: "sync",
            username: ws.username,
            hp: ws.hp,
            grid: ws.grid,
            turn: ws.turn,
            opp_username: ws.opponent.username,
            opp_hp: ws.opponent.hp,
            opp_grid: opp_grid,
        };

        ws.send(JSON.stringify(msg)); // Invio lo stato aggiornato
    } catch (e) {
        console.log("Si è verificato un errore nella funzione update");
    }
}

// Esegui la richiesta di login quando la pagina è pronta
sendLoginRequest();

import fetch from 'node-fetch';
import WebSocket from 'ws';

// Definizione delle variabili
const login = "true";
const username = "admin23";
const code = "1101101100000000000011101110100000000000111101110000000000000000000000000000000000000000000000000000";
const wsPort = "20002";

// Variabile per la connessione WebSocket
let ws;

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
            console.log('La griglia dell\'avversario:', message.opp_grid);
            console.log('La tua griglia:', message.grid);

            // Dopo aver ricevuto la griglia, esegui le mosse
            makeMoves(message.grid, message.opp_grid);
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

// Funzione per fare una mossa su tutte le caselle con ship=true
function makeMoves(grid, oppGrid) {
    // Trova tutte le caselle che contengono una nave (ship: true) e non sono già state colpite
    const shipCells = grid.filter(cell => cell.ship === true && !cell.hit);

    // Funzione per inviare le mosse una per una
    function sendNextMove(index) {
        if (index < shipCells.length) {
            const cell = shipCells[index];

            // Crea il messaggio della mossa
            const moveData = {
                type: 'move',
                username: username,
                code: code,
                ws_port: wsPort,
                target_id: cell.id // La casella da colpire (id della nave)
            };

            // Invia la mossa al server
            if (ws && ws.readyState === WebSocket.OPEN) {
                ws.send(JSON.stringify(moveData));
                console.log(`Mossa inviata: colpito id ${cell.id}`);

                // Dopo aver inviato la mossa, attendi la risposta del server per inviare la mossa successiva
                ws.once('message', (event) => {
                    const message = JSON.parse(event);
                    if (message.type === 'sync') {
                        // Dopo ogni mossa, controlla se una nave è stata affondata
                        checkSunkStatus(message.opp_grid);

                        // Procedi con la mossa successiva
                        sendNextMove(index + 1);
                    }
                });
            } else {
                console.log('La connessione WebSocket non è ancora aperta');
            }
        } else {
            console.log('Tutte le mosse sono state inviate');
        }
    }

    // Avvia il ciclo per inviare la prima mossa
    sendNextMove(0);
}

// Funzione per verificare se una nave è stata affondata
function checkSunkStatus(oppGrid) {
    // Verifica se una nave è affondata nella griglia dell'avversario
    oppGrid.forEach(cell => {
        if (cell.ship === true && cell.hit === true) {
            console.log(`La nave con id ${cell.id} è stata colpita!`);
            if (cell.sunk) {
                console.log(`La nave con id ${cell.id} è affondata!`);
            }
        }
    });
}

// Esegui la richiesta di login quando la pagina è pronta
sendLoginRequest();

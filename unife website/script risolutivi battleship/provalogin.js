import fetch from 'node-fetch';

async function login(username, code) {
    try {
        const response = await fetch('http://ctf.unife.it:20001/login2', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({ username: username, code: code })
        });

        // Verifica che la risposta sia in formato JSON
        const contentType = response.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            const data = await response.json();
            console.log(data); // Log la risposta JSON
        } else {
            const text = await response.text(); // Se non è JSON, prendi il corpo come testo
            console.log('La risposta non è JSON:', text);
        }
    } catch (error) {
        console.error('Errore durante il login:', error);
    }
}

// Esegui il login con un esempio
login('NomeUtente', 'someCode');

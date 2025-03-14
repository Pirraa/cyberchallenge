const sqlite = require('sqlite-async');
const crypto = require('crypto');

class Database {
    constructor(db_file) {
        this.db_file = db_file;
        this.db = undefined;
    }
    
    async connect() {
        this.db = await sqlite.open(this.db_file);
    }

    async migrate() {
        let rand = crypto.randomBytes(5).toString('hex');

        return this.db.exec(`
            DROP TABLE IF EXISTS emojis;
            DROP TABLE IF EXISTS flag_${ rand };

            CREATE TABLE IF NOT EXISTS flag_${ rand } (
                flag TEXT NOT NULL
            );

            INSERT INTO flag_${ rand } (flag) VALUES ('0xfe{fake_flag}');

            CREATE TABLE IF NOT EXISTS emojis (
                id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                emoji   VARCHAR(255),
                name    VARCHAR(255),
                count   INTEGERT
            );

            INSERT INTO emojis (emoji, name, count) VALUES
                ('👽', 'alien', 13),
                ('🛸', 'flying saucer', 3),
                ('👾', 'alien monster', 0),
                ('💩', '👇 = human', 118),
                ('🍌', 'banana', 21),
                ('🐶', 'dog', 80),
                ('🐧', 'clmlnz', 0),
                ('🧙', 'BL30', 0),
                ('🦄' , 'P3ACE', 37),
                ('🦖', 'Franfill', 0),
                ('👣', 'awakeopossum', 0),
                ('😸', 'bloodshadowwolf', 0),
                ('🤓','JDrifter', 0),
                ('👨', 'homo idiotus', 124)
        `);
    }

    async vote(id) {
        return new Promise(async (resolve, reject) => {
            try {
                let query = 'UPDATE emojis SET count = count + 1 WHERE id = ?';
                resolve(await this.db.run(query, [id]));
            } catch(e) {
                reject(e);
            }
        });
    }

    async getEmojis(order) {
        // TOOD: add parametrization
        return new Promise(async (resolve, reject) => {
            try {
                let query = `SELECT * FROM emojis ORDER BY ${ order }`;
                resolve(await this.db.all(query));
            } catch(e) {
                reject(e);
            }
        });
    }
}

module.exports = Database;

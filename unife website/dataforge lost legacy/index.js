import express from 'express';
import { sql } from './database.js';
import mustacheExpress from 'mustache-express';
const app = express();
const port = 3000;

app.use(express.static('public'))
	.set('view engine', 'mustache')
	.engine('mustache', mustacheExpress())
	.get('/', async (req, res) => {
		try {
			const posts = (await sql`SELECT * FROM posts ORDER BY id DESC`)[0];
			res.render('index', { posts });
		} catch {
			res.sendStatus(500);
		}
	})
	.get('/post/:id', async (req, res) => {
		try {
			const posts = (await sql`SELECT * FROM posts WHERE id=${req.params.id}`)[0];
			if (posts.length !== 1) {
				res.sendStatus(404);
				return;
			}
			res.render('post', { ...posts[0] });
		} catch {
			res.sendStatus(500);
		}
	})
	.get('/about', (req, res) => {
		res.render('about');
	})
	.listen(port, () => {
		console.log(`App listening on port ${port}`);
	});

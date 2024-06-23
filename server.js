const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql2');
const { OpaClient } = require('opa');

const app = express();
app.use(bodyParser.json());

const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'password',
    database: 'auth_demo'
});

db.connect(err => {
    if (err) {
        console.error('Error connecting to MySQL:', err);
        return;
    }
    console.log('Connected to MySQL');
});

const opa = new OpaClient({ url: 'http://localhost:8181' });

app.get('/todos', async (req, res) => {
    const { username } = req.query;

    db.query('SELECT karma, location FROM users WHERE username = ?', [username], async (err, results) => {
        if (err) {
            return res.status(500).send(err);
        }
        const user = results[0];
        const input = {
            input: {
                karma: user.karma,
                location: user.location
            }
        };
        const result = await opa.evaluatePolicy('todo_policy', input);
        if (result.result.allow) {
            db.query('SELECT * FROM todos WHERE user_id = ?', [user.id], (err, results) => {
                if (err) {
                    return res.status(500).send(err);
                }
                res.json(results);
            });
        } else {
            res.status(403).send('Forbidden');
        }
    });
});

app.post('/todos', (req, res) => {
    const { username, task } = req.body;

    db.query('SELECT id FROM users WHERE username = ?', [username], (err, results) => {
        if (err) {
            return res.status(500).send(err);
        }
        const userId = results[0].id;
        db.query('INSERT INTO todos (user_id, task, completed) VALUES (?, ?, false)', [userId, task], (err, results) => {
            if (err) {
                return res.status(500).send(err);
            }
            res.status(201).send('Todo created');
        });
    });
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});

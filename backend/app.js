// app.js

const express = require('express');
const cors = require('cors');

const app = express();
const port = 3000; 
app.use(cors());

// Middleware to parse JSON bodies
app.use(express.json());

const pool = require('./database/pool'); // Importing the PostgreSQL connection pool

app.get('/news', async (req, res) => {
  try {
    const client = await pool.connect(); // Get a client from the pool
    const result = await client.query('SELECT * FROM googlenews'); // Example query
    const articles = result.rows; // Extract rows from query result
    client.release(); // Release the client back to the pool
    res.json(articles); // Send JSON response with fetched data
  } catch (err) {
    console.error('Error fetching data', err);
    res.status(500).json({ error: 'Error fetching data' });
  }
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});

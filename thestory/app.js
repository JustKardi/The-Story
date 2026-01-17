const express = require('express');
const app = express();
const path = require('path');
const { spawn } = require('child_process');

const port = process.env.PORT || 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname, 'client')));

app.post('/api/generate', (req, res) => {
  const prompt = req.body.prompt;

  if (!prompt || !prompt.trim()) {
    return res.status(400).json({ error: 'Empty prompt' });
  }

  const python = spawn(
    'ai/venv_directml/Scripts/python.exe',
    ['ai/infer.py', prompt]
  );

  let output = '';
  let error = '';

  python.stdout.on('data', (data) => {
    output += data.toString();
  });

  python.stderr.on('data', (data) => {
    error += data.toString();
    console.error('PYTHON STDERR:', data.toString());
  });

  python.on('close', (code) => {
    console.log('Python exit code:', code);

    if (code !== 0) {
      return res.status(500).json({
        error: 'Python crashed',
        details: error
      });
    }

    res.json({ response: output.trim() });
  });
});



app.post('/api/predict', (req, res) => {
  const prompt = req.body.prompt;

  if (!prompt || !prompt.trim()) {
    return res.status(400).json({ error: 'Empty prompt' });
  }

  const python = spawn(
    'ai/venv_directml/Scripts/python.exe',
    ['ai/predictor_inference.py', prompt]
  );

  let output = '';
  let error = '';

  python.stdout.on('data', (data) => {
    output += data.toString();
  });

  python.stderr.on('data', (data) => {
    error += data.toString();
    console.error('PYTHON STDERR:', data.toString());
  });

  python.on('close', (code) => {
    console.log('Python exit code:', code);

    if (code !== 0) {
      return res.status(500).json({
        error: 'Python crashed',
        details: error
      });
    }

    res.json({ response: output.trim() });
  });
});



app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

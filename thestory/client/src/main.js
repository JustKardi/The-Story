const textInput = document.getElementById('textInput');
const submitButton = document.getElementById('submitButton');
const outputText = document.getElementById('outputText');

submitButton.addEventListener('click', async () => {
  const userInput = textInput.value;

  const prompts = userInput
    .split(';')
    .map(p => p.trim())
    .filter(p => p.length > 0);

  const result = await sendPrompt(prompts);
  outputText.textContent = result;
});

async function sendPrompt(prompts) {
  let output = '';

  for (let i = 0; i < prompts.length; i++) {
    const res = await fetch('/api/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ prompt: prompts[i] })
    });

    if (!res.ok) {
      throw new Error('Server error');
    }

    const data = await res.json();
    output += data.response + ' ';
  }

  return output.trim();
}

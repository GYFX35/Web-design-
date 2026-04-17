document.getElementById('ask').addEventListener('click', async () => {
  const prompt = document.getElementById('prompt').value;
  const provider = document.getElementById('provider').value;
  const responseDiv = document.getElementById('response');

  responseDiv.innerText = "Thinking...";

  try {
    const response = await fetch('http://localhost:8000/ask', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ prompt, provider })
    });

    const data = await response.json();
    if (data.response) {
      responseDiv.innerText = data.response;
    } else {
      responseDiv.innerText = "Error: " + (data.detail || "Unknown error");
    }
  } catch (error) {
    responseDiv.innerText = "Error connecting to AI service. Make sure it is running at http://localhost:8000";
  }
});

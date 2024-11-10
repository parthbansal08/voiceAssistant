fetch('http://127.0.0.1:5000/api/some-endpoint', { /* options */ })

document.getElementById('recordButton').onclick = async () => {
    // Code to record audio, send it to the backend API, and handle the response
    // Sample function: startRecording() will handle audio recording
};

document.getElementById('taskButton').onclick = async () => {
    const task = document.getElementById('taskInput').value;
    if (task) {
        const response = await fetch('/tasks', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ task })
        });
        const data = await response.json();
        // Update the tasks display with the new task
    }
};

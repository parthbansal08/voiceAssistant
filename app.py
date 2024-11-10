from flask import Flask, request, jsonify
from nanoassistant import VoiceAssistant  # Enhanced with Whisper TTS and task handling
import os


app = Flask(__name__)
from flask_cors import CORS
CORS(app)
assistant = VoiceAssistant()

@app.route('/listen', methods=['POST'])
def listen():
    # Receive an audio file, process it, and return a response
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400
    
    audio_file = request.files['audio']
    text_input = assistant.listen(audio_file)
    response_text = assistant.think(text_input)
    audio_response_path = assistant.speak(response_text)  # Assuming speak returns a file path
    
    return jsonify({'response_text': response_text, 'audio_url': audio_response_path})

@app.route('/command', methods=['POST'])
def command():
    # Handle text commands
    data = request.json
    text_input = data.get('text', '')
    response_text = assistant.think(text_input)
    audio_response_path = assistant.speak(response_text)
    
    return jsonify({'response_text': response_text, 'audio_url': audio_response_path})

@app.route('/tasks', methods=['POST', 'GET'])
def tasks():
    # Add task handling and retrieval logic here
    if request.method == 'POST':
        task = request.json.get('task')
        # Code to add task
        response = assistant.add_task(task)
        return jsonify({'message': 'Task added', 'task': response}), 201
    
    # For GET requests, return the list of tasks
    tasks = assistant.get_tasks()
    return jsonify({'tasks': tasks}), 200


if __name__ == '__main__':
    app.run(debug=True)

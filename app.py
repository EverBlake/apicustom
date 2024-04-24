# app.py
import subprocess
import uuid
from flask import Flask, request, jsonify, send_file
import requests
from werkzeug.utils import secure_filename
import os
import ffmpeg
import openai 

def create_app():
    app = Flask(__name__, static_folder='uploads', static_url_path='/uploads')
    app.config['UPLOAD_FOLDER'] = '/app/uploads/'
    upload_folder = app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    # Other setup code...
    return app


app = create_app()


@app.route('/', methods=['GET'])
def homepage():
    return "Homepage"


@app.route('/hello', methods=['GET'])
def hello():
    return "Hello"

# Set up your OpenAI API credentials
app.config['openai.api_key'] = os.getenv('OPENAI_API_KEY')
endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"

# API endpoint for generating a marketing report
@app.route('/generate-marketing-report', methods=['POST'])
def generate_marketing_report():
    # Get the URL from the request body
    url = request.json['url']

    # Define the prompt for the marketing report
    prompt = "Detailed Marketing Report for {url}:\n"

    # Generate the report using the OpenAI API
    response = openai.Completion.create(
        engine='gpt-3.5-turbo-16k',  # Use the new 16k token model
        prompt=prompt,
        max_tokens=15999,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Get the generated report text from the API response
    report = response.choices[0].text.strip()

    # Return the report as a JSON response
    return jsonify({'marketing_report': report})

# API endpoint for generating a SEO report
@app.route('/generate-seo-report', methods=['POST'])
def generate_seo_report():
    # Get the URL from the request body
    url = request.json['url']

    # Define the prompt for the marketing report
    prompt = "Detailed SEO Report for {url}:\n"

    # Generate the report using the OpenAI API
    response = openai.Completion.create(
        engine='gpt-3.5-turbo-16k',  # Use the new 16k token model
        prompt=prompt,
        max_tokens=15999,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Get the generated report text from the API response
    report = response.choices[0].text.strip()

    from moviepy.editor import VideoFileClip

fapp.route('/video_length', methods=[ 'POST'])
def video_length():
    video_url = request .get_json()['ur1']
    response = requests.get(video_url, stream=True)

    if response.status_code != 200:
    return jsonify({'error': 'Failed to download file'}), 400

    filename = secure_filename(video_url.split('/')[-1])
    file path = os.path.join(app.configl ['UPLOAD_FOLDER'], filename)

    with open(file_path, 'wb') as f:
        f..write(response.content)

    video = VideoFileClip(file_path)
    
    duration = video.duration

return jsonify({'video.length': duration})


    # Return the report as a JSON response
    return jsonify({'seo_report': report})

if __name__ == '__main__':
    app.run()

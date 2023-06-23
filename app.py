# app.py
import subprocess
import uuid
from flask import Flask, request, jsonify, send_file
import requests
from werkzeug.utils import secure_filename
import os
import ffmpeg


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
openai.api_key = process.env.OPENAI_API_KEY

# API endpoint for generating a marketing report
@app.route('/generate-marketing-report', methods=['POST'])
def generate_marketing_report():
    # Get the URL from the request body
    url = request.json['url']

    # Define the prompt for the marketing report
    prompt = f"Marketing Report for {url}:\n"

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
    return jsonify({'report': report})

if __name__ == '__main__':
    app.run()

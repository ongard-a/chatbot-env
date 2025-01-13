from flask import Flask, render_template, request, jsonify
from openai import AzureOpenAI
import os

app = Flask(__name__, template_folder='templates')

# Replace with your actual Azure OpenAI endpoint and API key
azure_endpoint = os.environ.get("azure_endpoint")
azure_api_key = os.environ.get("azure_api_key")

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=azure_endpoint,
    api_key=azure_api_key,
    api_version="2024-05-01-preview"  # Use the latest stable API version
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_text():
    try:
        prompt = request.form['prompt']

        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400

        response = client.chat.completions.create(
            model=os.environ.get("model"),  # Replace with your deployment name
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
            stream=False  
        )

        return jsonify({'response': response.choices[0].message.content})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=443, debug=True) 

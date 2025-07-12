from flask import Flask, render_template, request, jsonify
import os
import openai
import base64

app = Flask(__name__)

# Configurations
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16 MB

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    if 'imagen' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['imagen']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        imagen_bytes = file.read()
        imagen_b64 = base64.b64encode(imagen_bytes).decode("utf-8")

        prompt = """
Eres un experto en pruebas de admisión de la UTC, enfocado en razonamiento numérico y verbal. 
Observa la imagen, extrae el texto del ejercicio y responde únicamente con la opción correcta o la respuesta final, sin mostrar el procedimiento ni explicaciones.
        """

        ia_response = openai.OpenAI(api_key=OPENAI_API_KEY).chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{imagen_b64}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=1024
        )
        resultado = ia_response.choices[0].message.content.strip()

        return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
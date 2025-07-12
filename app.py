from flask import Flask, request, jsonify, render_template
import openai
from flask_cors import CORS
import base64
import os

app = Flask(__name__)
CORS(app)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/procesar", methods=["POST"])
def procesar():
    try:
        if 'imagen' not in request.files:
            return jsonify({"error": "No se recibió ninguna imagen."}), 400

        imagen = request.files['imagen']
        imagen_bytes = imagen.read()
        imagen_b64 = base64.b64encode(imagen_bytes).decode("utf-8")

        prompt = """
Eres un experto en pruebas de admisión de la UTC, enfocado en razonamiento numérico y verbal. 
Observa la imagen, extrae el texto del ejercicio y responde únicamente con la opción correcta o la respuesta final, sin mostrar el procedimiento ni explicaciones.
        """

        # Usa el modelo actualizado gpt-4o
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
        respuesta_ia = ia_response.choices[0].message.content

        return jsonify({"resultado": respuesta_ia})
    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500

if __name__ == "__main__":
    app.run(debug=True)
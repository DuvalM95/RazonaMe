from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Configurations
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16 MB

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

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
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Here you would add your image processing logic
        # For now, we will just return a mock response
        resultado = "Respuesta procesada para la imagen: " + file.filename

        return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
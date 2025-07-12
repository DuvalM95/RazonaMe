# RazonaMe

## Description
RazonaMe is a web application built with Flask that allows users to upload images of English exercises and receive translated and resolved answers instantly. The application provides a user-friendly interface for image uploads and displays the results in a clear format.

## Project Structure
```
RazonaMe
├── app.py
├── requirements.txt
├── templates
│   └── index.html
├── static
│   └── (your static files here)
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/DuvalM95/RazonaMe.git
   ```

2. Navigate to the project directory:
   ```
   cd RazonaMe
   ```

3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

3. Use the interface to upload an image of an English exercise or take a photo using your device's camera.

4. Click on "Generar Respuesta" to process the image and receive the translated answer.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
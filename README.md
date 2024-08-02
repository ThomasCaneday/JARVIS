# JARVIS: Python Virtual Assistant

JARVIS is a Python virtual assistant program based on the JARVIS system from Iron Man. It is designed to convert speech to text and text to speech using the ChatGPT model from OpenAI.

## Features

- Converts speech to text using the `speech_recognition` library.
- Generates responses using OpenAI's ChatGPT.
- Converts the generated text to speech using the `pyttsx3` library.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have Python 3 installed on your machine.
- You have an OpenAI API key. You can obtain it from [OpenAI](https://openai.com/api/).

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/thomascaneday/JARVIS.git
   ```

2. Navigate to the project directory:
   ```sh
   cd jarvis
   ```

3. Install the required Python packages:
   ```sh
   pip install speechrecognition pyttsx3 openai
   ```

## Usage

1. Set your OpenAI API key in the `OPENAI_KEY` variable in the script:
   ```python
   OPENAI_KEY = "YOUR_OPEN_AI_KEY"
   ```

2. Run the program:
   ```sh
   python JARVIS.py
   ```

3. Speak into your microphone when prompted. JARVIS will recognize your speech, send it to ChatGPT, and read out the response.

## Code Overview

- `SpeakText(command)`: Converts text to speech using the `pyttsx3` library.
- `record_text()`: Records audio from the microphone, converts it to text using Google’s speech recognition.
- `send_to_chatGPT(messages, model="gpt-3.5-turbo")`: Sends the recorded text to ChatGPT and receives a response.
- The main loop records the user's speech, sends it to ChatGPT, and speaks out the response.

## Troubleshooting

- If the program is not connecting to OpenAI, ensure you are logged in and the API key is correct.
- For issues with the microphone, check your audio settings and ensure the microphone is properly connected.

## Contributing

1. Fork the project.
2. Create your feature branch:
   ```sh
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:
   ```sh
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```sh
   git push origin feature/YourFeature
   ```
5. Open a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements

- [OpenAI](https://openai.com/) for providing the ChatGPT API.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) for speech recognition.
- [pyttsx3](https://pypi.org/project/pyttsx3/) for text-to-speech conversion.

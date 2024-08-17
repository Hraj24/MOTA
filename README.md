
# Multi-Tasking Objective Text Analyzer (MOTA)

## Overview

MOTA (Multi-Tasking Objective Text Analyzer) is a personal assistant tool designed to perform various tasks through voice commands. It can interact with users, provide information, and automate tasks on a computer using natural language processing and text-to-speech technologies.

## Features

- **Voice Interaction**: Responds to voice commands and provides feedback using text-to-speech.
- **Time and Date Announcement**: Announces the current time and date.
- **Greeting/Wishing**: Greets the user based on the time of day.
- **Wikipedia Search**: Retrieves and reads out summaries from Wikipedia.
- **Joke Telling**: Tells random jokes.
- **System Monitoring**: Monitors and reports system resource usage like CPU and memory.

## Installation

### Prerequisites

Ensure you have Python 3.x installed on your system. Additionally, you'll need to install the following libraries:

- `pyttsx3`: Text-to-speech conversion.
- `SpeechRecognition`: For recognizing voice commands.
- `wikipedia`: For fetching Wikipedia summaries.
- `pyautogui`: For automating mouse and keyboard actions.
- `pyjokes`: For telling jokes.
- `psutil`: For monitoring system resources.

You can install these dependencies using pip:

```bash
pip install pyttsx3 SpeechRecognition wikipedia pyautogui pyjokes psutil
```

## Usage

1. **Run the Script**: Start the MOTA script using Python.

```bash
python MOTA.py
```

2. **Voice Commands**: MOTA will greet you and wait for your commands. You can ask for the current time, date, a joke, or search for information on Wikipedia.

3. **Example Commands**:

   - "What's the time?"
   - "Tell me a joke."
   - "Search for Python programming on Wikipedia."

## Customization

You can customize the voice settings (rate, volume, voice type) within the `speak` function by adjusting the properties of the `pyttsx3` engine.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing

Contributions are welcome! If you want to contribute to MOTA, please fork the repository, make your changes, and create a pull request.

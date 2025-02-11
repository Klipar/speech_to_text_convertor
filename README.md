
# Speech to Text Converter

This project allows you to convert audio files to text using the `speech_recognition` library and the Google Web Speech API. There is also an option to format the text to improve readability.

## Demo

![Demo of Easy library](media/demo.gif)
## Functionality

- Supports multiple recognition languages (English, Ukrainian, Slovak, etc.)
- Convert audio files to text
- Improved formatting of recognized text

## Installation

1. Make sure you have installed python > 3.11
2. Clone this repository:
``` Bash
git clone https://github.com/Klipar/speech_to_text_convertor.git
cd speech_to_text_convertor
```
3. **Optional** create and log in to the virtual environment:
If you use `Bash`
``` Bash
python -m venv .venv && source .venv/bin/activate
```
If you use `Fish`
``` Bash
python -m venv .venv && source .venv/bin/activate.fish
```

4. Install the dependencies:
``` Bash
pip install -r dependencies.txt
```

## Usage/Examples
1. To use, simply enter the following command to start the script execution:
``` Bash
python main.py
```
You can also specify the name of the file to be transcribed right at startup as follows:
``` Bash
python main.py Path/to/your/audio.file
```
2. Select the recognition language.
3. Specify the path to the audio file (if you haven't already done so when you start the program).
4. You can format it for easier viewing or skip this step.
5. Get the text as a `.txt` file.
## Supported formats
- `.mp3`
- `.wav`
- `.flac`
- `.ogg`
## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.
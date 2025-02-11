# Speech to Text Converter

This project allows you to convert audio files to text using the `speech_recognition` library and the Google Web Speech API. There is also an option to format the text to improve readability. Works on Docker.


## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![Python 3.6](https://img.shields.io/badge/Python-3.6-blue?logo=python)

## Demo

![Demo of project](media/demo1.GIF)
![Demo of project](media/demo2.GIF)
## Functionality

- Supports multiple recognition languages (English, Ukrainian, Slovak, etc.)
- Convert audio files to text
- Improved formatting of recognized text

## Installation

1. Reset Docker and Docker Compose.

Before using, make sure that Docker and Docker Compose are installed:

🔹 On Linux (Arch, Ubuntu, Debian):
``` Bash
sudo pacman -S docker docker-compose  # For Arch
sudo apt install docker docker-compose -y  # For Ubuntu/Debian
```

🔹 On macOS and Windows — install using the official Docker website.

Make sure Docker is working:
``` Bash
docker --version
docker-compose --version
```
2. Clone this repository (make sure that you have installed the git):
``` Bash
git clone https://github.com/Klipar/speech_to_text_convertor.git
cd speech_to_text_convertor
```
3. Build a Docker image
This command builds the container with the project (using a `Dockerfile`).
``` Bash
docker-compose build
```
4. If the installation went smoothly, then congratulations, now you can start using it!


## Usage/Examples

1. Launch the container and immediately enter the terminal to work with the program:
``` Bash
docker-compose run --rm speech-to-text bash
```
2. To use, simply enter the following command to start the script execution:
``` Bash
python main.py
```
You can also specify the name of the file to be transcribed right at startup as follows:
``` Bash
python main.py Path/to/your/audio.file
```
3. Select the recognition language.
4. Specify the path to the audio file (if you haven't already done so when you start the program).
5. You can format it for easier viewing or skip this step.
6. Get the text as a `.txt` file.

## Supported formats
- `.mp3`
- `.wav`
- `.flac`
- `.ogg`
## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.
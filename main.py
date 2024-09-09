from pydub import AudioSegment
import speech_recognition as sr
import sys
import os
import textwrap
from Easy.massage import *





def SetLanguage ():

    print (colors.VIOLET + """
.▄▄ ·       ▄• ▄▌ ▐ ▄ ·▄▄▄▄      ▄▄▄▄▄          ▄▄▄▄▄▄▄▄ .▐▄• ▄ ▄▄▄▄▄
▐█ ▀. ▪     █▪██▌•█▌▐███▪ ██     •██  ▪         •██  ▀▄.▀· █▌█▌▪•██  
▄▀▀▀█▄ ▄█▀▄ █▌▐█▌▐█▐▐▌▐█· ▐█▌     ▐█.▪ ▄█▀▄      ▐█.▪▐▀▀▪▄ ·██·  ▐█.▪
▐█▄▪▐█▐█▌.▐▌▐█▄█▌██▐█▌██. ██      ▐█▌·▐█▌.▐▌     ▐█▌·▐█▄▄▌▪▐█·█▌ ▐█▌·
 ▀▀▀▀  ▀█▄▀▪ ▀▀▀ ▀▀ █▪▀▀▀▀▀•      ▀▀▀  ▀█▄▀▪     ▀▀▀  ▀▀▀ •▀▀ ▀▀ ▀▀▀ 
            ▄▄·        ▐ ▄  ▌ ▐·▄▄▄ .▄▄▄  ▄▄▄▄▄▄▄▄ .▄▄▄                         
            ▐█ ▌▪▪     •█▌▐█▪█·█▌▀▄.▀·▀▄ █·•██  ▀▄.▀·▀▄ █·                       
            ██ ▄▄ ▄█▀▄ ▐█▐▐▌▐█▐█•▐▀▀▪▄▐▀▀▄  ▐█.▪▐▀▀▪▄▐▀▀▄                        
            ▐███▌▐█▌.▐▌██▐█▌ ███ ▐█▄▄▌▐█•█▌ ▐█▌·▐█▄▄▌▐█•█▌                       
            ·▀▀▀  ▀█▄▀▪▀▀ █▪. ▀   ▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀ .▀  ▀      

"""+ colors.END)



    print(colors.GREEN + """
                    Availble Languages

                [1] English         [2] Ukrainian
                [3] Slovak          [4] Other
        """ + colors.END)
    templates = {
    '1': 'en-US',
    '2': 'uk-UA',
    '3': 'sk-SK',
    '4': 'Other',
    }

    number = input(colors.YELLOW + "[" + colors.END + "?" + colors.YELLOW + "]" + colors.END + "> ")
    if number == "4":
        choice = input("Write the name of your language model, like (en-US or uk-UA): ")
    elif (int(number) > 0 and int(number) < 5):
        choice = templates[number]
    else:
        failed ("Choise if out of range  :(")
        sys.exit
    print("Loading %s...." % (choice))
    return choice

def replace_nth_space_with_newline(text, n=10):
    space_count = 0
    result = []

    for char in text:
        if char == ' ':
            space_count += 1
            if space_count % n == 0:
                result.append('\n')  # Заміна кожного n-го пробілу на переніс рядка
                continue
        result.append(char)

    return ''.join(result)

def format_text_without_punctuation(text, line_width=80, words_per_sentence=15):
    # Розбиваємо текст на слова
    words = text.split()
    formatted_text = ""
    current_sentence = []

    for i, word in enumerate(words):
        current_sentence.append(word)
        
        # Додаємо крапку в кінці кожної групи з words_per_sentence слів
        if (i + 1) % words_per_sentence == 0:
            sentence = ' '.join(current_sentence) + '.'
            wrapped_sentence = textwrap.fill(sentence, width=line_width)
            formatted_text += wrapped_sentence + "\n\n"
            current_sentence = []
    
    # Додаємо залишок слів як останнє речення
    if current_sentence:
        sentence = ' '.join(current_sentence) + '.'
        wrapped_sentence = textwrap.fill(sentence, width=line_width)
        formatted_text += wrapped_sentence + "\n\n"

    return formatted_text



def main(language_model):
    file_path = ''
    if len(sys.argv) < 2:
        file_path = input("Enter the input file: ") 
    else:
        file_path = sys.argv[1]
    try:
        file_name, file_extension = os.path.splitext(file_path)
        file_extension = file_extension.lstrip('.')
    
        inform (f"Working on file: {file_path}")
        audio = AudioSegment.from_file(file_path, format=file_extension)
        audio.export((file_name+".wav"), format="wav")
    except Exception as e:
        failed (f"File Error   :(\n {e}")
        sys.exit
    try:    
    # Ініціалізація розпізнавача
        recognizer = sr.Recognizer()
    except Exception as e:
        failed (f"Recognition error   :(\n {e}")
        sys.exit
    try:        
        output_file_path = (file_name+'.txt')
        # Завантаження аудіофайлу
        with sr.AudioFile((file_name+".wav")) as source:
            audio = recognizer.record(source)  # Читання всього аудіофайлу
        os.remove((file_name+".wav"))
    except Exception as e:
        failed (f"File Error   :(\n {e}")
        sys.exit

    # Розпізнавання мови за допомогою Google Web Speech API
    try:
        text = str(recognizer.recognize_google(audio, language=language_model))  # Можна змінити мову розпізнавання
        success ("The text is recognized, do you want to improve its readability? (Yes/No): ", en = "")
        t = input().lower()
        if (t == "yes" or t == "y"):
            # text = format_text_without_punctuation(text)
            text = replace_nth_space_with_newline (text)
            # print (text)
            success ("The readability of the text is improved!")
        else:
            inform("Text improvement omitted.")
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        # with open(output_file_path, 'a') as file:
        #     file.write(text + '\n')
        # print("Розпізнаний текст: " + text)
    except sr.UnknownValueError:
        failed("Google Web Speech API can't recognised your file     :(")
    except sr.RequestError as e:
        failed(f"Failed to get results from their api                :({e}")

    success (f"Your content saved in file: {file_name}.txt")
if __name__ == "__main__":
    language_model = SetLanguage()
    main(language_model)
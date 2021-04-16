import requests
import parser


URL = r"https://translate.google.com/_/TranslateWebserverUi/data/batchexecute?"
FILENAME = "results.txt"


def get_translate_from_google(to_translate: str, output_lang: str='en', input_lang: str='auto', file_path: str=FILENAME) -> None:
    """ Получает данные с гугла по переводу строки to_translate языка input_lang на язык output_lang
    и сохраняет данные в файл по пути file_path
    """
    data = {
        "f.req": f'[[["MkEWBc","[[\\"{to_translate}\\",\\"{input_lang}\\",\\"{output_lang}\\",true],[null]]",null,"generic"]]]',
    }
    r = requests.post(URL, data=data)
    if r.status_code != 200:
        print(f"Error {r.status_code}, message {r.text}")
        return False
    
    with open(file_path, 'w') as w:
        w.write(r.text)
    return True

def get_languages() -> (str, str):
    """ Возвращает языки ввода и вывода
    """
    input_lang = input("Input language (press Enter for auto): ")
    output_lang = input("Output language: ")
    if input_lang == '':
        input_lang = 'auto'
    if output_lang == '':
        output_lang = 'en'
    return input_lang, output_lang

def main():
    """ Главная функция приложения """
    is_stopped = False
    while not is_stopped:
        input_lang, output_lang = get_languages()
        while True:
            to_translate = input("To translate: ")

            if not to_translate or to_translate == '/q':
                is_stopped = True
                break

            if to_translate == '/l':
                break

            if get_translate_from_google(to_translate, file_path=FILENAME, input_lang=input_lang.lower(), output_lang=output_lang.lower()):
                parser.translate(FILENAME)


if __name__ == "__main__":
    main()    
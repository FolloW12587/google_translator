import json
import re


FILENAME = "results.txt"


def get_file_data(filename: str, line_from: int=None, line_to: int=None) -> list:
    """ Возвращает содержимое файла filename в виде масива строк 
    начиная со строки line_from по строку line_to
    """
    with open(filename, 'r') as r:
        if line_from:
            data = r.readlines()
            if line_to:
                return data[line_from:line_to]
            else:
                return data[line_from:]
        else:
            return r.readlines()

def get_translation_from_file_data(file_data: list) -> str:
    """ Возвращает переведенный ответ основываясь на данных file_data - ответа с сервера гугл
    """
    data = list(map(lambda x: re.sub(r"\n$", "", x) ,file_data)) # returns same data without \n at the end of the line
    json_data = json.loads("".join(data))
    jd = json.loads(json_data[0][2])
    answers_list = jd[1][0][0][5]   # [0][0]
    if len(answers_list) > 1:
        answer = " ".join([x[0] for x in answers_list])
    else:
        answers_list = answers_list[0]
        answer = answers_list[0]
        if len(answers_list) > 1:
            answer += "\n" + ", ".join(answers_list[1])
    return answer

def translate(filename: str=None):
    """ Выводит перевод основываясь на данных с сервера гугл, сохраненных в файл filename
    """
    file_name = filename if filename else FILENAME 
    data = get_file_data(file_name, 2, 6)
    translation_data = get_translation_from_file_data(data)
    print(translation_data)


if __name__ == "__main__":
    translate()
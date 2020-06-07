# Цель: перевести программу на национальном языке в компилируемый вид для pascal
# и отправить ее на исполнение компилятору pascal

import os

# Это словарь где ключи - слова на нац языках, а значения - команды паскаль
# Также в ходе работы программы туда будут добавляться пары где ключ - название переменной на нац языке,
# значение - то под каким названием переменная будет использоваться в программе pascal
translator = {
    "от": "of",
    "до": "to",
    "делать": "do",
    "массив": "array",
    "вещественные": "real",
    "начало": "begin",
    "вставить": "insert",
    "вывести": "writeln",
    "длина": "length",
    "для": "for",
    "если": "if",
    "закрыть": "close",
    "иначе": "else",
    "квадрат": "sqr",
    "квадратныйкорень": "sqrt",
    "конец": "end",
    "округлить": "round",
    "остатокотделения": "mod",
    "переписать": "rewrite",
    "повторять": "repeat",
    "позиция": "pos",
    "пока": "while",
    "покане": "until",
    "символ": "char",
    "скопировать": "copy",
    "строка": "string",
    "считать": "read",
    "тогда": "then",
    "удалить": "delete",
    "целочисленноеделение": "div",
    "целыйтип": "integer",
    "сброс": "reset",
    "переменные": "var",
    "написать": "writeln",
    "модуль": "abs",
    "ввести": "readln",
    "функция": "function",
    "вернуть": "return",
    "de": "of",
    "hasta": "to",
    "hacer": "do",
    "macizo": "array",
    "reales": "real",
    "comienzo": "begin",
    "insertar": "insert",
    "inferir": "writeln",
    "longitud": "length",
    "para": "for",
    "si": "if",
    "cerrar": "close",
    "sino": "else",
    "cuadrado": "sqr",
    "raizcuadrada": "sqrt",
    "final": "end",
    "redondear": "round",
    "saldoafision": "mod",
    "hacerlalista": "rewrite",
    "repetir": "repeat",
    "posicion": "pos",
    "todavia": "while",
    "todaviano": "until",
    "simbolo": "char",
    "copiar": "copy",
    "fila": "string",
    "considerar": "read",
    "entonces": "then",
    "eliminar": "delete",
    "divisionentera": "div",
    "entero": "integer",
    "borrar": "reset",
    "variables": "var",
    "escribir": "writeln",
    "valorabsoluto": "abs",
    "introducir": "readln",
    "funcion": "function",
    "devolver": "return",
    "von": "of",
    "biszu": "to",
    "machen": "do",
    "array": "array",
    "reell": "real",
    "beginn": "begin",
    "einsetzen": "insert",
    "ableiten": "writeln",
    "abstand": "length",
    "fur": "for",
    "wenn": "if",
    "verdecken": "close",
    "ansonst": "else",
    "quadrat": "sqr",
    "quadratwurzel": "sqrt",
    "ende": "end",
    "aufrunden": "round",
    "restderdivision": "mod",
    "umschreiben": "rewrite",
    "wiederholen": "repeat",
    "bis": "while",
    "nochnicht": "until",
    "symbol": "char",
    "kopieren": "copy",
    "zeile": "string",
    "ablesen": "readln",
    "dann": "then",
    "entfernen": "delete",
    "ganzzahligedivision": "div",
    "ganzeart": "integer",
    "variable": "var",
    "schreiben": "writeln",
    "modul": "abs",
    "eingeben": "read",
    "funktion": "function",
    "abgeben": "return",
    "avant": "to",
    "faire": "do",
    "massif": "array",
    "reels": "real",
    "debut": "begin",
    "inserer": "insert",
    "fairesortir": "writeln",
    "longueur": "length",
    "pour": "for",
    "fermer": "close",
    "sinon": "else",
    "carree": "sqr",
    "racinecarree": "sqrt",
    "fin": "end",
    "arrondir": "round",
    "restedeladivision": "mod",
    "reecrire": "rewrite",
    "repeter": "repeat",
    "position": "pos",
    "encore": "while",
    "pasencore": "until",
    "symbole": "char",
    "copier": "copy",
    "ligne": "string",
    "introduire": "read",
    "alors": "then",
    "supprimer": "delete",
    "divisionentiere": "div",
    "entier": "integer",
    "reset": "reset",
    "ecrire": "writeln",
    "module": "abs",
    "saisir": "readln",
    "fonction": "function",
    "retourner": "return"
}

char_list_ = [':', ',', '=', ';', '+', '-', '/', '*', '%', '(', ')', '.', '<', '>', '[', ']']

current_var = 0


# функция перевода слова или переменной на язык pascal
def translate(word):
    if word in translator.keys():
        word = translator[word]
    return word


# функция перевода строки в компилируемый для pascal вид
def translate_pieces(word_list, flag_var, flag_type, flag_com, flag_str, current_var_):
    i = 0
    while i < len(word_list):
        if flag_str or flag_com:
            if word_list[i][-1] == '\'':
                flag_str = not flag_str
            elif word_list[i][0] == '{':
                flag_com = True
            elif word_list[i][-1] == '}':
                flag_com = False
        elif flag_var:
            if flag_type:
                if word_list[i] == ';':
                    flag_type = False
                else:
                    word_list[i] = translate(word_list[i])
            else:
                if word_list[i] == ':':
                    flag_type = True
                elif word_list[i] in translator.keys() or word_list[i] in translator.values():
                    flag_var = False
                    word_list[i] = translate(word_list[i])
                elif word_list[i] != ',':
                    translator[word_list[i]] = 'var' + str(current_var_)
                    word_list[i] = 'var' + str(current_var_)
                    current_var_ += 1
        else:
            if word_list[i][0] == '\'':
                flag_str = not flag_str
            elif word_list[i][0] == '{':
                flag_com = True
            elif word_list[i][-1] == '}':
                flag_com = False
            word_list[i] = translate(word_list[i])
            if word_list[i] == 'var':
                flag_var = True
        i += 1
    return word_list, flag_var, flag_type, flag_com, flag_str, current_var_


# функция которая преобразует строку в приемлемый вид для передачи в функцию translate_pieces()
def parse_line(s, char_list, flag_com, flag_str):
    if s == "":
        return s, flag_com, flag_str
    last_index = len(s) - 1
    i = 0
    new_s = ""
    while i <= last_index:
        if s[i] not in ['\'', '{', '}']:
            if flag_com or flag_str:
                new_s += s[i]
            else:
                if s[i] in char_list:
                    if i == last_index:
                        if last_index == 0:
                            new_s += s[i]
                        else:
                            if s[i - 1] not in ([' '] + char_list):
                                new_s += ' ' + s[i]
                            else:
                                new_s += s[i]
                    elif i == 0:
                        if last_index == 0:
                            new_s += s[i]
                        else:
                            if s[i + 1] not in ([' '] + char_list):
                                new_s += s[i] + ' '
                            else:
                                new_s += s[i]
                    else:
                        left_condition = s[i - 1] not in ([' '] + char_list)
                        right_condition = s[i + 1] not in ([' '] + char_list)
                        if left_condition and right_condition:
                            new_s += ' ' + s[i] + ' '
                        elif left_condition:
                            new_s += ' ' + s[i]
                        elif right_condition:
                            new_s += s[i] + ' '
                        else:
                            new_s += s[i]
                else:
                    new_s += s[i]
        else:
            if s[i] == '\'':
                flag_str = not flag_str
            elif s[i] == '{':
                flag_com = True
            else:
                flag_com = False
            new_s += s[i]
        i += 1
    return new_s, flag_com, flag_str


# output_file - исполняемый pas файл, изначально пустой
output_file = "pascal.pas"
ofhandle = open(output_file, 'w', encoding='utf-8')
file_path = input("Введите путь к текстовому файлу программы: ")
# program.txt - файд с исходной программой на национальных языках
if len(file_path) < 1:
    file_path = "program.txt"
try:
    ifhandle = open(file_path, encoding='utf-8')
except:
    print("Ошибка открытия файла!")
    ifhandle = open("program.txt", encoding='utf-8')

flag_com_ = False
flag_str_ = False
flag_com_1 = False
flag_str_1 = False
flag_var_ = False
flag_type_ = False

# Проход каждой строки исходного текста и запись ее в корректном виде в итоговый .pas файл
for line_ in ifhandle:
    line = line_.rstrip()
    parsed_line, flag_com_, flag_str_ = parse_line(line, char_list_, flag_com_, flag_str_)
    pieces = parsed_line.split()
    pieces[:], flag_var_, flag_type_, flag_com_1, flag_str_1, current_var = translate_pieces(pieces, flag_var_,
                                                                                             flag_type_, flag_com_1,
                                                                                             flag_str_1, current_var)
    new_line = " ".join(pieces)
    ofhandle.write(new_line + '\n')

ofhandle.close()
ifhandle.close()

# Отдача .pas файла на исполнение системой (передача команды в командную строку windows или terminal mac os)
exe_path = os.path.abspath(output_file)
os.system(exe_path)

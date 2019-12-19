
#include <iostream>
#include <string>
#include <fstream>
#include <windows.h>
#include <map>
#include <unordered_map>

using namespace std;

unordered_map <string, string> translator = {
        {"вещественные", "real"},
        {"начало","begin"},
        {"вставить", "insert"},
        {"вывести","writeln"},
        {"длина","length"},
        {"для","for"},
        {"если","if"},
        {"закрыть","close"},
        {"иначе","else"},
        {"квадрат","sqr"},
        {"квадратныйкорень","sqrt"},
        {"конец","end"},
        {"округлить","round"},
        {"остатокотделения","mod"},
        {"переписать","rewrite"},
        {"повторять","repeat"},
        {"позиция","pos"},
        {"пока","while"},
        {"покане","until"},
        {"символ","char"},
        {"скопировать","copy"},
        {"строка","string"},
        {"считать","read"},
        {"тогда","then"},
        {"удалить","delete"},
        {"целочисленноеделение","div"},
        {"целыйтип","integer"},
        {"читать","reset"},
        {"переменные","var"},
        {"вещественные","real"},
        {"написать","writeln"},
        {"модуль","abs"},
        {"ввести","readln"},
        {"ввод","readln"},
};

void word_change(string &word) {
    if (translator.find(word) != translator.end())
        word = translator[word];
}

void line_change(string &line) {
    int n = line.size();
    line += " ";
    string result;
    string alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя";
    string c;
    bool flag = 0;
    int i = 0;
    while (i < n) {
        c = line.substr(i, 1);
        if (c == "'") {
            if (flag)
                flag = 0;
            else
                flag = 1;
        }
        if (alphabet.find(c) != -1) {
            string word;
            while (alphabet.find(c) != -1 && i < n) {
                word += c;
                i++;
                c = line.substr(i, 1);
            }
            if (flag == 0)
                word_change(word);
            result += word;
        }
        else {
            result += c;
            i++;
        }
    }
    line = result;
}

int main() {
    SetConsoleOutputCP(CP_UTF8);
    while (true) {
        string path, line, s, pas_file;
        pas_file = "C:\\Users\\danil\\Desktop\\pas_file.pas";
        char answer;
        cout << "Введите путь к текстовому файлу программы: ";
        getline(cin, path);
        cout << endl;
        ifstream fin;
        ofstream fout;
        fout.open(pas_file);
        fin.open(path);
        if (!fin.is_open()) {
            cout << "Ошибка открытия файла!" << endl;
            cout << "Хотите начать работу программы заново? Y/n" << endl;
            cin >> answer;
            if (tolower(answer) == 'y') {
                getline(cin, s);
                continue;
            }
            else {
                getline(cin, s);
                break;
            }
        }
        else {
            while (!fin.eof()) {
                getline(fin, line);
                line_change(line);
                fout << line << endl;
            }
            cout << "Хотите начать работу программы заново? Y/n" << endl;
            cin >> answer;
            if (tolower(answer) == 'y') {
                getline(cin, s);
                continue;
            }
            else {
                getline(cin, s);
                break;
            }
        }
    }
}
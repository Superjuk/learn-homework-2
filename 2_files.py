"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    referat = ""
    with open("referat.txt", "r", encoding = "utf-8") as txt:
        referat = txt.read()
    print(f"Количество символов: {len(referat)}")
    print(f"Количество слов: {len(referat.split(' '))}")
    with open("referat2.txt", "w", encoding = "utf-8") as txt:
        txt.write(referat.replace(".", "!"))

if __name__ == "__main__":
    main()

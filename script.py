from modules.json_parser import parser
from modules.excel_writer import wrtie_xls


def main():
    data = parser('путь к файлу .jsonl')
    wrtie_xls(data, 'имя файла без расширения')


if __name__ == "__main__":
    main()

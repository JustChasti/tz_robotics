from modules.decorators import file_decorator
from modules.json_parser import parser
from modules.excel_writer import wrtie_xls, generate_name

@file_decorator('file saving error')
def generate_xlsx(content, filename):
    content = content.decode("utf-8", "ignore")
    file_type = filename.split('.')[1]
    name = generate_name()
    filename = f"{name}.{file_type}"
    with open(filename, "a") as j_file:
        j_file.write(content)
    data = parser(file_path = filename)
    name = generate_name()
    result = wrtie_xls(data, name)
    return result, name

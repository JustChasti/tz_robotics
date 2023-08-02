import json
from loguru import logger
from modules.decorators import default_decorator


@default_decorator('error in parse string')
def parse_string(alley: str, json_str: dict):
    col = json_str['col']
    row = json_str['row']
    action = json_str['action']
    adress = f"{alley}-{col}-{row}"
    barcode = json_str['barcode']
    if isinstance(barcode, list):
        barcode = barcode[0]
    if len(barcode) == 20 and barcode[0] == '0' and barcode[1] == '0':
        barcode =  barcode[2:]
    return (action, adress, barcode)


def remove_rescan(write_dict: dict, rescan_dict: dict):
    for i in rescan_dict.keys():
        write_dict.pop(i)
    return write_dict


@default_decorator('error in parsing file')
def parser(file_path: str):
    with open(file_path, 'r') as json_file:
        json_list = list(json_file)

    info = json.loads(json_list[0])
    json_list = json_list[1:]
    if isinstance(info, dict):
        alley = info['current_alley']
    else:
        raise Exception('No current_alley in file')
    write_dict= {}
    rescan_dict = {}
    for i in json_list:
        try:
            if i != '\n':
                json_str = json.loads(i)
                data = parse_string(alley, json_str)
                if data[0] == 'write_barcode':
                    write_dict[data[1]] = data[2]
                elif data[0] == 'RESCAN':
                    rescan_dict[data[1]] = data[2]
                else:
                    pass
        except Exception as e:
            logger.exception(e)
    return remove_rescan(write_dict, rescan_dict)
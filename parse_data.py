import json

with open("settings/config.json") as conf:
    conf_data = json.load(conf)


def get_attr(attr):
    """Получить параметр конфигурации из json файла"""
    return conf_data[attr]


def get_task():
    """Получить данные задачи для эфира или системы"""
    pass

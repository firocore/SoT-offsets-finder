import requests
import json
import re

'''
        Улучшенный офсетный искатель от @DougTheDruid
        Оригинадный код: https://raw.githubusercontent.com/DougTheDruid/SoT-Python-Offset-Finder

        Improved offset finder by @DougTheDruid
        Original code: https://raw.githubusercontent.com/DougTheDruid/SoT-Python-Offset-Finder
'''

cfg_path = 'config.json'


class Offset_finder():
    def __init__(self) -> None:
        self.load_config()

        out_dict = {}
        for line in self.cfg['offsets']:
            print(line, self.get_offset(self.cfg['offsets'][line]))
            out_dict[line] = self.get_offset(self.cfg['offsets'][line])

        with open('offsets.json', 'w+') as out_file:
            offsets = json.loads(str(out_dict).replace("'", '"'))
            out_file.write(json.dumps(offsets, indent=4))

    def get_offset(self, form: list):
        url = 'https://raw.githubusercontent.com/DougTheDruid/SoT-Python-Offset-Finder/main/SDKs/JSON-SDK/'
        file_name = form[0]
        title = form[1]
        memory_object = form[2]

        offset = "Not Found"

        offsets = requests.get(url + file_name + '.json').json()

        if memory_object == 'ActorId':
            return 24

        if offsets:
            components = offsets.get(title, None)
            if components:
                attributes = components.get('Attributes', None)
                for attribute in attributes:
                    if attribute['Name'] == memory_object:
                        offset = int(attribute.get('Offset'), 16)

        return offset

    def load_config(self):
        with open(cfg_path) as cfg:
            self.cfg = json.load(cfg)


if __name__ == "__main__":
    Offset_finder()

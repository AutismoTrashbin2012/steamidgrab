import os
import sys
import urllib.request
import xml.etree.ElementTree as ET
def get_ids():
    tree = ET.parse("games.xml")
    root = tree.getroot()

    if root.find('error') is not None:
        print(root.find('error').text)
        sys.exit(0)

    return {game.find('appID').text for game in root.iter('game')}


def main():
    path_to_save = '.'
    with open(path_to_save + '/ids.txt', 'w', encoding='utf-8') as f:
        for id in get_ids():
            f.write("{},".format(id))


if __name__ == '__main__':
    main()

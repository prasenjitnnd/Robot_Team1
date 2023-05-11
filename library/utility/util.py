import os
from pathlib import Path

from jproperties import Properties


def getKeyValueFromPropertiesFileInResource(relativePathOfFileInResourceFolder, key):
    propFilePath = str(Path(os.path.dirname(os.path.abspath(__file__))).parent.parent)+"\\resource\\"+relativePathOfFileInResourceFolder
    print('Reading .properties file @'+propFilePath)
    configs = Properties()
    with open(propFilePath, 'rb') as read_prop:
        configs.load(read_prop)
        print(configs.get(key)[0])


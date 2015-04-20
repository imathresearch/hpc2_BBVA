import simplejson as json
from HPC2.common.constants import CONS


CONS=CONS()

class ParseProperties(object):
    
    ROOT_FILE_SYSTEM = 'root.file.system'
    EXECUTION_DIR = 'execution.dir'
    SHAREIMATHCLOUD = 'share.imathcloud'
    FILE_CLIENT_DATA = 'file.client.data'
    VIRTUALENV = 'virtual.environment'
    ROOT_VIRTUALENV = 'root.virtual.environment'
    PYTHON_VIRTUALENV = 'python.virtual.environment'
    SSH_CONFIG = 'ssh.config'
    TEMPORAL_FILES = 'temporal.files'

    def __init__(self):
        with open(CONS.CONFIGFILE) as data_file:
            self.data = json.load(data_file)
            self.START_DELIMITER='${'
            self.END_DELIMITER='}'

    def getProperty(self, key):
        print "key"
        print key
        if key in self.data:
            value = self.data[key]
            print "value"
            print value
            endIndex = 0
            startIndex = value.find(self.START_DELIMITER, endIndex);
            endIndex = value.find(self.END_DELIMITER, startIndex)
            while ((startIndex >= 0)  and (endIndex >= 0)):
                variableName = value[startIndex + len(self.START_DELIMITER): endIndex]
                variableValue = None
                if variableName != key:
                    variableValue = self.getProperty(variableName)
                if variableName is None:
                    variableValue = self.START_DELIMITER + variableName + self.END_DELIMITER;
                value = value.replace(self.START_DELIMITER + variableName + self.END_DELIMITER, variableValue);
                endIndex = 0
                startIndex = value.find(self.START_DELIMITER, endIndex);
                endIndex = value.find(self.END_DELIMITER, startIndex)
            return value
        else:
            print "---not in---"
            return None;

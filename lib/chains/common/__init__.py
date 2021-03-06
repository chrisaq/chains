class ChainsException(Exception):
    pass

class ParameterException(ChainsException):
    pass

class NoSuchActionException(ChainsException):
    def __init__(self, command):
        ChainsException.__init__(self, 'No such action: %s' % command)
        self.command = command

class NoSuchDeviceException(ChainsException):
    def __init__(self, devid):
        ChainsException.__init__(self, 'No such device: %s' % devid)
        self.devid = devid

class NoSuchActionException(ChainsException):
    def __init__(self, action):
        ChainsException.__init__(self, 'No such action: %s' % action)

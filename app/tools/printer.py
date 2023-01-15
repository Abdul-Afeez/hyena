
class Printer:
    debugMode = False
    @staticmethod
    def print(message):
        if Printer.debugMode:
            print('######################################################################')
            print(message)
            print('######################################################################')
    @staticmethod
    def basic_print(message):
        if Printer.debugMode:
            print(message)
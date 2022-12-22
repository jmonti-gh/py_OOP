''' You are about to create a multifunction device (MFD) that can scan and print documents '''

import abc

class Scanner(abc.ABC):
    @abc.abstractmethod
    def scan_doc(self):
        pass

    @abc.abstractmethod
    def get_scanner_status(self):
        pass


class Printer(abc.ABC):
    @abc.abstractmethod
    def print_doc(self):
        pass

    @abc.abstractmethod
    def get_printer_status(self):
        pass

class MFD1(Scanner, Printer):
    def __init__(self, submodel):
        self.product = 'cheap - ' + str(submodel)
        self.max_resol = '300 dpi'

    def scan_doc(self):
        return 'Sanned Document: several lines'

    def get_scanner_status(self):
        scanner_desc = self.product + ' scanner: ' + self.max_resol
        return scanner_desc

    def print_doc(self):
        return 'Printed Document: several lines'

    def get_printer_status(self):
        print_desc = self.product + ' print:' + self.max_resol
        return print_desc


class MFD2(Scanner, Printer):
    def __init__(self, submodel):
        self.product = 'Std - ' + str(submodel)
        self.max_resol = '600 dpi'

    def scan_doc(self):
        return 'Sanned Document: several lines'

    def get_scanner_status(self):
        scanner_desc = self.product + ' scanner: ' + self.max_resol
        return scanner_desc

    def print_doc(self):
        return 'Printed Document: several lines'

    def get_printer_status(self):
        print_desc = self.product + ' print:' + self.max_resol
        return print_desc


class MFD3(Scanner, Printer):
    def __init__(self, submodel):
        self.product = 'Premium - ' + str(submodel)
        self.max_resol = '1200 dpi'

    def scan_doc(self):
        return 'Sanned Document: several lines'

    def get_scanner_status(self):
        scanner_desc = self.product + ' scanner: ' + self.max_resol
        return scanner_desc

    def print_doc(self):
        return 'Printed Document: several lines'

    def get_printer_status(self):
        print_desc = self.product + ' print:' + self.max_resol
        return print_desc

mdf1 = MFD1(123)
mdf2 = MFD2('std entry')
mdf3 = MFD3('px5')

for obj in mdf1, mdf2, mdf3:
    print()
    print(obj.scan_doc())
    print(obj.get_scanner_status())
    print(obj.print_doc())
    print(obj.get_printer_status())




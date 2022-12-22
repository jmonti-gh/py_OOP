''' ______'''

class LuxuryWatch:
    __watches_created = 0

    def __init__(self):  # __init__ is an instance meth by definition
        LuxuryWatch.__watches_created +=1   # increment w/ every instance created
        self.engraved = ''
        print('Ordinary __init__ was called creating obj.:', LuxuryWatch.__watches_created)

    @classmethod
    def get_nbr_of_watchs_created(cls):      # class method, @classmethod and 'cls' param
        return '# of watches created: {}'.format(cls.__watches_created)  # cls.__class_var_nm
    
    @classmethod
    def including_engraving(cls, engraved):
        print('Class -aditional_constructor- method was called')
        LuxuryWatch.validate_engraved(engraved)
        _watch = cls()
        _watch.engraved = engraved
        return _watch

    @staticmethod
    def validate_engraved(engraved):
        engraved = str(engraved)
        if not engraved.isalnum() or len(engraved) > 40:
            raise ValueError('Text to engrave do not comply with restrictions')
        else:
            return engraved

print()
w1 = LuxuryWatch()
print(LuxuryWatch.get_nbr_of_watchs_created())
print(w1.__dict__)
print()
w2 = LuxuryWatch.including_engraving('house')
print(LuxuryWatch.get_nbr_of_watchs_created())
print(w2.__dict__)

while True:    
    try:
        print()
        engraved = input('Enter the text to engrave: ')
        w3 = LuxuryWatch.including_engraving(engraved)
        print(LuxuryWatch.get_nbr_of_watchs_created())
        print(w3.__dict__)
    except ValueError:
        print('Engraved must not contain spaces and be lesser than 41 chars')
    else:
        break


## for loop & list curiosity....    
# a = [0,1,2,3,4]
# print(a, a[-1])

# for a[-1] in a:
#     print(a[-1])
# print(a, a[-1])

# for a[-3] in a:
#     print(a[-1])
# print(a, a[-1])
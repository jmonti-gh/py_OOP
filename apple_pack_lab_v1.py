''' Monitors the process of apple packaging before the apples are sent to a shop.
A shop owner has asked for 1000 apples, but the total weight limitation cannot exceed 300 units.
'''
from random import uniform

class Apple:
    counter = 0

    def __init__(self, weight):
        self.weight = weight
        Apple.counter += 1

## main
print()
Apple_max_nbr = 300
Apple_max_wght = 105

total = 1000
pkg_cnt, pkgid, pkg_wght, pkg_cuant, wght_amnt, apl_acc = 0, '', 0, 0, 0, 0

while Apple.counter < total:
    for p in range(Apple_max_nbr):
        wght_amnt += Apple(uniform(0.2, 0.5)).weight
        if wght_amnt >= Apple_max_wght or Apple.counter == total:
            break
    pkg_cnt += 1                                # buid a pkg
    pkgid = 'Apple Pakage #' + str(pkg_cnt)
    pkg_wght = wght_amnt
    pkg_cuant = Apple.counter - apl_acc
    apl_acc += pkg_cuant
    print(pkgid, pkg_wght, pkg_cuant, Apple.counter)

    wght_amnt = 0
        
print()
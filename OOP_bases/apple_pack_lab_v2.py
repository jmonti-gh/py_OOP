''' V2. refactor making a Pkg class and instance it in echa pkg creation
and V3 others products not only apples - other class obj to use de Pkg obj
with diff elements'''

from random import uniform

class Apple:
    counter = 0

    def __init__(self, weight):
        self.weight = weight
        Apple.counter += 1

class Pkg:
    counter = 0

    def __init__(self, prdct, wght, cuant):
        Pkg.counter += 1
        self.pkgid = prdct + 'pkg # ' + str(Pkg.counter)
        self.pkgwght = wght
        self.pkgcuant = cuant

## main
print()
Apple_max_nbr = 300
Apple_max_wght = 105

total = 1000
pkg_cnt, pkgid, pkg_wght, pkg_cuant, wght_amnt, apl_acc = 0, '', 0, 0, 0, 0

dpkg = {}
product = Apple
while product.counter < total:
    for p in range(Apple_max_nbr):
        wght_amnt += Apple(uniform(0.2, 0.5)).weight
        if wght_amnt >= Apple_max_wght or Apple.counter == total:
            break
    pkg_cnt += 1                                # buid a pkg
    #pkgid = 'Apple Pakage #' + str(pkg_cnt)
    #pkg_wght = wght_amnt
    pkg_cuant = Apple.counter - apl_acc
    apl_acc += pkg_cuant
    #print(pkgid, pkg_wght, pkg_cuant, Apple.counter)
    dpkg[pkg_cnt] = Pkg(Apple.__class__.__name__, round(wght_amnt, 4), pkg_cuant)
    wght_amnt = 0

for k in dpkg:
    print(dpkg[k].__dict__)

print()
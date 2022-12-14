class Duck:
    counter = 0
    species = 'duck'

    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex
        Duck.counter +=1

    def walk(self):
        pass

    def quack(self):
        print('quacks')

class Chicken:
    clucks = 0
    species = 'chicken'

    def walk(self):
        pass

    def cluck(self):
        Chicken.clucks += 1
        print('clucks')

duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")

chicken = Chicken()
clod = Chicken()

print('So many ducks were born:', Duck.counter)

for poultry in duckling, drake, hen, chicken:
    print(poultry.species, end=' ')
    if poultry.species == 'duck':
        poultry.quack()
    elif poultry.species == 'chicken':
        poultry.cluck()

print('So many clucks were heard:', Chicken.clucks)

# without using species class var.
print()
for bird in duckling, drake, hen, clod:
    #print(bird.__class__, end=' ')
    print(bird.__class__.__name__, end=' ')
    if isinstance(bird, Duck):
        bird.quack()
    if isinstance(bird, Chicken):
        bird.cluck()
print('So many clucks were heard:', Chicken.clucks)
print()

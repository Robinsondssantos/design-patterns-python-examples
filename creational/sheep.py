import copy


class Sheep(object):

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def clone(self):
        return copy.deepcopy(self)

def main():
    original_sheep = Sheep('Dolly', 'Finn Dorset')
    print('original_sheep.name: {}'.format(original_sheep.name))
    print('original_sheep.breed: {}'.format(original_sheep.breed))
    cloned_sheep = original_sheep.clone()
    print('cloned_sheep.name: {}'.format(cloned_sheep.name))
    print('cloned_sheep.breed: {}'.format(cloned_sheep.breed))

if __name__ == '__main__':
    main()

        


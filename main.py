import cowsay
import random


animals = ['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty',
           'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex',
           'turkey', 'turtle', 'tux']


def main() -> None:
    random_animal = random.choice(animals)

    getattr(cowsay, random_animal)('Hello world')


if __name__ == "__main__":
    main()
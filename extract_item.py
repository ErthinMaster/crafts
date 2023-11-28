
import random



if __name__ == '__main__':
    plants = []
    with open("./Plantes.txt", "r") as f:
        plants = f.readlines()
    plants = list(dict.fromkeys(sorted(v for v in random.choices(plants, k = (int(len(plants)/8))) if len(v) > 2)))
    with open("./NewPlantes.txt", "w") as f:
        f.writelines(plants)
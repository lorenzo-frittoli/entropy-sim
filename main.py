from ensamble import Ensamble


def main():
    ens = Ensamble(1)
    print(ens)
    print(ens.calculate_entropy())


if __name__ == '__main__':
    main()
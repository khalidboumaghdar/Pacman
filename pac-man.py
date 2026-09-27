import sys
from src.config.loader import Parser


def main():
    if len(sys.argv) <= 1:
        print("! warning must be config file")
    else:
        parser = Parser()

        config = parser.parse(sys.argv[1])

        print(config)


if __name__ == "__main__":
    main()

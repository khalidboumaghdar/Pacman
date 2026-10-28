from src.ui.hub import Hub


def main() -> None:
    try:
        hub = Hub()
        hub.runMenu()
    except KeyboardInterrupt:
        print("\ngame stopped!")


if __name__ == "__main__":
    main()

from src.ui.hub import Hub

if __name__ == "__main__":
    try:
        hub = Hub()
        hub.runMenu()
    except KeyboardInterrupt:
        print("\ngame stopped!")

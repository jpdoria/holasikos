import sys
import time
import keyboard
import requests


def read():
    data = requests.get("http://www.scifiscripts.com/scripts/swd1_5-74.txt")
    return data.text


def write(text):
    delay = 10
    print(
        f"Starting in {delay} seconds. Open any editor now!\nJust do CTRL-C to close this program.\nIf you're already in an editor in a different window,\nquickly switch back to the terminal (ALT-TAB) and execute CTRL-C.\nEnjoy! :)"
    )
    time.sleep(delay)

    while True:
        keyboard.write(text, delay=0.5)
        keyboard.press_and_release("enter")
        time.sleep(1)


def main():
    text = read()
    write(text)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Goodbye!\n")
        sys.exit(1)

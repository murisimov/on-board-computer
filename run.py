from time import ctime

from helpers.speech import speak
from helpers.maps import open_map
from helpers.sr import listen


def main():
    print(
    """
    List of commands:

      stop/exit/bye :       Exit

      time :                Current time

      location <location> : Open chrome tab with google maps and given location

    """
    )
    speak("Greetings!")

    while True:
        try:
            text = input("> ")

        except (SystemExit, KeyboardInterrupt, EOFError):
            speak("Detaching.")
            break

        except:
            speak("Input error, occured")
            break

        else:

            if text in ['stop', 'exit', 'bye']:
                speak("Shutting down.")
                break

            elif text == 'time':
                slowtime = ctime().replace(' ', '. ')
                speak(slowtime)

            elif text.startswith('location'):
                location = text.partition(' ')[-1]
                speak("Searching for " + location)
                open_map(location)

            elif text == 'chat':
                if listen:
                    speak("Sure, speak. . .")
                    speak("I heard you say this. " + listen())
                else:
                    speak("Sorry, but speech recognition module is not installed")

            elif not text:
                continue
            else:
                speak(text)


if __name__ == '__main__':
    main()

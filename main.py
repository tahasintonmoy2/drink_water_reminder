import pyttsx3
import time
from plyer import notification

while True:
    vivo = pyttsx3.init()
    vivo.say("you need drink water")
    vivo.runAndWait()
    timeout = 8

    if __name__ == "__main__":
       # while True:
            notification.notify(
                #title = "you need a drink water right now 🥰",
                message = "U.S. National Academies of Sciences, "
                        "Engineering, and Medicine determined "
                        "that an adequate daily fluid intake is: "
                        "About 15.5 cups (3.7 liters) of fluids a "
                        "day for men. About 11.5 cups (2.7 liters) "
                        "of fluids a day for women.",
                app_icon = "icon.ico",
                timeout = 12
       )
    time.sleep(60*60)


import sys
sys.path.append("..")
from src.telegramCurl import telegramBot
from time import sleep
import sys

  


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 5:
        bot = telegramBot(args[1])
        bot.sendFile(args[2],args[3],args[4])
    elif len(args) == 6:
        bot = telegramBot(args[1])
        bot.sendFile(args[2],args[3],args[4],args[5])
    else:
        print("to test:\n  python ./sendFile.py <toke> <chatId> <type> <file> <caption?>")

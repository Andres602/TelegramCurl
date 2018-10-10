import sys
sys.path.append("..")
from src.telegramCurl import telegramBot
from time import sleep
import sys


class app:
    def __init__(self, token):
        self.bot = telegramBot(token)
        self.updateId = False
        print("Runing bot {0}".format(self.bot.getMe()['result']['username']))

    def run(self):
        while 1:
            updates = self.bot.getUpdates(self.updateId)
            if(len(updates['result'])):
                self.updates = updates['result']
                self.updates.sort(key=lambda x: x["update_id"], reverse=False)
                self.updateId = self.updates[-1]['update_id']+1
                self.updateManager()
                sleep(1)

    def updateManager(self):
        for update in self.updates:
            id = None
            data = None
            if('chat' in update['message']):
                id = update['message']['chat']['id']
                data = update['message']
                self.process(id, data)

    def process(self, id, data):
        if 'text' in data:
            self.bot.sendMessage(id, data['text'])
        else:
            for dataType in ['photo', 'audio', 'document', 'video', 'voice', 'video_note']:
                if dataType in data:
                    fileId = data['photo'][-1]['file_id'] if dataType == 'photo' else data[dataType]['file_id']
                    self.bot.sendFileById(id, dataType,fileId)
                    break


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        botEcho = app(args[1])
        botEcho.run()
    else:
        print("to test:\n  python ./echo.py <toke>")

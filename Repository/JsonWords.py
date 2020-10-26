import json


class JsonWords:
    def get_data(self):
        data = json.load(open("words.json"))

        return data

    def get_words(self):
        words = self.get_data()["data"]

        return words

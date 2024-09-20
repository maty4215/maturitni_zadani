import json
import random

class lokalita:
    def __init__(self):
        self.bobri = []
        self.nory = []
        self.bobri_v_norach = {}

    def load_bobry(self, file_bobri):
        with open(file_bobri, 'r') as f:
            data = json.load(f)
            self.bobri = data['bobri']

    def load_nory(self, file_nory):
        with open(file_nory, 'r') as f:
            data = json.load(f)
            self.nory = data['nory']

    def assign_nory(self):
        if len(self.bobri) > len(self.nory):
            print("nedostatek nor")
            return
        random.shuffle(self.nory)
        self.bobri_v_norach = dict(zip(self.bobri, self.nory))

    def __str__(self):
        output = ""
        for bobr, nora in self.bobri_v_norach.items():
            output += f"{bobr} je v {nora}\n"
        return output

if __name__ == "__main__":
    lokalita = lokalita()

    lokalita.load_bobry("bobri.json")
    lokalita.load_nory("nory.json")

    lokalita.assign_nory()

    print(lokalita)

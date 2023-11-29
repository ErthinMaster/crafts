
def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def write_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_txt(path):
    with open(path, "r") as f:
        return f.readlines()

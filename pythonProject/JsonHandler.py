import json


class JsonHandler:

    def write_json(self, filename: str, my_data: list):
        with open(filename, "w") as f:
            json.dumps(my_data, fp=f, indent=4)

        f.close()

    def print_json(self, filename: str):
        with open(filename, "r") as f:
            loaded_json = json.loads(f)
            for x in loaded_json:
                print("%s: %d" % (x, loaded_json[x]))
        f.close()
        return loaded_json

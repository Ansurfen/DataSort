from core import data


class Container():
    key = ""
    prototype = ""
    data = {}

    def __init__(self, key, data):
        self.prototype = key
        self.key = key.lower()
        self.data = data

    def key_filter(self):
        for f in data.filter_table:
            self.key = self.key.replace(f, ' ')

    def key_map(self):
        for k in data.pre_map.keys():
            if k in self.key:
                self.key = self.key.replace(k, data.pre_map[k])


def chain_filter(chain):
    for i in range(0, len(chain)):
        chain[i].key_filter()
        chain[i].key_map()
    return chain

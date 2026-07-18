from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.minFreq = 0
        self.keyToVal = {}
        self.keyToFreq = {}
        self.freqToKeys = defaultdict(OrderedDict)

    def update(self, key):
        freq = self.keyToFreq[key]
        val = self.freqToKeys[freq].pop(key)
        if not self.freqToKeys[freq] and self.minFreq == freq:
            self.minFreq += 1
        self.keyToFreq[key] = freq + 1
        self.freqToKeys[freq + 1][key] = val

    def get(self, key: int) -> int:
        if key not in self.keyToVal:
            return -1
        self.update(key)
        return self.keyToVal[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.keyToVal:
            self.keyToVal[key] = value
            self.update(key)
            self.freqToKeys[self.keyToFreq[key]][key] = value
            return

        if len(self.keyToVal) == self.cap:
            old, _ = self.freqToKeys[self.minFreq].popitem(last=False)
            del self.keyToVal[old]
            del self.keyToFreq[old]

        self.keyToVal[key] = value
        self.keyToFreq[key] = 1
        self.freqToKeys[1][key] = value
        self.minFreq = 1

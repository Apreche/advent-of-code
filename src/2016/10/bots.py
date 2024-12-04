import pprint


class Bot:
    def __init__(self):
        self.values = []

    @property
    def full(self):
        return len(self.values) == 2

    @property
    def high(self):
        if self.values:
            return max(self.values)
        else:
            return None

    @property
    def low(self):
        if self.values:
            return min(self.values)
        else:
            return None

    def set(self, value):
        assert(len(self.values) < 2)
        self.values.append(value)

    def __unicode__(self):
        return 'H: %s L: %s' % (self.high, self.low)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()


class Factory:
    def __init__(self):
        self.bots = {}
        self.outputs = {}

    def input(self, bot, value):
        if bot not in self.bots:
            self.bots[bot] = Bot()
        self.bots[bot].set(value)

    def instruct(self, from_bot_id, from_val, to, to_id):
        assert(to in ['bot', 'output'])
        assert(from_val in ['low', 'high'])

        if from_bot_id not in self.bots:
            return False

        from_bot = self.bots[from_bot_id]
        if from_bot.full:
            if from_val == 'low':
                value = from_bot.low
            else:
                value = from_bot.high

            if to == 'bot':
                if to_id not in self.bots:
                    self.bots[to_id] = Bot()
                self.bots[to_id].set(value)
            elif to == 'output':
                if to_id not in self.outputs:
                    self.outputs[to_id] = []
                self.outputs[to_id].append(value)
            return True
        else:
            return False

    def __unicode__(self):
        bot_str = pprint.pformat(self.bots, indent=4)
        return "BOTS: %s\n\nOUTPUTS: %s" % (bot_str, self.outputs)

    def __str__(self):
        return self.__unicode__()

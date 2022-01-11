class Podpunkt_1_2_3:

    def __init__(self):
        self.pattern = ("o", "y", "o", "y", "o", "o", "r", "o", "r", "r")
        self.range = 6
        self.counter = 0
        self.number_of_throws = 7
        self.number_of_fields = 9
        self.map_of_throws = [0, 0, 0, 0, 0, 0, 0]

    def number_of_possibilities(self, how_far_we_are, which_throw, yellow, red):
        if yellow and red:
            self.map_of_throws[which_throw-1] += 1
            self.counter += 6**(self.number_of_throws - which_throw)  # doliczanie opcji
            return

        for k in range(1, self.range):
            if which_throw < self.number_of_throws and how_far_we_are + k <= self.number_of_fields:
                if self.pattern[how_far_we_are + k] == "y":
                    self.number_of_possibilities(how_far_we_are + k, which_throw + 1, True, red)
                if self.pattern[how_far_we_are + k] == "r":
                    self.number_of_possibilities(how_far_we_are + k, which_throw + 1, yellow, True)
                if self.pattern[how_far_we_are + k] == "o":
                    self.number_of_possibilities(how_far_we_are + k, which_throw + 1, yellow, red)

    def reset_counter(self):
        self.counter = 0

    def reset_map(self):
        self.map_of_throws = [0, 0, 0, 0, 0, 0, 0]

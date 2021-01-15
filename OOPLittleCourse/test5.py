class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = int(dollars)
        self.cents = int(cents)

    def add_money(self, deposit_dollars, deposit_cents):

        self.dollars += int(deposit_dollars)
        if self.cents + int(deposit_cents) <= 99:
            self.cents += int(deposit_cents)
        else:
            self.dollars = ((self.cents + int(deposit_cents)) // 100) + self.dollars
            self.cents = (self.cents + int(deposit_cents)) % 100

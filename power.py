#Creare una classe che passati due numeri x ed n ne esegua la potenza
class power:
    def __init__(self, x , n):
        self.x = x
        self.n = n

    def eleva(self):
        result = self.n**self.x
        print(result)
number = power(2, 4)
number.eleva()

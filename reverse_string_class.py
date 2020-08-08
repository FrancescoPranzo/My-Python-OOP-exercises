#write a class that reverse a string
class Reverse_string:
     def __init__(self, string):
         self.string = string

     def cambia(self):
         len_str = (len(self.string))-1
         cp_str = ""
         #print(len_str)
         while len_str >= 0:
             cp_str += self.string[len_str]
             len_str = len_str - 1
         print(cp_str)


prova = Reverse_string("Ciao")
prova.string
prova.cambia()

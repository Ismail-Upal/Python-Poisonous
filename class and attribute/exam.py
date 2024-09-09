class Exam:
    def __init__(self, name):
        self.name = name

    def attend(self,name):
        print(f'thanks for attend ,ningen {name}')
    def marks(self, name, num):
        print(f'ningen, {name} got {num}')


upal = Exam("upal")
upal.attend('upal')
upal.marks('upal', 34)

stone = Exam("stone")
stone.attend("stone")
stone.marks('stone', 75)
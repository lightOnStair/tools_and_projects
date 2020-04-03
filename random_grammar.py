class Random:
    def __init__(self,seed):
        self.seed = seed

    def next(self):
        self.seed = (16807*self.seed) % (2147483647)
        return self.seed

    def choose(self,objects):
        return objects[self.next()%len(objects)]

class Grammar:
    def __init__(self,seed):
        self.randint = Random(seed)
        self.rules = {}
    def rule(self,left,right):
        if self.rules.get(left,right) == right:
            self.rules[left] = [right]
        else:
            self.rules[left] += [right]

    def generate(self):
        if self.rules.get('Start') != None:
            return self.generating(('Start',))
        else:
            raise RuntimeError
    def generating(self,strings):
        res = ''
        for string in strings:
            if string not in self.rules and string != ".":
                res += string + " "
            elif string == ".":
                res += "."
            else:
                a = self.randint.choose(self.rules[string])
                res += self.generating(a)
        return res
def main():
    G = Grammar(101)
    G.rule('Noun',   ('cat',))                                #  01
    G.rule('Noun',   ('boy',))                            #  02
    G.rule('Noun',   ('dog',))                                #  03
    G.rule('Noun',   ('girl',))                               #  04
    G.rule('Verb',   ('bit',))                                #  05
    G.rule('Verb',   ('chased',))                             #  06
    G.rule('Verb',   ('kissed',))                             #  07
    G.rule('Phrase', ('the', 'Noun', 'Verb', 'the', 'Noun'))  #  08
    G.rule('Story',  ('Phrase',))                             #  09
    G.rule('Story',  ('Phrase', 'and', 'Story'))              #  10
    G.rule('Start',  ('Story', '.'))                          #  11
    print("\n\n20 results gained by running 'generate' are shown below:\n\n")
    for i in range(20):
        print(G.generate())
if __name__ == '__main__':
    main()

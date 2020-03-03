import re
import reprlib
RE_WORD = re.compile('\w+')



class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


s = Sentence('"The time has come," the Walrus said,')
for word in s :
    print(word)


class Sentence2:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)
        ''' #use generator to do it
        for word in self.words: 
            yield word
        return
        '''



class SentenceIterator:

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self



class Sentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()

        #or do it this way
        #return (match.group() for match in RE_WORD.finditer(self.text)) # generator object

def gen_AB(): #
    print('start')
    yield 'A' #
    print('continue')
    yield 'B' #
    print('end.') #

for c in gen_AB(): #
    print('-->', c)
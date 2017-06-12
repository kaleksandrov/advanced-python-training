def words(filename, chunk_size):
    word = []
    for ch in chars(filename, chunk_size):
        if ch.isalpha():
            word.append(ch)
        else:
            if word:
                yield ''.join(word)
                word = []

class _words(object):

    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        return WordIterator(self.filename, 1)

class WordIterator(object):


    def __init__(self, filename, chunk_size=1):
        self.filename = filename
        self.chunk_size = chunk_size
        self.file = open(filename, 'r')
        self.chunk=''
        self.chunk_index = 0


    def next_char(self):
        if len(self.chunk) == self.chunk_index:
            self.chunk = self.file.read(self.chunk_size)
            self.chunk_index = 0

            if not self.chunk:
                return None

        result = self.chunk[self.chunk_index]
        self.chunk_index += 1
        return result


class chars(object):

    def __init__(self, filename, chunk_size=1):
        self.filename = filename
        self.chunk_size = chunk_size

    def __iter__(self):
        return CharIterator(self.filename, self.chunk_size)

class CharIterator(object):


    def __init__(self, filename, chunk_size=1):
        self.filename = filename
        self.chunk_size = chunk_size
        self.chunk = ''
        self.chunk_index = 0
        self.file = open(filename, 'r')


    def __next__(self):
        if len(self.chunk) == self.chunk_index:
            self.chunk = self.file.read(self.chunk_size)
            self.chunk_index = 0

            if not self.chunk:
                raise StopIteration()

        result = self.chunk[self.chunk_index]
        self.chunk_index += 1
        return result

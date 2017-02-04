"""
    The Burrows-Wheeler transform rearranges strings into runs of similar characters.
    This is useful for compression since it tends to be easy to compress a string that has runs
    of repeated characters with techniques such as move-to-front transform and run-length encoding.
    Most importantly BWT is reversible.
"""


class BWT:
    @staticmethod
    def encode(text):
        n = len(text)
        table = [text[i:n] + text[0:i] for i in range(n)]
        table = sorted(table)
        encoded = ''.join(r[-1] for r in table)
        index = table.index(text)

        return index, encoded

    @staticmethod
    def decode(encoded, index):
        n = len(encoded)
        table = ['' for _ in encoded]
        for i in range(n):
            table = [c + table[j] for j, c in enumerate(encoded)]
            # for j, c in enumerate(encoded):
            #     table[j] = c + table[j]
            table = sorted(table)

        return table[index]


if __name__ == '__main__':
    input_str = 'banana'
    print('Input: {}'.format(input_str))
    idx, enc = BWT.encode(input_str)
    print('Index: {} Encoded: {}'.format(idx, enc))
    dec = BWT.decode(enc, idx)
    print('Decoded: {}'.format(dec))

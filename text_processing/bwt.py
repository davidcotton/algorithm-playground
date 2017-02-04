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
    # input_str = 'banana'
    # input_str = 'The Burrows-Wheeler transform rearranges strings into runs of similar characters.'
    input_str = 'The Burrows–Wheeler transform (BWT, also called block-sorting compression) rearranges a character ' \
                'string into runs of similar characters. This is useful for compression, since it tends to be easy ' \
                'to compress a string that has runs of repeated characters by techniques such as move-to-front ' \
                'transform and run-length encoding. More importantly, the transformation is reversible, without ' \
                'needing to store any additional data. The BWT is thus a "free" method of improving the efficiency ' \
                'of text compression algorithms, costing only some extra computation.'
    print('Input:\n  {}\n'.format(input_str))
    idx, enc = BWT.encode(input_str)
    print('Encoded:\n  {}\nIndex:\n  {}\n'.format(enc, idx))
    dec = BWT.decode(enc, idx)
    print('Decoded:\n  {}'.format(dec))

"""Computing kmers of a string."""

from collections import Counter
from typing import Iterator

class IllegalKValue(ValueError):
    pass

def string_into_kmer_iter(x: str, k: int) -> Iterator[str]:
    """
    Returns a generator of kmer strings from a string.
    >>> kmers = string_into_kmer_iter('AGTC', 3)
    >>> next(kmers)
    'AGT'
    >>> next(kmers)
    'GTC'
    """
    if k <= 0:
        raise IllegalKValue('You can not use k <= 0')
    for j in range(len(x) - k + 1):
        yield x[j : j + k]


def kmer(x: str, k: int) -> list[str]:
    """
    Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']
    """
    return [kmer for kmer in string_into_kmer_iter(x, k)]


def unique_kmers(x: str, k: int) -> list[str]:
    """
    Computer all unique k-mers of x.

    >>> unique_kmers('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'gtc', 'tcg']
    """
    return list(dict.fromkeys(kmer(x, k)))


def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computer all k-mers of x and count how often they appear.

    >>> count_kmers('AAAT', 3)
    {'AAA': 1, 'AAT': 1}
    """
    counter = Counter()
    for kmer in string_into_kmer_iter(x, k):
        counter.update((kmer,))
    return dict(counter)


def count_kmers_sorted(x: str, k: int) -> list[(str, int)]:
    """
    Computer all k-mers of x and count how often they appear. It returns a sorted list of tuples.

    >>> count_kmers_sorted('AAATTT', 2)
    [('AA', 2), ('TT', 2), ('AT', 1)]

    """
    d = count_kmers(x, k)
    return sorted(d.items(), key=lambda x: x[1], reverse=True)

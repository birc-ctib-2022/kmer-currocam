"""Computing kmers of a string."""

from collections import Counter
from typing import Iterator


def string_into_kmer_iter(x: str, k: int) -> Iterator[str]:
    for j in range(len(x) - k + 1):
        yield x[j:j + k]

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
    {'AA': 2, 'AT': 1}
    """
    counter = Counter() 
    for kmer in string_into_kmer_iter(x, k):
        counter.update((kmer,))
    return counter

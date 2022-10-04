"""Computing kmers of a string."""


def kmer(x: str, k: int) -> list[str]:
    """
    Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']
    """
    size = len(x) -k +1
    kmers = [None] * size
    i = 0
    for j in range(len(x) - k + 1):
        kmers[i] = x[j:j + k]
        i += 1
    return kmers


def unique_kmers(x: str, k: int) -> list[str]:
    """
    Computer all unique k-mers of x.

    """
    return list(dict.fromkeys(kmer(x, k)))


def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computer all k-mers of x and count how often they appear.

    FIXME: do you want more tests here?
    """
    ...

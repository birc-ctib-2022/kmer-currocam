# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from kmer import kmer, unique_kmers


def test_kmer_computes_all_kmers():
    """Given a non empty string, it returns all kmers"""
    assert kmer('agtagtcg', 3) == ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

def test_kmer_with_empty_string():
    """Given a empty string, it returns an empty list"""
    assert kmer('', 3) == []

def test_kmer_with_a_not_enough_long_string():
    """Given a string x, for which len(x) < k, it returns an empty list"""
    assert kmer('AA', 3) == []

def test_unique_kmers_works_with_non_unique_kmers():
    """Given a non empty string with non unique kmers, it returns all unique kmers"""
    assert unique_kmers('agtagtcg', 3) == ['agt', 'gta', 'tag', 'gtc', 'tcg']

def test_unique_kmers_works_with_unique_kmers():
    """Given a non empty string with non unique kmers, it returns all unique kmers"""
    string = 'ATTC'
    assert unique_kmers(string, 2) == ['AT', 'TT', 'TC']
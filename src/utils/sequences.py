

def get_subsequences(hand, length):
    """
    Gets all subsequences of a given length from the hand
    :param hand:  total list of cards
    :param length:  length of subsequences to get
    :param result: list of subsequences (list of list)
    :param tmp_seq: current subsequence being constructed
    :param idx: current index into hand
    :return:
    """
    sequences = []
    _get_subsequence(hand, length, sequences, [], 0)
    return sequences


def _get_subsequence(hand, length, all_sequences, tmp_seq, idx):
    """
    recursive method that builds sequences
    :param length: the length of the resulting sequence
    :param all_sequences: a list holding the sequences
    :param tmp_seq: the current, temporary sequence being built up
    :param idx: the current index into the hand
    :return:
    """
    if len(tmp_seq) == length:
        seq = tmp_seq.copy()
        seq.sort()
        all_sequences.append(seq)
        return

    if idx >= len(hand):
        return

    tmp_seq.append(hand[idx])
    _get_subsequence(hand, length, all_sequences, tmp_seq, idx+1)
    tmp_seq.pop()
    _get_subsequence(hand, length, all_sequences, tmp_seq, idx+1)
class NeedlemanWunsch:
    """
    Needleman-Wunsch Global Sequence Alignment.
    Finds optimal end-to-end alignment between biological sequences.
    """
    def __init__(self, match=1, mismatch=-1, gap=-2):
        self.match = match
        self.mismatch = mismatch
        self.gap = gap

    def align(self, s1, s2):
        n = len(s1)
        m = len(s2)
        score = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            score[i][0] = i * self.gap
        for j in range(m + 1):
            score[0][j] = j * self.gap

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                match_score = self.match if s1[i - 1] == s2[j - 1] else self.mismatch
                score[i][j] = max(
                    score[i - 1][j - 1] + match_score,
                    score[i - 1][j] + self.gap,
                    score[i][j - 1] + self.gap
                )
        return score[n][m]

from itertools import groupby
class Solution:
    def expressiveWords(self, s: str, words) -> int:
        count = 0
        lst_s = [(k, len(tuple(g))) for k, g in groupby(s)]
        len_lst_s = len(lst_s)
        print(lst_s)
        for w in words:
            lst_w = [(k, len(tuple(g))) for k, g in groupby(w)]
            if (len_lst_s == len(lst_w) and
                    all(c1 == c2 and (k1 == k2 or k1 < k2 >= 3)
                        for (c1, k1), (c2, k2) in zip(lst_w, lst_s))):
                count += 1
        return count
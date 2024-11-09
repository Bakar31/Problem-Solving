class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_s = sorted(list(s))
        t_s = sorted(list(t))

        if len(s_s) == len(t_s) and s_s == t_s:
            return True
        else:
            return False
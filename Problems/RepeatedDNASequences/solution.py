class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Use two sets:
        # 'seen' tracks all 10-letter sequences encountered so far,
        # 'res' stores sequences that have been seen more than once.
        seen, res = set(), set()

        # Loop over the string such that each substring of length 10 is examined.
        # The range is set to len(s) - 9 because we need to obtain a substring
        # from index l to l+10 (inclusive of l and exclusive of l+10), which requires
        # that l+10 <= len(s).
        for l in range(len(s) - 9):
            # Extract the substring (of 10 characters) starting at index 'l'.
            cur = s[l:l + 10]
            # Check if this sequence has been seen before.
            if cur in seen:
                # If it has, add the sequence to the result set.
                res.add(cur)
            else:
                # Otherwise, mark this sequence as seen.
                seen.add(cur)
        # Convert the set of repeated sequences into a list before returning.
        return list(res)
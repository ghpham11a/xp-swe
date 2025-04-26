class Solution:
    def hIndex(self, citations):
        # Get the number of papers
        n = len(citations)

        # Initialize an array to count how many papers have a certain number of citations
        # paper_counts[i] = number of papers with exactly i citations
        # paper_counts[n] will also count any paper with more than n citations
        paper_counts = [0] * (n + 1)
        
        # Fill the paper_counts array
        for c in citations:
            if c > n:
                # If a paper has more citations than the total number of papers,
                # count it as n (because h-index cannot exceed the number of papers)
                paper_counts[n] += 1
            else:
                # Otherwise, count the number of papers with exactly c citations
                paper_counts[c] += 1

        # Start checking h-index from the maximum possible value n down to 0
        h = n

        # papers keeps track of the cumulative number of papers with at least 'h' citations
        papers = paper_counts[n]

        # Decrease h until we find the largest h where there are at least h papers with ≥ h citations
        while papers < h:
            h -= 1
            papers += paper_counts[h]  # Add papers with exactly h citations to cumulative count

        # Return the h-index found
        return h
def compute_lps(pattern):
    # Create LPS array to hold the longest prefix suffix values for pattern
    lps = [0] * len(pattern)  # lps[i] = length of the longest prefix which is also a suffix for pattern[0..i]
    length = 0  # Length of the previous longest prefix suffix

    # Start from the second character
    for i in range(1, len(pattern)):
        # If there's a mismatch, fall back to the last known good prefix length
        while length > 0 and pattern[i] != pattern[length]:
            length = lps[length - 1]  # Try shorter previous prefix

        # If there's a match, increment length and set it in lps
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length  # Set the current lps value

    return lps

def kmp_search(text, pattern):
    if not pattern:
        return []  # Edge case: empty pattern always matches at every position, but here we return empty list

    lps = compute_lps(pattern)  # Preprocess pattern to get LPS table
    matches = []  # Store the starting indices of pattern matches in text
    j = 0  # Index for pattern

    # Loop over each character in the text
    for i in range(len(text)):
        # If mismatch after j matches, fall back in the pattern using LPS
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]  # Reuse previous matched prefix

        # If characters match, move forward in the pattern
        if text[i] == pattern[j]:
            j += 1

        # If we've matched the whole pattern
        if j == len(pattern):
            matches.append(i - j + 1)  # Match found, record starting index
            j = lps[j - 1]  # Continue searching for the next possible match

    return matches
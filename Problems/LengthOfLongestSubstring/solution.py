def solution(string),
    seen_chars = {}
    result = 0
    left = 0

    for right in range(len(string)):
        curr_char = string[right]

        if curr_char in seen_chars and seen_chars[curr_char] >= left:
            left = seen_chars[curr_char] + 1
        else:
            result = max(result, right - left + 1)
        seen_chars[curr_char] = right

    return result

    
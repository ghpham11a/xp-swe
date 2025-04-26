class Solution:
    def fullJustify(self, words, maxWidth):
        output = []
        line, length = [], 0

        i = 0

        while i < len(words):

            if length + len(line) + len(words[i]) > maxWidth:
                # Line complete
                extra_space = maxWidth - length

                spaces = extra_space // max(1, len(line) - 1)
                remainder = extra_space % max(1, len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line[j] += (" " * spaces)
                    if remainder:
                        line[j] += " "
                        remainder -= 1

                output.append("".join(line))
                line, length = [], 0
            
            line.append(words[i])
            length += len(words[i])
            i += 1

        # Handling last line
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        output.append(last_line + (" " * trail_space))
        return output
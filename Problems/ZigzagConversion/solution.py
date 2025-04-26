class Solution(object):
    def convert(self, string, num_rows):
        result = ["" for row in range(num_rows)]
    
        row_index = 0
        origin = 'CEILING'

        for char in string:

            result[row_index] += char

            if origin == 'CEILING':
                if (row_index + 1) >= num_rows:
                    origin = 'FLOOR'
                    row_index -= 1
                else:
                    row_index += 1
                    
            else:
                if (row_index - 1) < 0:
                    origin = 'CEILING'
                    row_index += 1
                else:
                    row_index -= 1


        printed_result = "" 
        for row in result:
            printed_result += row

        return printed_result
class Solution:

    def multiply(self, mat_a, mat_b):

        mat_a_row_count = len(mat_a)
        mat_a_col_count = len(mat_a[0])
        mat_b_col_count = len(mat_b[0])

        output_row_count = mat_a_row_count
        output_col_count = mat_b_col_count

        output = [[0 for _ in range(output_col_count)] for _ in range(output_row_count)]

        for mat_a_row in range(mat_a_row_count):
            for mat_a_col in range(mat_a_col_count):

                mat_a_element = mat_a[mat_a_row][mat_a_col]
                
                if mat_a_element:
                    
                    for mat_b_col in range(mat_b_col_count):
                        mat_b_element = mat_b[mat_a_col][mat_b_col]
                        output[mat_a_row][mat_b_col] += (mat_a_element * mat_b_element)
        

        return output
    
solution = Solution()

assert(solution.multiply([[1,0,0],[-1,0,3]], [[7,0,0],[0,0,0],[0,0,1]]) == [[7,0,0],[-7,0,3]])
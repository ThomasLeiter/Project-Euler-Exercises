"""
By starting at the top of the triangle below and 
moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible 
to solve this problem by trying every route. 
However, Problem 67, is the same challenge with a 
triangle containing one-hundred rows; it cannot be 
solved by brute force, and requires a clever method! ;o)
"""

from os.path import join
 
def read_and_parse_triangle(file_name):
    """
    Read a ' '-separated triangle from a file \n
    and return it as a list of lists.

    Parameters:
    ------------
    file_name : str
        The name of the file
    
    Returns:
    ---------
    list[list[int]]
        The list of rows of the triangle
    """
    path = join('Euler Project','Python',f'{file_name}.txt')
    triangle = []
    with open(path,'r') as f:
        for line in f:
            line = line[:-1]                # remove line-break
            line = line.split(' ')          # split at whitespace
            line = [int(n) for n in line]   # convert to number
            triangle.append(line)
    return triangle

def calculate_maximum_path(triangle):
    """
    Calculate the largest sum of all paths from \n
    top to bottom in the given triangular grid. \n
    Note that edge nodes have exactly one parent \n
    and other nodes have exactly two parents. 

    Parameters:
    ------------
    triangle : list[list[int]]
        The triangular grid as a list of lists
    
    Return:
    --------
    int 
        The largest sum among all paths from top to bottom.
    """
    last_row = triangle[0]
    for i in range(1,len(triangle)):
        new_row = [0 for j in range(i+1)]
        new_row[0] = last_row[0] + triangle[i][0]
        new_row[-1] = last_row[-1] + triangle[i][-1]
        for j in range(1,i):
            max_parent = max(last_row[j-1],last_row[j])
            new_row[j] = max_parent + triangle[i][j]
        last_row = new_row
    return max(last_row)
        

if __name__ == '__main__':
    triangle = read_and_parse_triangle('Problem_18_triangle')
    max_path_sum = calculate_maximum_path(triangle)
    print(f'The largest path in Problem 18 has a value of {max_path_sum}.')
    triangle = read_and_parse_triangle('Problem_67_triangle')
    max_path_sum = calculate_maximum_path(triangle)
    print(f'The largest path in Problem 67 has a value of {max_path_sum}.')
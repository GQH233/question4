IN_FILE_NAME = 'input_question_4.py'
OUT_FILE_NAME = 'output_question_4.py'


def read_matrix(file_name):
    """
    Read matrix from the file
    :param file_name: the name of the file
    :return: a 2D-list of integers
    """
    matrix = []
    file = open(file_name)
    for line in file.readlines():
        # delete the '\n' and space at the beginning and the end of the string
        data = line.strip()
        # split the data into pieces
        if '\t' in data:
            data = data.split('\t')
        elif ' ' in data:
            data = data.split(' ')
        data = [int(x) for x in data]  # convert the string to integers
        matrix.append(data)
    return matrix


def dfs(x, y, matrix, is_visited, count, connect_type):
    """
    Label the matrix with depth first searching
    :param x: x coordinate of the current point
    :param y: y coordinate of the current point
    :param matrix: a 2D-list of integers
    :param is_visited: a 2D-list recording whether the point has been visited
    :param count: the value to be labeled
    :param connect_type: the type of connection (4 or 8)
    :return: None
    """
    directions_4 = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    directions_8 = [(-1, 0), (0, 1), (0, -1), (1, 0), (-1, -1), (1, 1), (1, -1),
                    (-1, 1)]
    directions = directions_4
    if connect_type == 8:
        directions = directions_8
    is_visited[x][y] = True  # change the status of the is_visited[x][y]
    matrix[x][y] = count  # label the matrix
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) \
                and not is_visited[nx][ny] and matrix[nx][ny] == 1:
            # search the next position
            dfs(nx, ny, matrix, is_visited, count, connect_type)


def output_matrix(matrix, connect_type):
    """
    Traverse the matrix with depth first search.
    :param matrix: a 2D-list with integers
    :param connect_type: the type of connection
    :return: a 2D-list which is labeled
    """
    # set the status of is_visited matrix
    is_visited = [[False for _ in range(len(matrix[0]))] for _ in
                  range(len(matrix))]
    count = 1
    # traverse the matrix
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if not is_visited[i][j] and matrix[i][j] == 1:
                dfs(i, j, matrix, is_visited, count, connect_type)
                count += 1  # increment the count for next components
    return matrix


def write_to_file(matrix, file_name):
    """
    Write the labeled matrix to the file
    :param matrix: a 2D-list containing labeled data
    :param file_name: the name of the file
    :return: None
    """
    file = open(file_name, 'w')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            file.write(str(matrix[i][j]) + ' ')
        file.write('\n')
    file.close()


if __name__ == "__main__":
    matrix = read_matrix(IN_FILE_NAME)  # read data from file
    result = output_matrix(matrix, 4)  # label the matrix
    write_to_file(result, OUT_FILE_NAME)  # write the data to the file

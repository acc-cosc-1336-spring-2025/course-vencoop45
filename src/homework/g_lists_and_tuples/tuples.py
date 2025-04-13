def get_p_distance(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Input lists must have equal length")
    differences = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            differences += 1
    return differences / len(list1)

def get_p_distance_matrix(list_of_lists):
    n = len(list_of_lists)
    distance_matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = get_p_distance(list_of_lists[i], list_of_lists[j])
    return distance_matrix
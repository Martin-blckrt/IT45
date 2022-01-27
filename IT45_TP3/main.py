from math import sqrt

NBR_TOWNS = 6

dist = [[0 for j in range(NBR_TOWNS)] for i in range(NBR_TOWNS)]

starting_town = [0 for k in range(NBR_TOWNS)]
ending_town = [0 for p in range(NBR_TOWNS)]

best_solution = [0 for u in range(NBR_TOWNS)]
best_eval = -1.0

"""
Berlin52 :
    6 towns : Best solution (2315.15): 0 1 2 3 5 4
    10 towns : Best solution (2826.50): 0 1 6 2 7 8 9 3 5 4
"""
coord = [[565, 575], [25, 185], [345, 750], [945, 685], [845, 655], [880, 660]]


def print_matrix(mat):
    """ Print a matrix """
    for i, sub_list in enumerate(mat):
        print(i, " : ", end="")
        for elem in sub_list:
            print(elem, end="     ")
        print("")


def print_solution(sol, eval):
    print(f"({eval})")
    for i in range(NBR_TOWNS):
        print(f"{sol[i]}")


def evaluation_solution(sol):
    eval = 0
    for i in range(NBR_TOWNS - 1):
        eval += dist[sol[i]][sol[i + 1]]

    eval += dist[sol[NBR_TOWNS - 1]][sol[0]]

    return eval


def build_nearest_neighbour():
    global best_eval
    global best_solution
    sol = []
    temp = [9999 for _ in range(NBR_TOWNS)]
    sol.append(0)
    eval = next_ville = 0

    for _ in range(NBR_TOWNS - 1):
        temp = [9999 for _ in range(NBR_TOWNS)]
        for i in range(NBR_TOWNS):
            if i not in sol:
                temp[i] = dist[next_ville][i]

        min_index = temp.index(min(temp))
        if min_index not in sol:
            next_ville = min_index  # retrieves the index of the minimal value encountered
            sol.append(next_ville)

    eval = evaluation_solution(sol)
    print("Nearest neighbour ")
    print_solution(sol, eval)
    best_solution = sol
    print(best_solution)
    best_eval = eval


def build_solution():
    global best_eval
    indice_cour, ville_cour, solution = 0, 0, [0 for j in range(NBR_TOWNS)]

    while indice_cour < NBR_TOWNS:
        solution[indice_cour] = ville_cour

        # Test si le cycle est hamiltonien
        for i in range(indice_cour):
            if solution[i] == ville_cour:
                print("cycle non hamiltonien")
                return

        # Recherche de la ville suivante
        trouve, k = False, 0

        while (not trouve) and k < NBR_TOWNS:
            if starting_town[k] == ville_cour:
                trouve = True
                ville_cour = ending_town[k]
            k += 1
        indice_cour += 1

    eval = evaluation_solution(solution)

    if best_eval < 0 or eval < best_eval:
        best_eval = eval
        for t in range(NBR_TOWNS):
            best_solution[t] = solution[t]
        print("New best solution")
        print_solution(solution, best_solution)


def little_algorithm(d0, iteration, eval_node_parent):
    if iteration == NBR_TOWNS:
        build_solution()
        return

    d = d0.deepcopy  # we do the modifications on a copy of the distance matrix
    eval_nod_child = eval_node_parent
    """
     * substract the min of the rows and the min of the columns
     * and update the evaluation of the current node
     *  TO COMPLETE
     *  ...
     *  ...
     */
    """
    if 0 <= best_eval <= eval_nod_child:
        return

    """
     *  Compute the penalities to identify the zero with max penalty
     *  If no zero in the matrix, then return, solution infeasible
     *  TO COMPLETE
     *  ...
     *  ...
    /* row and column of the zero with the max penalty */
    """
    izero, jzero = -1, -1  # Row and column of the zero with the max penalty

    """
     *  Store the row and column of the zero with max penalty in
     *  starting_town and ending_town
     *  TO COMPLETE
    """
    d2 = d.deepcopy  # Do the modifications on a copy of the distance matrix
    """
     *  Modify the matrix d2 according to the choice of the zero with the max penalty
     *  TO COMPLETE
     *  ...
     *  ...
    """

    little_algorithm(d2, iteration + 1, eval_nod_child)  # Explore left child node according to given choice
    d2 = d.deepcopy  # Do the modifications on a copy of the distance matrix

    """
     *  Modify the dist matrix to explore the other possibility : the non-choice
     *  of the zero with the max penalty
     *  TO COMPLETE
     *  ...
     *  ...
    """
    little_algorithm(d2, iteration, eval_nod_child)  # Explore right child node according to non-choice


if __name__ == '__main__':
    best_eval = -1
    print("Points coordinates:")
    for i in range(NBR_TOWNS):
        print(f"Node {i}: x={coord[i][0]}, y={coord[i][1]}")

    # Calcul de la matrice des distances
    for j in range(NBR_TOWNS):
        for k in range(NBR_TOWNS):
            if j != k:
                dist[j][k] = round(sqrt(pow(coord[j][0] - coord[k][0], 2) + pow(coord[j][1] - coord[k][1], 2)), 2)
            else:
                dist[j][k] = -1.000

    print("Distance Matrix:")
    print_matrix(dist)

    build_nearest_neighbour()

    """
    iteration = 0
    lowerbound = 0.0
    little_algorithm(dist, iteration, lowerbound)

    print("Best solution")
    print_solution(best_solution, best_eval)
    """

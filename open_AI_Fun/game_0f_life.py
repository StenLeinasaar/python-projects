
def visualize_tsp(points, path):
    """
    Visualize traveling salesmen problem
    :param points: list of points
    :param path: list of indices of points in the path
    :return: None
    """
    plt.scatter([p[0] for p in points], [p[1] for p in points])
    for i in range(len(path)):
        plt.plot([points[path[i - 1]][0], points[path[i]][0]], [points[path[i - 1]][1], points[path[i]][1]], 'r-')
    plt.show()


"""
2. Visualize traveling salesmen problem with simulated annealing
"""


def visualize_tsp_sa(points, path, best_path, best_cost, costs):
    """
    Visualize traveling salesmen problem with simulated annealing
    :param points: list of points
    :param path: list of indices of points in the path
    :param best_path: list of indices of points in the best path
    :param best_cost: cost of the best path
    :param costs: list of costs of paths at each iteration
    :return: None
    """
    plt.subplot(2, 1, 1)
    plt.scatter([p[0] for p in points], [p[1] for p in points])
    for i in range(len(path)):
        plt.plot([points[path[i - 1]][0], points[path[i]][0]], [points[path[i - 1]][1], points[path[i]][1]], 'r-')

    plt.subplot(2, 1, 2)
    plt.plot(costs)

    plt.show()


"""
3. Visualize traveling salesmen problem with genetic algorithm
"""


def visualize_tsp_ga(points, paths, best_path, best_cost, costs):
    """
    Visualize traveling salesmen problem with genetic algorithm
    :param points: list of points
    :param paths: list of paths (list of indices of points in the path)
    :param best_path: list of indices of points in the best path
    :param best_cost: cost of the best path
    :param costs: list of costs of paths at each iteration
    :return: None
    """
    plt.subplot(2, 1, 1)
    plt.scatter([p[0] for p in points], [p[1] for p in points])

    for i in range(len(paths)):
        path = paths[i]
        for j in range(len(path)):
            plt.plot([points[path[j - 1]][0], points[path[j]][0]], [points[path[j - 1]][1], points[path[j]][1]], 'r-')

    plt.subplot(2, 1, 2)
    plt.plot(costs)

    plt.show()
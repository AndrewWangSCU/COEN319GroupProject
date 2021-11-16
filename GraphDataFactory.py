import numpy as np


def generate_data(verts, edges, distribution="power", save=False):
    if distribution is "uniform":
        data = np.random.randint(0, verts, (edges, 2))
        data = np.unique(data, axis=0)
        i = 0
        while i < len(data):
            indices = np.where(data[i][0] == data[i][1])
            if True in indices:
                data = np.delete(data, indices, axis=0)
                i = 0
            else:
                i += 1
    elif distribution is "power":
        data = np.empty((0, 0))
        for v in np.arange(0, verts):
            num_elts = edges // pow(2, (v + 1))
            if num_elts < 1:
                num_elts = 1
            sources = np.random.randint(0, verts, (num_elts, 1))
            sources = np.delete(sources, np.where(sources == v), axis=0)
            destinations = np.full((len(sources), 1), v)
            new_edges = np.append(sources, destinations, axis=1)
            new_edges = np.unique(new_edges, axis=0)
            if len(data) is 0:
                data = new_edges
            else:
                data = np.append(data, new_edges, axis=0)
    else:
        data = []
    if save:
        filename = distribution + "-" + str(verts) + "-" + str(len(data)) + ".edges"
        np.savetxt(filename, data, fmt="%i", delimiter=" ")
    return data


def main():
    # print(generate_data(100, 100, "uniform"))
    print(generate_data(100, 100, save=True))


main()

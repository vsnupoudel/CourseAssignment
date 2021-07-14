import numpy as np

def distances(vector, vectors_train):
    distances = { filename: np.linalg.norm(vector-vec, ord=2) for filename,
                                                             vec in vectors_train.items() }
    #L2( Euclidean distance)
    filename = min(distances, key=distances.get)
    return filename, distances


import numpy as np

def distances(vector, vectors_train):
    armin = np.argmin( list(map(np.linalg.norm, np.array(list(vectors_train.values())) - vector)) )
    return list(vectors_train.keys())[armin]
    # distances = dict( zip(  vectors_train , map(np.linalg.norm, vectors_train.values()) ))
    # return min(distances, key=distances.get)

def distances_old(vector, vectors_train):
    distances = { filename: np.linalg.norm(vector-vec, ord=2) for filename,
                                                             vec in vectors_train.items() }
    return min(distances, key=distances.get)


if __name__ == "__main__":
    import json
    import numpy as np
    from doc2vec import  LoadedModel
    from ocrfunction import  *
    TRAINED_EMBEDDINGS = 'vectors_train_500_4.json'
    TRAINED_MODEL = 'doc2vec_model_500_4'

    with open(TRAINED_EMBEDDINGS) as json_file:
        vectors_train = json.load(json_file)

    for i,j in enumerate( vectors_train.values()):
        if i == 6:
            vec = np.array(j)

    print(vec.shape)
    print('=============================================')
    print( np.array( list(vectors_train.values())).shape )
    # Method 1
    print(distances(vec, vectors_train))
    # This was used
    # ag= np.argmin( list( map(np.linalg.norm, np.array( list(vectors_train.values()))-vec )))
    #
    # for i in map(np.linalg.norm, np.array( list(vectors_train.values()))-vec ):
    #     print(i)
    # print('####################### The minimum distance index ')
    # print(ag)

    # print( list(vectors_train.keys())[ag])




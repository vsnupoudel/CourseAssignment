import numpy as np

def distances(vector, vectors_train):
    # distances = { filename: np.linalg.norm(vector-vec, ord=2) for filename,
    #                                                          vec in vectors_train.items() }
    amin = np.argmin(map(np.linalg.norm, np.array(list(vectors_train.values())) - vector))

    #L2( Euclidean distance)
    # filename = min(distances, key=distances.get)
    return list(vectors_train.keys())[amin]
    # return filename

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
        if i == 0:
            vec = np.array(j)

    print(vec.shape)
    print('=============================================')
    print( np.array( list(vectors_train.values())).shape )

    ag= np.argmin( map(np.linalg.norm, np.array( list(vectors_train.values()))-vec ))

    print( list(vectors_train.keys())[ag])

    # lm = LoadedModel(TRAINED_MODEL)  # read model, can be multiple(ensemble) models here later
    # emb = lm.input_image_embedding('')  # infer its embedding vector or length 500
    # filename, dist_vec = distances(emb, vectors_train)  # calculate distance
    # os.remove(input_filepath)  # remove the file from application
    # return filename, dist_vec



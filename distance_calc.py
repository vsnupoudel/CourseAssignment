import numpy as np
import json
from doc2vec import LoadedModel

with open('vectors_train_500_4.json') as json_file:
    vectors_train = json.load(json_file)

def distances(vector):
    distances = { filename:np.linalg.norm(vector-vec, ord=2) for filename,
                                                             vec in vectors_train.items() }
    #L2( Euclidean distance)
    filename = min(distances, key=distances.get)
    return filename, distances

if __name__=="__main__":
    p=r'.\document-000-113188.in.000.png'
    lm = LoadedModel('doc2vec_model_500_4')
    emb = lm.input_image_embedding(p)
    # print(emb)
    f,d = distances(emb)
    print(f, '\n\n')
    for i, c in d.items():
        print(i,' : ', c)
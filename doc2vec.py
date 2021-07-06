from gensim.models.doc2vec import Doc2Vec  #, TaggedDocument
import json
from ocrfunction import ocr_space

class LoadedModel():
    def __init__(self):
        self.loaded_model = Doc2Vec.load('doc2vec_model.h5')
    #
    def input_image_embedding(self, picture_path, scanned_fileName= 'scanned_file' ):
        json_output = json.loads( ocr_space(picture_path, overlay= False) )
        document = json_output['ParsedResults'][0]['ParsedText']
        document = document.replace('/r/n','')
        with open(scanned_fileName+'.txt', "w") as text_file:  #Not stored in database
            text_file.write(document)
        return self.loaded_model.infer_vector(scanned_fileName+'.txt')

if __name__== "__main__":
    import gensim
    print(gensim.__version__)
    loaded_model = Doc2Vec.load('doc2vec_model.h5')
    emb = loaded_model.infer_vector(doc_words= ['This','shit','is','crazy'] )
    print(emb)
    # p=r'C:\Users\admin\Downloads\Compressed\Document_Dataset\inputs\document-016-122390.in.000.png'
    # lm = LoadedModel()
    # emb = lm.input_image_embedding(p)
    # print(emb)

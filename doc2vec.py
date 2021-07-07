from gensim.models.doc2vec import Doc2Vec  #, TaggedDocument
import json
from ocrfunction import ocr_space
import regex as re

class LoadedModel():
    def __init__(self, loaded_model):
        self.loaded_model = Doc2Vec.load(loaded_model) #hardcoded for now
    #
    def input_image_embedding(self, picture_path, scanned_fileName= 'scanned_file' ):
        json_output = json.loads( ocr_space(picture_path, overlay= False) )
        document = json_output['ParsedResults'][0]['ParsedText'] #.lower()
        # list_doc = re.sub(r'\W+', ' ', document) # remove non words
        # list_doc = ''.join(i for i in list_doc if ord(i) < 128) # remove non ASCII
        # list_doc = re.sub(r'[0-9]+', '', list_doc ) #remove numbers
        list_doc = document.split(' ')
        # list_doc =  re.sub(r'\W+', ' ', document).split()
        # print(list_doc)
        # print(type(list_doc))
        with open('scanned_file.txt', "w") as text_file:  #Not stored in database
            text_file.write(document)
        # emb =  self.loaded_model.infer_vector()
        emb_file = self.loaded_model.infer_vector(doc_words = list_doc )
        return emb_file


if __name__== "__main__":
    p=r'C:\Users\admin\Downloads\Compressed\Document_Dataset\inputs\document-016-122390.in.000.png'
    lm = LoadedModel('doc2vec_model')
    emb = lm.input_image_embedding(p)
    print(emb)


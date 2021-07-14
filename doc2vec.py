from gensim.models.doc2vec import Doc2Vec  #, TaggedDocument
import json
from ocrfunction import ocr_space
import regex as re
import os

class LoadedModel():
    def __init__(self, loaded_model):
        self.loaded_model = Doc2Vec.load(loaded_model) #hardcoded for now

    def input_image_embedding(self, picture_path ):
        return self.loaded_model.infer_vector(doc_words =
                                                  json.loads(
                                                      ocr_space(picture_path, overlay=False))[
                                                      'ParsedResults'][0][
                                                      'ParsedText'].split(' ') )
from flask import Flask, render_template, request
from doc2vec import LoadedModel  # to load model
from distance_calc import * # distances
import os, json
TRAINED_EMBEDDINGS = 'vectors_train_500_4.json'
TRAINED_MODEL = 'doc2vec_model_500_4'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '.'
app.config['MAX_CONTENT_PATH'] = 1024*1024*25
with open(TRAINED_EMBEDDINGS) as json_file:
    vectors_train = json.load(json_file)

def similar_file(input_filepath):
    lm = LoadedModel(TRAINED_MODEL)  #read model, can be multiple(ensemble) models here later
    emb = lm.input_image_embedding(input_filepath) # infer its embedding vector or length 500
    sims = lm.dv.most_similar([emb], topn=len(lm.dv))
    return sims[0]
    # return distances(emb, vectors_train) # calculate distance

    # return filename

def clean_up_input_files(input_filepath):
    try:
        os.remove(input_filepath)  # remove the file from application
    except Exception as e:
        print('Error while deleting: ', e)
    # else:
    #     print('Input files deleted successfully')

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/output', methods=['GET','POST'])
def output():
    if request.method == 'POST':
        f = request.files['file']
        #f.save(f.filename)
        try:
            tem_file = similar_file(f.filename)
            out_json = {'input_filename': f.filename,
                        'output_filename': tem_file}
            clean_up_input_files(f.filename)
        except Exception as er:
            return render_template('output.html', data=[er])
        else:
            return render_template('output.html', data=[out_json])


if __name__ == '__main__':
    app.run(host='0.0.0.0')

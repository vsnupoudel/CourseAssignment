from flask import Flask, render_template, request
from doc2vec import LoadedModel  # to load model
from distance_calc import * # distances
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '.'
app.config['MAX_CONTENT_PATH'] = 1024*1024*25

def similar_file(input_filepath):
    lm = LoadedModel('doc2vec_model_500_4')
    emb = lm.input_image_embedding(input_filepath)
    filename, dist_vec = distances(emb)
    os.remove(input_filepath) #remove the file from application
    return filename

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/output', methods=['GET','POST'])
def output():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        try:
            tem_file = similar_file(f.filename)
            out_json = {'input_filename': f.filename,
                        'output_filenme': tem_file}
        except Exception as er:
            message = er
            return render_template('output.html', data=[message])
        else:
            return render_template('output.html', data=[out_json])


if __name__ == '__main__':
    app.run(host='0.0.0.0')

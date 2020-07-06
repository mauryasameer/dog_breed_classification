from fastai.vision import load_learner
from fastai.vision import open_image
import json
from io import BytesIO
from flask import Flask, render_template, request, send_file
import base64

app = Flask(__name__,template_folder='.')

def load_model():
    learn = load_learner('model/')
    return learn
def get_class():
    with open('classes.json') as classes:
        categories = json.load(classes)
    categories = json.loads(categories)
    return categories
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET','POST'])
def analyze():
    # print(request.files['file'].read())
    # print(request.files
    image_data = request.files
    image_bytes = image_data['file'].read()
    image = open_image(BytesIO(image_bytes))
    predict = get_class()[f'{load_model().predict(image)[1].item()}']
    # print(predict)
    # [load_model().predict(image)[1].item()] 
    # print(get_class()[load_model().predict(image)[1].item())
    return {'result':f'{predict}'}


if __name__ == "__main__":
    app.run(debug=True)
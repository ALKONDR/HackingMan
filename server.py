from flask import Flask
from flask import request
import json
import gensim

app = Flask(__name__)

goods = {}
model = []

@app.route("/api/recommend", methods=['POST'])
def main():
    predictions = model.most_similar(json.loads(request.data)['values'])

    response = {
        'predictions': []
    }

    for prediction in predictions:
        response['predictions'].append(goods[prediction[0]])

    return json.dumps(response, ensure_ascii=False).encode('utf8')

if __name__ == "__main__":
    with open('goods.json', 'r') as f:
        goods = json.load(f)

    model = gensim.models.KeyedVectors.load_word2vec_format('goods.model.bin', binary=True)

    app.run(port=8080)
from gensim.models import KeyedVectors
import string
from flask import Flask, jsonify, request
import boto3

consumer_key = 'XXXXXXX'
consumer_secret ='XXXXXXX'
access_token = 'XXXXXXX'
access_token_secret = 'XXXXXXX'

delivery_stream = 'kohotext'

app = Flask(__name__)

word_vectors = KeyedVectors.load_word2vec_format('lexvec.enwiki+newscrawl.300d.W.pos.vectors', binary=False)

table = str.maketrans(dict.fromkeys(string.punctuation))

@app.route('/api', methods=['GET'])

def api():
    if not request.json:
        return jsonify({'error': 'no request received'})
    text = preprocess_text(request.json)
    text_raw = ' '.join(text)+'\n'
    client.put_record(
                    DeliveryStreamName=delivery_stream,
                    Record={
                    'Data': text_raw
                    }
                )
    response = dict(word_vectors.most_similar(text))

    return jsonify(response)

def preprocess_text(request_dict):
    text = request_dict.get('text')
    text = text.translate(table)
    text = text.replace('\n',' ')
    text = text.split()
    text = [i.lower() for i in text]
    return text

if __name__ == '__main__':
    client = boto3.client('firehose', 
                          region_name='us-east-1',
                          aws_access_key_id='XXXXXXX',
                          aws_secret_access_key='XXXXXXX' 
                          )
    app.run(host='0.0.0.0', port=5000, debug=True)
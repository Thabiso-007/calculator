from flask import Flask, jsonify, request
import pickle
from flask_cors import CORS, cross_origin
 
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


model = pickle.load(open('wine_model.pickle', 'rb'))

 
@app.route('/')
@cross_origin()
def hello():
    return 'Hello, World!'

@app.route('/wine', methods=["GET"])
def predictionWine():
    try:
        if request.method == 'GET':
            alcohol = float(request.args.get('alcohol'))
            malic_acid = float(request.args.get('malic_acid'))
            ash = float(request.args.get('ash'))
            alcalinity = float(request.args.get('alcalinity_of_ash'))
            magnesium = float(request.args.get('magnesium'))
            phenos = float(request.args.get('total_phenos'))
            flavanoids = float(request.args.get('flavanoids'))
            nonflavanoid = float(request.args.get('nonflavanoid_phenols'))
            proanthocyanins = float(request.args.get('proanthocyanins'))
            intensity = float(request.args.get('color_intensity'))
            hue = float(request.args.get('hue'))
            od315 = float(request.args.get('od315_of_diluted_wines'))
            proline = float(request.args.get('proline'))

            final_features = ([[alcohol, malic_acid, ash, alcalinity, magnesium, phenos, flavanoids, nonflavanoid, proanthocyanins, intensity, hue, od315, proline]])

            prediction = model.predict(final_features)
        
        return jsonify(str(prediction[0]))
    except:
        print('Something went wrong.')
 
if __name__ == '__main__':
    app.run()
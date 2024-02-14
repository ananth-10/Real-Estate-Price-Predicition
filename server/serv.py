from flask import Flask, request, jsonify
from flask_cors import CORS
import loader

app = Flask(__name__)
CORS(app)

@app.route("/get_loc")
def get_loc():
	loader.load_files_inloc()

	response = jsonify({
		"locations": loader.get_loc()
	})
	response.headers.add("Access-Control-Allow-Origin", "*")
	
	return response

@app.route("/predict_home_price", methods=["POST"])
def predict_home_price():
	loader.load_files_inloc()
	loader.get_loc()

	location = request.form["location"]
	total_sqft = float(request.form["total_sqft"])
	bedrooms = int(request.form["bedrooms"])
	bath = int(request.form["bath"])

	response = jsonify({
		"estimated_price": loader.get_estimated_price(location, total_sqft, bedrooms, bath)
	})
	response.headers.add("Access-Control-Allow-Origin", "*")

	return response


if __name__ == "__main__":
	print("Starting Python server...")
	app.run()

## What does this repository contain?
This repository contains a code to:
	1- Make an ML model on a currency dataset from Kaggle
	2- Saving the ML model as pickle.
	3- Using ML model with a simple Flask service.
	4- Using flasgger to use the Flask API and produce a good UI for the user.


## How to use this repository?
After installing the requirements, simply prepare your own model from "random_ml.py"
or you may simply try running flask_simple.py / flask_webapp.py with the existing model.

PS- I am pushing in model and test files so you can see the results easily.

Please check Output images for more clarity.

## Docker
You may use the dockerfile.
Simply build a docker image using:
	docker build -t <name of img> .

After that, run the image:
	docker run -p 8000:8000 <name of img>

Finally check your results on:
	http://0.0.0.0:8000/apidocs


## References:
A big thanks to Krish Naik and his youtube videos.
Dataset: Kaggle

![alt text](https://github.com/shivekchhabra/Flask-API/blob/master/Outputs/flask-api.png)

![alt text](https://github.com/shivekchhabra/Flask-API/blob/master/Outputs/postman.png)

![alt text](https://github.com/shivekchhabra/Flask-API/blob/master/Outputs/flasgger1.png)

![alt text](https://github.com/shivekchhabra/Flask-API/blob/master/Outputs/flasgger2.png)


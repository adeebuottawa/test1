# This contains the code as well as the index for the api

# 1. Importing Necessary modules
import pickle
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from heartdiseasedata import patientData
app = FastAPI()
pickle_in = open("mlmodel.pkl", "rb")
classifier = pickle.load(pickle_in)
# Add CORS middleware
# Allow requests from any origin


origins = ["http://localhost", "http://localhost:8080", "https://myapp.herokuapp.com", "http://localhost:5000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 2. Declaring our FastAPI instance/ Create the app object



# 3. Defining path operation for root endpoint. Opens at http://127.0.0.1:8000/
@app.get('/')
def main():
    return {'message': 'Welcome to our Project!'}


# 4. Defining path operation for /name endpoint. Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def hello_name(name: str):
    # Defining a function that takes only string as input and output the
    # following message.
    return {'message': f'Welcome to our Project!, {name}'}


# 5. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted diagnosis with the confidence
@app.post('/predict')
def predict_disease(data: patientData):
    data = data.dict()  # 11 inputs
    age = data['age']
    sex = data['sex']
    cp = data['cp']
    trestbps = data['trestbps']
    chol = data['chol']
    fbs = data['fbs']
    restecg = data['restecg']
    thalach = data['thalach']
    exang = data['exang']
    oldpeak = data['oldpeak']
    slope = data['slope']
    ca = data['ca']
    thal = data['thal']

    # print(random_forest_model.predict([[inputs...]]))
    # the model takes the inputs passed through the api
    prediction: object = classifier.predict([[age, sex,cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak,slope, ca, thal]])

    # If prediction = 0 then patient do not have heart disease and if prediction = 1, patient has heart disease
    if prediction[0] == 1:
        prediction = "Heart Disease"
    else:
        prediction = "No Heart Disease"
    return {
         'prediction': prediction
          #print(prediction) 
     }


# 6. Run the API with uvicorn. Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# To run the API, first change the directory to the current project then use the command,
# uvicorn app:app --reload
# Then use swagger through http://127.0.0.1:8000/docs
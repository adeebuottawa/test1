# File to create a structure for the input to the ML model
# This way the attributes of the class patientData can be used as features of the data.

from pydantic import BaseModel


# Class which describes patient data measurements
# Contains 11 attibutes/inputs
class patientData(BaseModel):
    age: int
    sex: int
    cp:int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int
    

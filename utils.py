import pickle
import json
import pandas as pd
import numpy as np
#import config


class Premium_price(): 
    def __init__(self, Age, Diabetes, BloodPressureProblems, AnyTransplants, AnyChronicDiseases, Height, Weight, KnownAllergies, HistoryOfCancerInFamily, NumberOfMajorSurgeries):
        
        self.Age = Age 
        self.Diabetes = Diabetes 
        self.BloodPressureProblems = BloodPressureProblems 
        self.AnyTransplants = AnyTransplants 
        self.AnyChronicDiseases = AnyChronicDiseases 
        self.Height = Height
        self.Weight = Weight
        self.KnownAllergies = KnownAllergies
        self.HistoryOfCancerInFamily = HistoryOfCancerInFamily
        self.NumberOfMajorSurgeries = NumberOfMajorSurgeries
   

    def load_model(self):
        # with open(config.MODEL_FILE_PATH, "rb") as f:
        with open("best_model.pkl", "rb") as f:

            self.model = pickle.load(f)

        #with open(config.JSON_FILE_PATH, "r") as f:
        with open("project_data.json") as f:

            self.json_data = json.load(f)

    def get_prediction(self):

        self.load_model() # We have to call method >> load_model >> so that we can use their instance variables
        

        array = np.zeros(len(self.json_data["columns"]))
        array[0]=self.Age
        array[1]=self.Diabetes
        array[2]=self.BloodPressureProblems
        array[3]=self.AnyTransplants
        array[4]=self.AnyChronicDiseases
        array[5]=self.Height
        array[6]=self.Weight
        array[7]=self.KnownAllergies
        array[8]=self.HistoryOfCancerInFamily
        array[9]=self.NumberOfMajorSurgeries
    
        predicted_premium = self.model.predict([array])[0]
        return 'Premium_price of Insurance is:',round(predicted_premium,2)
       


if __name__ == "__main__":
    Age = 55
    Diabetes = 0
    BloodPressureProblems = 1
    AnyTransplants = 0
    AnyChronicDiseases = 0
    Height = 160
    Weight = 60
    KnownAllergies = 0
    HistoryOfCancerInFamily = 0
    NumberOfMajorSurgeries = 1

    obj = Premium_price(Age, Diabetes, BloodPressureProblems, AnyTransplants, AnyChronicDiseases, Height, Weight, KnownAllergies, HistoryOfCancerInFamily, NumberOfMajorSurgeries)
    premium = obj.get_prediction()
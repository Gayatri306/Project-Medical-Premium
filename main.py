from flask import Flask ,jsonify,render_template,request
from utils import Premium_price
import config

app = Flask(__name__)


@app.route("/")
def welcome():
    print("Welcome to the Medica insurance premium prediction")
    return render_template("index.html")

@app.route("/MedicalInsurance")
def predicted_class():
        if request.method == "GET":
            print("We are using GET Method")
            #print("Printing Data here :",request.form)
    
    
            # data = request.form
        
            Age = eval(request.args.get("Age"))
            Diabetes = eval(request.args.get("Diabetes"))
            BloodPressureProblems = eval(request.args.get("BloodPressureProblems"))
            AnyTransplants = eval(request.args.get("AnyTransplants"))
            AnyChronicDiseases = eval(request.args.get("AnyChronicDiseases"))
            Height = eval(request.args.get("Height"))
            Weight = eval(request.args.get("Weight"))
            KnownAllergies = eval(request.args.get("KnownAllergies"))
            HistoryOfCancerInFamily = eval(request.args.get("HistoryOfCancerInFamily"))
            NumberOfMajorSurgeries = eval(request.args.get("NumberOfMajorSurgeries"))
            
           
            col = Premium_price(Age, Diabetes, BloodPressureProblems, AnyTransplants, AnyChronicDiseases, Height, Weight, KnownAllergies, HistoryOfCancerInFamily, NumberOfMajorSurgeries)
            pred = col.get_prediction()
            return render_template("index.html", prediction = pred)
            

        else:
            print("We are using POST Method")

            Age = eval(request.form.get("Age"))
            Diabetes = eval(request.form.get("Diabetes"))
            BloodPressureProblems = eval(request.form.get("BloodPressureProblems"))
            AnyTransplants = eval(request.form.get("AnyTransplants"))
            AnyChronicDiseases = eval(request.form.get("AnyChronicDiseases"))
            Height = eval(request.form.get("Height"))
            Weight = eval(request.form.get("Weight"))
            KnownAllergies = eval(request.form.get("KnownAllergies"))
            HistoryOfCancerInFamily = eval(request.form.get("HistoryOfCancerInFamily"))
            NumberOfMajorSurgeries = eval(request.form.get("NumberOfMajorSurgeries"))


            col = Premium_price(Age, Diabetes, BloodPressureProblems, AnyTransplants, AnyChronicDiseases, Height, Weight, KnownAllergies, HistoryOfCancerInFamily, NumberOfMajorSurgeries)
            pred = col.get_prediction()
            return render_template("index.html", prediction = pred)
      

    

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=config.PORT_NUMBER, debug=True)
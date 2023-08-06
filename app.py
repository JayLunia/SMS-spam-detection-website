from flask import Flask , render_template,request , jsonify, request
from preprocessing import transform_text
import pickle
app = Flask(__name__)


model= pickle.load(open('sms_model.pkl', 'rb'))

@app.route("/")
def index():
    return render_template('index.html',title='SMS Spam Checker')

@app.route("/pred",methods=['POST'])
def pred():
    if request.method == 'POST':
        text=request.form['txt']
        print(text)
        txt=transform_text(text)
        print(txt)
        ans=model.predict([txt])
        if(ans==0):
            return  jsonify('ham')
        else:
            return jsonify('spam')



if __name__=="__main__":
    app.run()
# D:\flask api\sms spam\__pycache__
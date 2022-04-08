from flask import Flask, render_template
app = Flask(__name__)

@app.route('/Air_Pollution.html', methods=['GET', 'POST'])
def homepage():
    return render_template('Air_Pollution.html')

@app.route('/Air_Pollution_Data.html', methods=['GET', 'POST'])
def data():
    return render_template('Air_Pollution_Data.html')

@app.route('/Air_Pollution_FillData.html', methods=['GET', 'POST'])
def filldata():
    return render_template('Air_Pollution_FillData.html')

@app.route('/Air_Pollution_Prediction.html', methods=['GET', 'POST'])
def prediction():
    return render_template('Air_Pollution_Prediction.html')

@app.route('/Air_Pollution_About_Us.html', methods=['GET', 'POST'])
def aboutus():
    return render_template('Air_Pollution_About_Us.html')

if __name__ == "__main__":
    app.run(debug = True)
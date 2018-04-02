from flask import Flask,request,render_template
import unicodedata
import pandas as pd
from  recommendProducts import userRecommendations


app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('homepage.html')

@app.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    if request.method == 'POST':

        ItemId = request.form['ItemId']
        df_recommendations=userRecommendations(int(ItemId))
        final_dataframe=df_recommendations[['item2','score']]
        return render_template('analysis.html', tables=[final_dataframe.to_html(classes='final_dataframe')])



if __name__ == "__main__":
   app.run(debug = True)
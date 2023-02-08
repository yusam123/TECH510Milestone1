from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

users = []
number = 1
@app.route("/")
def index():
    global number 
    number = 1
    return render_template("index.html", number=number)

@app.route('/submit', methods=['POST'])
def get_post():
    global users
    global number
    ans_from_users = []
    if request.method == "POST":
        number += 1
        ans_from_users.append(request.form['color'])
        ans_from_users.append(request.form['age'])
        ans_from_users.append(request.form['time'])
        users.append(ans_from_users)
        if number>3:
            number = 1
            draw(users)
            users = []
            #return df.to_html()
            return render_template("analysis.html")
    return render_template("index.html", number=number)

@app.route('/back', methods=['POST'])
def back():
    global number
    number = 1
    return render_template("index.html", number=number)


def draw(users):
    df = pd.DataFrame(users,columns=['color','age','time'])
    color=df.groupby('color').size()
    avg_time = df['time'].astype(int).sum()/len(df)
    time = df['time'].astype(int)
    avg_age = df['age'].astype(int).sum()/len(df)
    age = df['age'].astype(int)

    plt.figure()
    plt.subplot(131)
    plt.bar(time.index, height=time)
    plt.axhline(y = avg_time, color = 'r', linestyle = '-')
    plt.text(0,avg_time,"average get up time "+str(round(avg_time)))
    plt.subplot(132)
    plt.pie(color,labels = color.index)
    plt.subplot(133)
    plt.bar(age.index, height=age)
    plt.axhline(y = avg_age, color = 'r', linestyle = '-')
    plt.text(0,avg_age,"average age "+str(round(avg_age)))
    plt.savefig('./static/image/plot.png')
if __name__ == "__main__":
    app.run(debug=True)
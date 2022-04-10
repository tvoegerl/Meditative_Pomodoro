from flask import Flask, render_template, url_for, request
import time

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    time_wanted = 0
    if request.method == 'POST':
        time_wanted = request.form.get("times")
        sessions_wanted = request.form.get("sessions")
        break_activity = request.form.get("break")
        return "time wanted: " + time_wanted + ", sessions: " + sessions_wanted + ", activity: " + break_activity
    else:
        return render_template('index.html')
    #time_secs = int(time_wanted) * 60
    #for i in range(0, time_secs):
    #    mins = (time_secs-i)//60
    #    secs = (time_secs-i)%60
    #    return str(mins) + ":" + str(secs)
    #    time.sleep(1)
    


if __name__ == "__main__":
    app.run(use_reloader= True, debug = True)
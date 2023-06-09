from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [{
  "id": 1,
  "title": "Data Analyst",
  "location": "Galle",
  "salary": "Rs. 100,000"
}, {
  "id": 2,
  "title": "Data Scienetist",
  "location": "Colombp",
  "salary": "Rs. 200,000"
}, {
  "id": 1,
  "title": "Frontend Engineer",
  "location": "remote",
  "salary": "Rs. 100,000"
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=jobs)


@app.route("/jobs")
def list_jobs():
  return jsonify(jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

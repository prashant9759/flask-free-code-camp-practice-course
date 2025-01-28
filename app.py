from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

jobs = [{
    "id": 1,
    "title": "Data Analyst",
    "location": "Bengaluru, India",
    "salary": "Rs. 10,00,000"
}, {
    "id": 2,
    "title": "Data Scientist",
    "location": "Delhi, India",
    "salary": "Rs. 15,00,000"
}, {
    "id": 3,
    "title": "Frontend Engineer",
    "location": "San Francisco, USA",
    "salary": "$120,000"
}, {
    "id": 4,
    "title": "Backend Engineer",
    "location": "San Francisco, USA",
    "salary": "$140,000"
}, {
    "id": 5,
    "title": "Software Engineer",
    "location": "San Francisco, USA",
    "salary": "$150,000"
}]


@app.route("/api/jobs")
def list_jobs():
  return jsonify(jobs)


@app.route("/")
def hello():
  return render_template("home.html")


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)

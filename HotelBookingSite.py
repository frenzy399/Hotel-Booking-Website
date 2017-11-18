from flask import Flask, render_template, request
import csv
from datetime import datetime

app = Flask(__name__)
#http://127.0.0.1:5000/

def readCSV(csvFile,):
    with open(csvFile, 'r') as fileToRead:
        fileReader = csv.reader(fileToRead)
        fileContent = [row for row in fileReader]
        return fileContent

def writeCSV(csvFile, contentToWrite):
    with open(csvFile, 'w', newline='') as fileToWrite:
        fileWriter = csv.writer(fileToWrite)
        fileWriter.writerows(contentToWrite)


@app.route("/", methods=["GET"])
def goHome():
    reviewList = readCSV('static\\reviews.csv')
    return render_template("home.html", reviewList = reviewList)

@app.route("/addReview", methods=["POST"])
def addReview():
    reviewFilepath = "static\\reviews.csv"
    reviewList = readCSV(reviewFilepath)
    newReviewName = request.form[("newReviewName")]
    newReviewTitle = request.form[("newReviewTitle")]
    now = datetime.now()
    newReviewTime = str(now.day) + "/" + str(now.month) + "/" + str(now.year) + " at " + str(now.hour) + ":" + str(now.minute)
    newReviewContent = request.form[("newReviewContent")]
    reviewList.append([newReviewTitle, newReviewName, newReviewTime, newReviewContent])
    writeCSV(reviewFilepath, reviewList)
    return render_template("home.html", reviewList = reviewList)

@app.route("/localAttractions", methods=["GET"])
def goLocalAttractions():
    return render_template("localAttractions.html", localAttractionsList = localAttractionsList)


if __name__ == '__main__':
    app.run(debug = True)
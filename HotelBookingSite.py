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
    newReviewUser = request.form[("newReviewUser")]
    ####HOW TO SPLIT DATETIME INTO DATE AND TIME
    #dateWtime = datetime.now()
    #date, time = dateWtime.split(" ")
    #newReviewTime = str(day) + "/" + str(month) + "/" + str(year) + " - " + str(hour) + ":" + str(minute) + ":" + str(second) + " - " + str(tzinfo)
    newReviewTime = datetime.now()
    newReviewContent = request.form[("newReviewContent")]
    reviewList.append([newReviewUser, newReviewTime, newReviewContent])
    writeCSV(reviewFilepath, reviewList)
    return render_template("home.html", reviewList = reviewList)

@app.route("/localAttractions", methods=["GET"])
def goLocalAttractions():
    return render_template("localAttractions.html", localAttractionsList = localAttractionsList)


if __name__ == '__main__':
    app.run(debug = True)
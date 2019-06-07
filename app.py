from flask import Flask, render_template, request
#from elasticsearch import Elasticsearch


app = Flask(__name__)
#es = Elasticsearch()



@app.route("/map", methods = ['GET','POST'])
def main():

	
    return render_template('newmapTwo.html')


if __name__ == "__main__":
	app.run()

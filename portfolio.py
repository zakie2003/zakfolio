from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():
    if(request.method=="POST"):
        return render_template("cv.html")    
    return render_template("cv.html")



@app.route("/proj",methods=["POST","GET"])
def proj():
    if(request.method=="POST"):
        return render_template("cv_proj.html")
    return render_template("cv_proj.html")



@app.route("/assign",methods=["GET","POST"])
def assign():
    if(request.method=="POST"):
        return render_template("cv_assign.html")
    return("cv_assign.html")




if __name__=="__main__":
    app.run(debug=True)
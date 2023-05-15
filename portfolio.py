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
    return render_template("cv_assign.html")

@app.route("/assign2",methods=["GET","POST"])
def assign2():
    if(request.method=="POST"):
        return render_template("cv_assign2.html")
    return render_template("cv_assign2.html")

@app.route("/assign3",methods=["GET","POST"])
def assign3():
    if(request.method=="POST"):
        return render_template("cv_assign3.html")
    return render_template("cv_assign3.html")

@app.route("/assign4",methods=["GET","POST"])
def assign4():
    if(request.method=="POST"):
        return render_template("cv_assign4.html")
    return render_template("cv_assign4.html")

@app.route("/assign5",methods=["GET","POST"])
def assign5():
    if(request.method=="POST"):
        return render_template("cv_assign5.html")
    return render_template("cv_assign5.html")




if __name__=="__main__":
    app.run(debug=True)

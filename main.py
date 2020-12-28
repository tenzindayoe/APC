import numpy as np 
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from functions import * 


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///APC.db"
db = SQLAlchemy(app)



@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/calculate",methods = ["GET","POST"])
def _calculate_(): 
    if request.method == "POST" : 
        answer = calculate(request.form["x"])
        return redirect("/show_answer/"+str(answer))
    else : 
        return render_template("calculate.html")

@app.route("/show_answer/<string:answer>")
def _show_answer(answer) :
    return render_template("answer.html", answer = answer)
@app.route("/graph_quadratic_equation",methods=["POST","GET"])
def graph_quadratic_equation():
    if request.method == "POST":
        _x2,_x1,_c,_rmin,_rmax,_step = int(request.form["x2"]),int(request.form["x1"]),int(request.form["c"]),int(request.form["rmin"]),int(request.form["rmax"]),int(request.form["step"])
        img_name = graph_quadratic(_x2,_x1,_c,_rmin,_rmax,_step)
        return redirect("/showgraph/"+img_name)
    else : 
        return render_template("quadratic_graph.html")
@app.route("/graph_linear_equation",methods=["POST","GET"])
def graph_linear():
    if request.method == "POST" : 
        _x1,_y1,_x2,_y2,_c1,_c2 = int(request.form["x1"]),int(request.form["y1"]),int(request.form["x2"]),int(request.form["y2"]),int(request.form["c1"]),int(request.form["c2"])
        img_name_ = graph_linear_equation(_x1,_y1,_x2,_y2,_c1,_c2)
        return redirect("/showgraph_linear/"+img_name_)
    else: 
        return render_template("linear_graph.html")
@app.route("/showgraph/<string:img_name>")
def show_graph(img_name):
    return render_template("showgraph.html",imgname = img_name)
@app.route("/showgraph_linear/<string:img_name>")
def show_graph_linear(img_name):
    return render_template("showgraph_linear.html",imgname = img_name)

@app.route("/sketched_graph/<string:imagenameG>")
def show_sketched_graph(imagenameG): 
    return render_template("spread_sheetgraph.html",img = imagenameG)
    
@app.route("/spreadsheet",methods = ["GET","POST"])
def spreadsheet():
    if request.method == "POST" : 
        x_label,y_label,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10 = request.form["X"],request.form["Y"],request.form["x1"],request.form["y1"],request.form["x2"],request.form["y2"],request.form["x3"],request.form["y3"],request.form["x4"],request.form["y4"],request.form["x5"],request.form["y5"],request.form["x6"],request.form["y6"],request.form["x7"],request.form["y7"],request.form["x8"],request.form["y8"],request.form["x9"],request.form["y9"],request.form["x10"],request.form["y10"]
        X_list = []
        Y_list = []
        for idx in range(10):
            X_list.append(int([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10][idx]))
            Y_list.append(int([y1,y2,y3,y4,y5,y6,y7,y8,y9,y10][idx]))

        img_G = sketch_graph(X_list, Y_list, x_label,y_label)
        return redirect("/sketched_graph/"+img_G)
    else:
        return render_template("spreadsheet.html")
@app.route("/linear_solver",methods = ["GET","POST"])
def Linear_Solver():
    if request.method == "POST":
        x1,y1,x2,y2,c1,c2 = int(request.form["x_1"]),int(request.form["y_1"]),int(request.form["x_2"]),int(request.form["y_2"]),int(request.form["c_1"]),int(request.form["c_2"])
        li = linear_solver_2(x1,y1,x2,y2,c1,c2)
        Solution = " x = "+str(li[0]) + ", y = "+str(li[1])
        return redirect("/show_answer/"+Solution)
    else: 
        return render_template("linear_solver.html") 
    
@app.route("/linear_solver_3",methods = ["GET","POST"])
def Linear_Solver_3():
    if request.method == "POST":
        x1,y1,z1,x2,y2,z2,x3,y3,z3,c1,c2,c3 = int(request.form["x_1"]),int(request.form["y_1"]),int(request.form["z_1"]),int(request.form["x_2"]),int(request.form["y_2"]),int(request.form["z_2"]),int(request.form["x_3"]),int(request.form["y_3"]),int(request.form["z_3"]),int(request.form["c_1"]),int(request.form["c_2"]),int(request.form["c_3"])
        li = linear_solver_3(x1,y1,z1,x2,y2,z2,x3,y3,z3,c1,c2,c3)
        Sol = "x = "+str(li[0])+", y = "+str(li[1])+", z = "+str(li[2])
        return redirect("/show_answer/"+Sol)
    else : 
        return render_template("linear_solver_3.html")
@app.route("/quadratic_solver",methods = ["GET","POST"])
def Q_Solver(): 
    if request.method == "POST":
        a = int(request.form["a"])
        b = int(request.form["b"])
        c = int(request.form["c"])
        solution = quadratic_solver(a,b,c)
        return redirect("/show_answer/"+solution)
    else : 
        return render_template("quadratic_solver.html")
if __name__ == "__main__":
    app.run(debug=True)

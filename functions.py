import numpy as np
from math import * 
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
import string
import random
import matplotlib
import math
matplotlib.use('Agg')
def calculate(x): 
    x = eval(x)
    return x
def linear_solver_2(x1,y1,x2,y2,c1,c2):
    A = np.array([[x1,y1],[x2,y2]])
    B = np.array([c1,c2])
    X = np.linalg.solve(A,B)
    return X
    
def linear_solver_3(x1,y1,z1,x2,y2,z2,x3,y3,z3,c1,c2,c3):
    A = np.array([[x1,y1,z1],[x2,y2,z2],[x3,y3,z3]])
    B = np.array([c1,c2,c3])
    X = np.linalg.solve(A,B)
    return X

def quadratic_solver(a,b,c):
    

    d = b**2-4*a*c # discriminant

    if d < 0:
        return "NO SOLUTION"
    elif d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/2*a
        sol = "This equation has one solutions: "+str(x)
        return sol
    else:
        x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
        x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
        sol = "This equation has two solutions: "+str(x1)+ " or "+str(x2)
        return sol

def graph_quadratic(x2,x1,c,rmin,rmax,step): 
    x = []
    y = []
    x = np.linspace(rmin,rmax,step)
    y = (x2*(x**2))+(x1*x)+c
    fig = plt.figure()
    plt.plot(x,y)
    plt.axvline(x=0,color='gray',linestyle='--')
    plt.axhline(y=0,color='gray',linestyle='--')

    imgname_ = ''.join(random.choice(
        string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    imgname_ +=".jpg"
            
    
    fig.savefig("static/graph_quadratic/"+imgname_)
    return imgname_

def graph_linear_equation(x1,y1,x2,y2,c1,c2): 
    #equation should be of the form x+y=c
    X1 = [] 
    Y1 = [] 
    X2 = []
    Y2= []
    X1 = np.linspace(-100,100,100)
    Y1 = (-(x1*X1)+c1)/y1
    X2 = np.linspace(-100,100,100)
    Y2 = (-(x2*X2)+c2)/y2
    A = np.array([[x1,y1],[x2,y2]])
    B = np.array([c1,c2])
    X = np.linalg.solve(A,B)
    x_intersection = X[0]
    y_intersection = X[1]
    fig = plt.figure()
    plt.plot(X1,Y1,label=str(x1)+"x+"+str(y1)+"y="+str(c1))
    plt.plot(X2,Y2,label=str(x2)+"x+"+str(y2)+"y="+str(c2))
    plt.plot(x_intersection,y_intersection,marker=".",markersize =8)
    plt.axvline(x=0,color='gray',linestyle='--')
    plt.axhline(y=0,color='gray',linestyle='--')
    plt.xlabel("Solution : x="+str(x_intersection)+" , y = "+str(y_intersection))
    plt.title("Equations should be of the form x+y=c")
   
    imgname__ = ''.join(random.choice(
        string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    imgname__ +=".jpg"
            
    
    fig.savefig("static/graph_linear/"+imgname__)
    return imgname__

def sketch_graph(X,Y,xlabel_,ylabel_):
    fig = plt.figure()
    plt.plot(X,Y)
    plt.xlabel(xlabel_)
    plt.ylabel(ylabel_)
    plt.title(xlabel_+" vs "+ylabel_+" graph")
    imgname_G = ''.join(random.choice(
        string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    imgname_G +=".jpg"
            
    
    fig.savefig("static/graphs/"+imgname_G)
    return imgname_G




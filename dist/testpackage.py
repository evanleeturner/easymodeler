import sys
import datetime
import os

sys.path.insert(0, os.path.abspath('EasyModeler'))
import emlib


print emlib.NuN("4.5")

totest = "05/20/2013"
date = emlib.mmddyyyy2date(totest)
print date
print type(date)

def ODE():
    return
print emlib.Model(ODE)



def LV_int(t,initial):
        x = initial[0]
        y = initial[1]
        A = 1
        B = 1
        C = 1
        D = 1

        x_dot = (A * x) - (B * x *y)
        y_dot = (D * x * y) - (C * y) 

        return [x_dot, y_dot]


LV = emlib.Model(LV_int)

LV.Integrate([3,2],maxdt=20)
LV.Draw()
LV.Integrate([3,2],maxdt=20, dt=.01)



LV.Draw()



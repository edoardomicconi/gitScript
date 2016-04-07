from wallCalculation import *


#Definition of the function

def sensitivityMultipleResult(material_List,size_list, T_inside,T_outside):
    resistanceListSeries = [R1,R2,R6]
    resistanceResults={}
    for material in material_List:
        for size in size_list:
            R4={"name":"R4","type":"cond","length":size,"area":0.22,"k":material["k"]}
            resistanceListParallel = [R3,R4,R5]
            heatTransfer = wallHeatTransfer(resistanceListSeries,resistanceListParallel,Ro,Ri, T_inside,T_outside)
            InputString="material= "+ str(material["name"])+ " length= " +str(size)
            resistanceResults[InputString]=heatTransfer
    return resistanceResults
    
    
# Data input

glassProp = {"name":"glass", "k":0.9}
brickProp ={"name":"brick", "k": 0.87}
cementProp ={"name":"cement", "k": 1.5}

Ti=20
To=-10

Ri={"name":"Ri","type":"conv","area":0.25,"hConv":10}
R1={"name":"R1","type":"cond","length":0.03,"area":0.25,"k":0.026}
R2={"name":"R2","type":"cond","length":0.02,"area":0.25,"k":0.22}
R3={"name":"R3","type":"cond","length":0.16,"area":0.015,"k":0.22}
R5={"name":"R5","type":"cond","length":0.16,"area":0.015,"k":0.22}
R6={"name":"R6","type":"cond","length":0.02,"area":0.25,"k":0.22}
Ro={"name":"Ro","type":"conv","area":0.25,"hConv":25}

material_List = [glassProp,brickProp,cementProp]
size_list = [0.2,0.35,0.95]

heatExchange=sensitivityMultipleResult(material_List, size_list, Ti, To)
print heatExchange
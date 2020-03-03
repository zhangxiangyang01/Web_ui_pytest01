import os

def red_login_txt(filename):
    with open(os.getcwd()+os.sep+"Data"+os.sep+filename, "r", encoding="utf-8")as f:
        # print(f.readlines())
        arr=[]
        for i in f.readlines():
            # print(i)
            # print(i.strip())
            # print(i.strip().split(","))
            # print(tuple(i.strip().split(",")))
            arr.append(tuple(i.strip().split(",")))
        return arr
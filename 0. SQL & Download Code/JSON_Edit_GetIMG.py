# Title : JSON_Edit_GetIMG (Open & Read & Edit & Save & get Image Data using urllib)
# Description :
# Original Source : https://engineer-mole.tistory.com/m/195
# Editor : Min-gyu Lee
# Version & Last Update : 18. Oct. 2022.

# 0. Python Library Import
import time
import datetime
import os
from tqdm import tqdm

import pandas as pd
import json
import urllib.request

def main(start, end) :

    # Time Check1
    start_time = time.time()

    # 1. File Path Setting

    # 1-1. Insert File Path & JSON File Name
    JSONFilePath = "D:/3. Research/0. My Project/1. ADML/Datasets/Skyserver_SQL_221018/Skyserver_SQL_221018_GALAXY_334521_080000-100000"
    JSONFileName = "Skyserver_SQL_221018_GALAXY_334521.json"

    JSONPath = JSONFilePath + "/" + JSONFileName


    # 1-2. Print JSON FIle Path & Name
    print("JSON File Path : ",  JSONFilePath)
    print("JSON File Name : ",  JSONFileName, "\n")
    print("JSON Path : " , JSONPath)

    # 2. JSON File Open & Data Load
    with open(JSONPath) as File :
        JSONData = json.load(File)

    # 2-1. Print JSON File Data : [List Index]["Dict Key"]
    print(JSONData[0],"\n")
    print(JSONData[0]["class"],"\n")

    for i in tqdm(range((start-1), (end))) :
        # 2-2. Data Insert : File Name (Format : Class_ObjID.jpg)
        JSONData[i]["FileName"] = str(JSONData[i]["class"]) + "_" + str(JSONData[i]["ObjID"]) + ".jpg"
        print(JSONData[i]["FileName"])  # Print Image Filename

        # 2-3. Data Insert : Image Link (Format : link + ra + dec + link)
        LinkHead = "http://skyserver.sdss.org/dr17/SkyServerWS/ImgCutout/getjpeg?TaskName=Skyserver.Explore.Image&ra="
        LinkTail = "&scale=0.2&width=512&height=512"

        JSONData[i]["Link"] = LinkHead + str(JSONData[i]["ra"]) + "&dec=" + str(JSONData[i]["dec"]) + LinkTail

        print(JSONData[i]["Link"])  # Print Image Link

        
        # 3. IMG Data Download using urllib
        URLLink = str(JSONData[i]["Link"])
        print(i, URLLink)
        URLName = str(JSONData[i]["FileName"])
        print(i, URLName)

        urllib.request.urlretrieve(URLLink, URLName)


    # 3. JSON File Open Write Mode & Data Upload
    with open(JSONPath, 'w', encoding='utf-8') as file:
        json.dump(JSONData, file, indent="\t")


    # Time Check

    end_time = time.time()
    ctime = end_time-start_time
    timelist = str(datetime.timedelta(seconds=ctime)).split(".")

    print("Run Time :  ", timelist)


start = int(input("Enter the starting index of the image >>> "))
end = int(input("Enter the end index of the image >>> "))

main(start, end)
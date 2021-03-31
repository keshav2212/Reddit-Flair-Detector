from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import datetime
import csv
import praw
import joblib
import os
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from django.core.files.storage import FileSystemStorage
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sub_name = ['india']
post_num = 250
reddit = praw.Reddit(
                     client_id='hDIJdjc2k5VzTA',
                     client_secret='fT9JnoUGAUAqDipudbAZ1XgeLFM',
                     username='HelloWorld13211',
                     password='Qwerty@123',
                     user_agent='web scrapper'
                     )
m=joblib.load('category.pkl')
cv=joblib.load("transformer.pkl")
mnb=joblib.load('model.pkl')
def home(request):
    if request.method=="POST":
        url=request.POST['kuchbhi']
        submission = reddit.submission(url=url)
        x=predict(submission.title)
        return render(request,"flair/index.html",{'data':1,'detected':x,'actual':submission.link_flair_text,'title':submission.title})
    return render(request,"flair/index.html",{'data':0})

def predict(title):
    title=cv.transform([title])
    index=int(mnb.predict(title))
    result=m[index]
    return result

# def testing(request):
#     comment=[]
#     if request.method=="POST":
#         file=request.FILES['raju']
#         fs=FileSystemStorage()
#         fs.save(file.name,file)
#         loc1='media/'+file.name
#         loc=os.path.join(BASE_DIR,loc1)
#         data = open(loc,"r") 
#         x=data.readlines()
#         for item in x:
#             res=predict(item)
#             comment.append( {item : res} )
#         return JsonResponse({'comments':comment})
#     return render(request,'flair/upload.html')
import pickle

import pandas as pd
from django.shortcuts import render, redirect
from .models import Member


# Create your views here.

def index(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'crud/index.html', context)


def coeur(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'crud/coeur.html', context)


def diabete(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'crud/diabete.html', context)


def create(request):
    global context
    members = Member.objects.all()

    member = Member(
        name=request.POST['name'],
        age=request.POST['age'],
        sex=request.POST['sex'],  # select
        cp=request.POST['cp'],
        trtbps=request.POST['trtbps'],
        chol=request.POST['chol'],
        fbs=request.POST['fbs'],
        restecg=request.POST['restecg'],
        thalachh=request.POST['thalachh'],
        exng=request.POST['exng'],
        caa=request.POST['caa'],
    )
    member.save()
    return ""
    # Load Model Content
    if member.name != "":
        df = pd.DataFrame(columns=['name', 'age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 'restecg',
                                   'thalachh', 'exng', 'caa'])

        df2 = {'name': str(member.name), 'age': int(member.age), 'sex': int(member.sex), 'cp': int(member.cp),
               'trtbps': int(member.trtbps), 'chol': int(member.chol), 'fbs': int(member.fbd),
               'restecg': int(member.restecg),
               'thalachh': int(member.thalachh), 'exng': int(member.exng), 'caa': int(member.caa)}

        df = df.append(df2, ignore_index=True)
        # load the model from disk
        filename = 'crud/heart84.6.pickle'
        pca = pickle.load(open(filename, 'rb'))
        data = pca.transform(df)
        # filename1 = 'crud/heart84.6.pickle'
        # loaded_model = pickle.load(open(filename1, 'rb'))

        res = pca.predict(data)
        print("Value of res is :", res)
        context = {'prediction': res, 'members': members}
    # End of model
    # return redirect('/')
    return render(request, 'crud/index.html', context)


def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/edit.html', context)


def update(request, id):
    member = Member.objects.get(id=id)
    member.attrite = request.POST['attrite']
    member.name = request.POST['name']
    member.save()
    return redirect('/crud/')


def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/crud/')

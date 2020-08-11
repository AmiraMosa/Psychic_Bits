from django.shortcuts import render, get_object_or_404, redirect
from pyexpat.errors import messages

from .models import prediction
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import predictionSerializer
from .models import prediction
from PsychicBits.models import Match
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

@api_view(['GET'])
def showPrediction(pk):
    try:

        predict = prediction.objects.get(pk=pk)
    except prediction.DoesNotExist:
        return HttpResponseNotFound('<h1>no such ID</h1>')

    # if request.method == 'GET':
    #     serializer = predictionSerializer(predict)
    #     return Response(serializer.data)

#vote/<int:matchID>/
@login_required(login_url='psychicbits/mainhome.html')
def vote(request, matchID):
    if request.method == 'POST':
        vote = request.POST['browser']
        username = request.user.username
        match = Match.objects.get(pk=matchID)
        user = get_object_or_404(User, username=username)
        profileObj = get_object_or_404(Profile, user=user)
        newVote = prediction.objects.create(userID=profileObj, matchID=match, vote=vote)

    return redirect('/psychicbits/mainhome')


def calculateScore(request, matchID, result):
    match = Match.objects.get(pk=matchID)

    # return queryset of matchID res filtered prediction
    truePredictions = prediction.objects.filter(matchID__id=matchID).filter(vote=result)

    if not truePredictions:
        return HttpResponse('<h1>No true prediction</h1>')

    for predictionObj in truePredictions:
        predictor = User.objects.get(pk=predictionObj.userID)
        predictor.profile.score += 1
        predictor.save()
    return HttpResponse('score increased')


def topTen():
    scoreList = Profile.objects.all().order_by('-score')[:10]
    names = []
    scores = []
    for user in scoreList:
        names.append(user.user)
        scores.append(user.score)
    return names, scores

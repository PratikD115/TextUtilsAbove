from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text after submitting the form
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')

    if removepunc == 'on':
        punc = '''+_)(*&^%$#@!~`=-}{|\][":';?></.,'''
        analyzed = ""
        for char in djtext:
            if char not in punc:
                analyzed = analyzed + char
        djtext = analyzed
        # params = {'purpose': 'Remove Punctuations', 'analyzedText': analyzed}
        # return render(request, 'Analyze.html', params)

    if uppercase == 'on':
        analyzed = ""
        analyzed = djtext.upper()
        djtext = analyzed
        # params = {'purpose': 'Upper Case', 'analyzedText': analyzed}
        # return render(request, 'Analyze.html', params)

    if newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        djtext = analyzed
        # params = {'purpose': 'Removed NewLines', 'analyzedText': analyzed}
        # return render(request, 'Analyze.html', params)

    if spaceremove == 'on':
        analyzed = ""
        for i, char in enumerate(djtext):
            if not (djtext[i] == " " and djtext[i + 1] == " "):
                analyzed = analyzed + char
        djtext = analyzed
        # params = {'purpose': 'Remove Extra Space', 'analyzedText': analyzed}
        # return render(request, 'Analyze.html', params)

    if removepunc == 'on' or uppercase == 'on' or newlineremove == 'on' or spaceremove == 'on':
        purpose = ''
        if removepunc == 'on':
            purpose = purpose + '"Remove Punctuations"'
        if uppercase == 'on':
            purpose = purpose + ' "UPPER CASE"'
        if newlineremove == 'on':
            purpose = purpose + ' "REMOVE NEW LINE"'
        if spaceremove == 'on':
            purpose = purpose + ' "REMOVE SPACE"'
        params = {'purpose': purpose, 'analyzedText': djtext}
        return render(request, 'Analyze.html', params)
    else:
        return HttpResponse('Error !! Please select at-least one functionality.')
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
import requests
import json

def index(request):
    return render(request, 'MovieTitlesDataVisualization/index.html', {})


def ajaxResponse(request):
    if request.is_ajax and request.method == "GET":
        userInput = request.GET.get('data', None)
        
        word_query = userInput
        year_counter = 2013
        response_ = {}

        while(year_counter != 2021):
            Data = (requests.get('http://www.omdbapi.com/?s=' + word_query +'*&y=' + str(year_counter) + '&type=movie&apikey=7efd04e4')).json()

            if(Data['Response'] == 'True'):
                response_[year_counter] = Data['totalResults']
                
            else:
                response_[year_counter] = '0'

            year_counter += 1
        
    else:
        raise Http404('An error occurred')
    
    print(response_)

    return JsonResponse({'response_': response_})

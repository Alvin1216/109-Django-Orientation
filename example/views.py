from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from example.models import Movies
from datetime import datetime
import json

# Create your views here.
@csrf_exempt
def selectMovie(request):
    if request.method == "POST":
        request_body = json.loads(request.body.decode('utf-8'))
        movie_id = request_body['movie_id']
        movie_info = Movies.objects.filter(movie_id=int(movie_id))

        movie_list = []
        print(len(movie_info))
        for index in range(0,len(movie_info)):
            index = int(index)
            data = {
                "movie_id": movie_info[index].movie_id,
                "title": movie_info[index].title,
                "genres": movie_info[index].genres
            }
        movie_list.append(data)
        print(movie_list)
        return JsonResponse({"movie_list": movie_list})
    else:
        return HttpResponse("wrong method@@")

def renderExample(request):
    name = "大雄"
    current_time = str(datetime.now())
    print(current_time)
    return render(request, 'example/index.html', locals())
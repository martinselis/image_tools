from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import requests
import io
import json
from django.http import Http404

def index(request):
    return render(request, "image_tools/index.html")

def submitted(request):
    input_url = request.POST.get("urlname")
    if (input_url[-1] == "/"):
        input_url = input_url[0:-1]
    extension = input_url.split('.')
    extension = extension[len(extension) - 1]
    if (extension.lower() == 'jpg'):
        extension = 'JPEG'

    #Capture URL
    response = requests.get(input_url, stream=True)
    response.raw.decode_content = True # handle spurious Content-Encoding

    width = request.POST.get("width")
    height = request.POST.get("height")
    bytes_img = resize(request, response, width, height, extension)
    #error(request, 'Unable to read the file. Please verify the URL.')

    #generate the file
    request = HttpResponse(bytes_img.getvalue(), content_type='image/{}'.format(extension))
    request['Content-Disposition'] = 'attachment; filename=resized_{}x{}.{}'.format(width, height, extension)
    return request

def resize(request, response, width, height, extension):
    im = Image.open(response.raw)
    #error(request, 'Unable to read the file. Please verify the URL.')

    size = (int(width), int(height))
    upgraded_img = im.resize(size, Image.ANTIALIAS)
    bytes_img = io.BytesIO()
    upgraded_img.save(bytes_img, format=extension, quality=100)
    return bytes_img

def error(request, error):
    return render (request, 'image_tools/index.html', {'url_info': json.dumps(error)})
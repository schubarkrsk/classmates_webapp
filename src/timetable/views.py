from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Index of/</h1><br>"
                        "<p>Hello, world!<br><br>"
                        "Start:<br>"
                        "MOV AX, 9<br>"
                        "MOV DX, OFFSET Message<br>"
                        "INT 21h<br>"
                        "RET<br>"
                        "Message DB \"I Love IE\"<br>"
                        "End Start</p>")
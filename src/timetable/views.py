from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Index of/</h1><br>"
                        "<p>Hello, world!<br><br>"
                        "<h3>Пасхалка от Стасяна</h3><br>"
                        "Start:<br>"
                        "MOV AX, 9<br>"
                        "MOV DX, OFFSET Message<br>"
                        "INT 21h<br>"
                        "RET<br>"
                        "Message DB \"I Love IE\"<br>"
                        "End Start</p>"
                        "<br><br>"
                        "<p>SECRET HASH: b42acda9b495eac5b6c303fc993afe02e3a594e1bffb801be9b46aecec9f55fa</p>")
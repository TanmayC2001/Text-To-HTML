from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "home.html")

def output(request):
    if request.method == "POST":
        htmlformat = request.POST.get("text")
        html = str(htmlformat).replace("<", "\n<").replace(">",">\n")

        return render(request, "output.html", {"htmlcode": htmlformat, "html": html})
    else:
        return HttpResponse(htmlformat)






from django.shortcuts import render
from .models import Thesis


# Create your views here.
def index(request):
    thesis_list = Thesis.objects.all()

    return render(request, "index.html", {"thesis_list": thesis_list})


def detail(request, id):
    detail = Thesis.objects.get(pk=id)
    authors = detail.authors.all()
    panelists = detail.panelists.all()

    return render(
        request,
        "detail.html",
        {"detail": detail, "authors": authors, "panelists": panelists},
    )

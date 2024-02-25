from django.shortcuts import render
from .models import Thesis
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    thesis_list = Thesis.objects.all()
    paginator = Paginator(thesis_list, 5)
    page_number = request.GET.get("page", 1)
    thesis_list = paginator.page(page_number)

    return render(request, "post/list.html", {"thesis_list": thesis_list})


def detail(request, id):
    detail = Thesis.objects.get(pk=id)
    authors = detail.authors.all()
    panelists = detail.panelists.all()

    return render(
        request,
        "post/detail.html",
        {"detail": detail, "authors": authors, "panelists": panelists},
    )

from django.shortcuts import render, get_object_or_404
from .models import Thesis
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from .forms import CommentForm

# Create your views here.

def landing(request):
    return render(request, "landing.html")

def post_list(request):
    thesis_list = Thesis.objects.all()
    paginator = Paginator(thesis_list, 5)
    page_number = request.GET.get("page", 1)
    thesis_list = paginator.page(page_number)

    return render(request, "post/list.html", {"thesis_list": thesis_list})


def detail(request, id):
    detail = Thesis.objects.get(pk=id)
    authors = detail.authors.all()
    panelists = detail.panelists.all()
    comments = detail.comments.filter(active=True)
    form = CommentForm()

    return render(
        request,
        "post/detail.html",
        {"detail": detail, "authors": authors, "panelists": panelists, "form": form, "comments": comments},
    )

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Thesis, id=post_id, status=Thesis.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    return render(request, "post/comment.html",
                        {'post': post,
                         'form': form, 
                         'comment': comment})

@require_POST
def search(request):

    words = request.POST.get('words', None)
    print(words)
    thesis_list = Thesis.objects.filter(abstract__contains=words)

    return render(request, "post/search_results.html", {"thesis_list": thesis_list})
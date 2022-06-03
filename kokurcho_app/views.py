from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm
import json

from kokurcho_app.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['email', 'contents']


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def form_telegram(request):
    return render(request, "form_telegram.html")


def main_menu(request):
    return render(request, "main_menu.html")


def feedback(request):
    return render(request, "feedback.html", context={
        'comment': CommentForm()
    })


def valid(request):
    #return render(request, "valid.html", {'form': form})
    return render(request, "valid.html")


def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(json.loads(request.body))
        if form.is_valid():
            Comment.objects.create(**form.cleaned_data)
            return HttpResponse("Created")
        else:
            return HttpResponse("Bad Request", status=400)
    else:
        return HttpResponse("Bad method", status=400)


def get_comment(request):
    comments = Comment.objects.all()
    result = []
    for comment in comments:
        result.append({
            'email': comment.email,
            'contents': comment.contents
        })
    return HttpResponse(json.dumps(result))

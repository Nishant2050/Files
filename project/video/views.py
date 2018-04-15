from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from video.forms import DocForm
from .models import Document

# Create your views here.

def IndexView(request):
    return render_to_response('homepage.html')
    # return HttpResponse('hi!!!')

def UploadFiles(request):
    if request.method == 'POST':
        form = DocForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            return redirect('index')
    else:
        form = DocForm()
    images = Document.objects.all()
    return render(request, 'uploadform.html', {'form':form, 'images': images})

# def DisplayFiles(request):
#     image = get_object_or_404(Document)
#     form = DocForm(request.POST or None, request.FILES or None, image=image)
#     if form.is_valid():
#         image = form.save()


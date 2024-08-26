from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Image
from .forms import PostForm


def gallery(request):
    images = Image.objects.all()
    return render(request, 'gallery/gallery.html', {'images': images})

def image_details(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request, 'gallery/image_details.html', {'image': image})

def post_image(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        print(form)
        if form.is_valid():
            image = form.save(commit=False)
            image.published_date = timezone.now()
            image.save()
            return redirect('gallery.html', pk=image.pk)
    else:
        form = PostForm()
    return render(request, 'gallery/post_image.html', {'form': form})   
    
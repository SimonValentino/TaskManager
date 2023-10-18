from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

# Create your views here.
def index(request):
    if request.method == "POST":
        content = request.POST.get("content", "")

        if content:
            try:
                task = Todo(content=content)
                task.save()
            except Exception as e:
                return "There was an error adding the task."

            return redirect("index")

    tasks = Todo.objects.all().order_by("created_on")
    return render(request, "core/index.html", {"tasks": tasks})


def delete(request, id):
    task = get_object_or_404(Todo, pk=id)
    task.delete()
    return redirect("index")


def update(request, id):
    content = request.POST.get("content", "")
    task = get_object_or_404(Todo, pk=id)
    if content:
        try:
            task.content = content
            task.save()
        except Exception as e:
            return "There was an error updating the task."
        
        return redirect("index")
    
    return render(request, "core/update.html", {"task": task})

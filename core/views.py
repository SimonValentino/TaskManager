from django.shortcuts import render, redirect
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
                return render(request, "core/error.html", {"error_message": str(e)})

            return redirect("index")

    tasks = Todo.objects.all().order_by("created_on")
    return render(request, "core/index.html", {"tasks": tasks})

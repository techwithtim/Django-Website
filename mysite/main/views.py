from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import ToDoList
from .forms import CreateListForm
# Create your views here.

def index(request, id):
	ls = ToDoList.objects.get(id=id)

	if request.method == "POST":
		if request.POST.get("save"):
			for item in ls.item_set.all():
				p = request.POST
				
				if "clicked" == p.get("c"+str(item.id)):
					item.complete = True
				else:
					item.complete = False

				if "text" + str(item.id) in p:
					item.text = p.get("text" + str(item.id))


				item.save()

		elif request.POST.get("add"):
			newItem = request.POST.get("new")
			if newItem != "":
				ls.item_set.create(text=newItem, complete=False)
			else:
				print("invalid")

	return render(request, "main/index.html", {"ls": ls})


def get_name(request):
	if request.method == "POST":
		form = CreateListForm(request.POST)

		if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n, date=timezone.now())
			t.save()
			
			return HttpResponseRedirect("/%i" %t.id)

	else:
		form = CreateListForm()

	return render(request, "main/create.html", {"form": form})


def home(request):
	return render(request, "main/home.html", {})


def view(request):
	l = ToDoList.objects.all()
	return render(request, "main/view.html", {"lists":l})

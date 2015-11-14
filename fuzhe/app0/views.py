from django.shortcuts import render,render_to_response
from django import template
from app0.models import Book,Author
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,Context
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
	if request.method == "GET":
		if "Delete" in request.GET:
			ISBN1 = request.GET["Delete"]
			DD=Book.objects.filter(ISBN=ISBN1)
			DD.delete()
			
	options = Book.objects.all()
	return render_to_response('home.html',{'options':options})
	

def Information(request,i):
	book1 = Book.objects.get(ISBN = i)
	return render_to_response('Information.html',{'book1':book1})

@csrf_exempt
def Add(request):
	options2 = Author.objects.all()
	if request.method == 'POST':
		id = request.POST.get("select")
		#return HttpResponse(id)
		authorid = Author.objects.get(AuthorID = id)
		
		book=Book.objects.create(
					ISBN=request.POST['ISBN'],
					Title=request.POST['Title'],
					AuthorID=authorid,
					Publisher=request.POST['Publisher'],
					PublishDate=request.POST['PublishDate'],
					Price=request.POST['Price'])
		book.save()
	return render_to_response('Add.html',{'options2':options2})
	
@csrf_exempt
def Search(request):
	if request.method=='POST':
		Name=request.POST['Name']
		#return HttpResponse(Name)
		authorid = Author.objects.get(Name = Name)
		options = authorid.book_set.all()
		return render_to_response('Search.html',{'options':options})
	return render_to_response('Search.html')
	
@csrf_exempt	
def Change(request,i):
	options2 = Author.objects.all()
	book1 = Book.objects.get(ISBN = i)
	if request.method == 'POST':
		id = request.POST.get("select")
		#return HttpResponse(id)
		authorid = Author.objects.get(AuthorID = id)
		
		book1.AuthorID=authorid
		book1.Publisher=request.POST['Publisher']
		book1.PublishDate=request.POST['PublishDate']
		book1.Price=request.POST['Price']
		book1.save()
		
	return render_to_response('Change.html',{'options2':options2,'book1':book1})
	
@csrf_exempt
def AddAuthor(request):
	#options2 = Author.objects.all()
	if request.method == 'POST':
		#id = request.POST.get("select")
		#return HttpResponse(id)
		#authorid = Author.objects.get(AuthorID = id)
		
		author=Author.objects.create(
					AuthorID=request.POST['AuthorID'],
					Name=request.POST['Name'],
					Age=request.POST['Age'],
					Country=request.POST['Country'])
		author.save()
	return render_to_response('AddAuthor.html')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

		
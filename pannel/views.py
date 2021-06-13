from django.shortcuts import render, HttpResponse  , redirect,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User  # sign me user create ke liye module
from .models import Student
from django.utils import timezone  # time module
# Create your views here.

def login(request):
	if request.user.is_authenticated:
		return redirect('view')
	else:
		if request.method=='POST':
			user=auth.authenticate(username = request.POST['username'] , password = request.POST['password'])
			if user is  not None:
				auth.login(request,user)
				return redirect('view')
			else:
				return render(request,'pannel/login.html',{'error':'*username or password is incorrect !!!* '})
		else:
			return render(request,'pannel/login.html')




def view(request):
	data  =  Student.objects.all()
	return render(request,'pannel/view.html',{'data':data})
	



def delete_student(request,id):
	p = Student.objects.get(std_id = id)
	p.delete()
	return  redirect('view')



def insert_student(request):
	if request.method=='POST':
		if request.POST['name'] and request.POST['roll']:
			s =  Student(name = request.POST['name'],roll = request.POST['roll'],phone = request.POST['phone'],age = request.POST['age'],address = request.POST['address'])
			s.save()
			return redirect('view')
		else:
			return render(request,'pannel/insert.html',{'error':'Please fill the required feilds!!!'})



		return render(request,'pannel/insert.html')

	return render(request,'pannel/insert.html')





def edit_student(request,id): 
	s = Student.objects.filter(std_id=id)
	if request.method=='POST':
		f =  Student(name = request.POST['name'],roll = request.POST['roll'],phone = request.POST['phone'],age = request.POST['age'],address = request.POST['address'],std_id=id)
		f.save()
		return redirect('view')


	return render(request,'pannel/edit.html',{'p':s})




def search(request):
	query = request.GET['search']
	data = Student.objects.filter( name = query )

	return render(request,'pannel/view.html',{'data':data})

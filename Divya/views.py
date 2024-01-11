from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage

from .models import *

def index(request):

	My_profile_nav_object = My_profile_nav.objects.all()
	My_profile_home_object = My_profile_home.objects.all()
	My_portfolio_object = My_portfolio.objects.all().filter(Featured=1)[:4]
	My_blog_object = My_blog.objects.all().filter(Featured=1)[:4]
	My_certifications_object = Certification.objects.all().filter(Featured=1)[:3]
	video = Video.objects.all()
	context = {
		'My_profile_nav_object': My_profile_nav_object,
		'My_profile_home_object': My_profile_home_object,
		'My_portfolio_object': My_portfolio_object,
		'My_blog_object': My_blog_object,
		'My_certifications_object': certifications,
		'video': video,
	}

	return render(request, 'index.html', context)


def portfolio(request):

	My_profile_nav_object = My_profile_nav.objects.all()
	My_portfolio_object = My_portfolio.objects.all()

	p = Paginator(My_portfolio_object, 6)
	page_num = request.GET.get('page', 1)

	try:
		page = p.page(page_num)
	except EmptyPage:
		page = p.page(1)

	context = {
		'My_profile_nav_object': My_profile_nav_object,
		'My_portfolio_object': page,
	}

	return render(request, 'portfolio.html', context)
def blog(request):
	My_profile_nav_object = My_profile_nav.objects.all()
	My_blog_object = My_blog.objects.all()

	p = Paginator(My_blog_object, 6)
	page_num = request.GET.get('page', 1)

	try:
		page = p.page(page_num)
	except EmptyPage:
		page = p.page(1)

	context = {
		'My_profile_nav_object': My_profile_nav_object,
		'My_blog_object': page,
	}

	return render(request, 'blog-home.html', context)
	

def contact(request):
	My_profile_nav_object = My_profile_nav.objects.all()

	context = {
		'My_profile_nav_object': My_profile_nav_object,
	}

	if request.method=="POST":
		contact = Contact()
		name = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('message')
		contact.con_name = name
		contact.con_email = email
		contact.con_message = message
		contact.save()
		
		return render(request, 'contact_thank.html', context)
	

	

	return render(request, 'contact.html', context)

def featured_profiles(request):
    featured_profiles = My_profile_nav.objects.filter(status=1)
    return render(request, 'index.html', {'featured_profiles': featured_profiles})


def certifications(request):

	My_profile_nav_object = My_profile_nav.objects.all()
	My_certifications_object = Certification.objects.order_by('id').all()

	p = Paginator(My_certifications_object, 6)
	page_num = request.GET.get('page', 1)

	try:
		page = p.page(page_num)
	except EmptyPage:
		page = p.page(1)

	context = {
		'My_profile_nav_object': My_profile_nav_object,
		'certifications': page,
	}

	return render(request, 'certification.html', context)	

def intro_video(request):
	video = Video.objects.all	
	return render(request, 'intro_video.html', {'video': video})



# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

def login_root(request):
	# Login form submitted?
	if request.method == 'POST':

		username=request.POST.get('username')
		password=request.POST.get('password')

		if username and password:
			user = authenticate(request,username=username, password=password)
			#import pdb; pdb.set_trace()
			# Login succeeded
			if user is not None:
				return HttpResponseRedirect(reverse('login_success'))

		#if username==request.POST.get('username'):
			#return HttpResponseRedirect(reverse('login_success'))
		# Login failed
		return HttpResponseRedirect(reverse('login_fail'))


	return render(request, 'login_root.html')

def login_success(request):
	return render(request, 'login_success.html')

def login_fail(request):
	return render(request, 'login_fail.html')

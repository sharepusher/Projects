from django.shortcuts import render
from .models import Tinyurl
from .forms import TinyurlForm
# a view is a function that takes a web request and return a web response
from django.http import HttpResponseRedirect
# cache
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.shortcuts import render_to_response

# for login function 
from .forms import LoginForm
# To login, we need to import authenticate and login functions from contrib.auth
from django.contrib.auth import authenticate, login, logout
from .models import User

# login verify
from django.contrib.auth.decorators import login_required

# exceptions
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@cache_page(60)
def index_test(request):
    # call the render function with the request and template name 
    # as parameters to render a template.
    cache.set('testkey', 'test cache', 30)
    return render_to_response('index.html', {'name': cache.get('testkey')})

#@login_required(login_url='/login/')
def index(request):
    # call the render function with the request and template name 
    # as parameters to render a template.
    return render(request, 'index.html')
    #return HttpResponse('<h1>Hello, the world</h1>')

def unknown(request):
    return render(request, '404.html')

def convert(request, short_url):
    return render(request, 'redirect')

def statistics(request):
    tinyurls = Tinyurl.objects.all()
    return render(request, 'statics.html', {"tinyurls":tinyurls}) 

def encode(request):
    # parse the long url
    form = TinyurlForm(request.POST)
    if not form.is_valid():
        return HttpResponseRedirect('/')
    lurl = form.cleaned_data['long_url']
    if not lurl:
        return HttpResponseRedirect('/')
    # 
    # check cache
    cached_url = cache.get(lurl)
    if cached_url:
        return render(request, 'url.html', {"long_url":lurl, "short_url":cached_url})
    # check db
    try:
        db_url = Tinyurl.objects.get(long_url=lurl)
        return render(request, 'url.html', {"long_url":lurl, "short_url":db_url.short_url})
    except:
        pass
    # encode
    try:
        urlid = Tinyurl.objects.latest('id')
        urlid = urlid.id
    except:
        urlid = 0
    surl = convertTo62(urlid+1)
    # update to cache
    cache.set(surl, lurl)
    cache.set(lurl, surl)
    # store to db
    tinyurl = Tinyurl(user = request.user, long_url = lurl, short_url = surl)
    tinyurl.save()
    #return HttpResponseRedirect('/')
    return render(request, 'url.html', {"long_url":lurl, "short_url":surl})

def convertTo62(num):
    ret = ""
    encode = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    while num != 0:
        inx = num % 62
        ret += encode[inx:inx+1]
        num //= 62
    if len(ret) < 6:
        return ret + encode[:6-len(ret)+1]
    return ret

def decode(request, surl):
    # parse the short url from request
    if not surl:
        return render(request, '404.html')
    # check cache    
    lurl = cache.get(surl)
    if not lurl:
        # query db
        try:
            db_url = Tinyurl.objects.get(short_url=surl)
        except:
            return render(request, '404.html')
        lurl = db_url.long_url
        cache.set(surl, lurl)
        cache.set(lurl, surl)
    if lurl.startswith('http'):
        return HttpResponseRedirect(lurl) 
    lurl = "http://" + lurl
    return HttpResponseRedirect(lurl) 

def login_view(request):
    # check the request first
    if request.method != 'POST':
        form = LoginForm()
        # if it's not a post, simply display the LoginForm
        return render(request, 'login.html', {'form': form})
    # if this was a post, then we would want to authenticate the submitted us
    form = LoginForm(request.POST)
    if form.is_valid():
        u = form.cleaned_data['username']
        p = form.cleaned_data['password']
        user = authenticate(username=u, password=p)
        if user:
	    if user.is_active:
                # built-in login function to login
		login(request, user)
		return HttpResponseRedirect('/')
            else:
		print("The account has been disabled!")
	else:
	    print("The username and password were incorrect.")

def logout_view(request):
    logout(request)
    # simply call the built-in logout function imported from django.contrib.auth
    # then redirect to the homepage.
    return HttpResponseRedirect('/')   
 
def profile(request, username):
    # look up the user object in the User model by its username
    user = User.objects.get(username=username)
    # The QuerySet filter will look up all of the treasures that belongs to this user.
    tinyurls = Tinyurl.objects.filter(user=user)
    # pass the username and urls list in a dictionary to template profile.html for rendering
    return render(request, 'profile.html', {'username': username, 'tinyurls':tinyurls})



from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse
from urllib.parse import urlencode
from app.models import Student


# Create your views here.
def landingpage(request):
    return render(request,'landingpage.html')

def register(request):
    return render(request,'register.html')


def login(request):
    return render(request,'login.html')

def logindata(request):
    if request.method=='POST':
        le = request.POST.get('lemail')
        lp = request.POST.get('lpassword')
        # print(le,lp)
        user = Student.objects.filter(email=le)
        if user:
            userdata = Student.objects.get(email=le)
            id = userdata.id
            name = userdata.name
            email = userdata.email
            gender = userdata.gender
            password = userdata.password
            higher = userdata.higher
            details = userdata.detail
            photo = userdata.photo
            contact = userdata.contact
            qualification = userdata.qualification
            # print(name,email,password,gender,higher,details,photo,contact,qualification)
            if (lp==password):
                # data = {'name':name}
                # return render(request,'database.html',data)   // in our url it show logindata
                base_url = reverse('dashboard')
                data = urlencode({'id':id,'name':name,'email':email,'contact':contact,'gender':gender,'higher':higher,'password':password})
                url = f'{base_url}?{data}'
                return redirect(url)

            else:
                msg = 'Email & Password not Matched'
                return render(request,'login.html',{'msg':msg,'email':le})
        else:
            msg = "Email is not register"
def dashboard(req):
    e = req.GET.get('email')
    p = req.GET.get('password')
    if e and p :
        i = req.GET.get('id')
        n = req.GET.get('name')
        c = req.GET.get('contact')
        g = req.GET.get('gender')
        h = req.GET.get('higher')
        data = {'id':i,'name':n,'contact':c,'gender':g,'higher':h,'email':e,'password':p}
        return render(req,'dashboard.html',{"data":data})
    else:
        # return render(req,'login.html')
        url = reverse('login')
        return redirect(url)
def registerdata(request):
    if request.method=='POST':
        n = request.POST.get('name')
        e = request.POST.get('email')
        c = request.POST.get('contact')
        d = request.POST.get('details')
        g = request.POST.get('gender')
        q = request.POST.getlist('qualification')
        h = request.POST.get('higher')
        p = request.FILES.get('photo')
        do = request.FILES.get('document')
        a = request.FILES.get('audio')
        v = request.FILES.get('video')
       
    

        pa = request.POST.get('password')
        cpass = request.POST.get('cpassword')

        # print(n,e,c,d,g,q,h,p,a,v)
        user = Student.objects.filter(email=e)
        if user:
            msg = 'User Already Exist'
            return render(request,'register.html',{'x':msg})
        else:
            if pa==cpass:
                
                Student.objects.create(name=n,email=e,contact=c,detail=d,gender=g,qualification=q,higher = h,photo=p,document=do,audio = a,video=v,password=pa)
                return render(request,'login.html',{'y':'Registration Done'})

            else:
                msg= 'password does not matched'
                data = {'name':n,'email':e,'contact':c,'detail':d,'gender':g,'qualification':q,'higher' : h,'photo':p,'document':do,'audio' : a,'video':v}
                return render(request,'register.html',{'pmsg':msg,'data':data})
            
        
        
    

        return render(request,'register.html')


def dynamic_url(request,age,name,qual):
    data = {'age':age,'name':name,'qual':qual}
    return render(request,'dynamic_url.html',{'data':data})

def query(request,pk):
    userdata = Student.objects.get(id=pk)
    data = {
        'id' : userdata.id,
        'name' : userdata.name,
        'email'  : userdata.email,
        'gender' : userdata.gender,
        'password' : userdata.password,
        'higher' : userdata.higher,
        'details' : userdata.detail,
        'photo' : userdata.photo,
        'qualification' : userdata.qualification,
        'contact' : userdata.contact,
    }
    return render(request,'dashboard.html',{'data':data,'query':pk})
    # print(pk)

from app.models import Query
def query_data(req,pk):
    if req.method =='POST':
        nam = req.POST.get('name')
        e = req.POST.get('email')
        q = req.POST.get('query')

    Query.objects.create(Name=nam,Email=e,Query=q)
    userdata=Student.objects.get(id=pk)
    data = {
            'id':userdata.id,
            'name':userdata.name,
            'email':userdata.email,
            'contact':userdata.contact,
            'details':userdata.detail,
            'gender':userdata.gender,
            'qualification':userdata.qualification,
            'higher':userdata.higher,
            'photo':userdata.photo,
            'document':userdata.document,
            'audio':userdata.audio,
            'video':userdata.video
        }
    return render(req,'dashboard.html',{'data':data})

def show_query(req,pk):
    userdata=Student.objects.get(id=pk)
    data = {
            'id':userdata.id,
            'name':userdata.name,
            'email':userdata.email,
            'contact':userdata.contact,
            'details':userdata.detail,
            'gender':userdata.gender,
            'qualification':userdata.qualification,
            'higher':userdata.higher,
            'photo':userdata.photo,
            'document':userdata.document,
            'audio':userdata.audio,
            'video':userdata.video
        }
    all_query = Query.objects.filter(Email=userdata.email)
    return render(req,'dashboard.html',{'data':data,'aq':all_query})

    

    # userdata = Student.objects.get(id=pk)
    # data = {'id':userdata.id,
    #         'name':userdata.n,
    #         'email':userdata.e,
    #         'contact':userdata.c,
    #         'detail':userdata.d,
    #         'gender':userdata.g,
    #         'qualification':userdata.q,
    #         'higher' : userdata.h,
    #         'photo':userdata.p,
    #         'document':userdata.do,
    #         'audio' :userdata.a,
    #         'video':userdata.v}
    # return render(request,'dashboard.html',{'data':data})
            
   
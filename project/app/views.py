from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader

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
            name = userdata.name
            email = userdata.email
            gender = userdata.gender
            password = userdata.password
            higher = userdata.higher
            details = userdata.detail
            photo = userdata.photo
            contact = userdata.contact
            qualification = userdata.qualification
            print(name,email,password,gender,higher,details,photo,contact,qualification)

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
                data = {'name':n,'email':e,'contact':c,'detail':d,'gender':g,'qualification':q,'higher' : h,'photo':p,'document':do,'audio' : a,'vide':v}
                return render(request,'register.html',{'pmsg':msg,'data':data})
            
        
        
    

        return render(request,'register.html')




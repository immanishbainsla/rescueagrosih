from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.
from farmers.models import Farmer
from reg.models import address1, Organisation
from farmers.forms import FarmerForm
from django.core.mail import send_mail

def Farmer_Organ(request): # homepage/dashboard
    user = request.user
    categ = Organisation.objects.get(user=user).organisations
    farmer_address = None
    try:
        farmer_address = address1.objects.get(user=user)
    except:
        pass
    user_id = User.objects.get(username = user).id
    food_past = Farmer.objects.filter(user_id = user_id) # on_hold
    provider = Farmer.objects.filter(is_active=True)

    form = FarmerForm()
    if request.method=='POST':
        form=FarmerForm(request.POST, None)
        if form.is_valid():

            form.save(commit=False)
            cmd = form.save(commit=False)
            cmd.user = request.user

            cmd.save()
        return redirect('farmer')
    return render(request,'farmer/farmers_dashboards.html',{'form':form,'providers':provider,'food_past':food_past, 'categ': categ, 'farmer_address': farmer_address})


def DeleteView(request,id):

    post = Farmer.objects.get(id = id)
    user = request.user
    u_id = User.objects.get(username=user).id
    org = Organisation.objects.get(user=u_id)
    try:
        poster_id = post.user.id
        poster_org = Organisation.objects.get(user=poster_id)
        poster_org.total_times_donated += 1
        poster_org.save()
        org.total_fedeed += post.amount
        org.save()
    except:
        pass
    post.is_active = False
    post.save()
    return redirect('farmer')

#email
def email(request,id):
    post = Farmer.objects.get(id = id)
    a = request.user
    email_to = User.objects.get(username = a).email
    print(email_to)
    if email_to:
        Name = post.user
        Name = str(Name)
        email_to_from = User.objects.get(username = Name).email
        crop_name =  post.crop_name
        quantity =   str(post.quantity)
        time =  str(post.time_type)
        if time == "m_3":
            time = "3 months"
        elif time == "m_1":
            time = "1 month"
        elif time == "m_6":
            time = "6 months"
        elif time == "m_12":
            time = "12 months"
        elif request.method == 'POST':
            price = request.POST['price']
        price = 1000
        message = "Hello Ma'am/Sir,\t "+"\n\n"+"Name:\t"+Name+ "\n"+"Crop Name\t"+ crop_name+"\n"+"Quantity \t"+ quantity + "\n" + "Time \t" +time + "\n" +"\n \n" +"For more details contact ......\t" + "9654457446" +"\n"
        # print(message)
        send_mail('These are the details you request',message,'testwebsite7777@gmail.com',[email_to_from, email_to],fail_silently=False)
        return redirect('farmer')
    else:
        return redirect('farmer')


def addressupdate(request):
    if request.method == "POST":
        house = request.POST.get('house', None)
        street = request.POST.get('street', None)
        area = request.POST.get('area', None)
        pincode = request.POST.get('pincode', None)
        district = request.POST.get('district', None)
        state = request.POST.get('state', None)

        try:
            update_add = address1.objects.get(user=request.user)
        except:
            update_add = address1()
        update_add.user = request.user
        if(house):
            update_add.house = house

        if(street):
            update_add.street = street

        if(area):
            update_add.area = area

        if(pincode):
            update_add.pincode = pincode

        if(district):
            update_add.district = district

        if(state):
            update_add.state = state

        update_add.save()
        # message.success(request, 'Address Updated.')
        return redirect('farmer')

    else:
        return redirect('farmer')

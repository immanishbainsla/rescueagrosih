from django import template
from django.contrib.auth.models import User
from reg.models import Organisation, Post, address1
register=template.Library()

def check_farmer(value):
     a = Organisation.objects.get(user = value).organisations
     # print(a)
     if a == "M":
         a = "None12"
         return a
     else:
         a = None
         return a
register.filter('check_farmer',check_farmer)


def addre(value):
    user_id = User.objects.get(username = value).id
    pincode = address1.objects.get(user = user_id).pincode
    district = address1.objects.get(user_id = user_id).district
    state = address1.objects.get(user_id = user_id).state
    full_add = str(district)+" "+str(state) + " "+ str(pincode)
    print(full_add)
    return full_add
register.filter('addre',addre)

def time(value):
    if value == "m_3":
        return "3 months"
    elif value == "m_1":
        return "1 month"
    if value == "m_6":
        return "6 months"
    if value == "m_12":
        return "12 months" 
register.filter('time',time)



def check(value):
    name = User.objects.get(username = value).id
    # print(name)
    return name
register.filter('check',check)

def check_donor(value):
    a = Organisation.objects.get(user = value).organisations
    # print(a)
    if a == "D":
        a = "None12"
        return a
    else:
        a = None
        return a
register.filter('check_donor',check_donor)

def ftype(value):
    if value=="0":
        a = "Raw Food."
    elif value=="1":
        a = "Fresh Food with validity 1 Day."
    else:
        a = "Stale Food."
    return a
register.filter('ftype',ftype)

def add(value):
    username = value
    add = Post.objects.filter(user=username)
    print("a",add)
    return add
register.filter('add',add)

from datetime import datetime

from django.shortcuts import render
import pyrebase
from django.contrib import auth
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View


firebaseConfig = {
    "apiKey": "AIzaSyBLCBUGHTwEMk3IpO-fhoQnomEITEH-L3s",
    "authDomain": "shree-nilay-615c8.firebaseapp.com",
    "databaseURL": "https://shree-nilay-615c8-default-rtdb.firebaseio.com",
    "projectId": "shree-nilay-615c8",
    "storageBucket": "shree-nilay-615c8.appspot.com",
    "messagingSenderId": "260857163450",
    "appId": "1:260857163450:web:8fc3335b3484a465c65c83",
    "measurementId": "G-54WX0WRK8G"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)

# Get a reference to the auth service
authe = firebase.auth()

# Get a reference to the database service
db = firebase.database()


# Create your views here.
def signIn(request):
    return render(request, 'shree_nilay_accounting/index.html')


# for signin
def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')

    try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message = "Please enter valid email and password"
        return render(request, 'shree_nilay_accounting/index.html', {'msg': message})

    session_id = user['idToken']
    request.session['uid'] = str(session_id)

    return render(request, 'shree_nilay_accounting/Home.html', {'e': email})


def logout(request):
    auth.logout(request)
    return render(request, 'shree_nilay_accounting/index.html')


# for signUp
def postsignup(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')

    try:
        user = authe.create_user_with_email_and_password(email, passw)
    except:
        message = "Unable to create account try again"
        return render(request, 'shree_nilay_accounting/index.html', {'msg': message})

    return render(request, 'shree_nilay_accounting/index.html')


# home
def home(request):
    return render(request, 'shree_nilay_accounting/home.html')


# about
def about(request):
    return render(request, 'shree_nilay_accounting/about.html')


# report
def report(request):
    return render(request, 'shree_nilay_accounting/report.html')


# customer_entry
def customer_entry(request):
    return render(request, 'shree_nilay_accounting/customer entry.html')


# stcok
def stock(request):
    return render(request, 'shree_nilay_accounting/stock.html')


# dealer
def dealer(request):
    return render(request, 'shree_nilay_accounting/dealer.html')


def payment(request):
    return render(request, 'shree_nilay_accounting/payment.html')


# material
def grit(request):
    return render(request, 'shree_nilay_accounting/grit.html')


def bricks(request):
    return render(request, 'shree_nilay_accounting/bricks.html')


def sand(request):
    return render(request, 'shree_nilay_accounting/sand.html')


def water_tank(request):
    return render(request, 'shree_nilay_accounting/water_tank.html')


def earth_work(request):
    return render(request, 'shree_nilay_accounting/earth work.html')


def jcb(request):
    return render(request, 'shree_nilay_accounting/jcb.html')


def cement(request):
    return render(request, 'shree_nilay_accounting/cement.html')


def steel(request):
    return render(request, 'shree_nilay_accounting/steel.html')


# GET date and time
def time_milis():
    import time
    from datetime import datetime, timezone, date

    import pytz  # time zone

    # create time zone
    tz = pytz.timezone('Asia/Kolkata')

    # get the current datatime
    timezone = datetime.now(timezone.utc).astimezone(tz),

    # convert time_now into miliseconds
    # millis = int(time.mktime(timezone.timetuple()))
    millis = int(round(time.time() * 1000))

    d = str(date.today())
    m = str(millis)
    dm = d + "-" + m
    return dm


# get id token
def id_token(request):
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    print("info" + str(a))
    return a


# data entry in database
def grit_entry(request):
    dealer = request.POST.get('dealer')
    numoftruck = request.POST.get('numoftruck')
    vehicle_no = request.POST.get('vehicle_no')
    date1 = request.POST.get('date')
    pass_no = request.POST.get('pass_no')
    weight = request.POST.get('weight')
    quality = request.POST.get('quality')

    dm = time_milis()
    a = id_token(request)

    data = {
        "Dealer": dealer,
        "Numoftruck": numoftruck,
        "Vehicle_No": vehicle_no,
        "Date": date1,
        "Pass_No": pass_no,
        "Weight": weight,
        "Quality": quality,
        "Payment": ""

    }

    if date1:
        db.child('Users').child(a).child("Grit").child(dealer).child(date1).set(data)
        # db.child('Users').child(a).child("Grit").child("Mix").child(date1).set(data)
        message = "Data Insert Successfully"
        return render(request, 'shree_nilay_accounting/grit.html', {"msg": message})
    else:
        pass
    return render(request, 'shree_nilay_accounting/grit.html')


def bricks_entry(request):
    dealer = request.POST.get('dealer')
    numoftruck = request.POST.get('numoftruck')
    vehicle_no = request.POST.get('vehicle_no')
    date1 = request.POST.get('date')
    challanNo = request.POST.get('challanNo')
    nos = request.POST.get('nos')
    quality = request.POST.get('quality')

    dm = time_milis()
    a = id_token(request)

    data = {
        "Dealer": dealer,
        "Numoftruck": numoftruck,
        "Vehicle_No": vehicle_no,
        "Date": date1,
        "Challan_No": challanNo,
        "Nos": nos,
        "Quality": quality,
        "Payment": ""
    }

    if date1:
        db.child('Users').child(a).child("Bricks").child(dealer).child(date1).set(data)
        # db.child('Users').child(a).child("Bricks").child("Mix").child(date1).set(data)
        message = "Data Insert Successfully"
        return render(request, 'shree_nilay_accounting/bricks.html', {"msg": message})
    else:
        pass
    return render(request, 'shree_nilay_accounting/bricks.html')


def sand_entry(request):
    dealer = request.POST.get('dealer')
    numoftruck = request.POST.get('numoftruck')
    vehicle_no = request.POST.get('vehicle_no')
    date1 = request.POST.get('date')
    weight = request.POST.get('weight')

    dm = time_milis()
    a = id_token(request)

    data = {
        "Dealer": dealer,
        "Numoftruck": numoftruck,
        "Vehicle_No": vehicle_no,
        "Date": date1,
        "Weight": weight,
        "Payment": ""
    }
    if date1:
        db.child('Users').child(a).child("Sand").child(dealer).child(date1).set(data)
        # db.child('Users').child(a).child("Sand").child("Mix").child(date1).set(data)
        message = "Data Insert Successfully"
        return render(request, 'shree_nilay_accounting/sand.html', {"msg": message})
    else:
        pass
    return render(request, 'shree_nilay_accounting/sand.html')


def water_tank(request):
    dealer = request.POST.get('dealer')
    numofwatertank = request.POST.get('numofwatertank')
    vehicle_no = request.POST.get('vehicle_no')
    date1 = request.POST.get('date')
    dirvername = request.POST.get('dirvername')
    purpose = request.POST.get('purpose')

    dm = time_milis()
    a = id_token(request)

    data = {
        "Dealer": dealer,
        "NumofWatertank": numofwatertank,
        "Vehicle_No": vehicle_no,
        "Date": date1,
        "Dirvername": dirvername,
        "Purpose": purpose,
        "Payment": ""
    }
    if date1:
        db.child('Users').child(a).child("Water_Tank").child(dealer).child(date1).set(data)
        message = "Data Insert Successfully"
        return render(request, 'shree_nilay_accounting/water_tank.html', {"msg": message})
    else:
        pass
    return render(request, 'shree_nilay_accounting/water_tank.html')


def earth_work(request):
    date1 = request.POST.get('date')
    rate = request.POST.get('rate')
    nos = request.POST.get('nos')
    vehicle_type = request.POST.get('typeofvehicle')

    dm = time_milis()
    a = id_token(request)

    data = {
        "Date": date1,
        "Rate": rate,
        "Nos": nos,
        "vehicle_type": vehicle_type,
        "Payment": ""

    }
    if date1:
        db.child('Users').child(a).child("Earth_Work").child(date1).set(data)
        message = "Data Insert Successfully"
        return render(request, 'shree_nilay_accounting/earth work.html', {"msg": message})
    else:
        pass
    return render(request, 'shree_nilay_accounting/earth work.html')


def jcb(request):
    date1 = request.POST.get('date')
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    purpose = request.POST.get('purpose')

    dm = time_milis()
    a = id_token(request)

    data = {
        "Date": date1,
        "Start_Time": start_time,
        "End_Time": end_time,
        "Purpose": purpose,
        "Payment": ""
    }
    if date1:
        db.child('Users').child(a).child("Jcb").child(date1).set(data)
        message = "Data Insert Successfully"
        return render(request, 'shree_nilay_accounting/jcb.html', {"msg": message})
    else:
        pass
    return render(request, 'shree_nilay_accounting/jcb.html')


def cement(request):
    dealer = request.POST.get('dealer')
    numoftruck = request.POST.get('numoftruck')
    vehicle_no = request.POST.get('vehicle_no')
    date1 = request.POST.get('date')
    nos = request.POST.get('nos')

    dm = time_milis()
    a = id_token(request)

    data = {
        "Dealer": dealer,
        "Date": date1,
        "NumofTrucks": numoftruck,
        "Vehicle_No": vehicle_no,
        "Nos": nos,
        "Payment": ""

    }
    if date1:
        db.child("Users").child(a).child("Cement").child(dealer).child(date1).set(data)
        db.child("Users").child(a).child("Cement").child("Mix").child(date1).set(data)
        message = "Data Insert Successfully"
        return render(request, 'shree_nilay_accounting/cement.html', {"msg": message})
    else:
        pass
    return render(request, 'shree_nilay_accounting/cement.html')


def customer_entry1(request):
    customer_name = request.POST.get('customer_name')
    contact_no = request.POST.get('contact_no')
    house_no = request.POST.get('house_no')
    address = request.POST.get('address')

    dm = time_milis()
    a = id_token(request)

    data = {
        "Customer_Name": customer_name,
        "Contact_No": contact_no,
        "House_No": house_no,
        "Address": address,
    }
    if contact_no:
        db.child("Users").child(a).child("Customer_Entry").child(dm).set(data)
        message = "Data Insert Successfully"
        return render(request, 'shree_nilay_accounting/customer entry.html', {"msg": message})
    else:
        pass

    return render(request, 'shree_nilay_accounting/customer entry.html')


def dealer_entry(request):
    dealer_name = request.POST.get('dealer_name')
    contact_no = request.POST.get('contact_no')
    dealership = request.POST.get('dealership')
    address = request.POST.get('address')
    gst_no = request.POST.get('gst_no')

    dm = time_milis()
    a = id_token(request)

    data = {
        'Dealer_Name': dealer_name,
        'Contact_No': contact_no,
        'Dealership': dealership,
        'Address': address,
        'Gst_No': gst_no

    }
    if contact_no:
        db.child('Users').child(a).child('Dealer').child(dm).set(data)
        message = "Data Insert Successfully"
        return render(request, 'shree_nilay_accounting/dealer.html', {"msg": message})
    else:
        pass
    return render(request, 'shree_nilay_accounting/dealer.html')


# retrive data

def grit_report(request):
    return render(request, 'shree_nilay_accounting/Grit_Report.html')


def Bricks_Report(request):
    return render(request, 'shree_nilay_accounting/Bricks_Report.html')


def Sand_Report(request):
    return render(request, 'shree_nilay_accounting/Sand_Report.html')


def Water_Tank_Report(request):
    return render(request, 'shree_nilay_accounting/Water_Tank_Report.html')


def Earth_Work_Report(request):
    return render(request, 'shree_nilay_accounting/Earth_Work_Report.html')


def Jcb_Report(request):
    return render(request, 'shree_nilay_accounting/Jcb_Report.html')


def Cement_Report(request):
    return render(request, 'shree_nilay_accounting/Cement_Report.html')


def Steel_Report(request):
    return render(request, 'shree_nilay_accounting/Steel_Report.html')


def Grit_Ledger(request):
    a = id_token(request)
    dealer_name = request.POST.get('dealer')
    start_date = request.POST.get('sdate')
    end_date = request.POST.get('edate')


    d = db.child("Users").child(a).child("Grit").child(dealer_name).shallow().get().val()
    mdate = []  # main date like key
    date = []
    dealer = []
    Numoftruck = []
    Vehicle_No = []
    Pass_No = []
    Weight = []
    Quality = []
    Payment = []
    flag = 0
    for i in d:
        if start_date <= i <= end_date:
            mdate.append(i)
        elif start_date > end_date:
            message = "Select Valid Date"
            flag = 1
        elif start_date == end_date:
            message = "Select Valid Date"
            flag = 1
        else:
            pass

    mdate.sort()

    for i in mdate:
        date1 = db.child("Users").child(a).child("Grit").child(dealer_name).child(i).child("Date").shallow().get().val()
        date.append(date1)

        dealer1 = db.child("Users").child(a).child("Grit").child(dealer_name).child(i).child(
            "Dealer").shallow().get().val()
        dealer.append(dealer1)

        Numoftruck1 = db.child("Users").child(a).child("Grit").child(dealer_name).child(i).child(
            "Numoftruck").shallow().get().val()
        Numoftruck.append(Numoftruck1)

        Vehicle_No1 = db.child("Users").child(a).child("Grit").child(dealer_name).child(i).child(
            "Vehicle_No").shallow().get().val()
        Vehicle_No.append(Vehicle_No1)

        Pass_No1 = db.child("Users").child(a).child("Grit").child(dealer_name).child(i).child(
            "Pass_No").shallow().get().val()
        Pass_No.append(Pass_No1)

        Weight1 = db.child("Users").child(a).child("Grit").child(dealer_name).child(i).child(
            "Weight").shallow().get().val()
        Weight.append(Weight1)

        Quality1 = db.child("Users").child(a).child("Grit").child(dealer_name).child(i).child(
            "Quality").shallow().get().val()
        Quality.append(Quality1)

        Payment1 = db.child("Users").child(a).child("Grit").child(dealer_name).child(i).child(
            "Payment").shallow().get().val()
        Payment.append(Payment1)

    total_Numoftruck = 0;
    for i in Numoftruck:
        total_Numoftruck = total_Numoftruck + int(i);

    total_weight = 0;
    for i in Weight:
        total_weight = total_weight + int(i);

    comb_list = zip(date, dealer, Vehicle_No, Pass_No, Numoftruck, Weight, Quality, Payment)

    if flag == 1:
        return render(request, 'shree_nilay_accounting/Grit_Report.html', {"Message": message})
    else:
        return render(request, 'shree_nilay_accounting/Grit_Ledger.html',
                      {"Comb_List": comb_list, "total_weight": total_weight, "total_Numoftruck": total_Numoftruck})


def Bricks_Ledger(request):
    a = id_token(request)
    dealer_name = request.POST.get('dealer')
    start_date = request.POST.get('sdate')
    end_date = request.POST.get('edate')

    d = db.child("Users").child(a).child("Bricks").child(dealer_name).shallow().get().val()
    mdate = []  # main date like key
    date = []
    dealer = []
    Numoftruck = []
    Vehicle_No = []
    Challan_No = []
    Nos = []
    Quality = []
    Payment = []
    flag = 0

    for i in d:
        if start_date <= i <= end_date:
            mdate.append(i)
        elif start_date > end_date:
            message = "Select Valid Date"
            flag = 1
        elif start_date == end_date:
            message = "Select Valid Date"
            flag = 1
        else:
            pass

    mdate.sort()

    for i in mdate:
        date1 = db.child("Users").child(a).child("Bricks").child(dealer_name).child(i).child(
            "Date").shallow().get().val()
        date.append(date1)

        dealer1 = db.child("Users").child(a).child("Bricks").child(dealer_name).child(i).child(
            "Dealer").shallow().get().val()
        dealer.append(dealer1)

        Numoftruck1 = db.child("Users").child(a).child("Bricks").child(dealer_name).child(i).child(
            "Numoftruck").shallow().get().val()
        Numoftruck.append(Numoftruck1)

        Vehicle_No1 = db.child("Users").child(a).child("Bricks").child(dealer_name).child(i).child(
            "Vehicle_No").shallow().get().val()
        Vehicle_No.append(Vehicle_No1)

        Challan_No1 = db.child("Users").child(a).child("Bricks").child(dealer_name).child(i).child(
            "Challan_No").shallow().get().val()
        Challan_No.append(Challan_No1)

        Nos1 = db.child("Users").child(a).child("Bricks").child(dealer_name).child(i).child(
            "Nos").shallow().get().val()
        Nos.append(Nos1)

        Quality1 = db.child("Users").child(a).child("Bricks").child(dealer_name).child(i).child(
            "Quality").shallow().get().val()
        Quality.append(Quality1)

        Payment1 = db.child("Users").child(a).child("Bricks").child(dealer_name).child(i).child(
            "Payment").shallow().get().val()
        Payment.append(Payment1)

    total_Numoftruck = 0;
    for i in Numoftruck:
        total_Numoftruck = total_Numoftruck + int(i);

    total_nos = 0;
    for i in Nos:
        total_nos = total_nos + int(i);

    comb_list = zip(date, dealer, Vehicle_No, Challan_No, Numoftruck, Nos, Quality, Payment)

    if flag == 1:
        return render(request, 'shree_nilay_accounting/Bricks_Report.html', {"Message": message})
    else:
        return render(request, 'shree_nilay_accounting/Bricks_Ledger.html',
                      {"Comb_List": comb_list, "total_nos": total_nos, "total_Numoftruck": total_Numoftruck})


def Sand_Ledger(request):
    a = id_token(request)
    dealer_name = request.POST.get('dealer')
    start_date = request.POST.get('sdate')
    end_date = request.POST.get('edate')

    d = db.child("Users").child(a).child("Sand").child(dealer_name).shallow().get().val()
    mdate = []  # main date like key
    date = []
    dealer = []
    Numoftruck = []
    Vehicle_No = []
    Weight = []
    Payment = []
    flag = 0

    for i in d:
        if start_date <= i <= end_date:
            mdate.append(i)
        elif start_date > end_date:
            message = "Select Valid Date"
            flag = 1
        elif start_date == end_date:
            message = "Select Valid Date"
            flag = 1
        else:
            pass

    mdate.sort()

    for i in mdate:
        date1 = db.child("Users").child(a).child("Sand").child(dealer_name).child(i).child("Date").shallow().get().val()
        date.append(date1)

        dealer1 = db.child("Users").child(a).child("Sand").child(dealer_name).child(i).child(
            "Dealer").shallow().get().val()
        dealer.append(dealer1)

        Numoftruck1 = db.child("Users").child(a).child("Sand").child(dealer_name).child(i).child(
            "Numoftruck").shallow().get().val()
        Numoftruck.append(Numoftruck1)

        Vehicle_No1 = db.child("Users").child(a).child("Sand").child(dealer_name).child(i).child(
            "Vehicle_No").shallow().get().val()
        Vehicle_No.append(Vehicle_No1)

        Weight1 = db.child("Users").child(a).child("Sand").child(dealer_name).child(i).child(
            "Weight").shallow().get().val()
        Weight.append(Weight1)

        Payment1 = db.child("Users").child(a).child("Sand").child(dealer_name).child(i).child(
            "Payment").shallow().get().val()
        Payment.append(Payment1)

    total_Numoftruck = 0;
    for i in Numoftruck:
        total_Numoftruck = total_Numoftruck + int(i);

    total_weight = 0;
    for i in Weight:
        total_weight = total_weight + int(i);

    comb_list = zip(date, dealer, Vehicle_No, Numoftruck, Weight, Payment)

    if flag == 1:
        return render(request, 'shree_nilay_accounting/Sand_Report.html', {"Message": message})
    else:
        return render(request, 'shree_nilay_accounting/Sand_Ledger.html',
                      {"Comb_List": comb_list, "total_weight": total_weight, "total_Numoftruck": total_Numoftruck})


def Water_Tank_Ledger(request):
    a = id_token(request)
    dealer_name = request.POST.get('dealer')
    start_date = request.POST.get('sdate')
    end_date = request.POST.get('edate')

    d = db.child("Users").child(a).child("Water_Tank").child(dealer_name).shallow().get().val()
    mdate = []  # main date like key
    date = []
    dealer = []
    Numofwatertank = []
    Vehicle_No = []
    DriverName = []
    Purpose = []
    flag = 0
    Payment = []

    for i in d:
        if start_date <= i <= end_date:
            mdate.append(i)
        elif start_date > end_date:
            message = "Select Valid Date"
            flag = 1
        elif start_date == end_date:
            message = "Select Valid Date"
            flag = 1
        else:
            pass

    mdate.sort()

    for i in mdate:
        date1 = db.child("Users").child(a).child("Water_Tank").child(dealer_name).child(i).child(
            "Date").shallow().get().val()
        date.append(date1)

        dealer1 = db.child("Users").child(a).child("Water_Tank").child(dealer_name).child(i).child(
            "Dealer").shallow().get().val()
        dealer.append(dealer1)

        Numofwatertank1 = db.child("Users").child(a).child("Water_Tank").child(dealer_name).child(i).child(
            "NumofWatertank").shallow().get().val()
        Numofwatertank.append(Numofwatertank1)

        Vehicle_No1 = db.child("Users").child(a).child("Water_Tank").child(dealer_name).child(i).child(
            "Vehicle_No").shallow().get().val()
        Vehicle_No.append(Vehicle_No1)

        DriverName1 = db.child("Users").child(a).child("Water_Tank").child(dealer_name).child(i).child(
            "Dirvername").shallow().get().val()
        DriverName.append(DriverName1)

        Purpose1 = db.child("Users").child(a).child("Water_Tank").child(dealer_name).child(i).child(
            "Purpose").shallow().get().val()
        Purpose.append(Purpose1)

        Payment1 = db.child("Users").child(a).child("Water_Tank").child(dealer_name).child(i).child(
            "Payment").shallow().get().val()
        Payment.append(Payment1)

    total_Numofwatertank = 0;
    for i in Numofwatertank:
        total_Numofwatertank = total_Numofwatertank + int(i)

    comb_list = zip(date, dealer, Vehicle_No, Numofwatertank, DriverName, Purpose, Payment)

    if flag == 1:
        return render(request, 'shree_nilay_accounting/Water_Tank_Report.html', {"Message": message})
    else:
        return render(request, 'shree_nilay_accounting/Water_Tank_Ledger.html',
                      {"Comb_List": comb_list, 'total_Numofwatertank': total_Numofwatertank})


def Earth_Work_Ledger(request):
    a = id_token(request)
    start_date = request.POST.get('sdate')
    end_date = request.POST.get('edate')

    d = db.child("Users").child(a).child("Earth_Work").shallow().get().val()
    mdate = []  # main date like key
    date = []
    Nos = []
    Rate = []
    Vehicle_Type = []
    Payment = []
    flag = 0

    for i in d:
        if start_date <= i <= end_date:
            mdate.append(i)
        elif start_date > end_date:
            message = "Select Valid Date"
            flag = 1
        elif start_date == end_date:
            message = "Select Valid Date"
            flag = 1
        else:
            pass

    mdate.sort()
    for i in mdate:
        date1 = db.child("Users").child(a).child("Earth_Work").child(i).child("Date").shallow().get().val()
        date.append(date1)

        Nos1 = db.child("Users").child(a).child("Earth_Work").child(i).child(
            "Nos").shallow().get().val()
        Nos.append(Nos1)

        Rate1 = db.child("Users").child(a).child("Earth_Work").child(i).child(
            "Nos").shallow().get().val()
        Rate.append(Rate1)

        Vehicle_Type1 = db.child("Users").child(a).child("Earth_Work").child(i).child(
            "vehicle_type").shallow().get().val()
        Vehicle_Type.append(Vehicle_Type1)

        Payment1 = db.child("Users").child(a).child("Earth_Work").child(i).child(
            "Payment").shallow().get().val()
        Payment.append(Payment1)

    total_nos = 0
    for i in Nos:
        total_nos = total_nos + int(i)

    total_rate = 0
    for i in Rate:
        total_rate = total_rate + int(i)

    comb_list = zip(date, Nos, Rate, Vehicle_Type, Payment)

    if flag == 1:
        return render(request, 'shree_nilay_accounting/Earth_Work_Report.html', {"Message": message})
    else:
        return render(request, 'shree_nilay_accounting/Earth_Work_Ledger.html',
                      {"Comb_List": comb_list, "total_rate": total_rate, "total_nos": total_nos})


def Jcb_Ledger(request):
    a = id_token(request)
    start_date = request.POST.get('sdate')
    end_date = request.POST.get('edate')

    d = db.child("Users").child(a).child("Jcb").shallow().get().val()
    mdate = []  # main date like key
    date = []
    Stime = []
    Etime = []
    Purpose = []
    Payment = []
    flag = 0

    for i in d:
        if start_date <= i <= end_date:
            mdate.append(i)
        elif start_date > end_date:
            message = "Select Valid Date"
            flag = 1
        elif start_date == end_date:
            message = "Select Valid Date"
            flag = 1
        else:
            pass

    mdate.sort()
    for i in mdate:
        date1 = db.child("Users").child(a).child("Jcb").child(i).child("Date").shallow().get().val()
        date.append(date1)

        Stime1 = db.child("Users").child(a).child("Jcb").child(i).child(
            "Start_Time").shallow().get().val()
        Stime.append(Stime1)

        Etime1 = db.child("Users").child(a).child("Jcb").child(i).child(
            "End_Time").shallow().get().val()
        Etime.append(Etime1)

        Purpose1 = db.child("Users").child(a).child("Jcb").child(i).child(
            "Purpose").shallow().get().val()
        Purpose.append(Purpose1)

        Payment1 = db.child("Users").child(a).child("Jcb").child(i).child(
            "Payment").shallow().get().val()
        Payment.append(Payment1)

    comb_list = zip(date, Stime, Etime, Purpose, Payment)

    if flag == 1:
        return render(request, 'shree_nilay_accounting/Jcb_Report.html', {"Message": message})
    else:
        return render(request, 'shree_nilay_accounting/Jcb_Ledger.html', {"Comb_List": comb_list})


def Cement_Ledger(request):
    a = id_token(request)
    dealer_name = request.POST.get('dealer')
    start_date = request.POST.get('sdate')
    end_date = request.POST.get('edate')

    d = db.child("Users").child(a).child("Cement").child(dealer_name).shallow().get().val()
    mdate = []  # main date like key
    date = []
    dealer = []
    NumofTruck = []
    Vehicle_No = []
    Nos = []
    Payment = []
    flag = 0

    for i in d:
        if start_date <= i <= end_date:
            mdate.append(i)
        elif start_date > end_date:
            message = "Select Valid Date"
            flag = 1
        elif start_date == end_date:
            message = "Select Valid Date"
            flag = 1
        else:
            pass

    mdate.sort()

    for i in mdate:
        date1 = db.child("Users").child(a).child("Cement").child(dealer_name).child(i).child(
            "Date").shallow().get().val()
        date.append(date1)

        dealer1 = db.child("Users").child(a).child("Cement").child(dealer_name).child(i).child(
            "Dealer").shallow().get().val()
        dealer.append(dealer1)

        NumofTruck1 = db.child("Users").child(a).child("Cement").child(dealer_name).child(i).child(
            "NumofTrucks").shallow().get().val()
        NumofTruck.append(NumofTruck1)

        Vehicle_No1 = db.child("Users").child(a).child("Cement").child(dealer_name).child(i).child(
            "Vehicle_No").shallow().get().val()
        Vehicle_No.append(Vehicle_No1)

        Nos1 = db.child("Users").child(a).child("Cement").child(dealer_name).child(i).child(
            "Nos").shallow().get().val()
        Nos.append(Nos1)

        Payment1 = db.child("Users").child(a).child("Cement").child(dealer_name).child(i).child(
            "Payment").shallow().get().val()
        Payment.append(Payment1)

    comb_list = zip(date, dealer, Vehicle_No, NumofTruck, Nos, Payment)

    if flag == 1:
        return render(request, 'shree_nilay_accounting/Cement_Report.html', {"Message": message})
    else:
        return render(request, 'shree_nilay_accounting/Cement_Ledger.html', {"Comb_List": comb_list})

    return render(request, 'shree_nilay_accounting/Cement_Ledger.html')


def Payment(request):
    material = request.POST.get('material')
    start_date = request.POST.get('sdate')
    end_date = request.POST.get('edate')
    dealer_name = request.POST.get('dealer')
    a = id_token(request)
    print(dealer_name)
    print(material)

    if dealer_name != "other":
        d = db.child("Users").child(a).child(material).child(dealer_name).shallow().get().val()
    else:
        d = db.child("Users").child(a).child(material).shallow().get().val()
    print(d)

    date = []
    Payment = "yes"
    for i in d:
        if start_date <= i and end_date >= i:
            date.append(i)
        elif start_date == end_date:
            message = "select valid date"
        else:
            message = "select valid date"

    for i in date:
        if dealer_name != "other":
            if db.child('Users').child(a).child(material).child(dealer_name).child(i).child("Payment").set(Payment):
                message = "Paid Sucessfully"
        elif dealer_name == "other":
            if db.child('Users').child(a).child(material).child(i).child("Payment").set(Payment):
                message = "Paid Sucessfully"
        else:
            pass

    return render(request, 'shree_nilay_accounting/Payment.html', {"Message": message})




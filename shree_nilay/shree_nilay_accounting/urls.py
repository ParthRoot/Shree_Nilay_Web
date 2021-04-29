from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
#from .views import GeneratePdf

urlpatterns = [
    path('', views.signIn, name="signIn"),
    path('postsign', views.postsign, name="postsign"),
    path('logout', views.logout, name="logout"),
    path('postsignup', views.postsignup, name="postsignup"),
    path('home', views.home, name="home"),
    path('about', views.about, name="about"),
    path('report', views.report, name="report"),
    path('customer_entry', views.customer_entry, name="customer_entry"),
    path('stock', views.stock, name='stock'),
    path('dealer', views.dealer, name='dealer'),
    path('payment', views.payment, name='payment'),
    path('grit', views.grit, name='grit'),
    path('bricks', views.bricks, name='bricks'),
    path('sand', views.sand, name='sand'),
    path('water_tank', views.water_tank, name='water_tank'),
    path('earth_work', views.earth_work, name='earth_work'),
    path('jcb', views.jcb, name='jcb'),
    path('cement', views.cement, name='cement'),
    path('steel', views.steel, name='steel'),
    path('water_tank', views.water_tank, name='water_tank'),
    path('earth_work', views.earth_work, name='earth_work'),

    # insert data in database
    path('grit_entry', views.grit_entry, name='grit_entry'),
    path('bricks_entry', views.bricks_entry, name='bricks_entry'),
    path('sand_entry', views.sand_entry, name='sand_entry'),
    path('jcb', views.jcb, name='jcb'),
    path('cement', views.cement, name='cement'),
    path('customer_entry1', views.customer_entry1, name='customer_entry1'),
    path('dealer_entry', views.dealer_entry, name='dealer_entry'),

    # retrive data from database
    path('grit_report', views.grit_report, name='grit_report'),
    path('Bricks_Report', views.Bricks_Report, name='Bricks_Report'),
    path('Sand_Report', views.Sand_Report, name='Sand_Report'),
    path('Water_Tank_Report', views.Water_Tank_Report, name='Water_Tank_Report'),
    path('Earth_Work_Report', views.Earth_Work_Report, name='Earth_Work_Report'),
    path('Jcb_Report', views.Jcb_Report, name='Jcb_Report'),
    path('Cement_Report', views.Cement_Report, name='Cement_Report'),
    path('Steel_Report', views.Steel_Report, name='Steel_Report'),

    # ledgers
    path('Grit_Ledger', views.Grit_Ledger, name='Grit_Ledger'),
    path('Bricks_Ledger', views.Bricks_Ledger, name='Bricks_Ledger'),
    path('Sand_Ledger', views.Sand_Ledger, name='Sand_Ledger'),
    path('Water_Tank_Ledger', views.Water_Tank_Ledger, name='Water_Tank_Ledger'),
    path('Earth_Work_Ledger', views.Earth_Work_Ledger, name='Earth_Work_Ledger'),
    path('Jcb_Ledger', views.Jcb_Ledger, name='Jcb_Ledger'),
    path('Cement_Ledger', views.Cement_Ledger, name='Cement_Ledger'),

    path('Payment', views.Payment, name='Payment'),

    #pdf



]

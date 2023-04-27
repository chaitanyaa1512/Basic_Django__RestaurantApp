from django.shortcuts import render
from .models import Food
from .models import Tables
from .models import Waiters
from .models import Orders

# Create your views here.
def index(request):
    return render(request , "index.html")

def food(request):
    return render(request , "food.html")

def table(request):
    return render(request , "table.html")

def waiter(request):
    return render(request , "waiter.html")

def order(request):
    return render(request , "order.html")


def fooddata(request):
    F_name =  request.POST['Food_Name']
    F_charge =  request.POST['Food_Charge']
    f_obj = Food(mainStreamFoodName = F_name ,subCategoryFoodCharge = F_charge )
    f_obj.save()
    obj_food = Food.objects.all()
    return render( request , "food.html",{'msg':"Data saved successfully",'objfood':obj_food})


def tabledata(request):
    T_name =  request.POST['Table_Name']
    t_obj = Tables(tableName = T_name )
    t_obj.save()
    obj_table = Tables.objects.all()
    return render( request , "table.html",{'msg':"Data saved successfully",'objtable':obj_table})



def waiterdata(request):
    W_name =  request.POST['Waiter_Name']
    w_obj = Waiters( waiterName= W_name )
    w_obj.save()
    obj_waiter = Waiters.objects.all()
    return render( request , "waiter.html",{'msg':"Data saved successfully",'objwaiter':obj_waiter})




def orderdata(request):
    F_name =  request.POST['Food_Name']
    F_price =  request.POST['Food_Price']
    F_table =  request.POST['Name_Table']
    F_waiter =  request.POST['Name_Waiter']
    b_obj = Orders( foodName= F_name ,foodPrice= F_price, nameOfTable=F_table, 
                   nameOfWaiter=F_waiter )
    b_obj.save()
    obj_book = Orders.objects.all()
    return render( request , "order.html",{'msg':"Data saved successfully",'objbook':obj_book})





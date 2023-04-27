# Basic_Django__RestaurantApp

django framework:

-pycache
contains byte code(binary code) 

-django by default supports sqlite database

-mysite is base directory or root directory

Django uses MVT architecture(Model View Template)
URL-path of entire project
Model-communicates with database
View-BLL Business Logic Layer
Template-Presentation Layer(communicates with HTML pages)
Model & Template do not interact directly to avoid threat & hacking.
Hence, this architecture helps your project to be highly secure.

-------------------------------------------------------------
-settings.py- contains entire connectivity of the project
1.Include app_name(polls) in settings.py in Installed Apps
2.Create template folder in mysite
3.Create index.html file in template
4.Import os in settings.py
5.Include template path in settings.py 
synatx:'DIRS': [os.path.join(BASE_DIR,'templates')],
________________________________________________________________
-render function sends both static as well as dynamic data
-Logic Creation:
1.Class based view
2.Function based views
--------------------------------------------------------------

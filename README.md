# OrderManagementSystem

#Nightly Build :

Prerequisite : 

      python version = 3.8.2
      Django version = 3.0.6
      Active Internet connection for Bootstrap
      Bootstrap version : 4.0
      
Summary :

        This Project provides the solution of Online Food order services, This project is capable to store various type of food and categorize them accordingly.
        
Models Used:

      1. User Model : To register user onto to web application I have used django's default User model
      2. Product Model : Product model represent the food item, it stores all the attribute that a food product can have
      3. Order Model : this model is a child model that inherit user model and product details, the combination of product and user model gives Order
      
Views :
        This project have two apps, One namely accounts and order
        The account app is responsible for registeration, login whereas Order is responsible for generating checkouts


Active Errors : 
      Unable to store JSON data (product name, Quantity), found a solution Mysql database supports JSON storage.
      
      
 Installation Guide:
              
              1. Setup your system with above mentioned requirement
              2. Download and extract the project.
                 Project can also be cloned from github in case of any package loss : https://github.com/awsomkiller/OrderManagementSystem.git
              3.Open Commandprompt / shell / terminal and get into the root directory of the project 
              4. activate virtual environment, to activate type : source env/bin/activate
                 Once the enviroment is activated
              5. Cd into orderSystem
                  you will find all django files including manage.py
              6. Now, make the migration for the database
                  command : python manage.py makemigrations
                  then : python manage.py migrate
              7. Now create a superUser to manage the project
                    python manage.py createsuperuser
                    fill all the details
              8. Now run the localserver
                  python manage.py runserver

              Now your project is running, You'll have to register product models to Operate further
              
          
             
                 

# Stozkle
Stozkle is stock management systems using Django and Bootstrap

this project is for borrow something from stock

if you want to change it to shopping website

you can change "Borrow" in file [equip](https://github.com/DreamN/Stozkle/blob/master/templates/equiplist.html) and [equip.html](https://github.com/DreamN/Stozkle/blob/master/templates/equip.html) to "Buy"

![User's Profile](http://isara.kmi.tl/Stozkle/Stozkle1.PNG)


![Item in the Store](http://isara.kmi.tl/Stozkle/Stozkle2.PNG)


![Product's detail](http://isara.kmi.tl/Stozkle/Stozkle3.png)




## To Run the app

1. python manage.py migrate

2. create superuser (python manage.py createsuperuser)

3. Run Server (python manage.py runserver)

## To add the product to stock

1. "127.0.0.0:8000/admin" and login by superuser

2. in Mystock go to member (http://127.0.0.1:8000/admin/myStock/member/)

3. create user Nick name = "Store"

4. when you want to add product to store please add product to user "Store"


# Getting started 

This is a small project ,requirements provided by Mulytic Labs .

The webapp gives following functionalities . 
* CRUD on products
* Create Category for products
* Order Products
    * Check stock and give a message if the product quantity is greater than
    * Adjust stock after order
* Generates qr code and saves as pdf . 

Here I focused backend parts, write clean human-readable codes, use django's generic classes and override them according to my usage . 

## Git repo

Use this github link to find the project.  [Github](https://github.com/DigantaBiswas/mylytic_test) 'master' branch.

## Installation
Create virtual environment . Active your vertiual env and go to project root directory where the manage.py file is located. 
Now install the requirements

```bash
pip install -r requirements.txt 
```

Now run the following commandas to initate databse for the first time as the migration files are in gitignore you will need to create them first. 

```bash
1. python manage.py makemigrations
2. python manage.py migrate
```
Now project is ready to run in your local server . use this command to run the project in local server

```bash
python manage.py runserver
```
## Populate data  (Optional)
There is a command included to populate the current data base with demo data to test . you can use it if you want before testing the orders. 

```bash
python manage.py initiate_sample_data
```

## Instructions to webapp
When you go to the home page of the web app you will find the required fields for creating a  order mentioned in the requirements in a simpliest way 
![Home Page](https://i.ibb.co/82rkssT/Screenshot-103.png)

* To order first provide name, number and emial. The products are listed in below fields . Here you will find the product name and quantity to order (default=0). 
*If you want to order someting just change the quantity then click order . Successful order will redirect you to  order list page. 

* In order page you will find the name of the customer and order time on the list items . If you click on it A details page will be opened where you can find the invoice and with a qr code where the customer information resides . 

![List Pgae](https://i.ibb.co/YXmJrLY/Screenshot-104.png)

* In details page of a order the invoice is shown . there you will find a print option . It saves the invoice in your desired folder . 
![invoice print](https://i.ibb.co/rxchwPN/Screenshot-107.png)


**This is the documantation for for ordering , the other options you will find in nav bar which are just basic functionalities works pretty straight forwoard**

import datetime, uuid
from collections import defaultdict
from flask import Flask, render_template, request, redirect, url_for, Blueprint, current_app

entries = []
blogpages = Blueprint("blogs",__name__, template_folder= "templates", static_folder="static")

@blogpages.route("/")  
def about():
    return render_template("index.html")   

@blogpages.route("/home", methods=["GET","POST"])
def home():
    #global entries_list
    if request.method == "POST":
        entry_content = request.form.get("content")     #inserting from textarea
        entry_title = request.form.get("title")
        entry_date = datetime.datetime.today().strftime("%Y-%m-%d")
        current_app.db.entries.insert_one({"title": entry_title,"content": entry_content, "date": entry_date })  #inserting records in Mongodb    #format_date = datetime.datetime.today().strptime(entry_date,"%Y-%m-%d").strftime("%b %d")
        entries.append((entry_title, entry_content,entry_date))
        print(entries) 
    list = [
            (entry["title"], entry["content"], entry["date"]) for entry in current_app.db.entries.find({})
            ]
    print(list)
    return render_template("index1.html",entries = list)  #, entries = database_list) 

@blogpages.route("/contact")  
def contactme():
    return render_template("contact.html") 

@blogpages.route("/biodata")  
def biodata():
    return render_template("my_biodata.html")   

@blogpages.route("/previousblogs")  
def blogs():
    return render_template("blogs.html")   

@blogpages.route("/calender")  
def calender():
    return render_template("calender.html")
    #return app    
        

import datetime, uuid
from collections import defaultdict
from flask import Flask, render_template, request, redirect, url_for, Blueprint, current_app

habit_list=["drink milk","excercise"]
habit_dates={}
habit_add = defaultdict(list)     #dictionary  {'2023-01-30':['drink milk','excercise' ]} 
habit_completed = []
habit_checked=[]
habit_done= defaultdict(list)       #{ "2023-01-31","exercise"}
entries = []
pages = Blueprint("habits",__name__, template_folder= "templates", static_folder="static")

@pages.route("/habit", methods=['GET','POST'])
def habit():
    habitdone =[(done["habitdone"], done["date"]) for done in current_app.db.completed.find({})] #getting data from DB ina list 
    """for y in habitdone:
        print(f"PRINTING :{y[0]} , {y[1]}")
    print(habitdone) """
    return render_template("index2.html", title = "Habit", habitdone=habitdone ) 
    
def today_at_midnight():
    today = datetime.datetime.today()
    return datetime.datetime(today.year, today.month,today.day) 

@pages.route("/add", methods=['GET','POST'])
def add():
    if request.method == "POST":
        #habit_list.append(request.form.get("habit")) #habit_entry= request.form.get(habit) #habit_list.append(habit_entry)
        habit_entry_date =  datetime.datetime.today().strftime("%Y-%m-%d")        #habit_date =today_at_midnight()
        current_app.db.habits.insert_one(
            {"_id":uuid.uuid4().hex, "date": habit_entry_date, "habitname":request.form.get("habit")} ) #tablename habits
    habitlist = [(habit["habitname"], habit["date"]) for habit in current_app.db.habits.find({})] #getting data from DB ina list 
        
    """for y in habitlist:
        print(f"PRINTING :{y[0]} , {y[1]}")
    print(habitlist)"""
    return render_template("add.html", title = "Add Habit", habits = habitlist )     #pass data to HTML
        #("home.html", habits = habit_list , title = "Habit Tracker" )

@pages.route("/dohabit", methods=['GET','POST'])
def dohabit():
    if request.method == "POST":
        habit_completed=request.form.getlist(habit)
        habit_entry_date = request.form.get("habitdate")
        habit_checked = request.form.getlist("checkboxvalue")
        if habit_entry_date == None :
            pass
        print(habit_completed)
        print(habit_entry_date)
        print(habit_checked)
        habit_id = request.form.get("habit")
        current_app.db.completed.insert_one({"date": habit_entry_date,"habitdone": habit_checked })  #tablename completed
    habitlist = [(habit["habitname"], habit["date"]) for habit in current_app.db.habits.find({})] #getting data from DB ina list 
    #habitdone =[(done["habitdone"], done["date"]) for done in current_app.db.completed.find({})] #getting data from DB ina list 
    #zip_habit_complete = zip(habitlist, habitdone)    print(zip_habit_complete)
    return render_template("dohabit.html", title = "Track Habit", habitlist=habitlist) 

"""@pages.route("/blog", methods=['GET','POST'])  
def blogs():
    if request.method == "POST":
        entry_content = request.form.get("content")     #inserting from textarea
        entry_title = request.form.get("title")
        entry_date = datetime.datetime.today().strftime("%Y-%m-%d")
        current_app.db.entries.insert_one({"title": entry_title,"content": entry_content, "date": entry_date })  #inserting records in Mongodb    #format_date = datetime.datetime.today().strptime(entry_date,"%Y-%m-%d").strftime("%b %d")
        entries.append((entry_title, entry_content,entry_date))
        print(entries) 
    list = [
            (entry["title"], entry["content"], entry["date"]) for entry in app.db.entries.find({})
            ]
    print(list)
    return render_template("index.html",title = "Microblog",entries = list)  #, entries = database_list) """

"""@blogpages.route("/about")  
def about():
    return render_template("about_me1.html")   

@blogpages.route("/biodata")  
def biodata():
    return render_template("my_biodata1.html")   

@blogpages.route("/previousblogs")  
def blogs():
    return render_template("blogs.html")   
    #return app   """ 
   

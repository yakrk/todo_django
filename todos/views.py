from django.shortcuts import render, redirect
from .models import Todo, Category
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .picklist_values import default_status, default_priority, default_pic
from datetime import date

# Create your views here.
def index(request):
    if User.is_authenticated:
        todo_lists = Todo.objects.filter(user_id = request.user.id).order_by("-status", "priority", "due_date")
        context = {
            "todo_lists" : todo_lists,
            "default_status": default_status,
            "default_priority": default_priority,
            "default_pic": default_pic
        }
        return render(request, "todos/list.html", context)
    else:
        return redirect('login')

def update_todos(request, todo_id):
    if User.is_authenticated:
        #Get options for picklists
        category = Category.objects.all()
        context = {
                    "category" : category,
                    "status": default_status,
                    "priority": default_priority,
                    "pic": default_pic
                }
        if request.method=="POST":
            todo = request.POST["new_todo"]
            status = request.POST["status"]
            priority = request.POST["priority"]
            due_date = request.POST.get("due_date",date.today)
            pic = request.POST.get("pic","me")
            category_id = request.POST["category"]
            category_obj = Category.objects.get(id=category_id)
            user_id = request.user.id
            #when updating existing todo
            if Todo.objects.filter(id= todo_id).exists():
                update_todo = Todo.objects.get(id=todo_id)
                update_todo.todo = todo
                update_todo.status = status
                update_todo.priority = priority
                update_todo.due_date = due_date
                update_todo.pic = pic
                update_todo.category = category_obj
                update_todo.save()
                messages.success(request, "Todo was updated successfully")
            #when creating new todo
            else:
                todo = Todo.objects.create(
                    todo = todo,
                    status = status,
                    priority = priority,
                    due_date = due_date,
                    pic = pic,
                    category = category_obj,
                    user_id = user_id,
                )
                messages.success(request, "New todo was added successfully")
            return render (request, "todos/update_todos.html")
            
        else:
            todo = Todo.objects.get(id = todo_id)
            context["todo"] = todo
            return render(request, "todos/update_todos.html", context)
    else:
        return redirect('login')


def update_categories(request):
    if request.method == "POST":
        new_category = request.POST["new_category"]
        Category.objects.create(category = new_category)
        messages.success(request, "New category was added successfully")
    existing_categories = Category.objects.all()
    context = {
        "categories": existing_categories,
    }
    return render(request, "todos/update_categories.html", context)

def done(request):
    todo_id = request.POST["done"]
    print(todo_id)
    if request.method == "POST":
        status_to_done = Todo.objects.get(id=todo_id)
        status_to_done.status = "Done"
        status_to_done.save()
    return redirect ('index')
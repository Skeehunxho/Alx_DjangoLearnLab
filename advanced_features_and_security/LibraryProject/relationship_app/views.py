from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView #cbv
from .models import Book #fbv
from .models import Library 
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
#cbv


# Create your views here.
def index(request):
    return HttpResponse("Hello, You're at the relationship_app index.")

#fbv
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

#cbv
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


#setup user login and logout authentication views
#login_view: Handles user login using AuthenticationForm. 
# It checks credentials, authenticates the user, 
# and redirects to the desired page upon successful login.
def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('home')  # Redirect to your desired page after login
      else:
        # Login failed
        form.add_error(None, 'Invalid username or password')
  else:
    form = AuthenticationForm()
  return render(request, 'relationship_app/login.html', {'form': form})

#logout_view: Logs out the user using logout function and redirects to the login page.
def logout_view(request):
  logout(request)
  return redirect('login')  # Redirect to login page after logout

#register_view: Handles user registration using UserCreationForm. 
# It saves the new user on successful form submission and redirects to the login page.
def register_view(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('login')  # Redirect to login page after registration
  else:
    form = UserCreationForm()
  return render(request, 'relationship_app/register.html', {'form': form})

#home_view: Renders the home page.
def home_view(request):
    return render(request, 'relationship_app/home.html')


from django.contrib.auth.decorators import user_passes_test,login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import UserProfile

#Defining user access control (Rbac)
#This code defines a function that checks if the user is an admin or a member
# and redirects them to the appropriate page.

#get_user_role: handle cases where a UserProfile might not exist:
# Returns the user's role, if it exists.
def get_user_role(user):
    try:
        return user.userprofile.role
    except ObjectDoesNotExist:
        return None
    
def is_admin(user):
    return user.is_authenticated and get_user_role(user) == 'Admin'

def is_member(user):
    return user.is_authenticated and get_user_role(user) == 'Member'

def is_librarian(user):
    return user.is_authenticated and get_user_role(user) == 'Librarian'

#These views use the "@user_passes_test" decorator to check the user's role before granting access.
#I also created the corresponding HTML templates (admin_view.html, librarian_view.html, and member_view.html)
# and placed them in your templates directory.
@user_passes_test(is_admin)
def admin_view(request):
   return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_member)
def member_view(request):
   return render(request, 'relationship_app/member_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
   return render(request, 'relationship_app/librarian_view.html')


# relationship_app/views.py

from django.shortcuts import  get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm

# raise_exception=True argument means it will raise a PermissionDenied exception
#  if the user doesn't have the required permission, instead of redirecting to the login page.
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relationship_app.book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('relationship/book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

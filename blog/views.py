from django.shortcuts import render # type: ignore
from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from blog.models import Product, Customer
from blog.forms import  CommentModelForm,CustomerForm
from django.db.models import Q # type: ignore
from django.core.paginator import Paginator # type: ignore
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    product = Product.objects.all()
    # customer = Customer.objects.all()
    # paginator = Paginator(customer,2)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    
    context = {
        'product': product,
    }
    return render(request, 'blog/index.html', context)


# def index(request):



def detail_product(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product ,
    }

    return render(request, 'blog/product-detail.html', context)


def customer_list(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()

    search_query = request.GET.get("search", "")
    customers = Customer.objects.filter(
        Q(name__icontains=search_query) | Q(email__icontains=search_query)
    )
    paginator = Paginator(customers, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    contex ={
        "customers": page_obj,
        "search_query": search_query,
        "form": form
    }
    return render(request, "blog/customers.html", contex)


def customer_details(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    context = {
        'customer': customer,
    }
    return render(request, 'blog/customer-detail.html', context)




def delete_customer(request,pk):
    customer = Customer.objects.filter(id=pk).first()
    if customer:
        customer.delete()
        return redirect('customer_list')    
    contex ={
    'customer' : customer,
       }
    return render(request,'blog/customer_list',contex)



def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'blog/customer_edit.html', {'form': form})




    





def add_comment(request, product_id):
    # product = Product.objects.get(id=product_id)
    product = get_object_or_404(Product, id=product_id)
    form = CommentModelForm()
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('detail', product_id)

    context = {
        'form': form,
        'product': product
    }

    return render(request, 'blog/detail.html', context)


# def login_logic(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home.htnl')  # Redirect to home page after login
#         else:
#             return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
#     else:
#         return render(request, 'blog/auth/login.html')

def login_logic(request):

    return render(request,'blog/auth/login.html')

def logout_logic(request):
    
    return render(request,'blog/auth/logout.html')


def register_logic(request):
    
    return render(request,'blog/auth/register.html')


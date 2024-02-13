from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from django.contrib.auth import logout

# Create your views here.

@api_view(['GET'])
def ShowAll(request):
    # products = Product.objects.all()
    user_email = request.session.get('user_email', None)
    if user_email:
        products = Product.objects.filter(user_email=user_email)
    else:
        products = Product.objects.none()
    
    serializer = ProductSerializer(products, many=True)
    # return Response(serializer.data, status=status.HTTP_200_OK)
    return render(request, 'products.html', {'products': serializer.data})

@api_view(['GET', 'POST'])
def CreateProduct(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return redirect('api:product-list')
    
    user_email = request.session.get('user_email', '')
    # return Response(serializer.data)
    return render(request, 'product_form.html', {'user_email': user_email})

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return redirect('login')

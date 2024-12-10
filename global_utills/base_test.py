from users.models import User
from rest_framework_simplejwt.tokens import AccessToken
from product.models import Product, Category
from comment.models import Comment
from uuid import uuid4

def generate_user(email=None) -> User :
    u = User.objects.create_user(
        email=f'test_{uuid4()}@gmail.com' if not email else email, # make unique email on each call
        full_name='test',
        password='test123'
    )
    return u

def generate_headers (user=None) -> dict:
    if not user :
        u = generate_user()
    else:
        u = user

    tokens =  AccessToken.for_user(u)

    return {
        'Authorization' : f"Bearer {tokens}"
    }

def generate_product() -> Product : 
    return Product.objects.create(
        title='test',
        description='test',
        quantity=10,
        discount=0,
        price=100,
        category=Category.objects.create(name='test')
    )

def generate_comment(user=None) -> Comment : 
    user = user if user else generate_user()
    comm = Comment.objects.create(
        user= user,
        product=generate_product(),
        content='test content'
    )
    comm.save()
    return comm
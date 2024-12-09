from users.models import User
from rest_framework_simplejwt.tokens import AccessToken
from product.models import Product, Category
from comment.models import Comment
from uuid import uuid4

def generate_user() -> User :
    u = User.objects.create_user(
        email=f'test_{uuid4()}@gmail.com', # make unique email on each call
        full_name='test',
        password='test123'
    )
    return u

def generate_headers () -> dict:
    u = generate_user()
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

def generate_comment() -> Comment : 
    return Comment.objects.create(
        user= generate_user(),
        product=generate_product(),
        content='test content'
    )
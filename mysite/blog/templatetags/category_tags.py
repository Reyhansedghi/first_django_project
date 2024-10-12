from django import template
from blog.models import Post
from products.models import ProductsCategory
from services.models import ServicesCategory

register = template.Library()
@register.inclusion_tag('blog/category_menu.html',takes_context=True)
def category_menu(context):
    productcategories=ProductsCategory.objects.filter(parent=None)
    servicecategories=ServicesCategory.objects.filter(parent=None)
    return{'productcategories':productcategories,'servicecategories':servicecategories,'request':context['request']}


@register.inclusion_tag('blog/post_categories.html',takes_context=True)
def post_categories(context,post):
    categories=post.product.category.all() if post.type == 'product' else post.service.category.all()
    for category in categories:
        category.parents=[]
        parent=category.parent
        while parent is not None:
            category.parents.append(parent)
            parent=parent.parent
        category.parents.reverse()
    return{'categories':categories,'request':context['request']}    
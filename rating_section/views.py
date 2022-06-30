from django.shortcuts import redirect
from django.views import generic as views

from .models import Comment
from .forms import CommentForm
from store_products.models import Product


class AddCommentView(views.View):
    form_class = CommentForm
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        product = Product.objects.get(slug=self.kwargs['slug'])
        comment = Comment(
            user_name=form.cleaned_data['user_name'],
            user_email=form.cleaned_data['user_email'],
            text=form.cleaned_data['text'],
            product=product,   
        )
        comment.save()
        return redirect('store:product details', product.slug)
    
    def form_invalid(self, form):
        pass


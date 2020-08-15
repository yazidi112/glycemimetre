from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Article
from .forms import ArticleForm
from django.shortcuts import redirect

 

def index(request):
     
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    #return render(request, 'home/index.html', {'derniers_articles': articles})
    form = ArticleForm(request.POST or None)
     
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        post = form.save(commit=False)
        post.save()
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'home/index.html', {'form': form,'articles':articles} )

def delete(request,id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('/myapp')
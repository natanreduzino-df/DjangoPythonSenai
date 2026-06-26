from django.shortcuts import render, get_object_or_404
from .models import Artigo

def index(request):
    termo_busca = request.GET.get('busca', '').strip()
    id_eixo = request.GET.get('eixo', '').strip()

    artigos = Artigo.objects.all()
    
    if termo_busca:
        artigos = artigos.filter(texto__icontains=termo_busca)
        
    if id_eixo:
        artigos = artigos.filter(eixo_id=id_eixo)

    return render(request, 'motorartigos/index.html', {"artigos": artigos})

def artigo(request, id):
    artigo_obj = get_object_or_404(Artigo, id=id)
    return render(request, 'motorartigos/artigo.html', {'artigo': artigo_obj})
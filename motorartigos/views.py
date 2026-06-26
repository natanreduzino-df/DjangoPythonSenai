from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from .models import Artigo, EixoTecnologia
from django.contrib import messages

def index(request):
    termo_busca = request.GET.get('busca', '').strip()
    id_eixo = request.GET.get('eixo', '').strip()

    artigos_lista = Artigo.objects.all().order_by('-data_publicacao')
    
    if termo_busca:
        artigos_lista = artigos_lista.filter(texto__icontains=termo_busca)
        
    if id_eixo:
        artigos_lista = artigos_lista.filter(eixo_id=id_eixo)

    artigos_recentes = Artigo.objects.all().order_by('-data_publicacao')[:4]

    paginator = Paginator(artigos_lista, 6) 
    page_number = request.GET.get('page')
    artigos = paginator.get_page(page_number)

    eixos = EixoTecnologia.objects.all()

    context = {
        "artigos": artigos,
        "artigos_recentes": artigos_recentes,
        "eixos": eixos
    }

    return render(request, 'motorartigos/index.html', context)

def artigo(request, id):
    artigo_obj = get_object_or_404(Artigo, id=id)
    return render(request, 'motorartigos/artigo.html', {'artigo': artigo_obj})

def contato(request):
    if request.method == 'POST':
        messages.success(request, "Sua mensagem foi enviada com sucesso!")
        return redirect('contato')
    return render(request, 'motorartigos/contato.html')

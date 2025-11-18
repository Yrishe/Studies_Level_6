from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView

def index(request):
    master_genes = Gene.objects.all() # query Gene table
    return render(request, 'genedata/index.html', {'master_genes': master_genes})

def gene(request, pk):
    gene = Gene.objects.get(pk=pk)
    gene.access += 1
    print("Gene record: ", pk, "access count:", str(gene.access))
    gene.save()
    master_genes = Gene.objects.all()
    return render(request, 'genedata/gene.html', {'gene': gene, 'master_genes': master_genes})

def list(request, type):
    genes = Gene.objects.filter(entity__exact=type)
    master_genes = Gene.objects.all()
    return render(request, 'genedata/list.html', {'genes': genes, 'type': type, 'master_genes': master_genes})

def poslist(request):
    genes = Gene.objects.filter(entity__exact='Chromosome').filter(sense__startswith='+')
    master_genes = Gene.objects.all()
    return render(request, 'genedata/list.html', {'genes': genes, 'type': 'PosList', 'master_genes': master_genes})

def delete(request, pk):
    GeneAttributeLink.objects.filter(gene_id=pk).delete()
    Gene.objects.filter(pk=pk).delete()
    return HttpResponseRedirect('/')

def create_ec(request):
    master_genes = Gene.objects.all()
    ecs = EC.objects.all()
    if request.method == 'POST':
        form = ECForm(request.POST)
        if form.is_valid():
            ec = EC()
            ec.ec_name = form.cleaned_data['ec_name']
            ec.save()
            return HttpResponseRedirect('/create_ec/')
        else:
            return render(request, 'genedata/ec.html', {'error': 'failed', 'ecs': ecs, 'form': form})
    else:
        form = ECForm()
    return render(request, 'genedata/ec.html', {'form': form,'ecs': ecs, 'master_genes': master_genes})

def create_gene(request):
    master_genes = Gene.objects.all()
    if request.method == 'POST':
        form = GeneForm(request.POST)
        if form.is_valid():
            gene = form.save()
            return HttpResponseRedirect('/create_gene/')
        else:
            return render(request, 'genedata/create_gene.html', {'error': 'failed', 'master_genes': master_genes, 'form': form})
    else: 
        form = GeneForm()
    return render(request, 'genedata/create_gene.html', {'form': form, 'master_genes': master_genes})


class GeneList(ListView):
    model = Gene
    context_obejct_name = 'master_genes'
    template_name = 'genedata/index.html'
    
class GeneDetail(DetailView):
    model = Gene
    context_object_name = 'gene'
    template_name = 'genedata/gene.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context
    
class GeneCreate(CreateView):
    model = Gene
    template_name = 'genedata/create_gene.html'
    form_class = GeneForm
    success_url = '/create_gene/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context
    
class GeneDelete(DeleteView):
    model = Gene
    success_url = '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context
    
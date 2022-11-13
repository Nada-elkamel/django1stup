from django.shortcuts import render
from tempfile import template
from urllib import request
from django.http import HttpResponse
from django.template import loader

def index (request):
      template =loader.get_template('CVNada.html')
      return HttpResponse (template.render())

def index1 (request):
      template =loader.get_template('competences.html')
      return HttpResponse (template.render())

def index2 (request):
      template =loader.get_template('diplome.html')
      return HttpResponse (template.render())

def index3 (request):
      template =loader.get_template('experience.html')
      return HttpResponse (template.render())

from django import template
import feedparser
import json
import requests
import time

register = template.Library()

@register.simple_tag(takes_context=True)
def cur_val(context, string):
    string = str(string)
    link = "http://www.google.com/finance/info?infotype=infoquoteall&q="
    url = link+"%s:%s" % ("BOM",string)

    u = requests.get(url)
    content = u.json()
    data = json.loads(content)
    x= json.dumps(data)
    info = data[0]
    l = float(str(info["l_fix"]).replace(",",""))
    return l

@register.simple_tag(takes_context=True)
def tot_val(context, string, qty):
    string = str(string)
    link = "http://www.google.com/finance/info?infotype=infoquoteall&q="
    url = link+"%s:%s" % ("BOM",string)

    u = requests.get(url)
    content = u.json()
    data = json.loads(content)
    x= json.dumps(data)
    info = data[0]
    l = float(str(info["l_fix"]).replace(",",""))

    return l*qty

@register.simple_tag(takes_context=True)
def tot_gl(context, string, qty, boughtat):
    string = str(string)
    link = "http://www.google.com/finance/info?infotype=infoquoteall&q="
    url = link+"%s:%s" % ("BOM",string)

    u = requests.get(url)
    content = u.json()
    data = json.loads(content)
    x= json.dumps(data)
    info = data[0]
    l = float(str(info["l_fix"]).replace(",",""))
    diff=(l-boughtat)*qty

    return diff

@register.simple_tag(takes_context=True)
def cur_gl(context, string,boughtat):
    string = str(string)
    link = "http://www.google.com/finance/info?infotype=infoquoteall&q="
    url = link+"%s:%s" % ("BOM",string)

    u = requests.get(url)
    content = u.json()
    data = json.loads(content)
    x= json.dumps(data)
    info = data[0]
    l = float(str(info["l_fix"]).replace(",",""))
    diff=(l-boughtat)

    return diff

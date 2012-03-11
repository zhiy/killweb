#!/usr/bin/env python
import random,string
def build_element(item):
    code=item["code"]
    size=item["size"]
    time=item["time"]
    type=item["type"]
    if type=="inline-css":
        return build_inline_css(size)
    elif type=="external-css":
        return build_external_css(code,size,time)
    elif type=="inline-js":
        return build_inline_js(size)
    elif type=="external-js":
        return build_external_js(code,size,time)
    elif type=="png":
        return build_png(code,size,time)
    elif type=="html-elem":
        return build_html_elem(size)
    elif type=="iframe-elem":
        return build_iframe_elem(code,size,time)
def build_head(head):
    str=""
    for item in head:
        str+=build_element(item)
    return str
def build_body(body):
    str=""
    for item in body:
        str+=build_element(item)
    return str
def random_string(n):
    return ''.join(random.choice(string.letters+ string.punctuation + string.digits) for x in range(n))
def random_name(n):
    return ''.join(random.choice(string.letters+string.digits) for x in range(n))
def build_inline_css(size):
    content=''.join("."+random_name(4)+"{}" for x in range(int(size)))
    return "<style type=\"text/css\">"+content+"</style>"
def build_inline_js(size):
    content=''.join("var "+random_name(4)+"=''" for x in range(int(size)))
    return "<script type=\"text/javascript\">"+content+"</script>"
def build_external_css(code,size,time):
    elem="<link href=/pages/%s.css?code=%s&size=%s&time=%s rel=\"stylesheet\" type=\"text/css\"/><br>" % (random_name(4),code,size,time)
    return elem
def build_external_js(code,size,time):
    elem="<script src=/pages/%s.js?code=%s&size=%s&time=%s rel=\"stylesheet\" type=\"text/javascript\"/><br>" % (random_name(4),code,size,time)
    return elem
def build_html_elem(size):
    elem="<input type=button value='damn the web'><br>"
    content=''.join(elem for x in range(int(size)))
    return content
def build_png(code,size,time):
    elem="<img src=/pages/%s.png?code=%s&size=%s&time=%s /><br>" % (random_name(4),code,size,time)
    return elem
def build_iframe_elem(code,size,time):
    elem="<iframe src='http://www.yahoo.com' width=200 heigth=200></iframe>"
    return elem
def send_png(size):
    return random_string(size)
def send_css(size):
    return random_string(size)
def send_js(size):
    return random_string(size)

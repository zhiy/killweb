#!/usr/bin/env python
import tornado.ioloop
import tornado.web
import os
import tornado.options
from utils import *
import time
import sys
tornado.options.parse_command_line()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/index.html")
class HTMLHandler(tornado.web.RequestHandler):
    def get(self,name):
        f=open("pages/"+name+".html",'r')
        content=f.read()
        f.close()
        self.set_header("Content-Type", "text/html")
        self.write(content)
class PNGHandler(tornado.web.RequestHandler):
    def get(self,data):
        size1=self.get_argument("size")
        code1=self.get_argument("code")
        time1=self.get_argument("time")
        time.sleep(int(time1))
        self.set_status(int(code1))
        self.set_header("Content-Type", "image/png")
        self.write(send_png(int(size1)))
class CSSHandler(tornado.web.RequestHandler):
    def get(self,data):
        size1=self.get_argument("size")
        code1=self.get_argument("code")
        time1=self.get_argument("time")
        time.sleep(int(time1))
        self.set_status(int(code1))
        self.set_header("Content-Type", "text/css")
        self.write(send_css(int(size1)))
class JSHandler(tornado.web.RequestHandler):
    def get(self,data):
        size1=self.get_argument("size")
        code1=self.get_argument("code")
        time1=self.get_argument("time")
        time.sleep(int(time1))
        self.set_status(int(code1))
        self.set_header("Content-Type", "application/javascript")
        self.write(send_js(int(size1)))
class PageHandler(tornado.web.RequestHandler):
    def post(self):
        data=self.process(self.request.arguments)
        head_str=build_head(data[0])
        body_str=build_body(data[1])
        fname="pages/"+random_name(10)+".html"
        f=open(fname,'w')
        head="<html><head><title>kill the web</title>"+head_str+"</head>"
        body="<body>"+body_str+"</body></html>"
        f.write(head+body)
        f.flush()
        f.close()
        self.write(fname)
    def process(self,data):
        result_map={}
        for k,v in data.iteritems():
            n=k.split("-")[1]
            key=k.split("-")[0]
            if result_map.has_key(n):
                result_map[n][key]=v[0]
            else:
                result_map[n]={}
                result_map[n][key]=v[0]
        keys = result_map.keys()
        keys.sort()
        tmp=[result_map[key] for key in keys]
        head=[]
        body=[]
        for item in tmp:
            if item["section"]=="head":
                head.append(item)
            elif item["section"]=="body":
                body.append(item)
        return [head,body]

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
    "xsrf_cookies": False,
    "debug": True,
    }
application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/gen_page", PageHandler),
    (r"/pages/(.*).png",PNGHandler),
    (r"/pages/(.*).css",CSSHandler),
    (r"/pages/(.*).js",JSHandler),
    (r"/pages/(.*).html",HTMLHandler),],**settings)

if __name__ == "__main__":
    port=int(sys.argv[1])
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()

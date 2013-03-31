# -*- coding: utf-8 -*-
import web

urls = (
	'/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")		# render 作为渲染用

class Index(object):
	def GET(self):
		return render.hello_form()

	def POST(self):
		form = web.input(name="Nobody", greet="Hello")
		greeting = "%s, %s" % (form.greet, form.name)		
		return render.index(greeting = greeting)	# 触发index.GET之后，返回render.index，并将greeting作为变量传递

if __name__ == "__main__":
	app.run()

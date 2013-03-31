# -*- coding: utf-8 -*-
import web

urls = (
	'/hello', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')		# render 作为渲染用

class index(object):
	def GET(self):
		form = web.input(name="Nobody")
		greeting = "Hello, %s" % form.name

		return render.index(greeting = greeting)	# 触发index.GET之后，返回render.index，并将greeting作为变量传递

if __name__ == "__main__":
	app.run()

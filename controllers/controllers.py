# -*- coding: utf-8 -*-
from openerp import http

# class Lesson1(http.Controller):
#     @http.route('/lesson1/lesson1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lesson1/lesson1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lesson1.listing', {
#             'root': '/lesson1/lesson1',
#             'objects': http.request.env['lesson1.lesson1'].search([]),
#         })

#     @http.route('/lesson1/lesson1/objects/<model("lesson1.lesson1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lesson1.object', {
#             'object': obj
#         })
# -*- coding: utf-8 -*-
# from odoo import http


# class Ejemplo01-holaMundo(http.Controller):
#     @http.route('/ejemplo01-hola_mundo/ejemplo01-hola_mundo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ejemplo01-hola_mundo/ejemplo01-hola_mundo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ejemplo01-hola_mundo.listing', {
#             'root': '/ejemplo01-hola_mundo/ejemplo01-hola_mundo',
#             'objects': http.request.env['ejemplo01-hola_mundo.ejemplo01-hola_mundo'].search([]),
#         })

#     @http.route('/ejemplo01-hola_mundo/ejemplo01-hola_mundo/objects/<model("ejemplo01-hola_mundo.ejemplo01-hola_mundo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ejemplo01-hola_mundo.object', {
#             'object': obj
#         })


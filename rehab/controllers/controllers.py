# from odoo import http


# class Plantilla(http.Controller):
#     @http.route('/plantilla/plantilla', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/plantilla/plantilla/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('plantilla.listing', {
#             'root': '/plantilla/plantilla',
#             'objects': http.request.env['plantilla.plantilla'].search([]),
#         })

#     @http.route('/plantilla/plantilla/objects/<model("plantilla.plantilla"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('plantilla.object', {
#             'object': obj
#         })


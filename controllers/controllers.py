# -*- coding: utf-8 -*-
from odoo import http

# class EbArchiveTasks(http.Controller):
#     @http.route('/eb_archive_tasks/eb_archive_tasks/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eb_archive_tasks/eb_archive_tasks/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('eb_archive_tasks.listing', {
#             'root': '/eb_archive_tasks/eb_archive_tasks',
#             'objects': http.request.env['eb_archive_tasks.eb_archive_tasks'].search([]),
#         })

#     @http.route('/eb_archive_tasks/eb_archive_tasks/objects/<model("eb_archive_tasks.eb_archive_tasks"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eb_archive_tasks.object', {
#             'object': obj
#         })
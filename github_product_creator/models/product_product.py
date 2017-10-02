# -*- coding: utf-8 -*-
# Copyright (C) 2016-Today: Odoo Community Association (OCA)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api, _
from openerp.tools import html_sanitize


class ProductProduct(models.Model):
    _inherit = 'product.product'

    odoo_module_version_id = fields.Many2one('odoo.module.version', 'Odoo Module')

    license = fields.Char(string='License (Manifest)', readonly=True, related="odoo_module_version_id.license", store=True)
    summary = fields.Char(string='Summary (Manifest)', readonly=True, related="odoo_module_version_id.summary", store=True)
    website = fields.Char(string='Website (Manifest)', readonly=True, related="odoo_module_version_id.website", store=True)
    external_dependencies = fields.Char(
        string='External Dependencies (Manifest)', readonly=True, related="odoo_module_version_id.external_dependencies", store=True)
    description_rst = fields.Char(
        string='RST Description (Manifest)', readonly=True, related="odoo_module_version_id.description_rst", store=True)
    description_rst_html = fields.Html(
        string='HTML the RST Description', readonly=True, related="odoo_module_version_id.description_rst_html", store=True)
    version = fields.Char(string='Version (Manifest)', readonly=True, related="odoo_module_version_id.version", store=True)
    author = fields.Char(string='Author (Manifest)', readonly=True, related="odoo_module_version_id.author", store=True)
    image = fields.Binary(string='Icon Image', reaonly=True, related="odoo_module_version_id.image", store=True)
    github_url = fields.Char(
        string='Github URL', readonly=True, related="odoo_module_version_id.github_url", store=True)

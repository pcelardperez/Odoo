# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Teachers(models.Model):
    _name = 'academy.teachers'

    name = fields.Char()
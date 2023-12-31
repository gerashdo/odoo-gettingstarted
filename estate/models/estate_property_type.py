from odoo import api, fields, models


class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Type of a property"
    _order = "secuence, name"

    name = fields.Char()
    property_ids = fields.One2many("estate.property", "property_type_id")
    secuence = fields.Integer(default=1)
    offer_ids = fields.One2many("estate.property.offer", "property_type_id")
    offer_count = fields.Integer(compute="_compute_offer_count")

    _sql_constraints = [("name_unique", "UNIQUE(name)", "The name must be unique.")]

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)

from odoo import models, fields, api

class aparcamiento (models.Model):
    _name = 'garaje.aparcamiento'
    _description = 'Permite definir las caracteristicas de un aparcamiento'
    name = fields.Char('Direccion', required=True)
    plazas = fields.Integer(string='Plazas', required=True)

    #Relaciones entre tablas
    coche_ids = fields.One2many('garaje.coche','aparcamiento_id', string='Coches')


class coche(models.Model):
    _name = 'garaje.coche'
    _description = 'Permite definir las caracteristicas del coche'
    _order = 'name'

    name = fields.Char(string='Matricula', required=True, size=7)
    modelo = fields.Char(string='Modelo', required=True)
    construido = fields.Date(string='Fecha de construccion')
    consumo = fields.Float('Consumo', (4,1),default=0.0, help='Promedio cada 100km')
    averiado = fields.Boolean(string='Averiado', default=False)
    annos = fields.Integer('Años', compute='_get_annos')
    descripcion = fields.Text('Descripcion')

    #Relaciones entre tablas
    aparcamiento_id = fields.Many2one(
        'garaje.aparcamiento',string='Aparcamiento')
    mantenimiento_id = fields.Many2many('garaje.mantenimiento',string='Mantenimientos')


    @api.depends('construido')
    def _get_annos(self):
        for coche in self:
            coche.annos = 0

class mantenimiento(models.Model):
    _name = 'garaje.mantenimiento'
    _description = 'Permite definir mantenimientos de rutina'
    _order = 'fecha'

    fecha = fields.Date('Fecha', required=True, default=fields.date.today())
    tipo = fields.Selection(string='Tipo', selection=[('l','Lavar'),('r','Revision'),('m','Mecanica'),('p','pintura')], default='l')
    coste = fields.Float('Coste', (8,2), help='Coste total de mantenimiento')

    #relaciones entre tablas
    coche_ids = fields.Many2many('garaje.coche',string='Coches')


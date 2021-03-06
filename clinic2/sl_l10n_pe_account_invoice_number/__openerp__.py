# -*- coding: utf-8 -*-
##############################################################################
#
#    Softlab Perú SAC
#    Copyright (C) 2016-TODAY Tech-Receptives(<http://www.softlabperu.com>)
#    Special Credit and Thanks to Luis Paredes :D
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name' : "Editar número de comprobante",
    'version' : "1.1",
    'depends' : ["account"],
    'author' : "Luis Paredes para Softlab Perú SAC",
    'category' : "",
    'description' :
        """
        Modificaciones para comprobates (account.invoice)

    """,
    'website' : "http://www.softlabperu.com",
    'license' : "AGPL-3",
    'init_xml' : [],
    'demo_xml' : [],
    'update_xml' : [
    ],
    'data': [
        'views/account_invoice_view.xml'
    ],
    'installable' : True,
    'active' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

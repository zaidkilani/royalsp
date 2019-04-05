# -*- coding: utf-8 -*-
{
    'name': "Base Enhancement",
    'summary': """
        Summary""",

    'description': """
        description
    """,

    'author': "author",
    'website': "website",

    'category': 'Uncategorized',
    'version': '12.0.1.0',
    'depends': ['base','contacts','sale','base_address_city','product'],

    'data': [
       'security/ir.model.access.csv',
       'views/views.xml',
       'views/delivery_place_view.xml',
       'views/container_size_view.xml',
       'views/agreement_method_view.xml',
       'views/custoemr_class_view.xml',
       'report/sale_report.xml',
       'views/customs_declaration_view.xml',
       'views/insurance_type_view.xml',
       'views/truck_type_view.xml',
       'views/weight_type_view.xml',
       'views/vessel_views.xml',
       'views/place_view.xml',
       'views/transport_type_view.xml',
       'views/line_cost_views.xml',
       'views/loading_place_view.xml',
       'views/insurance_cost_view.xml',
       'views/transport_cost_view.xml',
       'views/clearance_cost_view.xml',
       'views/sale_inquiry.xml',
       'data/data.xml',
       'views/invoice_charges.xml'
       
       
    ],
}
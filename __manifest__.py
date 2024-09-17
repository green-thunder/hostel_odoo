{
    "name": "Hostel Management",
    "author": "Nodirbek",
    "depends": ["base"],
    "data": [           
        'security/hostel_security.xml',
        'security/ir.model.access.csv',
        'views/hostel.xml',
        'views/hostel_room.xml',
        'views/hostel_amenities.xml',
        'views/hostel_categ.xml',
        'views/hostel_student.xml',
        'views/hostel_menus.xml',
        'data/data.xml',
    ],
    "installable": True, 
    "application": True, 
}
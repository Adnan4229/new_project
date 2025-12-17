{
    'name': 'School Management System',
    'version': '1.0',
    'author': '',
    'category': 'Host Project Management',

    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/student_school.xml',
        'views/teacher_school.xml',
        'views/attendence_view.xml',
        'views/class_view.xml',
        'views/exam_view.xml',
        'views/fee_view.xml',
        'views/parent_school.xml',
        'views/result_view.xml',
        'views/section_view.xml',
        'views/subject_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'new_project/static/src/css/style.css',
        ],
    },

    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
}

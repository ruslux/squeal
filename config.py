db_uri = 'mongodb://localhost:27017'
db_name = 'SPL'

to_default_recipients = [
    'Semen Smirnov <semen.smirnov@spl.co>',
    'Anton Reyman <anton.reyman@spl.co>'
]
cc_default_recipients = [
    'Artem Kharitonov <artem.kharitonov@spl.co>',
    'Andrey Suschenya <andrey.suschenya@spl.co>',
    'Ekaterina Frantskevitch <ekaterina.frantskevitch@spl.co>'
]

cc_exception_overtime = to_default_recipients + ['Ekaterina Vasilyeva <ekaterina.vasilyeva@spl.co>']
to_exception_monetization = ['Artem Kharitonov <artem.kharitonov@spl.co>']
cc_exception_monetization = ['Andrey Sushchenya <andrey.suschenya@spl.co>']

# #دسته های اصلی
# load_main_type = [
#     {"name": "رنگی", "sub_array": ["بنزین", "نفت گاز", "نفت سفید"], 'codes': ['۵۵۱۵', '۱۳۲۳', '۵۵۱۵۴']},
#     {"name": "نفت کوره", "sub_array": ["نفت کوره"], 'codes': ['۹۹۲۹۸']}
#     ]

# #نوع ارسال
# sent_type = ["تدارکات", "ارسال مستقیم", "باجه فروش", "حواله", "ارسال مستقیم - آزاد"]

# #نماینده ها
# agents = ["اکیپ درخشنده", "اکیپ هاشمیان", "اکیپ نقی و تقی"]

# #قرارداد ها
# old_deals = [
#        {'name': 'شرکت ساراد', 'id': '۴۴۱۲', 'load_name': 'پوشاک', 'start_date': '1404/01/01', 'end_date': '1404/03/31', 'fee_company': '2300', 'fee_driver': '3400', "packages": []},
#        {'name': 'شرکت امیرد', 'id': '۸۹۷۲', 'load_name': 'اوره صنعتی', 'start_date': '1404/02/15', 'end_date': '1404/03/15', 'fee_company': '4500', 'fee_driver': '5600', "packages": []}
# ]

# current_deals = [
#        {'name': 'شرکت نفت', 'id': '۷۸۰۴', 'load_name': 'نفت خام', 'start_date': '1403/01/01', 'end_date': '1404/04/31', 'fee_company': '5500', 'fee_driver': '', "packages": [{'id': '۱', 'bols': ['۲۰۱', '۲۰۲', '۲۰۳', '۲۰۴', '۲۰۵', '۲۰۶', '۲۰۷'], 'submit_date': '1404/04/17', 'payed': False}]},
#        {'name': 'شرکت پتروشیمی', 'id': '۹۸۱۲', 'load_name': 'اوره صنعتی', 'start_date': '1403/02/15', 'end_date': '1404/07/15', 'fee_company': '6100', 'fee_driver': '5100', "packages": []}
# ]

# # {"type": "register user",
# #                 "description":"فردی به نام حمید هاشمیان، درخواست ثبت نام در سامانه را دارد.",
# #                 "params": {'user': {"name":"حمید", "lastname":"هاشمیان", "phone":"09127781982", "id":"51351", "email":"hashemian_hamid@yahoo.com", "username":"hamid", "password":"234", "role":"کارمند", "lastseen_date":"1404/03/31", "lastseen_time":"2:10", "notifications":[]}},
# #                 "date": {'date': '1404/04/27', 'clock': '10:59'},
         
# #        },
# #          {"type": "credit deal",
# #                 "description":"اعتبار قرارداد شرکت نفت، رو به اتمام است!",
# #                 "params": {'deal': {'name': 'شرکت نفت', 'id': '۷۸۰۴', 'load_name': 'نفت خام', 'start_date': '1403/01/01', 'end_date': '1404/06/31', 'fee_company': '5500', 'fee_driver': '', "packages": []}},
# #                 "date": {'date': '1404/06/27', 'clock': '14:21'},
         
# #        }, 
# #          {"type": "credit smart cart driver",
# #                 "description":"اعتبار کارت هوشمند راننده، رو به اتمام است!",
# #                 "params": {'driver': {"name": "امیر",     "lastname": "زارع",    "id": "۱۲۳", "phone": "۰۹۱۲۳۴۵۶۷۸۹", "car_id": '۴۴ع۴۴۴-ایران۴۴', "smart_id": "۱۵۱۵", "licence_id": "۲۰۲۰۲۰۲۰۲۰", "start_smart_date": "1404/09/13", "end_smart_date": "1404/12/13"}},
# #                 "date": {'date': '1404/06/27', 'clock': '14:21'},
         
# #        }, 
# #          {"type": "credit smart cart car",
# #                 "description":"اعتبار کارت هوشمند نفتکش، رو به اتمام است!",
# #                 "params": {'car': {"car_id": "۲۲ب۲۴۳-ایران۵۳", "smart_car_id": "۱۶۱۶", "owner_name": "هاشم کرامتی",  "driver_name": [], "start_date": "۱۴۰۱/۱۲/۱۲", "end_date": "۱۴۰۳/۱۲/۱۲", "benzin": "۳۲۲۰۰", "sefid": "۳۲۲۰۰", "gas": "۲۹۰۰۰", "koore": "۲۷۰۰۰"},},
# #                 "date": {'date': '1404/06/27', 'clock': '14:21'},
         
# #        }, 
# #          {"type": "credit workcart",
# #                 "description":"اعتبار کارت تردد، رو به اتمام است!",
# #                 "params": {'workcart': {'driver_name': 'مهران مدیری', 'driver_id': '۳۴۵', 'car_id': '۲۲ع۲۲۲-ایران۲۲', 'start_date': '1403/12/12', 'end_date': '1404/12/12', "serial_number": '۵۵۱۳۴۵۱'}},
# #                 "date": {'date': '1404/06/27', 'clock': '14:21'},
         
# #        },
# #          {"type": "credit security",
# #                 "description":"اعتبار کارت ایمنی، رو به اتمام است!",
# #                 "params": {'security': {'driver_name': 'مهران مدیری', 'car_id': '۲۲ع۲۲۲-ایران۲۲', 'date': '1404/04/24', 'sign': 'مهدی درخشنده'}},
# #                 "date": {'date': '1404/06/27', 'clock': '14:21'},
         
# #        },
# #          {"type": "credit licence",
# #                 "description":"اعتبار گواهینامه تأیید صلاحیت، رو به اتمام است!",
# #                 "params": {'licence': {'licence_id': '۱۳۴۱۳۴۵۱۳۵', 'start_date': '1403/09/12', 'end_date': '1404/09/12', 'car_id': '۲۲ع۲۲۲-ایران۲۲', 'sign': 'مهدی درخشنده'}},
# #                 "date": {'date': '1403/11/07', 'clock': '15:34'},
         
# #        }
         
# users = [
#        {"name":"محسن", 
#      "lastname":"درخشنده", 
#      "phone":"09121016466",
#      "id":"5513534", 
#      "email":"mohsen1355@yahoo.com", 
#      "username":"mohsen", 
#      "password":"123", 
#      "role":"مدیر", 
#      "lastseen_date":"1404/04/28",
#      "lastseen_time":"16:01",
#      "notifications":[]
#     },
#     {"name":"مهدی", 
#      "lastname":"شهرآیینی", 
#      "phone":"09121209372",
#      "id":"0150298072", 
#      "email":"saradr76@yahoo.com", 
#      "username":"mehdi", 
#      "password":"234", 
#      "role":"کارمند", 
#      "lastseen_date":"1398/04/13",
#      "lastseen_time":"14:39",
#      "notifications":[]
#     },
#     {"name":"امیرمحمد", 
#      "lastname":"درخشنده", 
#      "phone":"09393368646",
#      "id":"0150298072", 
#      "email":"amirmohammadd@yahoo.com", 
#      "username":"amir", 
#      "password":"123", 
#      "role":"مدیر", 
#      "lastseen_date":"1398/07/13",
#      "lastseen_time":"11:34",
#      "notifications":[]
#     },
#     {"name":"سارا", 
#      "lastname":"درخشنده", 
#      "phone":"09121209372",
#      "id":"0150298072", 
#      "email":"saradr76@yahoo.com", 
#      "username":"sara", 
#      "password":"234", 
#      "role":"کارمند", 
#      "lastseen_date":"1401/12/09",
#      "lastseen_time":"9:18",
#      "notifications":[]
#     },
#     {"name":"سپهر", 
#      "lastname":"جندقی", 
#      "phone":"09121209372",
#      "id":"0150298072", 
#      "email":"saradr76@yahoo.com", 
#      "username":"sepehr", 
#      "password":"234", 
#      "role":"کارمند", 
#      "lastseen_date":"1404/04/02",
#      "lastseen_time":"14:14",
#      "notifications":[]
#     },
#     {"name":"کریم", 
#      "lastname":"مختاری", 
#      "phone":"09121209372",
#      "id":"0150298072", 
#      "email":"saradr76@yahoo.com", 
#      "username":"karim", 
#      "password":"234", 
#      "role":"کارمند", 
#      "lastseen_date":"1404/04/01",
#      "lastseen_time":"21:33",
#      "notifications":[]
#     },
#     {"name":"نیلا", 
#      "lastname":"سرکارات", 
#      "phone":"09234457861",
#      "id":"4860", 
#      "email":"nila@yahoo.com", 
#      "username":"nila", 
#      "password":"123", 
#      "role":"کارمند", 
#      "lastseen_date":"1404/03/30",
#      "lastseen_time":"23:11",
#      "notifications":[]
#     }
# ]

# #کاربر وارد شده
# loged_in_user = {"name":"نیلا", 
#      "lastname":"سرکارات", 
#      "phone":"09234457861",
#      "id":"4860", 
#      "email":"nila@yahoo.com", 
#      "username":"nila", 
#      "password":"123", 
#      "role":"کارمند", 
#      "lastseen_date":"1404/03/30",
#      "lastseen_time":"23:11",
#      "notifications":[]
#     }

# chats = [
#        {"sender":"sara", "receiver":"amir", "message":"سلام", "date":"1401/02/16", "time":"۱۲:۵۱", "seen":True},
#        {"sender":"mehdi", "receiver":"sepehr", "message":"پس کی میای؟", "date":"1403/04/04", "time":"۱۰:۱۰", "seen":True},
#        {"sender":"sepehr", "receiver":"sara", "message":"منتظرم جواب باشم", "date":"1402/10/23", "time":"۳:۳۱", "seen":True},
#        {"sender":"amir", "receiver":"karim", "message":"سلام", "date":"1400/11/06", "time":"۱۵:۳۰", "seen":True},
#        {"sender":"sara", "receiver":"amir", "message":"خوبی؟", "date":"1402/01/14", "time":"۷:۳۶", "seen":True},
#        {"sender":"karim", "receiver":"sepehr", "message":"سلام", "date":"1403/02/28", "time":"۱۱:۴۹", "seen":True},
#        {"sender":"mehdi", "receiver":"amir", "message":"در حال انجام کار هستم", "date":"1401/05/17", "time":"۲۰:۵۵", "seen":True},
#        {"sender":"sepehr", "receiver":"karim", "message":"پس کی میای؟", "date":"1400/12/24", "time":"۱۳:۵۷", "seen":True},
#        {"sender":"amir", "receiver":"sara", "message":"فعلاً سرکارم", "date":"1402/05/10", "time":"۸:۱۳", "seen":True},
#        {"sender":"sara", "receiver":"karim", "message":"پروژه رو شروع کردی؟", "date":"1403/03/19", "time":"۱۶:۰۲", "seen":True},
#        {"sender":"karim", "receiver":"amir", "message":"هنوز منتظرم", "date":"1402/11/17", "time":"۲۲:۵۰", "seen":True},
#        {"sender":"mehdi", "receiver":"sara", "message":"کارت چیه الان؟", "date":"1401/09/03", "time":"۱۴:۳۵", "seen":True},
#        {"sender":"sepehr", "receiver":"mehdi", "message":"عجله کن", "date":"1400/08/27", "time":"۱۷:۵۸", "seen":True},
#        {"sender":"sara", "receiver":"mehdi", "message":"امروز جلسه داریم", "date":"1401/10/05", "time":"۹:۱۷", "seen":True},
#        {"sender":"karim", "receiver":"sara", "message":"چیزی لازم نداری؟", "date":"1402/06/14", "time":"۲۱:۰۹", "seen":True},
#        {"sender":"mehdi", "receiver":"karim", "message":"کامنت گذاشتم", "date":"1401/04/26", "time":"۱۶:۴۸", "seen":True},
#        {"sender":"amir", "receiver":"sepehr", "message":"کد تصحیح شد", "date":"1403/08/20", "time":"۱:۲۱", "seen":True},
#        {"sender":"sara", "receiver":"amir", "message":"منتظرم", "date":"1402/12/29", "time":"۱۶:۳۷", "seen":True},
#        {"sender":"karim", "receiver":"mehdi", "message":"جلسه کنسل شد", "date":"1400/05/21", "time":"۸:۱۵", "seen":True},
#        {"sender":"mehdi", "receiver":"sepehr", "message":"پس کی میای؟", "date":"1402/01/20", "time":"۱۲:۰۲", "seen":True},
#        {"sender":"amir", "receiver":"sara", "message":"موفق باشی", "date":"1402/09/18", "time":"۱۰:۴۹", "seen":True},
#        {"sender":"sepehr", "receiver":"karim", "message":"پروژه رو خوندم", "date":"1401/11/22", "time":"۱۸:۴۰", "seen":True},
#        {"sender":"sara", "receiver":"sepehr", "message":"بروزرسانی رو دیدی؟", "date":"1403/10/10", "time":"۱۵:۴۷", "seen":True},
#        {"sender":"karim", "receiver":"amir", "message":"فعلاً خداحافظ", "date":"1402/02/09", "time":"۲۲:۰۶", "seen":True},
#        {"sender":"mehdi", "receiver":"sara", "message":"امروز نمیام", "date":"1401/12/14", "time":"۷:۲۷", "seen":True},
#        {"sender":"amir", "receiver":"karim", "message":"کارت عالی بود", "date":"1401/07/10", "time":"۹:۴۵", "seen":True},
#        {"sender":"sepehr", "receiver":"mehdi", "message":"جوابمو بده", "date":"1403/06/06", "time":"۱۸:۳۴", "seen":True},
#        {"sender":"karim", "receiver":"sara", "message":"مقاله رو فرستادم", "date":"1400/02/02", "time":"۱۰:۵۰", "seen":True},
#        {"sender":"mehdi", "receiver":"sepehr", "message":"پیشتاز باش", "date":"1403/03/01", "time":"۱:۱۸", "seen":True},
#        {"sender":"amir", "receiver":"mehdi", "message":"کلاس دیر شروع شد", "date":"1400/06/03", "time":"۶:۱۲", "seen":True},
#        {"sender":"sepehr", "receiver":"amir", "message":"کلیک کن", "date":"1401/08/10", "time":"۲:۰۳", "seen":True},
#        {"sender":"sara", "receiver":"karim", "message":"ادامه بده", "date":"1401/07/13", "time":"۱۶:۵۵", "seen":True},
#        {"sender":"karim", "receiver":"mehd", "message":"فراموشم شد", "date":"1402/09/28", "time":"۱۴:۱۰", "seen":True},
#        {"sender":"mehdi", "receiver":"amir", "message":"حضور دارم", "date":"1400/10/12", "time":"۱۲:۲۷", "seen":True},
#        {"sender":"amir", "receiver":"sepehr", "message":"شروع کنم؟", "date":"1401/12/05", "time":"۲۱:۳۸", "seen":True},
#        {"sender":"sara", "receiver":"amir", "message":"چه خبر؟", "date":"1400/01/17", "time":"۹:۰۹", "seen":True},
#        {"sender":"karim", "receiver":"sara", "message":"سایت بالاست", "date":"1403/02/13", "time":"۱۲:۴۴", "seen":True},
#        {"sender":"mehdi", "receiver":"amir", "message":"جلسه تموم شد", "date":"1402/05/30", "time":"۲:۵۰", "seen":True},
#        {"sender":"amir", "receiver":"karim", "message":"ممنون", "date":"1402/09/11", "time":"۱۸:۰۰", "seen":True},
#        {"sender":"sepehr", "receiver":"sara", "message":"نرم‌افزار رو اپ کردم", "date":"1401/10/14", "time":"۱:۴۶", "seen":True},
#        {"sender":"sara", "receiver":"mehd", "message":"ذخیره کن", "date":"1403/08/22", "time":"۱۰:۲۱", "seen":True},
#        {"sender":"mehdi", "receiver":"sepehr", "message":"خریدم انجام شد", "date":"1402/01/27", "time":"۵:۵۹", "seen":True},
#        {"sender":"sepehr", "receiver":"karim", "message":"ممنون", "date":"1402/02/04", "time":"۲۲:۳۰", "seen":True},
#        {"sender":"sara", "receiver":"amir", "message":"کارت درسته", "date":"1403/04/14", "time":"۱۰:۰۴", "seen":False}
# ]

#دسته های اصلی
load_main_type = [
    {"name": "رنگی", "sub_array": ["بنزین", "نفت گاز", "نفت سفید"], 'codes': ['۵۵۱۵', '۱۳۲۳', '۵۵۱۵۴']},
    {"name": "نفت کوره", "sub_array": ["نفت کوره"], 'codes': ['۹۹۲۹۸']}
    ]

#نوع ارسال
sent_type = ["تدارکات", "ارسال مستقیم", "باجه فروش", "حواله", "ارسال مستقیم - آزاد"]

#نماینده ها
agents = ["اکیپ درخشنده", "اکیپ هاشمیان", "اکیپ نقی و تقی"]

#قرارداد ها
old_deals = [
       
]

current_deals = [
       
]

         
users = [
       {"name":"نیلا", 
     "lastname":"سرکارات", 
     "phone":"09234457861",
     "id":"4860", 
     "email":"nila@yahoo.com", 
     "username":"nila", 
     "password":"123", 
     "role":"مدیر", 
     "lastseen_date":"1404/03/30",
     "lastseen_time":"23:11",
     "notifications":[]
    }
]

#کاربر وارد شده
loged_in_user = {
    }

chats = [
       
]

host="146.19.212.151"
database="derakhshandehbar"
user="amimoh"
password="Amirsara7681&@"
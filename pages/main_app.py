import customtkinter as ctk
from login_page import LoginPage
from register_page import RegisterPage
from main_dashboard import Dashboard
from register_bol_page import RegisterBol
from view_bol_page import ViewBol
from reporting_page import ReportPage
from driver_info_page import DriverInfo
from station_info_page import StationInfo
from route_info_page import RouteInfo
from splash_page import SplashPage
from car_info import CarInfo
from date import Date
from show_bol import ShowBol
from dashboar1 import Dashboard1
from register_insystemdata_page import RegisterInsystemdata
from register_deal_page import RegisterDeal
from chatbox import chatBox
from profile_page import Profile
from old_deals_page import oldDeals
from setting_page import Setting
from archived_drivers import ArchivedDrivers
from archived_cars import ArchivedCars
from bol_groups_page import BolGroups
from archived_bols import ArchivedBols
from startpoint_info_page import StartPointInfo
from car_driver_table import CarDriverTable
from dashboard2 import Dashboard2

from workcart_page import WorkcartPage
from archived_workcart import ArchivedWorkcart

from car_licence import CarLicence
from archived_licence import ArchivedLicence

from taahod_page import TaahodPage
from archived_taahod import ArchivedTaahod

from security_page import SecurityCart
from archived_security import ArchivedSecurity

import colors

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x600")
        self.title("سامانه حمل و نقل درخشنده‌بار")
        self.current_frame = None
        self.loged_in_username = None
        colors.set_theme_colors("green")
        self.show_driver_info()
    
    def clear_frame(self):
        while self.current_frame:
            self.current_frame.destroy()
            self.current_frame = None

    def show_splash(self):
        self.clear_frame()
        self.current_frame = SplashPage(self, go_to_login=self.show_login)
        self.current_frame.pack(fill="both", expand=True)
        
    def show_login(self):
        self.clear_frame()
        self.title("صفحه ورود")
        self.current_frame = LoginPage(self, go_to_register=self.show_register, go_to_dashboard=self.show_dashboard)
        self.current_frame.pack(fill="both", expand=True)

    def show_register(self):
        self.clear_frame()
        self.title("ثبت نام")
        self.current_frame = RegisterPage(self, go_to_login=self.show_login)
        self.current_frame.pack(fill="both", expand=True)

    def show_dashboard(self):
        self.clear_frame()
        self.title("منوی اصلی")
        self.current_frame = Dashboard(self, 
                                       go_to_login=self.show_login, 
                                       go_to_register_bol=self.show_register_bol,
                                       go_to_view_bol=self.show_view_bol,
                                       go_to_report=self.show_report,
                                       go_to_register_deal=self.show_register_deal,
                                       go_to_dashboard=self.show_dashboard,
                                       go_to_dashboard1=self.show_dashboard1,
                                       go_to_chat_box=self.show_chatbox,
                                       go_to_profile=self.show_profile,
                                       go_to_insystem_data=self.show_register_insystemdata,
                                       go_to_driver=self.show_driver_info,
                                       go_to_cars = self.show_car_info,
                                       go_to_security = self.show_security_cart,
                                       go_to_licence=self.car_licence,
                                       go_to_workcart=self.show_workcart_page)
        self.current_frame.pack(fill="both", expand=True)
    
    def show_dashboard1(self):
        self.title("منوی اطلاعات رانندگان و ...")
        self.clear_frame()
        self.current_frame = Dashboard1(self, 
                                        go_to_driver_info=self.show_driver_info,
                                        go_to_car_info=self.show_car_info,
                                        go_to_startpoint_info=self.show_startpoint_info,
                                        go_to_station_info=self.show_station_info,
                                        go_to_route_info=self.show_route_info,
                                        back_to_dashboard=self.show_dashboard,
                                        go_to_dashboard2=self.show_dashboard2,
                                        go_to_car_driver_assign=self.show_driver_car_assign)
        self.current_frame.pack(fill="both", expand=True)
    
    def show_dashboard2(self):
        self.title("اطلاعات چهاربرگ")
        self.clear_frame()
        self.current_frame = Dashboard2(self, 
                                        go_to_security=self.show_security_cart,
                                        go_to_licence=self.car_licence,
                                        go_to_taahod=self.show_taahod_page,
                                        go_to_workcart=self.show_workcart_page,
                                        back_to_dashboard=self.show_dashboard1)
        self.current_frame.pack(fill="both", expand=True)
    
    def car_licence(self):
        self.title("گواهینامه تأیید صلاحیت نفتکش")
        self.clear_frame()
        self.current_frame = CarLicence(self,
                                     back_to_dashboard2=self.show_dashboard2,
                                     go_to_archive = self.archived_licences,
                                     reset_page=self.car_licence)
        self.current_frame.pack(fill="both", expand=True)  
    
    def archived_licences(self):
        self.title("آرشیو گواهینامه های تأیید صلاحیت")
        self.clear_frame()
        self.current_frame = ArchivedLicence(self,
                                     back_to_licence=self.car_licence)
        self.current_frame.pack(fill="both", expand=True)  
        
    def show_workcart_page(self):
        self.title("کارت تردد")
        self.clear_frame()
        self.current_frame = WorkcartPage( self, 
                                          back_to_dashboard2=self.show_dashboard2,
                                                go_to_archive = self.archived_workcart,
                                                reset_page=self.show_workcart_page)
        self.current_frame.pack(fill="both", expand=True)
    
    def archived_workcart(self):
        self.title("آرشیو کارت های تردد")
        self.clear_frame()
        self.current_frame = ArchivedWorkcart(self,
                                     back_to_workcart=self.show_workcart_page)
        self.current_frame.pack(fill="both", expand=True)  
        
    def show_taahod_page(self):
        self.title("تعهدنامه")
        self.clear_frame()
        self.current_frame = TaahodPage( self, 
                                        back_to_dashboard2=self.show_dashboard2,
                                                go_to_archive = self.archived_taahod,
                                                reset_page=self.show_taahod_page)
        self.current_frame.pack(fill="both", expand=True)
    
    def archived_taahod(self):
        self.title("آرشیو کارت های تردد")
        self.clear_frame()
        self.current_frame = ArchivedTaahod(self,
                                     back_to_taahod=self.show_taahod_page)
        self.current_frame.pack(fill="both", expand=True)  
        
    def show_security_cart(self):
        self.title("کارت ایمنی")
        self.clear_frame()
        self.current_frame = SecurityCart( self, 
                                          back_to_dashboard2=self.show_dashboard2,
                                                go_to_archive = self.archived_security,
                                                reset_page=self.show_security_cart)
        self.current_frame.pack(fill="both", expand=True)
    
    def archived_security(self):
        self.title("آرشیو کارت های تردد")
        self.clear_frame()
        self.current_frame = ArchivedSecurity(self,
                                     back_to_security=self.show_security_cart)
        self.current_frame.pack(fill="both", expand=True)  
        
    def show_driver_car_assign(self):
        self.title("جدول راننده-نفتکش")
        self.clear_frame()
        self.current_frame = CarDriverTable( self, 
                                                go_to_dashboard1=self.show_dashboard1,
                                                reset_page=self.show_driver_car_assign)
        self.current_frame.pack(fill="both", expand=True)
        
    def show_profile(self):
        self.title("پروفایل کاربر")
        self.clear_frame()
        self.current_frame = Profile(self,
                                         go_to_dashboard=self.show_dashboard)
        self.current_frame.pack(fill="both", expand=True)
        
    def show_register_insystemdata(self):
        self.title("اطلاعات سیستمی")
        self.clear_frame()
        self.current_frame = RegisterInsystemdata(self,
                                         go_to_dashboard=self.show_dashboard,
                                         reset_page = self.show_register_insystemdata)
        self.current_frame.pack(fill="both", expand=True)
    
    
    def show_register_deal(self):
        self.title("صفحه قرارداد")
        self.clear_frame()
        self.current_frame = RegisterDeal(self,
                                         go_to_dashboard=self.show_dashboard,
                                         go_to_old_deals = self.old_deals_page,
                                         reset_page=self.show_register_deal)
        self.current_frame.pack(fill="both", expand=True)
    
    def old_deals_page(self):
        self.title("آرشیو قرارداد ها")
        self.clear_frame()
        self.current_frame = oldDeals(self,
                                         go_to_register_deal=self.show_register_deal)
        self.current_frame.pack(fill="both", expand=True)
        
    def show_register_bol(self):
        self.title("ثبت بارنامه")
        self.clear_frame()
        self.current_frame = RegisterBol(self,
                                         go_to_dashboard=self.show_dashboard, 
                                         go_to_veiw_bol=self.show_view_bol)
        self.current_frame.pack(fill="both", expand=True)
    
    def show_view_bol(self):
        self.title("بارنامه های فعال")
        self.clear_frame()
        self.current_frame = ViewBol(self,
                                         go_to_dashboard=self.show_dashboard,
                                         go_to_bol_groups = self.bol_groups,
                                         go_to_archived_bols = self.archived_bols,
                                         reset_page = self.show_view_bol)
        self.current_frame.pack(fill="both", expand=True)
        
    def show_report(self):
        self.title("گزارش‌گیری")
        self.clear_frame()
        self.current_frame = ReportPage(self,
                                         go_to_dashboard=self.show_dashboard,
                                         go_to_veiw_bol=self.show_view_bol,
                                         go_to_bol_groups = self.bol_groups,
                                         reset_page = self.show_report)
        self.current_frame.pack(fill="both", expand=True)
        
    def show_driver_info(self):
        self.title("اطلاعات راننده")
        self.clear_frame()
        self.current_frame = DriverInfo(self,
                                         go_to_dashboard1=self.show_dashboard1,
                                         go_to_archive = self.old_drivers,
                                         reset_page=self.show_driver_info)
        self.current_frame.pack(fill="both", expand=True)
        
    def show_car_info(self):
        self.title("اطلاعات نفتکش")
        self.clear_frame()
        self.current_frame = CarInfo(self,
                                         go_to_dashboard1=self.show_dashboard1,
                                         go_to_archive = self.old_cars,
                                         go_to_car_licence=self.car_licence,
                                         reset_page=self.show_car_info)
        self.current_frame.pack(fill="both", expand=True)
    
    def show_startpoint_info(self):
        self.title("اطلاعات مبدأ بارگیری")
        self.clear_frame()
        self.current_frame = StartPointInfo(self,
                                         go_to_dashboard1=self.show_dashboard1,
                                         reset_page=self.show_startpoint_info)
        self.current_frame.pack(fill="both", expand=True)
            
    def show_station_info(self):
        self.title("اطلاعات جایگاه")
        self.clear_frame()
        self.current_frame = StationInfo(self,
                                         go_to_dashboard1=self.show_dashboard1,
                                         reset_page=self.show_station_info)
        self.current_frame.pack(fill="both", expand=True)
    
    def show_route_info(self):
        self.title("اطلاعات مسیر ها")
        self.clear_frame()
        self.current_frame = RouteInfo(self,
                                         go_to_dashboard1=self.show_dashboard1,
                                         reset_page=self.show_route_info)
        self.current_frame.pack(fill="both", expand=True)
    
    def show_date(self):
        self.title("نمایش تاریخ")
        self.clear_frame()
        self.current_frame = Date(self)
        self.current_frame.pack(fill="both", expand=True)    
    
    def show_bol(self):
        self.title("نمایش بارنامه")
        self.clear_frame()
        self.current_frame = ShowBol(self, go_to_dashboard=self.show_dashboard)
        self.current_frame.pack(fill="both", expand=True)    
    
    def show_chatbox(self):
        self.title("صفحه گفت و گو")
        self.clear_frame()
        self.current_frame = chatBox(self,
                                     go_to_dashboard=self.show_dashboard)
        self.current_frame.pack(fill="both", expand=True)    
    
    def show_setting(self):
        self.title("تنظیمات")
        self.clear_frame()
        self.current_frame = Setting(self,
                                     go_to_dashboard=self.show_dashboard)
        self.current_frame.pack(fill="both", expand=True)  
    
    def old_drivers(self):
        self.title("آرشیو رانندگان")
        self.clear_frame()
        self.current_frame = ArchivedDrivers(self,
                                     go_to_drivers=self.show_driver_info,
                                     reset_page = self.old_drivers)
        self.current_frame.pack(fill="both", expand=True)  
    
    def old_cars(self):
        self.title("آرشیو نفتکش ها")
        self.clear_frame()
        self.current_frame = ArchivedCars(self,
                                     go_to_cars=self.show_car_info,
                                     reset_page = self.old_cars)
        self.current_frame.pack(fill="both", expand=True)  
    
    def bol_groups(self):
        self.title("صورت بارنامه‌ها")
        self.clear_frame()
        self.current_frame = BolGroups(self,
                                     go_to_view_bol=self.show_view_bol)
        self.current_frame.pack(fill="both", expand=True)  
    
    def archived_bols(self):
        self.title("آرشیو بارنامه ها")
        self.clear_frame()
        self.current_frame = ArchivedBols(self,
                                     back_to_view_bol=self.show_view_bol)
        self.current_frame.pack(fill="both", expand=True)  
        
if __name__ == "__main__":
    app = App()
    app.attributes("-fullscreen", True)
    app.mainloop()

#main imports
import customtkinter as ctk
import common_ctk as ck
import common_controller as cc
import psycopg2

#data imports
import bol_fake_data
import insystem_data

#colors
import colors
    
#نمایش باکس تأیید(با گزینه های بله و خیر)
def show_confirmation_box(box, yes_action, no_action, box_text, selected_data):
    confirm_box = ck.make_frame(box, 350, 100, colors.light_green_1, colors.light_green_1, None, 0, 0, 0.5, 0.5, "center")
    ck.make_label(confirm_box, 300, 30, colors.light_green_1,
                  colors.light_green_1, colors.dark_green_6, box_text,
                  0, "center", (None, 16), 0.5, 0.2, "center")

    ck.make_button(confirm_box, "بله", 70, 30, None, 10, 
                   colors.light_green_1, colors.light_green_1, colors.dark_green_6,
                   colors.green_3, yes_action, 0.35, 0.8, "center")
    ck.make_button(confirm_box, "خیر", 70, 30, None, 10, 
                   colors.light_green_1, colors.light_green_1, colors.dark_green_6,
                   colors.green_3, no_action, 0.65, 0.8, "center")
    
    return confirm_box
    

#ثبت نام راننده    
def register_driver(name, lastname, id, phone, smart_id, licence_id, start_smart_date, end_smart_date, box, reset_page):
    def save_driver_to_db(name, lastname, national_id, phone, licence_id, smart_id, start_smart_date, end_smart_date):
        try:
            conn = psycopg2.connect(
                host=insystem_data.host,
                database=insystem_data.database, 
                user=insystem_data.user,
                password=insystem_data.password
            )
            cur = conn.cursor()

            sql = """
            INSERT INTO drivers (name, lastname, national_id, phone_number, smart_id, licence_id, start_smart_date, end_smart_date)
            VALUES (%s, %s, %s, %s, %s, %s,  %s, %s)
            """
            cur.execute(sql, (
                name, 
                lastname,
                national_id,
                phone,
                smart_id,
                licence_id,
                start_smart_date,
                end_smart_date
            ))

            conn.commit()
            cur.close()
            conn.close()
            print("✅ راننده با موفقیت ذخیره شد.")
            ck.make_label(box, 200, 40, colors.dark_green_6, colors.red_color, colors.white, "✅ راننده با موفقیت ذخیره شد.", 20, None, (None, 15, "bold"), 0.9, 0.9, 'center')
        except Exception as e:
            print("❌ خطا در ذخیره‌سازی راننده:", e)
            ck.make_label(box, 200, 40, colors.dark_green_6, colors.red_color, colors.white, "❌ خطا در ذخیره‌سازی راننده:", 20, None, (None, 15, "bold"), 0.9, 0.9, 'center')
        
    label = ck.make_label(box, 150, 40, 
                          colors.dark_green_6, colors.dark_green_6, colors.red_color,
                          "", 0, None, (None, 17, "bold"), 0.9, 0.2, "e")
    if(not name.get()): ck.show_error(name, colors.dark_green_6, 1000)
    elif(not lastname.get()): ck.show_error(lastname, colors.dark_green_6, 1000)
    elif(not id.get()): ck.show_error(id, colors.dark_green_6, 1000)
    elif(not phone.get()): ck.show_error(phone, colors.dark_green_6, 1000)
    elif(not smart_id.get()): ck.show_error(smart_id, colors.dark_green_6, 1000)
    elif(not licence_id.get()): ck.show_error(licence_id, colors.dark_green_6, 1000)
    elif(start_smart_date.cget("text") == "تاریخ شروع هوشمند"): ck.show_error(start_smart_date, colors.dark_green_6, 1000)
    elif(end_smart_date.cget("text") == "تاریخ پایان هوشمند"): ck.show_error(end_smart_date, colors.dark_green_6, 1000)
    elif(cc.does_item_exist(bol_fake_data.driver_sample_data, "id", id.get())): 
        ck.show_error(id, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "راننده ای با این کد ملی، قبلا ثبت شده است!")
    elif(cc.is_phone_format(phone.get())): 
        ck.show_error(phone, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "شماره تلفن وارد شده، صحیح نیست!")
    elif(cc.does_item_exist(bol_fake_data.driver_sample_data, "smart_id", smart_id.get())): 
        ck.show_error(smart_id, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "راننده ای با این شماره هوشمند، قبلا ثبت شده است!")
    elif(cc.is_date_above(start_smart_date.cget("text"), end_smart_date.cget("text"))): 
        ck.show_error(start_smart_date, colors.dark_green_6, 1000)
        ck.show_error(end_smart_date, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "تاریخ پایان اعتبار باید بعد از تاریخ شروع باشد!")
    else:
        def do_regester():
            save_driver_to_db(
                name.get(),
                lastname.get(),
                cc.persian_to_eng_date(id.get()),
                cc.persian_to_eng_date(phone.get()),
                cc.persian_to_eng_date(smart_id.get()),
                cc.persian_to_eng_date(licence_id.get()),
                cc.persian_to_eng_date(start_smart_date.cget("text")),
                cc.persian_to_eng_date(end_smart_date.cget("text"))
            )
            box.destroy()
            #sdi
            reset_page()
        # def do_regester():
        #     bol_fake_data.driver_sample_data.append({
        #         "name": name.get(),
        #         "lastname": lastname.get(),
        #         "id": cc.persian_to_eng_date(id.get()),
        #         "phone": cc.persian_to_eng_date(phone.get()),
        #         "car_id": '',
        #         "smart_id": cc.persian_to_eng_date(smart_id.get()),
        #         "licence_id": cc.persian_to_eng_date(licence_id.get()),
        #         "start_smart_date": cc.persian_to_eng_date(start_smart_date.cget("text")),
        #         "end_smart_date": cc.persian_to_eng_date(end_smart_date.cget("text"))
        #     })
        #     box.destroy()
        #     reset_page()
            
        def cancel(): 
            confirm_box.destroy()
        
        confirm_box = show_confirmation_box(box, do_regester, cancel, "آیا از اطلاعات این راننده مطمئن هستید؟", None)
    
def edit_driver(selected, name, lastname, id, phone, smart_id, licence_id, start_smart_date, end_smart_date, box, reset_page):#
    label = ck.make_label(box, 150, 25, 
                          colors.dark_green_6, colors.dark_green_6, colors.red_color,
                          "", 0, None, (None, 13, "bold"), 0.9, 0.17, "e")
    if(not name.get()): ck.show_error(name, colors.dark_green_6, 1000)
    elif(not lastname.get()): ck.show_error(lastname, colors.dark_green_6, 1000)
    elif(not id.get()): ck.show_error(id, colors.dark_green_6, 1000)
    elif(not phone.get()): ck.show_error(phone, colors.dark_green_6, 1000)
    elif(not smart_id.get()): ck.show_error(smart_id, colors.dark_green_6, 1000)
    elif(not licence_id.get()): ck.show_error(licence_id, colors.dark_green_6, 1000)
    elif(cc.persian_to_eng_date(id.get()) != cc.persian_to_eng_date(selected["id"]) and cc.does_item_exist(bol_fake_data.driver_sample_data, "id", id.get())): 
        ck.show_error(id, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "راننده ای با این کد ملی، قبلا ثبت شده است!")
    elif(cc.persian_to_eng_date(smart_id.get()) != cc.persian_to_eng_date(selected["smart_id"]) and 
         cc.does_item_exist(bol_fake_data.driver_sample_data, "smart_id", smart_id.get())): 
        ck.show_error(smart_id, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "راننده ای با این شماره هوشمند، قبلا ثبت شده است!")
    elif(cc.is_phone_format(phone.get())): 
        ck.show_error(phone, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "شماره تلفن وارد شده، صحیح نمی‌باشد!")
    else:
        def do_edit():
            bol_fake_data.driver_sample_data.remove(selected)
            bol_fake_data.driver_sample_data.append({
                "name": name.get(),
                "lastname": lastname.get(),
                "id": cc.persian_to_eng_date(id.get()),
                "phone": cc.persian_to_eng_date(phone.get()),
                "car_id": selected['car_id'],
                "smart_id": cc.persian_to_eng_date(smart_id.get()),
                "licence_id": cc.persian_to_eng_date(licence_id.get()),
                "start_smart_date": cc.persian_to_eng_date(start_smart_date),
                "end_smart_date": cc.persian_to_eng_date(end_smart_date)
            })
            box.destroy()
            reset_page()
            
        def cancel(): 
            confirm_box.destroy()
        
        confirm_box = show_confirmation_box(box, do_edit, cancel, "آیا از اطلاعات این راننده مطمئن هستید؟", None)

def extend_smart_driver(box, text, driver):
    confirm_box = ck.make_frame(box, 400, 300, colors.light_green_1, colors.light_green_1, None, 0, 0, 0.5, 0.5, "center")
    
    label = ck.make_label(confirm_box, 150, 25, 
                          colors.light_green_1, colors.light_green_1, colors.red_color,
                          "", 0, None, (None, 13, "bold"), 0.9, 0.25, "e")
    
    ck.make_label(confirm_box, 300, 30, colors.light_green_1,
                  colors.light_green_1, colors.dark_green_6, text,
                  0, "center", (None, 22, "bold"), 0.5, 0.15, "center")

    #تاریخ شروع و پایان اعتبار هوشمند راننده
    start_smart_date = ck.make_button(confirm_box, "تاریخ شروع هوشمند", 200, 35, (None, 15), 20, 
                                    colors.gray_2, colors.light_green_1,colors.dark_green_6,colors.green_3, 
                                    lambda: ck.open_calendar(box, start_smart_date, 0.5, 0.5, colors.white), 0.5, 0.45, "center")
    
    end_smart_date = ck.make_button(confirm_box, "تاریخ پایان هوشمند", 200, 35, (None, 15), 20, 
                                    colors.gray_2, colors.light_green_1,colors.dark_green_6,colors.green_3, 
                                    lambda: ck.open_calendar(box, end_smart_date, 0.5, 0.5, colors.white), 0.5, 0.6, "center")
    
    #دکمه ثبت
    def do_extend():
        driver["start_smart_date"] = start_smart_date.cget("text")
        driver["end_smart_date"] = end_smart_date.cget("text")
        box.destroy()
    
    def cancel():
        confirm_box.destroy()
        
    def confirm_method():
        if(start_smart_date.cget("text") == "تاریخ شروع هوشمند"): ck.show_error(start_smart_date, colors.light_green_1, 1000)
        elif(end_smart_date.cget("text") == "تاریخ پایان هوشمند"): ck.show_error(end_smart_date, colors.light_green_1, 1000)
        elif(cc.is_date_above(start_smart_date.cget("text"), end_smart_date.cget("text"))): 
            ck.show_error(start_smart_date, colors.light_green_1, 1000)
            ck.show_error(end_smart_date, colors.light_green_1, 1000)
            ck.update_label_error(label, 1000, "تاریخ پایان اعتبار باید بعد از تاریخ شروع باشد!")
        else:
            tmp_box = show_confirmation_box(confirm_box, do_extend, cancel, "آیا از اطلاعات وارد شده، اطمینان دارید؟", None)
            tmp_box.configure(fg_color = colors.dark_green_6)
            tmp_box.winfo_children()[0].configure(fg_color = colors.dark_green_6, text_color = colors.light_green_1, font=(None, 21, "bold"))
            tmp_box.winfo_children()[1].configure(bg_color = colors.dark_green_6, fg_color = colors.light_green_1, text_color = colors.dark_green_6, font=(None, 18, "bold"))
            tmp_box.winfo_children()[2].configure(bg_color = colors.dark_green_6, fg_color = colors.light_green_1, text_color = colors.dark_green_6, font=(None, 18, "bold"))
    
    #دکمه ثبت  
    ck.make_button(confirm_box, "ثبت", 100, 35, (None, 22, "bold"), 20, colors.light_green_1, 
                    colors.white, colors.dark_green_6, colors.green_3, 
                    confirm_method, 
                    0.96, 0.95, "se")
    
    #دکمه بستن
    ck.make_button(confirm_box, "بستن", 100, 35, (None, 22, "bold"), 20, colors.light_green_1, 
                    colors.white, colors.dark_green_6, colors.green_3, 
                    lambda: confirm_box.destroy(), 
                    0.04, 0.95, "sw")
#ثبت نام ماشین
def register_car(car_id, car_smart_id, owner_name, start_date, end_date, benzin, sefid, gas, koore, box, reset_page):
    label = ck.make_label(box, 150, 25, 
                          colors.dark_green_6, colors.dark_green_6, colors.red_color,
                          "", 0, None, (None, 19, "bold"), 0.9, 0.2, "e")
    if(not car_id.get()): ck.show_error(car_id, colors.dark_green_6, 1000)
    elif(not car_smart_id.get()): ck.show_error(car_smart_id, colors.dark_green_6, 1000)
    elif(not owner_name.get()): ck.show_error(owner_name, colors.dark_green_6, 1000)
    elif(start_date.cget("text") == "تاریخ صدور"): ck.show_error(start_date, colors.dark_green_6, 1000)
    elif(end_date.cget("text") == "تاریخ انقضا"): ck.show_error(end_date, colors.dark_green_6, 1000)
    elif(not benzin.get()): ck.show_error(benzin, colors.dark_green_6, 1000)
    elif(not sefid.get()): ck.show_error(sefid, colors.dark_green_6, 1000)
    elif(not gas.get()): ck.show_error(gas, colors.dark_green_6, 1000)
    elif(not koore.get()): ck.show_error(koore, colors.dark_green_6, 1000)
    elif(not cc.car_id_format_is_right(car_id.get())): 
        ck.show_error(car_id, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "شماره پلاک وارد شده، صحیح نمی‌باشد!")
    elif(cc.does_item_exist(bol_fake_data.car_sample_data, "smart_car_id", car_smart_id.get())): 
        ck.show_error(car_smart_id, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "نفتکشی با این شماره هوشمند، قبلا ثبت شده است!")
    elif(cc.is_date_above(start_date.cget("text"), end_date.cget("text"))): 
        ck.show_error(start_date, colors.dark_green_6, 1000)
        ck.show_error(end_date, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "تاریخ پایان اندازه‌گیری، باید بعد از تاریخ شروع باشد!")
    else:
        def do_delete():
            bol_fake_data.car_sample_data.append({
                "car_id": car_id.get(),
                "smart_car_id": cc.persian_to_eng_date(car_smart_id.get()),
                "owner_name": owner_name.get(),
                "driver_name": [],
                "start_date": cc.persian_to_eng_date(start_date.cget("text")),
                "end_date": cc.persian_to_eng_date(end_date.cget("text")),
                "benzin": cc.persian_to_eng_date(benzin.get()),
                "sefid": cc.persian_to_eng_date(sefid.get()),
                "gas": cc.persian_to_eng_date(gas.get()),
                "koore": cc.persian_to_eng_date(koore.get())
            })
            box.destroy()
            reset_page()
            
        def cancel(): 
            confirm_box.destroy()
        
        confirm_box = show_confirmation_box(box, do_delete, cancel, "آیا از اطلاعات این نفتکش مطمئن هستید؟", None)
    
def edit_car(selected_data, car_id, car_smart_id, owner_name, start_date, end_date, benzin, sefid, gas, koore, box, reset_page):
    label = ck.make_label(box, 150, 25, 
                    colors.dark_green_6, colors.dark_green_6, colors.red_color,
                    "", 0, None, (None, 19, "bold"), 0.97, 0.17, "e")
    
    if(not car_id.get()): ck.show_error(car_id, colors.dark_green_6, 1000)
    elif(not car_smart_id.get()): ck.show_error(car_smart_id, colors.dark_green_6, 1000)
    elif(not owner_name.get()): ck.show_error(owner_name, colors.dark_green_6, 1000)
    elif(start_date.cget("text") == "تاریخ صدور"): ck.show_error(start_date, colors.dark_green_6, 1000)
    elif(end_date.cget("text") == "تاریخ انقضا"): ck.show_error(end_date, colors.dark_green_6, 1000)
    elif(not benzin.get()): ck.show_error(benzin, colors.dark_green_6, 1000)
    elif(not sefid.get()): ck.show_error(sefid, colors.dark_green_6, 1000)
    elif(not gas.get()): ck.show_error(gas, colors.dark_green_6, 1000)
    elif(not koore.get()): ck.show_error(koore, colors.dark_green_6, 1000)
    elif(not cc.car_id_format_is_right(car_id.get())): 
        ck.show_error(car_id, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "شماره پلاک وارد شده، صحیح نمی‌باشد!")
    elif(cc.persian_to_eng_date(car_smart_id.get()) != cc.persian_to_eng_date(selected_data["smart_car_id"]) and cc.does_item_exist(
        bol_fake_data.car_sample_data, "smart_car_id", car_smart_id.get()
    )):
        ck.show_error(car_smart_id, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "شماره هوشنمد، قبلا ثبت شده است!")
    elif(cc.is_date_above(start_date.cget("text"), end_date.cget("text"))): 
        ck.show_error(start_date, colors.dark_green_6, 1000)
        ck.show_error(end_date, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "تاریخ پایان اندازه‌گیری، باید بعد از تاریخ شروع باشد!")
    else:
        def do_edit():
            bol_fake_data.car_sample_data.remove(selected_data)
            bol_fake_data.car_sample_data.append({
                "car_id": car_id.get(),
                "smart_car_id": car_smart_id.get(),
                "owner_name": owner_name.get(),
                "driver_name": selected_data['driver_name'],
                "start_date": cc.persian_to_eng_date(start_date.cget("text")),
                "end_date": cc.persian_to_eng_date(end_date.cget("text")),
                "benzin": cc.persian_to_eng_date(benzin.get()),
                "sefid": cc.persian_to_eng_date(sefid.get()),
                "gas": cc.persian_to_eng_date(gas.get()),
                "koore": cc.persian_to_eng_date(koore.get())
            })
            box.destroy()
            reset_page()
            
        def cancel(): 
            confirm_box.destroy()
        
        confirm_box = show_confirmation_box(box, do_edit, cancel, "آیا از اطلاعات این نفتکش مطمئن هستید؟", None)
        
#ثبت جایگاه
def register_station(id, name, address, box, reset_page):
    label = ck.make_label(box, 150, 25, 
                          colors.dark_green_6, colors.dark_green_6, colors.red_color,
                          "", 0, None, (None, 19, "bold"), 0.9, 0.68, "e")
    if(not id.get()): ck.show_error(id, colors.dark_green_6, 1000)
    elif(not name.get()): ck.show_error(name, colors.dark_green_6, 1000)
    elif(not address.get()): ck.show_error(address, colors.dark_green_6, 1000)
    elif(cc.does_item_exist(bol_fake_data.station_sample_data, "id", id.get())):
        ck.show_error(id, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "جایگاه با کد وارد شده، قبلا ثبت شده است!")
    else:
        def do_register():
            bol_fake_data.station_sample_data.append({
                "id": cc.persian_to_eng_date(id.get()),
                "name": cc.persian_to_eng_date(name.get()),
                "address": cc.persian_to_eng_date(address.get())
            })
            box.destroy()
            reset_page()
            
        def cancel(): 
            confirm_box.destroy()
        
        confirm_box = show_confirmation_box(box, do_register, cancel, "آیا از اطلاعات این جایگاه، مطمئن هستید؟", None)

def edit_station(selected_data, id, name, address, box, reset_page):
    label = ck.make_label(box, 150, 25, 
                    colors.dark_green_6, colors.dark_green_6, colors.red_color,
                    "", 0, None, (None, 19, "bold"), 0.97, 0.7, "e")
    
    if(not id.get()): ck.show_error(id, colors.dark_green_6, 1000)
    elif(not name.get()): ck.show_error(name, colors.dark_green_6, 1000)
    elif(not address.get()): ck.show_error(address, colors.dark_green_6, 1000)
    elif(cc.persian_to_eng_date(id.get()) != cc.persian_to_eng_date(selected_data["id"]) and cc.does_item_exist(
        bol_fake_data.station_sample_data, "id", id.get()
    )):
        ck.show_error(id, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "جایگاه با کد وارد شده، قبلا ثبت شده است!")
    else:
        def do_edit():
            for item in bol_fake_data.station_sample_data:
                if(item["id"] == selected_data["id"]):
                    bol_fake_data.station_sample_data.remove(item)
                    bol_fake_data.station_sample_data.append({
                        "id": cc.persian_to_eng_date(id.get()),
                        "name": name.get(),
                        "address": address.get()
                    })
            box.destroy()
            reset_page()
            
        def cancel(): 
            confirm_box.destroy()
        
        confirm_box = show_confirmation_box(box, do_edit, cancel, "آیا از اطلاعات این جایگاه، مطمئن هستید؟", None)
        
#ثبت مسیر
def register_route(start, end, distance, rate, decrement, id, box, reset_page):
    if(not start.get()): ck.show_error(start, colors.dark_green_6, 1000)
    elif(not end.get()): ck.show_error(end, colors.dark_green_6, 1000)
    elif(not distance.get()): ck.show_error(distance, colors.dark_green_6, 1000)
    elif(not rate.get()): ck.show_error(rate, colors.dark_green_6, 1000)
    elif(not decrement.get()): ck.show_error(decrement, colors.dark_green_6, 1000)
    else:
        if(not id.get()): 
            id.delete(0, 'end')
            id.insert(0, 'فاقد کد')
        def do_register():
            bol_fake_data.route_sample_data.append({
                "start": start.get(),
                "end": end.get(),
                "distance": cc.persian_to_eng_date(distance.get()),
                "rate": cc.persian_to_eng_date(rate.get()),
                "decremente": cc.persian_to_eng_date(decrement.get()),
                "id": cc.eng_to_persian_date(id.get())
            })
            box.destroy()
            reset_page()
            
        def cancel(): 
            confirm_box.destroy()
        
        confirm_box = show_confirmation_box(box, do_register, cancel, "آیا از اطلاعات این مسیر، مطمئن هستید؟", None)

def edit_route(selected_data, start, end, distance, rate, decrement, id, box, reset_page):
    if(not start.get()): ck.show_error(start, colors.dark_green_6, 1000)
    elif(not end.get()): ck.show_error(end, colors.dark_green_6, 1000)
    elif(not distance.get()): ck.show_error(distance, colors.dark_green_6, 1000)
    elif(not rate.get()): ck.show_error(rate, colors.dark_green_6, 1000)
    elif(not decrement.get()): ck.show_error(decrement, colors.dark_green_6, 1000)
    else:
        def do_edit():
            bol_fake_data.route_sample_data.remove(selected_data)
            bol_fake_data.route_sample_data.append({
                "start": start.get(),
                "end": end.get(),
                "distance": cc.persian_to_eng_date(distance.get()),
                "rate": cc.persian_to_eng_date(rate.get()),
                "decremente": cc.persian_to_eng_date(decrement.get()),
                "id": cc.eng_to_persian_date(id.get())
            })
            box.destroy()
            reset_page()
            
        def cancel(): 
            confirm_box.destroy()
        
        confirm_box = show_confirmation_box(box, do_edit, cancel, "آیا از اطلاعات این مسیر، مطمئن هستید؟", None)

      
#ثبت مبدأ
def register_startpoint(name, id, address, deal_name, deal_id, box, reset_page):
    if(not id.get()): ck.show_error(id, colors.dark_green_6, 1000)
    elif(not name.get()): ck.show_error(name, colors.dark_green_6, 1000)
    elif(not deal_name.get()): ck.show_error(deal_name, colors.dark_green_6, 1000)
    elif(not deal_id.get()): ck.show_error(deal_id, colors.dark_green_6, 1000)
    else:
        def do_register():
            if(address.get() == None or address.get() == ''): text = '-'
            else: text = address.get()
            bol_fake_data.startpoint_sample_data.append({
                "id": cc.eng_to_persian_date(id.get()),
                "name": name.get(),
                "address": text,
                "deal": {"name": deal_name.get(), 'id': cc.eng_to_persian_date(deal_id.get())}
            })
            box.destroy()
            reset_page()
            
        def cancel(): 
            confirm_box.destroy()
        
        confirm_box = show_confirmation_box(box, do_register, cancel, "آیا از اطلاعات این مبدأ مطمئن هستید؟", None)

def edit_startpoint(selected_data, name, id, address, deal_name, deal_id, box, reset_page):
    if(not name.get()): ck.show_error(name, colors.dark_green_6, 1000)
    elif(not id.get()): ck.show_error(id, colors.dark_green_6, 1000)
    elif(not address.get()): ck.show_error(address, colors.dark_green_6, 1000)
    elif(not deal_name.get()): ck.show_error(deal_name, colors.dark_green_6, 1000)
    elif(not deal_id.get()): ck.show_error(deal_id, colors.dark_green_6, 1000)
    else:
        def do_edit():
            bol_fake_data.startpoint_sample_data.remove(selected_data)
            bol_fake_data.startpoint_sample_data.append({
                "id": cc.eng_to_persian_date(id.get()),
                "name": name.get(),
                "address": address.get(),
                "deal": {"name": deal_name.get(), 'id': cc.eng_to_persian_date(deal_id.get())}
            })
            box.destroy()
            reset_page()
            
        def cancel(): 
            confirm_box.destroy()
        
        confirm_box = show_confirmation_box(box, do_edit, cancel, "آیا از اطلاعات این مبدأ، مطمئن هستید؟", None)

def edit_deal(selected_data, company_name, deal_id, load_name, fee_company, fee_driver, start_date, end_date, box, reset_page):
    if(not company_name.get()): ck.show_error(company_name, colors.dark_green_6, 1000)
    elif(not deal_id.get()): ck.show_error(deal_id, colors.dark_green_6, 1000)
    elif(not load_name.get()): ck.show_error(load_name, colors.dark_green_6, 1000)
    elif(not start_date.cget('text')): ck.show_error(start_date, colors.dark_green_6, 1000)
    elif(not end_date.cget('text')): ck.show_error(end_date, colors.dark_green_6, 1000)
    else:
        def do_edit():
            insystem_data.current_deals.remove(selected_data)
            insystem_data.current_deals.append({
                "name": company_name.get(),
                "id": cc.eng_to_persian_date(deal_id.get()),
                "load_name": load_name.get(),
                "start_date": start_date.cget('text'),
                "end_date": end_date.cget('text'),
                "fee_company": cc.persian_to_eng_date(fee_company.get()),
                "fee_driver": cc.persian_to_eng_date(fee_driver.get()),
                "packages": selected_data['packages']
            })
            box.destroy()
            reset_page()
            
        def cancel(): 
            confirm_box.destroy()
        
        confirm_box = show_confirmation_box(box, do_edit, cancel, "آیا از اطلاعات این قرارداد، مطمئن هستید؟", None)

def extend_licence(box, text, car):
    confirm_box = ck.make_frame(box, 400, 300, colors.light_green_1, colors.light_green_1, None, 0, 0, 0.5, 0.5, "center")
    
    label = ck.make_label(confirm_box, 150, 25, 
                          colors.light_green_1, colors.light_green_1, colors.red_color,
                          "", 0, None, (None, 13, "bold"), 0.9, 0.25, "e")
    
    ck.make_label(confirm_box, 300, 30, colors.light_green_1,
                  colors.light_green_1, colors.dark_green_6, text,
                  0, "center", (None, 22, "bold"), 0.5, 0.15, "center")

    #تاریخ شروع و پایان اعتبار هوشمند راننده
    start_smart_date = ck.make_button(confirm_box, "تاریخ شروع اعتبار", 200, 35, (None, 15), 20, 
                                    colors.gray_2, colors.light_green_1,colors.dark_green_6,colors.green_3, 
                                    lambda: ck.open_calendar(box, start_smart_date, 0.5, 0.5, colors.white), 0.5, 0.45, "center")
    
    end_smart_date = ck.make_button(confirm_box, "تاریخ پایان اعتبار", 200, 35, (None, 15), 20, 
                                    colors.gray_2, colors.light_green_1,colors.dark_green_6,colors.green_3, 
                                    lambda: ck.open_calendar(box, end_smart_date, 0.5, 0.5, colors.white), 0.5, 0.6, "center")
    
    #دکمه ثبت
    def do_extend():
        car["start_date"] = start_smart_date.cget("text")
        car["end_date"] = end_smart_date.cget("text")
        box.destroy()
    
    def cancel():
        confirm_box.destroy()
        
    def confirm_method():
        if(start_smart_date.cget("text") == "تاریخ شروع اعتبار"): ck.show_error(start_smart_date, colors.light_green_1, 1000)
        elif(end_smart_date.cget("text") == "تاریخ پایان اعتبار"): ck.show_error(end_smart_date, colors.light_green_1, 1000)
        elif(cc.is_date_above(start_smart_date.cget("text"), end_smart_date.cget("text"))): 
            ck.show_error(start_smart_date, colors.light_green_1, 1000)
            ck.show_error(end_smart_date, colors.light_green_1, 1000)
            ck.update_label_error(label, 1000, "تاریخ پایان اعتبار باید بعد از تاریخ شروع باشد!")
        else:
            tmp_box = show_confirmation_box(confirm_box, do_extend, cancel, "آیا از اطلاعات وارد شده، اطمینان دارید؟", None)
            tmp_box.configure(fg_color = colors.dark_green_6)
            tmp_box.winfo_children()[0].configure(fg_color = colors.dark_green_6, text_color = colors.light_green_1, font=(None, 21, "bold"))
            tmp_box.winfo_children()[1].configure(bg_color = colors.dark_green_6, fg_color = colors.light_green_1, text_color = colors.dark_green_6, font=(None, 18, "bold"))
            tmp_box.winfo_children()[2].configure(bg_color = colors.dark_green_6, fg_color = colors.light_green_1, text_color = colors.dark_green_6, font=(None, 18, "bold"))
    
    #دکمه ثبت  
    ck.make_button(confirm_box, "ثبت", 100, 35, (None, 22, "bold"), 20, colors.light_green_1, 
                    colors.white, colors.dark_green_6, colors.green_3, 
                    confirm_method, 
                    0.96, 0.95, "se")
    
    #دکمه بستن
    ck.make_button(confirm_box, "بستن", 100, 35, (None, 22, "bold"), 20, colors.light_green_1, 
                    colors.white, colors.dark_green_6, colors.green_3, 
                    lambda: confirm_box.destroy(), 
                    0.04, 0.95, "sw")

def register_security(driver_name, car_id, date, sign, register_box, reset_page):
    label = ck.make_label(register_box, 150, 30, 
                          colors.dark_green_6, colors.dark_green_6, colors.red_color,
                          "", 0, None, (None, 17, "bold"), 0.9, 0.245, "e")
    if(not driver_name.get()): ck.show_error(driver_name, colors.dark_green_6, 1000)
    elif(not car_id.get()): ck.show_error(car_id, colors.dark_green_6, 1000)
    elif(date.cget('text') == 'تاریخ صدور'): ck.show_error(date, colors.dark_green_6, 1000)
    elif(not sign.get()): ck.show_error(sign, colors.dark_green_6, 1000)
    elif(not cc.car_id_format_is_right(car_id.get())): 
        ck.show_error(car_id, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "شماره پلاک وارد شده، صحیح نمی‌باشد!")
    elif(not cc.does_item_exist(bol_fake_data.car_sample_data, "car_id", car_id.get())): 
        ck.show_error(car_id, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "نفتکشی با این شماره پلاک در سامانه ثبت نشده است!")
    else:
        def do_register():
            bol_fake_data.security.append({
                "driver_name": cc.eng_to_persian_date(driver_name.get()),
                "car_id": cc.eng_to_persian_date(car_id.get()),
                "date": cc.eng_to_persian_date(date.cget('text')),
                "sign": cc.eng_to_persian_date(sign.get()),
            })
            register_box.destroy()
            reset_page()
            
        def cancel(): 
            confirm_box.destroy()
        
        confirm_box = show_confirmation_box(register_box, do_register, cancel, "آیا از اطلاعات این کارت ایمنی، مطمئن هستید؟", None)
    
def register_licence(licence_id, start_date, end_date, car_id, sign, register_box, reset_page):
    label = ck.make_label(register_box, 150, 40, 
                          colors.dark_green_6, colors.dark_green_6, colors.red_color,
                          "", 0, None, (None, 17, "bold"), 0.9, 0.2, "e")
    if(not licence_id.get()): ck.show_error(licence_id, colors.dark_green_6, 1000)
    elif(start_date.cget('text') == 'تاریخ صدور'): ck.show_error(start_date, colors.dark_green_6, 1000)
    elif(end_date.cget('text') == 'تاریخ انقضا'): ck.show_error(end_date, colors.dark_green_6, 1000)
    elif(not car_id.get()): ck.show_error(car_id, colors.dark_green_6, 1000)
    elif(not sign.get()): ck.show_error(sign, colors.dark_green_6, 1000)
    elif(not cc.car_id_format_is_right(car_id.get())): 
        ck.show_error(car_id, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "شماره پلاک وارد شده، صحیح نمی‌باشد!")
    elif(cc.does_item_exist(bol_fake_data.car_licence, "car_id", car_id.get())): 
        ck.show_error(car_id, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "گواهی‌ای برای این نفتکش، قبلا ثبت شده است!")
    elif(not cc.does_item_exist(bol_fake_data.car_sample_data, "car_id", car_id.get())): 
        ck.show_error(car_id, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "نفتکشی با این شماره پلاک در سامانه ثبت نشده است!")
    elif(cc.is_date_above(start_date.cget("text"), end_date.cget("text"))): 
        ck.show_error(start_date, colors.dark_green_6, 1000)
        ck.show_error(end_date, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "تاریخ پایان اعتبار باید بعد از تاریخ شروع باشد!")
    else:
        def do_register():
            bol_fake_data.car_licence.append({
                "licence_id": cc.eng_to_persian_date(licence_id.get()),
                "start_date": cc.eng_to_persian_date(start_date.cget('text')),
                "end_date": cc.eng_to_persian_date(end_date.cget('text')),
                "car_id": cc.eng_to_persian_date(car_id.get()),
                "sign": sign.get()
            })
            register_box.destroy()
            reset_page()
            
        def cancel(): 
            confirm_box.destroy()
        
        confirm_box = show_confirmation_box(register_box, do_register, cancel, "آیا از اطلاعات این گواهینامه، مطمئن هستید؟", None)

def register_taahod(name, car_id, security_number, register_box, reset_page):
    label = ck.make_label(register_box, 150, 40, 
                          colors.dark_green_6, colors.dark_green_6, colors.red_color,
                          "", 0, None, (None, 17, "bold"), 0.9, 0.2, "e")
    if(not name.get()): ck.show_error(name, colors.dark_green_6, 1000)
    elif(not car_id.get()): ck.show_error(car_id, colors.dark_green_6, 1000)
    elif(not security_number.get()): ck.show_error(security_number, colors.dark_green_6, 1000)
    elif(not cc.car_id_format_is_right(car_id.get())): 
        ck.show_error(car_id, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "شماره پلاک وارد شده، صحیح نمی‌باشد!")
    elif(not cc.does_item_exist(bol_fake_data.car_sample_data, "car_id", car_id.get())): 
        ck.show_error(car_id, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "نفتکشی با این شماره پلاک در سامانه ثبت نشده است!")
    else:
        def do_register():
            bol_fake_data.taahod.append({
                "driver_name": cc.eng_to_persian_date(name.get()),
                "car_id": cc.eng_to_persian_date(car_id.get()),
                'security_num': cc.eng_to_persian_date(security_number.get())
            })
            register_box.destroy()
            reset_page()
            
        def cancel(): 
            confirm_box.destroy()
        
        confirm_box = show_confirmation_box(register_box, do_register, cancel, "آیا از اطلاعات این تعهدنامه، مطمئن هستید؟", None)
    
def register_workcart(name, id, car_id, start_date, end_date, serial_number, register_box, reset_page):
    label = ck.make_label(register_box, 150, 40, 
                          colors.dark_green_6, colors.dark_green_6, colors.red_color,
                          "", 0, None, (None, 17, "bold"), 0.9, 0.215, "e")
    if(not name.get()): ck.show_error(name, colors.dark_green_6, 1000)
    elif(not id.get()): ck.show_error(id, colors.dark_green_6, 1000)
    elif(not car_id.get()): ck.show_error(car_id, colors.dark_green_6, 1000)
    elif(not serial_number.get()): ck.show_error(serial_number, colors.dark_green_6, 1000)
    elif(start_date.cget('text') == 'تاریخ صدور'): ck.show_error(start_date, colors.dark_green_6, 1000)
    elif(end_date.cget('text') == 'تاریخ انقضا'): ck.show_error(end_date, colors.dark_green_6, 1000)
    elif(not cc.car_id_format_is_right(car_id.get())): 
        ck.show_error(car_id, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "شماره پلاک وارد شده، صحیح نمی‌باشد!")
    elif(not cc.does_item_exist(bol_fake_data.car_sample_data, "car_id", car_id.get())): 
        ck.show_error(car_id, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "نفتکشی با این شماره پلاک در سامانه ثبت نشده است!")
    elif(not cc.get_driver_licence(name.get(), id.get())): 
        ck.show_error(name, colors.dark_green_6, 1000)
        ck.show_error(id, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "راننده با مشخصات وارد شده، یافت نشد!")
    elif(cc.is_date_above(start_date.cget("text"), end_date.cget("text"))): 
        ck.show_error(start_date, colors.dark_green_6, 1000)
        ck.show_error(end_date, colors.dark_green_6, 1000)
        ck.update_label_error(label, 1000, "تاریخ پایان اعتبار باید بعد از تاریخ شروع باشد!")
    else:
        def do_register():
            bol_fake_data.workcart.append({
                "driver_name": cc.eng_to_persian_date(name.get()),
                "driver_id": cc.eng_to_persian_date(id.get()),
                "car_id": cc.eng_to_persian_date(car_id.get()),
                "start_date": cc.eng_to_persian_date(start_date.cget('text')),
                "end_date": cc.eng_to_persian_date(end_date.cget('text')),
                'serial_number': cc.eng_to_persian_date(serial_number.get())
            })
            register_box.destroy()
            reset_page()
            
        def cancel(): 
            confirm_box.destroy()
        
        confirm_box = show_confirmation_box(register_box, do_register, cancel, "آیا از اطلاعات این کارت تردد، مطمئن هستید؟", None)
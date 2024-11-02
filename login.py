import customtkinter,tkinter
import json
import os
#from PIL import ImageTk,Image
import main_menu

class Giris(customtkinter.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.place(x=1,y=1,relwidth=1,relheight=1)
        
    def LoginScreen(self):
        self.giris_frame = customtkinter.CTkFrame(self,corner_radius=10)
        self.giris_frame.place(relx=0,rely=0,relwidth=1,relheight=1)
    
        # giriş frame entryler var
        self.giris1_frame = customtkinter.CTkFrame(self.giris_frame,
                                         fg_color="black",
                                         corner_radius=20)
        self.giris1_frame.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER,relwidth=0.35,relheight=0.9)
        
        # giriş yap label
        self.giris_yap = tkinter.Label(self.giris1_frame,text="GİRİŞ YAP",font="Times 25",background="black",foreground="white")
        self.giris_yap.place(relx=0.49,rely=0.26,anchor = tkinter.CENTER,relwidth=0.8,relheight=0.1)
     # kullanıcı adı şifre entry
        self.userid_entry = customtkinter.CTkEntry(self.giris1_frame,
                                      placeholder_text="Kullanıcı Adı",
                                      border_width=2,
                                      corner_radius=10)
        self.userid_entry.place(relx=0.5,rely=0.4,anchor = tkinter.CENTER,relwidth=0.7,relheight=0.07)

        self.password_entry =   customtkinter.CTkEntry(self.giris1_frame,
                                    placeholder_text="Şifre",
                                    border_width=2,
                                    show="*",
                                    corner_radius=10)
        self.password_entry.place(relx=0.5,rely=0.5,anchor = tkinter.CENTER,relwidth=0.7,relheight=0.07)
        
        # giriş kaydol button
        
        self.my_stringvar2 = customtkinter.StringVar()
        self.giriş_label= customtkinter.CTkLabel(self.giris1_frame,textvariable=self.my_stringvar2,text_color="red",font=("Arial",9))
        self.giriş_label.place(relx=0.47,rely=0.58,anchor=tkinter.CENTER,relwidth=0.8,relheight=0.08)
        
        self.giris_button=customtkinter.CTkButton(self.giris1_frame,
                                         text="Giriş Yap",command=self.kontrol)
        self.giris_button.place(relx=0.7,rely=0.65,anchor=tkinter.CENTER,relwidth=0.35,relheight=0.07)
    
        self.kaydol_button=customtkinter.CTkButton(self.giris1_frame,text="Kaydol",command=self.LogonUI)
        self.kaydol_button.place(relx=0.3,rely=0.65,anchor=tkinter.CENTER,relwidth=0.35,relheight=0.07)


# parola ve kullanıcı adı kontrol eder
    def kontrol(self):
        if os.path.exists("dosyalar/"):
            pass
        else:
            os.makedirs("dosyalar")
        try:
            with open(f"dosyalar\\{self.userid_entry.get()}.json",encoding="utf-8") as file:
                self.data= json.load(file)
            if self.data["Kullanici Adi"]==self.userid_entry.get()and self.data["Sifre"]==self.password_entry.get():
                menu = main_menu.Menu(self, user_id = self.userid_entry.get())
                self.giris_frame.destroy()
            elif self.userid_entry.get()=="" or self.password_entry.get()=="":
                self.my_stringvar2.set("Lütfen kullanıcı adı ve şifre girin")
            elif self.data["Kullanici Adi"]== self.userid_entry.get() and self.data["Sifre"]!=self.password_entry.get():
                self.my_stringvar2.set("Şifre Yanlış")
        except Exception:
                    self.my_stringvar2.set("Kullanıcı Bulunamadı Lütfen Kaydolun")
           
    # kaydolma ekran         
    def LogonUI(self):
        self.giriş_label.place_forget()
        self.kaydol_lbl = tkinter.Label(self.giris1_frame,text="KAYDOL",font="Times 25",background="black",foreground="white")
        self.kaydol_lbl.place(relx=0.49,rely=0.26,anchor = tkinter.CENTER,relwidth=0.8,relheight=0.1)
        # kaydol butonu 
        self.giris_button.place_forget()
        self.kaydol_button.place_forget()
        self.kaydet_button=customtkinter.CTkButton(self.giris1_frame,text="Kaydol",command=self.kullanıcıadısifre_kaydet)
        self.kaydet_button.place(relx=0.5,rely=0.65,anchor=tkinter.CENTER,relwidth=0.7,relheight=0.07)
        
        # label uyarı
        self.mystringvar3 = customtkinter.StringVar()
        self.uyarı_lbl_kaydol =  customtkinter.CTkLabel(self.giris1_frame,textvariable=self.mystringvar3,text_color="red",font=("Arial",10))
        self.uyarı_lbl_kaydol.place(relx=0.47,rely=0.58,anchor=tkinter.CENTER,relwidth=0.8,relheight=0.05)
        
        # geri buton
        
        self.geri_button=customtkinter.CTkButton(self.giris1_frame,width=40,height=30,text="Geri",fg_color="black",text_color="white",command=self.geri)
        self.geri_button.place(relx=0.03,rely=0.03)
        
    def geri(self):
        self.kaydol_lbl.place_forget()
        self.giris_yap.place()
        self.uyarı_lbl_kaydol.place_forget()
        self.geri_button.place_forget()
        
        self.kaydet_button.place_forget()
        self.giris_button.place(relx=0.7,rely=0.65,anchor=tkinter.CENTER,relwidth=0.35,relheight=0.07)
        self.kaydol_button.place(relx=0.3,rely=0.65,anchor=tkinter.CENTER,relwidth=0.35,relheight=0.07)
        
# şifreleri bir json dosyasına kaydeder 
    def kullanıcıadısifre_kaydet(self):
            try:
                if os.path.exists(f"dosyalar\\{self.userid_entry.get()}.json"):
                    self.mystringvar3.set("Lütfen Farklı Bir kullanıcı Girin")
                    self.uyarı_lbl_kaydol._text_color = "red"
                elif self.userid_entry.get()=="" or self.password_entry.get()=="":
                   self.mystringvar3.set("Bütün Yerleri Doldurmalısınız")
                else:
                    person_dict={"Kullanici Adi":f"{self.userid_entry.get()}","Sifre":f"{self.password_entry.get()}"}
                    with open(f"dosyalar\\{self.userid_entry.get()}.json","a") as file:   
                        json.dump(person_dict,file)
                    menu = main_menu.Menu(self, user_id = self.userid_entry.get())
                    self.giris_frame.destroy()
            except Exception as a:
                print(a)
                self.mystringvar3.set("Lütfen Farklı Bir kullanıcı Girin")
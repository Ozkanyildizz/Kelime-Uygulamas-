import tkinter.messagebox
import customtkinter
import os
from CTkListbox import CTkListbox
import login
import list
import translate
import exercise
import gemini_gramer

class Menu(customtkinter.CTkFrame):
    def __init__(self,parent,user_id):
        super().__init__(parent)
        self.user_id = user_id
        self.place(x=1,y=1,relwidth=1,relheight=1)
        self.ana_frame = customtkinter.CTkFrame(self,corner_radius=10)
        self.ana_frame.place(relx=0,rely=0,relwidth=1,relheight=1)
        self.ceviri_ac = None
        self.alıstırma_ac = None
        self.frame2 = None
        self.gramer_frame = None
        self.widgets_button()
        self.widgets_list()
        
    def widgets_list(self):
        # liste frami
        self.frame2 = customtkinter.CTkScrollableFrame(self.ana_frame,corner_radius=15)
        self.frame2.place(relx=0.295,rely=0.100,relwidth=0.7,relheight=0.96)
        # -----------Frame2 liste bölümü ---------------------------------
        self.frame3 = customtkinter.CTkFrame(self.ana_frame,corner_radius=15)
        self.frame3.place(relx=0.295,rely=0.01,relwidth=0.7,relheight=0.1)
        self.label_kelime = customtkinter.CTkLabel(self.frame3,text="Kelime listesi")
        self.label_kelime.place(relx=0.01,rely=0.4,relwidth=0.17,relheight=0.2)
        # buttons
        self.button_ekle = customtkinter.CTkButton(self.frame3,text="Yeni Liste",width=80,corner_radius=15,command=self.ekle).place(relx=0.2,rely=0.25,relwidth=0.25,relheight=0.5)
        self.button_Ac = customtkinter.CTkButton(self.frame3,text="Listeyi Aç",width=80,corner_radius=15,command=self.liste_ac).place(relx=0.47,rely=0.25,relwidth=0.25,relheight=0.5)
        self.button_Sil = customtkinter.CTkButton(self.frame3,text="Sil",width=80,corner_radius=15,command=self.liste_sil).place(relx=0.73,rely=0.25,relwidth=0.25,relheight=0.5)
        # list
        self.listbox = CTkListbox(self.frame2,multiple_selection=True,height=640)
        self.listbox.pack(fill="both", expand=True, padx=5, pady=5)
        self.oku(self.listbox)
    
    def widgets_button(self):
        # menu frame
        self.frame1 = customtkinter.CTkFrame(self.ana_frame,fg_color="black",corner_radius=15)
        self.frame1.place(x=1,y=1,relwidth=0.29,relheight=1)
        
        self.buton_benimsözlük = customtkinter.CTkButton(self.frame1,text="Listem",corner_radius=15,
                                                command=self.listem).place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.1)
        self.buton_onlinesözlük = customtkinter.CTkButton(self.frame1,text="Çeviri",corner_radius=15,
                                                 command=self.ceviri).place(relx=0.1,rely=0.41,relwidth=0.8,relheight=0.1)
        self.buton_profil = customtkinter.CTkButton(self.frame1,text="Alıştırma",corner_radius=15,
                                           command=self.alıstırma).place(relx=0.1,rely=0.73,relwidth=0.8,relheight=0.1)
        self.buton_gramer = customtkinter.CTkButton(self.frame1,text="Gramer kontrol",corner_radius=15,
                                           command=self.gramer_kontrol).place(relx=0.1,rely=0.57,relwidth=0.8,relheight=0.1)
        self.lbl1= customtkinter.CTkLabel(self.frame1,text="",corner_radius=25,fg_color="green",height=50,width=5)
        self.lbl1.place(relx=0.01,rely=0.25,relwidth=0.04,relheight=0.1)
        self.lbl2= customtkinter.CTkLabel(self.frame1,corner_radius=25,text="",fg_color="black",height=50,width=5)
        self.lbl2.place(relx=0.001,rely=0.41,relwidth=0.04,relheight=0.1)
        self.lbl3= customtkinter.CTkLabel(self.frame1,corner_radius=25,text="",fg_color="black",height=50,width=5)
        self.lbl3.place(relx=0.01,rely=0.57,relwidth=0.04,relheight=0.1)
        self.lbl4= customtkinter.CTkLabel(self.frame1,corner_radius=25,text="",fg_color="black",height=50,width=5)
        self.lbl4.place(relx=0.01,rely=0.73,relwidth=0.04,relheight=0.1)
        # hoşgeldin yazısı
        self.my_stringvar = customtkinter.StringVar()
        self.kullanıcılbl = customtkinter.CTkLabel(self.frame1,textvariable=self.my_stringvar).place(relx=0.2,rely=0.17,relwidth=0.6,relheight=0.05)
        self.my_stringvar.set(f"Hoşgeldin {self.user_id.upper()}")
        # self.designer_lbl = customtkinter.CTkLabel(self.frame1,text="Designed By Özkan Yıldız",font=("Arial",11)).place(relx=0.02,rely=0.9,relwidth=0.9,relheight=0.1)
        self.cıkıs_bıton= customtkinter.CTkButton(self.frame1,text="Çıkış Yap",command=self.cıkıs).place(relx=0.1,rely=0.04,relwidth=0.8,relheight=0.04)
        return True

    # frame1 butonları
    def listem(self):
        self.lbl_hide()
        self.lbl1.configure(fg_color="green")
        if self.ceviri_ac is not None:
            self.ceviri_ac.frame_ceviri.destroy()
        if self.alıstırma_ac is not None:
            self.alıstırma_ac.frame_alıstırma.destroy()
        if self.gramer_frame is not None:
            self.gramer_frame.destroy()
        self.widgets_list()
        
    def ceviri(self):
        self.lbl_hide()
        self.lbl2.configure(fg_color="green")
        self.frame3.destroy()
        self.frame2.destroy()
        if self.alıstırma_ac is not None:
            self.alıstırma_ac.frame_alıstırma.destroy()
        if self.gramer_frame is not None:
            self.gramer_frame.destroy()
        self.ceviri_ac= translate.Ceviri_ac(self,self.ana_frame,self.listbox.get("all"))
        
    def alıstırma(self):
        self.lbl_hide()
        self.lbl4.configure(fg_color="green")
        self.frame3.destroy()
        self.frame2.destroy()
        if self.ceviri_ac is not None:
            self.ceviri_ac.frame_ceviri.destroy()
        if self.gramer_frame is not None:
            self.gramer_frame.destroy()
        self.alıstırma_ac = exercise.Alıstırma_ac(self,self.ana_frame,self.listbox.get("all"))
        
    def gramer_kontrol(self):
        self.lbl_hide()
        self.lbl3.configure(fg_color="green")
        self.frame3.destroy()
        self.frame2.place_forget()
        if self.alıstırma_ac is not None:
            self.alıstırma_ac.frame_alıstırma.destroy()
        if self.ceviri_ac is not None:
            self.ceviri_ac.frame_ceviri.destroy()
        self.gramer_frame = gemini_gramer.Gemini_gramer_kontrol(self,self.ana_frame)
        
    # frame1 çıkış butonu
    def cıkıs(self):
        cık_mesagebox = tkinter.messagebox.askyesno("Çıkış","Çıkış yapmak istediğinize emin misiniz?")
        if cık_mesagebox == True:
            self.ana_frame.destroy()
            giriss= login.Giris(self)
            giriss.LoginScreen()
            
    # Frame1 label gizle    
    def lbl_hide(self):  
            self.lbl1.configure(fg_color="black",bg_color="black")
            self.lbl2.configure(fg_color="black",bg_color="black")
            self.lbl3.configure(fg_color="black",bg_color="black")         
            self.lbl4.configure(fg_color="black",bg_color="black")       
              
# Listeye Kaydedilenleri yükler        
    def oku(self,a):   
        file = open(f"dosyalar\\{self.user_id}.txt","a")
        file.close() 
        self.oku5 =open(f"dosyalar\\{self.user_id}.txt","r")
        b = self.oku5.readlines()
        for i in b:    
            i = i.replace("\n","")        
            a.insert(self.listbox.size(),i)    
        self.oku5.close()
        
#Listeye yeni satır ekler ve kaydeder siler --------------frame4----------------------
    def kaydet(self):
        self.get_content = self.listbox.get("all")
        with open(f"dosyalar\\{self.user_id}.txt", "w") as file:
            #file.write(f"{self.get_content}")
            for i in self.get_content:
                if i!="\n":
                    file.write(f"{i}\n")
                else:
                    break
                
    def ekle(self):
        self.dialog = customtkinter.CTkInputDialog(text="Liste Adı: ", title="Liste Adı")
        resultt = self.dialog.get_input()
        if resultt !="":
            self.listbox.insert("END",resultt)  
        self.kaydet()  
        
    def liste_sil(self):
        cık_mesagebox = tkinter.messagebox.askyesno("Sil","seçili listeleri silmek isteediğinie emin misiniz?")
        if cık_mesagebox == True:
            for i in reversed(self.listbox.curselection()):
                if os.path.exists(f"dosyalar\\{self.listbox.get()[0]}.txt"):
                    os.remove(f"dosyalar\\{self.listbox.get()[0]}.txt")
                self.listbox.delete(i)
        self.kaydet()
        
    def liste_ac(self):
        try:
            self.result =  self.listbox.get()[0]  
            deger2 = self.result.replace("\n","")
            ac = open(f"dosyalar\\{deger2}.txt","a")
            ac.close()
            
            if len(self.listbox.get())==1:
                self.open_list= list.Liste_ac(self,liste=self.result,ana_frame=self.ana_frame)
            else:
                message = tkinter.messagebox.showwarning("Liste Seçin", "Açmak istediğiniz bi tane listeyi seçin")
        except Exception as a:
            message = tkinter.messagebox.showwarning("Liste Seçin", "Açmak istediğiniz bir tane listeyi seçin")



    
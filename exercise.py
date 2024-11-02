import customtkinter
import tkinter.messagebox
import random
from CTkListbox import CTkListbox
import gemini_quiz


class Alıstırma_ac(customtkinter.CTkFrame,):
    def __init__(self,parent,ana_frame,liste,):
        super().__init__(parent)
        self.ana_frame = ana_frame
        self.listbox_get=liste
        # frame alıştırma
        self.frame_alıstırma = customtkinter.CTkFrame(self.ana_frame,corner_radius=10)
        self.frame_alıstırma.place(relx=0.295,rely=0.009,relwidth=0.7,relheight=0.99)
        # kendi listelerim
        self.alıstırma_lbl = customtkinter.CTkLabel(self.frame_alıstırma,font=("Times",25),corner_radius=50
                                                    ,fg_color="gray",text_color="white",height=40,
                                                    text=("Alıştırma yapmak istediğiniz listeyi seçiniz."))
        self.alıstırma_lbl.place(relx=0.001,rely=0.03,relheight=0.1,relwidth=1)
        self.lbl_list_alıştırma = customtkinter.CTkLabel(self.frame_alıstırma,text="Kendi listelerinizden seçin.")
        self.lbl_list_alıştırma.place(relx=0.001,rely=0.15,relwidth=0.4)
        self.listbox_alıstırma = CTkListbox(self.frame_alıstırma,multiple_selection=True)
        self.listbox_alıstırma.place(relx=0.001,rely=0.20,relheight=0.65,relwidth=0.4)
        self.oku()
        # yapay zeka 
        self.lbl_gemini = customtkinter.CTkLabel(self.frame_alıstırma,text="Yapay zeka sizin için testi oluştursun.")
        self.lbl_gemini.place(relx=0.45,rely=0.15,relwidth=0.5,)
        # konu seçimi
        self.lbl_konu = customtkinter.CTkLabel(self.frame_alıstırma,text="Konu seçiniz.")
        self.lbl_konu.place(relx=0.4,rely=0.3,relwidth=0.2)
        self.optionmenuVar = customtkinter.StringVar(value="Kelimeler")
        self.konuCombobox =customtkinter.CTkComboBox(self.frame_alıstırma,
                                          values=["Gramer","Kelimeler"],
                                          variable=self.optionmenuVar)
        self.konuCombobox.place(relx=0.59,rely=0.3,relwidth=0.4)
        # seviye seçimi 
        self.lbl_seviye = customtkinter.CTkLabel(self.frame_alıstırma,text="Seviye seçiniz.")
        self.lbl_seviye.place(relx=0.4,rely=0.45,relwidth=0.2)
        self.optionmenuVar2 = customtkinter.StringVar(value="B2")
        # konu seçimi
        self.konuCombobox =customtkinter.CTkComboBox(self.frame_alıstırma,
                                          values=["A1","A2","B1","B2","C1","C2"],
                                          variable=self.optionmenuVar2)
        self.konuCombobox.place(relx=0.59,rely=0.45,relwidth=0.4)
        # uzunluk
        self.lbl_uzunluk = customtkinter.CTkLabel(self.frame_alıstırma,text="Soru uzunluğu")
        self.lbl_uzunluk.place(relx=0.4,rely=0.6,relwidth=0.2)
        self.optionmenuVar3 = customtkinter.StringVar(value="Orta")
        self.uzunlukCombobox =customtkinter.CTkComboBox(self.frame_alıstırma,
                                          values=["Kısa","Orta","Uzun"],
                                          variable=self.optionmenuVar3)
        self.uzunlukCombobox.place(relx=0.59,rely=0.6,relwidth=0.4)
        # radio butonları 
        self.radio_var = tkinter.StringVar(value="AI")

        listem_radiobutton = customtkinter.CTkRadioButton(self.frame_alıstırma,text="Seçili listeden alıştırmaya başla",
                                                #command=radiobutton_event,
                                                variable=self.radio_var,value="listem",)
        listem_radiobutton.place(relx=0.45,rely=0.7,relwidth=0.5)
        gemini_radiobutton = customtkinter.CTkRadioButton(self.frame_alıstırma,text="Yapay zeka oluştursun",
                                                #command=radiobutton_event,
                                                variable=self.radio_var,value="AI",)
        gemini_radiobutton.place(relx=0.45,rely=0.8,relwidth=0.5)
        # alıştırma aç butonu
        self.alıstırma_ac_button = customtkinter.CTkButton(self.frame_alıstırma,text=("Alıştırmaya Başla"),corner_radius=60,command=self.button)
        self.alıstırma_ac_button.place(relx=0.001,rely=0.87,relheight=0.1,relwidth=1)
    
    def button(self):
        if self.radio_var.get()=="listem":
            self.alıstırma_listelerim()
        else:
            self.alıstırma_gemini()

    # alıştırma Frami açar 
    def alıstırma_listelerim(self):     
        
        if self.kontroll():
            self.frame_alıstırma1 = customtkinter.CTkFrame(self.ana_frame,corner_radius=10)
            self.frame_alıstırma1.place(relx=0.295,rely=0.009,relwidth=0.7,relheight=0.99)
        
            self.frame_alıstırma2= customtkinter.CTkFrame(self.frame_alıstırma1,width=600,corner_radius=150,height=600)
            self.frame_alıstırma2.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)
            lbl= customtkinter.CTkLabel(self.frame_alıstırma2,bg_color="#292929",corner_radius=15,font=("Arial",25),text="Doğru Cevapı İşaretleyin")
            lbl.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.1)
            self.cvp1_strvar = customtkinter.StringVar() 
            self.cvp2_strvar = customtkinter.StringVar()    
            self.cvp3_strvar = customtkinter.StringVar()    
            self.cvp4_strvar = customtkinter.StringVar()  
            self.lbl_ingkelimevar = customtkinter.StringVar() 
            self.lbl_cvpvar= customtkinter.StringVar()
            self.yeni_soru()
            self.lbl_ing=customtkinter.CTkLabel(self.frame_alıstırma2,corner_radius=50,bg_color="#292929",font=("Arial",30),textvariable=self.lbl_ingkelimevar)
            self.lbl_ing.place(relx=0.18,rely=0.25,relwidth=0.8,relheight=0.1)
            self.cvp= customtkinter.CTkLabel(self.frame_alıstırma2,corner_radius=100,width=450,height=50,bg_color="#292929",textvariable=self.lbl_cvpvar)
            self.cvp.place(relx=0.129,rely=0.82,relwidth=0.75,relheight=0.1)
            
            cvp4_button= customtkinter.CTkButton(self.frame_alıstırma2,corner_radius=150,bg_color="#292929",width=200,height=50,textvariable=self.cvp4_strvar,command=self.cvp4).place(relx=0.1,rely=0.4,relwidth=0.4,relheight=0.1)
            cvp2_button= customtkinter.CTkButton(self.frame_alıstırma2,corner_radius=150,bg_color="#292929",width=200,height=50,textvariable=self.cvp2_strvar,command=self.cvp2).place(relx=0.52,rely=0.4,relwidth=0.4,relheight=0.1)
            cvp3_button= customtkinter.CTkButton(self.frame_alıstırma2,corner_radius=150,bg_color="#292929",width=200,height=50,textvariable=self.cvp3_strvar,command=self.cvp3).place(relx=0.1,rely=0.55,relwidth=0.4,relheight=0.1)
            cvp1_button= customtkinter.CTkButton(self.frame_alıstırma2,corner_radius=150,bg_color="#292929",width=200,height=50,textvariable=self.cvp1_strvar,command=self.cvp1).place(relx=0.52,rely=0.55,relwidth=0.4,relheight=0.1)
            next_button= customtkinter.CTkButton(self.frame_alıstırma2,corner_radius=150,bg_color="#292929",width=450,height=50,text="Sonraki",command=self.yeni_soru).place(relx=0.14,rely=0.7,relwidth=0.75,relheight=0.1)
            geri_button=  customtkinter.CTkButton(self.frame_alıstırma2,corner_radius=200,bg_color="#292929",width=50,height=40,font=("Ariel",18),text="<",command=lambda: self.geri_alıstırma(self.frame_alıstırma1)).place(relx=0.02,rely=0.26,relwidth=0.15,relheight=0.08)
    def oku(self):
        for i in self.listbox_get:
            self.listbox_alıstırma.insert(self.listbox_alıstırma.size(),i)    
    def alıstırma_gemini(self):
        self.frame_alıstırma3 = customtkinter.CTkFrame(self.ana_frame,corner_radius=10)
        self.frame_alıstırma3.place(relx=0.295,rely=0.009,relwidth=0.7,relheight=0.99)
        lbl= customtkinter.CTkLabel(self.frame_alıstırma3,bg_color="#292929",corner_radius=30,font=("Times",20),text="Gemini Alıştırma")
        lbl.place(relx=0.14,rely=0.003,relwidth=0.8,relheight=0.06)
        self.textbox= customtkinter.CTkTextbox(self.frame_alıstırma3,width=600,corner_radius=30,height=600)
        self.textbox.place(relx=0.05,rely=0.08,relwidth=0.9,relheight=0.6)
        
        cvp4_button= customtkinter.CTkButton(self.frame_alıstırma3,corner_radius=50,bg_color="#292929",width=200,height=50,text="A",command=lambda: self.cvp_G("A")).place(relx=0.1,rely=0.69,relwidth=0.3,relheight=0.08)
        cvp2_button= customtkinter.CTkButton(self.frame_alıstırma3,corner_radius=50,bg_color="#292929",width=200,height=50,text="B",command=lambda: self.cvp_G("B")).place(relx=0.65,rely=0.69,relwidth=0.3,relheight=0.08)
        cvp3_button= customtkinter.CTkButton(self.frame_alıstırma3,corner_radius=50,bg_color="#292929",width=200,height=50,text="C",command=lambda: self.cvp_G("C")).place(relx=0.1,rely=0.79,relwidth=0.3,relheight=0.08)
        cvp1_button= customtkinter.CTkButton(self.frame_alıstırma3,corner_radius=50,bg_color="#292929",width=200,height=50,text="D",command=lambda: self.cvp_G("D")).place(relx=0.65,rely=0.79,relwidth=0.3,relheight=0.08)
        next_button= customtkinter.CTkButton(self.frame_alıstırma3,corner_radius=50,bg_color="#292929",width=450,height=50,text="Sonraki",command=self.yeni_soru_gemini).place(relx=0.30,rely=0.9,relwidth=0.5,relheight=0.08)
        geri_button=  customtkinter.CTkButton(self.frame_alıstırma3,corner_radius=100,bg_color="#292929",width=50,height=40,font=("Ariel",18),text="<",command=lambda: self.geri_alıstırma(self.frame_alıstırma3)).place(relx=0.005,rely=0.009,relwidth=0.1,relheight=0.05)
        try:
            self.textbox.configure(state="normal")
            olay = gemini_quiz.ask(f"konu: ingilizce {self.optionmenuVar.get()}, seviye: {self.optionmenuVar2.get()}, ve uzunluk{self.optionmenuVar3.get()}")
            self.textbox.insert("end",olay)
            self.textbox.configure(state="disabled")
        except Exception as a :
            tkinter.messagebox.showwarning(a+" HATA","Cevap alınamadı. Tekrar deneyin.")


    def cvp_G(self,cvp):
        try:
            self.textbox.configure(state="normal")
            olay = gemini_quiz.ask(f"is answer {cvp}? Explain in Turkish")
            self.textbox.insert("end",f"\n{olay}")
            self.textbox.configure(state="disabled")
        except Exception:
            tkinter.messagebox.showwarning("HATA","Cevap alınamadı. Tekrar deneyin.")
    def yeni_soru_gemini(self):
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0","end")
        try:
            olay = gemini_quiz.ask("Now ask a new question use the same topic and level")
            self.textbox.insert("end",f"-------------------------------------------------\n{olay}")
            self.textbox.configure(state="disabled")
        except Exception:
            tkinter.messagebox.showwarning("HATA","Cevap alınamadı. Tekrar deneyin.")
    
    #alıştırma geri tuşu 
    def geri_alıstırma(self,frame):
        frame.place_forget()

# yeni soru 
    # liste kontrol 
    def kontroll(self):
        try:
            self.result =  self.listbox_alıstırma.get()
            if len(self.result)>1:
                    message = tkinter.messagebox.showwarning("Liste Seçin", "Açmak istediğiniz bir tane listeyi seçin liste boş olmamalı")   
            elif len(self.result)==1:
                self.oku7= open(f"dosyalar\\{self.result[0]}.txt","r",encoding='utf-8')
                self.b = self.oku7.readlines()  
                self.degerr = len(self.b)
                if self.degerr<=4:
                    message = tkinter.messagebox.showwarning("Liste Boş", "Seçtiğiniz listede en az 4 kelime bulunmalı")   
                else:
                    return True
        except Exception:
            message = tkinter.messagebox.showwarning("Liste Seçin", "Açmak istediğiniz bir tane listeyi seçin liste boş olmamalı")
            
    def yeni_soru(self):
        try:
            # kelimeleri oku    
            self.kontroll()
            self.list1=[]
            self.list2=[]    
            randomm= random.randint(1,self.degerr-1)
            ing = self.b[randomm].split("=")[0]
            tr = self.b[randomm].split("=")[1]
            self.list1.append(ing)
            self.list2.append(tr)

            for i in range(3):
                randomn= random.randint(1,self.degerr-1)
                self.list2.append(self.b[randomn].split("=")[1])
            self.karısık = random.sample(self.list2,4)
            self.cvp1_strvar.set(f"{self.karısık[0]}")
            self.cvp2_strvar.set(f"{self.karısık[1]}")
            self.cvp3_strvar.set(f"{self.karısık[2]}")
            self.cvp4_strvar.set(f"{self.karısık[3]}")
            self.lbl_ingkelimevar.set(f"{self.list1[0]}")         
            self.cvp.place_forget()
        except Exception:
            pass

        
    def cvp1(self):
        self.cvp.place(relx=0.129,rely=0.82,relwidth=0.75,relheight=0.1)
        if self.karısık[0] == self.list2[0]:
            self.lbl_cvpvar.set("Doğru yaptınız")
            self.cvp.configure(fg_color="blue")
        else:
            self.lbl_cvpvar.set(f"Yanıldınız Cevap ({self.list2[0]}) olmalı ")
            self.cvp.configure(fg_color="red")
    def cvp2(self):
        self.cvp.place(relx=0.129,rely=0.82,relwidth=0.75,relheight=0.1)
        if self.karısık[1] == self.list2[0]:
            self.lbl_cvpvar.set("Doğru yaptınız")
            self.cvp.configure(fg_color="blue")
        else:
            self.lbl_cvpvar.set(f"Yanıldınız Cevap ({self.list2[0]}) olmalı ")
            self.cvp.configure(fg_color="red")
    def cvp3(self):
        self.cvp.place(relx=0.129,rely=0.82,relwidth=0.75,relheight=0.1)
        if self.karısık[2] == self.list2[0]:
            self.lbl_cvpvar.set("Doğru yaptınız")
            self.cvp.configure(fg_color="blue")
        else:
            self.lbl_cvpvar.set(f"Yanıldınız Cevap ({self.list2[0]}) olmalı ")
            self.cvp.configure(fg_color="red")
    def cvp4(self):
        self.cvp.place(relx=0.129,rely=0.82,relwidth=0.75,relheight=0.1)
        if self.karısık[3] == self.list2[0]:
            self.lbl_cvpvar.set("Doğru yaptınız")
            self.cvp.configure(fg_color="blue")
        else:
            self.lbl_cvpvar.set(f"Yanıldınız Cevap ({self.list2[0]}) olmalı ")
            self.cvp.configure(fg_color="red")
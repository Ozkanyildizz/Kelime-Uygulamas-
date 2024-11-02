import customtkinter
from googletrans import Translator
import tkinter.messagebox
from tkinter import EXTENDED
from CTkListbox import CTkListbox

class Ceviri_ac(customtkinter.CTkFrame,):
    def __init__(self,parent,ana_frame,liste):
        super().__init__(parent)
        self.ana_frame = ana_frame
        self.listbox_get=liste
        self.toplevel_window= None
        self.toplevel_window2= None    
        
        self.frame_ceviri = customtkinter.CTkFrame(self.ana_frame,corner_radius=10)
        self.frame_ceviri.place(relx=0.295,rely=0.009,relwidth=0.7,relheight=0.99)
        
        self.optionmenuVar = customtkinter.StringVar(value="ingilizce > Türkçe")
        self.dilCombobox =customtkinter.CTkComboBox(self.frame_ceviri,
                                          values=["ingilizce > Türkçe","Türkçe > İngilizce"],
                                          variable=self.optionmenuVar)
        self.dilCombobox.place(relx=0.1,rely=0.11, relwidth=0.5)
        
        self.textboks1 = customtkinter.CTkTextbox(self.frame_ceviri,width=300,height=150,corner_radius=15)
        self.textboks1.place(relx=0.1,rely=0.18,relwidth=0.8,relheight=0.35)

        
        self.textboks1.insert("0.0"," ")
        
        self.text_sonuc = customtkinter.CTkTextbox(self.frame_ceviri,
                                                   width=300,height=150,corner_radius=15)
        self.text_sonuc.place(relx=0.1,rely=0.55,relwidth=0.8,relheight=0.35)

        btn_cevir = customtkinter.CTkButton(self.frame_ceviri,text="Çevir",height=35,width=300,command=self.ceviri).place(relx=0.1,rely=0.93,relwidth=0.4,relheight=0.05)
        btn_temizle = customtkinter.CTkButton(self.frame_ceviri,text="Hepsini Sil",height=35,width=300,command=self.sil).place(relx=0.57,rely=0.93,relwidth=0.4,relheight=0.05)
        btn_listeye_ekle = customtkinter.CTkButton(self.frame_ceviri,text="Listeye Ekle",width=80,height=30,command=self.toplevel_ac).place(relx=0.66,rely=0.11,relwidth=0.25,relheight=0.05)
        
        label_ceviri = customtkinter.CTkLabel(self.frame_ceviri,font=("Times",30),text="Çeviri").place(relx=0.006,rely=0.02,relwidth=0.4,relheight=0.08)
    
# cevirme işlemi yapar
    def ceviri(self):
        if self.optionmenuVar.get() == "ingilizce > Türkçe":
            self.cevir_en_tr()
        elif self.optionmenuVar.get() == "Türkçe > İngilizce":
            self.cevir_tr_en()
        else:
            pass
    def cevir_tr_en(self):  
        translator = Translator()  
        try: 
            self.text_sonuc.delete("0.0","end")
            input2= self.textboks1.get(1.0, "end")
            result=translator.translate(input2,src="tr",dest="en").text
            self.text_sonuc.insert("0.0",str(result))
        except Exception as a:
            tkinter.messagebox.showwarning("HATA","Çevrilemedi tekrar deneyin\n(internete bağlı olduğunuzdan emin olun).")
                
    def cevir_en_tr(self):  
        translator = Translator()  
        try: 
            self.text_sonuc.delete("0.0","end")
            input= self.textboks1.get(1.0, "end")
            result=translator.translate(input,src="en",dest="tr").text
            self.text_sonuc.insert("0.0",str(result))
        except Exception as a:
            tkinter.messagebox.showwarning("HATA","Çevrilemedi tekrar deneyin\n(internete bağlı olduğunuzdan emin olun).")
# cevirideki bütün txttboksları temizler
    def sil(self):
        self.textboks1.delete("0.0","end")
        self.text_sonuc.delete("0.0","end")
    
    def toplevel(self):
        if self.optionmenuVar.get() == "ingilizce > Türkçe":
            self.Add_to_list_ing()
        elif self.optionmenuVar.get() == "Türkçe > İngilizce":
            self.Add_to_list_tr()
        else:
            pass
    def toplevel_ac(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_acıldı() # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it
    # çeviri kelimelerini listeye ekler
    def toplevel_acıldı(self):
        self.toplevel_window = customtkinter.CTkToplevel(master=self)
        self.toplevel_window.state("normal")
        self.toplevel_window.title("Listeye Ekle")
        self.toplevel_window.resizable(False,False)
        button_ceviri_listeye_ekle = customtkinter.CTkButton(self.toplevel_window,width=80,height=30,text="Listeye ekle",command=self.toplevel).grid(row=2,pady=10)
        self.listbox_ceviri = CTkListbox(self.toplevel_window,multiple_selection=False,height=250,width=220)
        self.listbox_ceviri.grid(row=1,padx=7,pady=5)
        for i in self.listbox_get:
            self.listbox_ceviri.insert(self.listbox_ceviri.size(),i)      
            
    def Add_to_list_ing(self):
        yaz = f"{self.textboks1.get(1.0, "end-1c")}={self.text_sonuc.get(1.0, "end-1c")}=\n"
        oku6 =open(f"dosyalar/{self.listbox_ceviri.get(self.listbox_ceviri.curselection())}.txt","a",encoding='utf-8')
        oku6.write(yaz)
        oku6.close()
        self.toplevel_window.destroy()
    
    def Add_to_list_tr(self):
        yaz = f"{self.text_sonuc.get(1.0, "end-1c")}={self.textboks1.get(1.0, "end-1c")}=\n"
        oku6 =open(f"dosyalar/{self.listbox_ceviri.get(self.listbox_ceviri.curselection())}.txt","a",encoding='utf-8')
        oku6.write(yaz)
        oku6.close()
        self.toplevel_window.destroy()
        
        
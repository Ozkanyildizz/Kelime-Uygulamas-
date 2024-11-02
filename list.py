import customtkinter, tkinter
from tkinter import ttk

class Liste_ac(customtkinter.CTkFrame):
    def __init__(self,parent,liste,ana_frame):
        super().__init__(parent)
        self.liste = liste
        self.ana_frame = ana_frame
        self.frame4 = customtkinter.CTkFrame(self.ana_frame,corner_radius=10)
        self.frame4.place(relx=0.295,rely=0.01,relwidth=0.7,relheight=0.99)
        
        self.frame_list = customtkinter.CTkScrollableFrame(self.frame4,width=700,height=600,corner_radius=10)
        self.frame_list.place(relx=0.005,rely=0.09,relwidth=0.99,relheight=0.90)
        
        self.kelime_entry = customtkinter.CTkEntry(self.frame4,
                                      placeholder_text="Kelime",
                                      width=200,
                                      height=35,
                                      border_width=2,
                                      corner_radius=10)
        self.kelime_entry.place(relx=0.23,rely=0.03,relwidth=0.2,relheight=0.05)
        
        self.anlam_entry = customtkinter.CTkEntry(self.frame4,
                                      placeholder_text="Anlamı",
                                      width=200,
                                      height=35,
                                      border_width=2,
                                      corner_radius=10)
        self.anlam_entry.place(relx=0.44,rely=0.03,relwidth=0.2,relheight=0.05)
        
        self.ornek_entry = customtkinter.CTkEntry(self.frame4,
                                      placeholder_text="Örnek kullanım",
                                      width=200,
                                      height=35,
                                      border_width=2,
                                      corner_radius=10)
        self.ornek_entry.place(relx=0.65,rely=0.03,relwidth=0.2,relheight=0.05)
        
        self.geri_buton= customtkinter.CTkButton(self.frame4,text="Geri",corner_radius=20,command=self.geri).place(relx=0.01,rely=0.03,relheight=0.05,relwidth=0.2)
        self.ekle_buton= customtkinter.CTkButton(self.frame4,text="Ekle",corner_radius=20,command=self.listeye_ekle).place(relx=0.87,rely=0.03,relwidth=0.1,relheight=0.05)
        # treeview
        self.baslık_kelime = ("Kelime","Anlamı","Örnek Kullanımı")
        self.treeview = ttk.Treeview(self.frame_list,show="headings",columns=self.baslık_kelime,height=500)
        self.treeview.column("Kelime",anchor="w",minwidth=50,width=250,stretch="No")
        self.treeview.column("Anlamı",anchor="w",minwidth=50,width=250)
        self.treeview.column("Örnek Kullanımı",anchor="w",minwidth=150,width=350)
        self.treeview.pack()
        for col_name in self.baslık_kelime:
            self.treeview.heading(col_name,text=col_name)  
        self.kelimeleri_getir()
# kelimeleri getir  treeviewe ekle
    def kelimeleri_getir(self):
        deger = self.liste.replace("\n","")
        oku6 =open(f"dosyalar\\{deger}.txt","r",encoding='utf-8')
        b = oku6.readlines()  
        for i in b:   
            new_values= (i.split("=")[0],i.split("=")[1],i.split("=")[2])
            self.treeview.tag_configure('oddrow',background="white")
            self.treeview.tag_configure('ovenrow',background="lightgreen")
            self.treeview.insert('',tkinter.END,values=new_values,tags='ovenrow')
            oku6.close()
    def listeye_ekle(self):
        self.values=(self.kelime_entry.get(),self.anlam_entry.get(),self.ornek_entry.get())
        if self.kelime_entry.get() == "" or self.anlam_entry.get() == "":
            pass
        else:
            self.treeview.tag_configure('oddrow',background="white")
            self.treeview.tag_configure('ovenrow',background="lightgreen")
            self.treeview.insert('',tkinter.END,values=self.values,tags='ovenrow')
        
            deger2 = self.liste.replace("\n","")
            oku6 =open(f"dosyalar\\{deger2}.txt","a",encoding='utf-8')
            oku6.write(f"{self.kelime_entry.get()}={self.anlam_entry.get()}={self.ornek_entry.get()}\n")
            oku6.close()
            self.anlam_entry.delete(0,"end")
            self.kelime_entry.delete(0,"end")
            self.ornek_entry.delete(0,"end")
            
    def geri(self):
        self.frame4.destroy()
        
        
import customtkinter
import google.generativeai as genai
from dotenv import load_dotenv
import os

class Gemini_gramer_kontrol(customtkinter.CTkFrame,):
    def __init__(self,parent,ana_frame):
        super().__init__(parent)
        self.ana_frame = ana_frame
        self.frame_gramer = None

        self.frame_gramer = customtkinter.CTkFrame(self.ana_frame,corner_radius=10)
        self.frame_gramer.place(relx=0.295,rely=0.009,relwidth=0.7,relheight=0.99)

        self.lbl_yazı = customtkinter.CTkLabel(self.frame_gramer,corner_radius=15,
                                               text="GRAMER DÜZELTME",
                                               font=("Times",20),)
        self.lbl_yazı.place(relx=0.05,rely=0.0014,relwidth=0.9,relheight=0.07)
        
        self.textbox_gemini = customtkinter.CTkTextbox(self.frame_gramer,corner_radius=15)
        self.textbox_gemini.place(relx=0.01,rely=0.081,relwidth=0.98,relheight=0.74)
        
        self.textbox_kullanıcı = customtkinter.CTkTextbox(self.frame_gramer,corner_radius=10)
        self.textbox_kullanıcı.place(relx=0.01,rely=0.84,relwidth=0.85,relheight=0.15)
        
        self.buton_gönder = customtkinter.CTkButton(self.frame_gramer,text="Gönder",corner_radius=80,command=self.gramer_kontrol)
        self.buton_gönder.place(relx=0.87,rely=0.85,relwidth=0.13,relheight=0.13)
        self.textbox_gemini.insert("1.0","Metninizi yazınız ve Gemini yapay zeka aracı metnizdeki gramer ve diğer hataları sizin için bulsun")
        self.textbox_gemini.configure(state="normal")  
        self.textbox_gemini.configure(state="disabled")
        
        
    def gramer_kontrol(self):
        self.textbox_gemini.configure(state="normal")
        kullanici_mesaji = self.textbox_kullanıcı.get(1.0, "end")
        self.textbox_gemini.insert("end",f"\n--------------------------------------------\n{self.textbox_kullanıcı.get(1.0,"end")}")
        load_dotenv()
        api_key = os.getenv("API_KEY")
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Please check the following text for english grammatical errors and suggest the corrected form of it and explain the corrections while you use the Turkish language to explain so don't use english while explaining and do not tanslate to Turkish: text: '{kullanici_mesaji}'")
        self.textbox_gemini.insert("end",f"\n{response.text}")
        self.textbox_gemini.see("end")
        self.textbox_gemini.configure(state="disabled")
        self.textbox_kullanıcı.delete("0.0","end")






        

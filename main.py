import customtkinter
import login

class App(customtkinter.CTk):
    def __init__(self):
        
        super().__init__()
        
        customtkinter.set_appearance_mode("dark") 
        customtkinter.set_default_color_theme("green")
        self.title("Word App")
        self.minsize(800,500)
        self.iconbitmap(r"dosyalar\\icon2.ico")
        self.state("withdrawn")
        
        # widgets
        self.giris = login.Giris(self)
        self.giris.LoginScreen()
        self.mainloop()
        
if __name__=="__main__":
    app = App()



# ======= Instalando dependências =========

import customtkinter as ctk
from PIL import Image, ImageTk

# =========== função de login =============

def login_valid ():
    username = user.get()
    password = ent_pass.get()
    # Validar login
    if username == 'username@gmail.com' and password == '12345678':
        log_result.configure(text = 'Successful login', text_color = 'green')
    else: 
        log_result.configure(text = 'Wrong email address or password', text_color = 'red')

# =========== função de login =============

def toggle_password():
    if show_pass.get():
        ent_pass.configure(show="")
    else:
        ent_pass.configure(show="*")


# escolhendo a aparencia da interface
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('dark-blue')

# criação do app
app = ctk.CTk()
app.title('Login')
app.geometry('600x400')
app.resizable(False, False)

# Dividindo a janela em duas colunas iguais
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# Frame 1 (esquerda)
frame_left= ctk.CTkFrame(master = app, width=400, height= 400, corner_radius=10, fg_color = "transparent")
frame_left.grid(row=0, column=0, sticky="nsew")

# frame 2 (direita)
frame_right = ctk.CTkFrame(master = app, width=400, corner_radius=10, fg_color ="#D5CE9B")
frame_right.grid(row=0, column=1, sticky="nsew")

# ============= logo + texto =============
login_title_frame = ctk.CTkFrame(master=frame_left, fg_color="transparent")
login_title_frame.pack(pady=(20, 10))

# Carregar a imagem da logo
logo = Image.open('logo.png')
logo = logo.resize((40, 40))  
logo_img = ImageTk.PhotoImage(logo)

# Logo à esquerda
logo_label = ctk.CTkLabel(master=login_title_frame, image=logo_img, text="")
logo_label.pack(side="left", padx=5)

# Texto "Welcome Back!" à direita da logo
label_login = ctk.CTkLabel(
    master=login_title_frame,
    text='Welcome Back!',
    text_color="#4e441b",
    bg_color='transparent',
    font=('MS Sans Serif', 20, 'bold')
)
label_login.pack(side="left", padx=5)

# Subtitle label
subtitle = ctk.CTkLabel(master = frame_left, text="Login to create account")
subtitle.pack(pady = 0, padx = 0)
# Label username + icon email
email_icon = ctk.CTkImage(Image.open('mail.png'), size=(20, 20))
email_frame = ctk.CTkFrame(master=frame_left, fg_color="transparent")
email_frame.pack(anchor = 'w', pady = (10, 0), padx  = 20)
email_icon_label = ctk.CTkLabel(master=email_frame, image = email_icon, text="")
email_icon_label.pack(side="left", pady =(20, 0))
user_label = ctk.CTkLabel(master = email_frame, text = 'Email Address:', font = ('MS Sans Serif', 12))
user_label.pack(pady = (20, 0), padx = 5)
# Campo a ser preenchido com o email do usuario
user = ctk.CTkEntry(master = frame_left,
                    placeholder_text= '',
                    bg_color = '#F3EFD6',
                    border_color="#D5CE9B",
                    corner_radius= 15,
                    width=200, height=30)
user.pack()

# Label Password + icon lock
lock_icon = ctk.CTkImage(Image.open('lock.png'), size=(20, 20))
lock_frame = ctk.CTkFrame(master = frame_left, fg_color = 'transparent')
lock_frame.pack(anchor = 'w', pady = (10, 0), padx = 20)
lock_icon_label = ctk.CTkLabel(master=lock_frame, image = lock_icon, text="")
lock_icon_label.pack(side = 'left', )
passw = ctk.CTkLabel(master = lock_frame, text = 'Password', font = ('MS Sans Serif', 12))
passw.pack(padx = 5)
# Campo a ser preenchido com a senha
ent_pass = ctk.CTkEntry(master = frame_left,
                    placeholder_text= '',
                    bg_color = '#F3EFD6',
                    border_color="#D5CE9B",
                    corner_radius= 15,
                    width=200, height=30, show = '*')
ent_pass.pack()

# Botão login
log_button = ctk.CTkButton(master = frame_left,
                           text = 'Log in',
                           command = login_valid,
                           width=200, fg_color = "#28755f",
                           hover_color = 'black',
                           corner_radius = 15)
log_button.pack(pady = 10)

# feedback de login
log_result = ctk.CTkLabel(master = frame_left, text = '')
log_result.pack(pady = 10)

# checkbox mostrar senha 
show_pass = ctk.BooleanVar()
check_btn = ctk.CTkCheckBox(master=frame_left,
                            text="Show Password",
                            variable=show_pass,
                            command=toggle_password,
                            checkbox_width= 15,
                            checkbox_height= 15)
check_btn.pack()

# Conteudo do frame da direita 
image = Image.open ('bg.png')
image = image.resize((400, 400))
img = ImageTk.PhotoImage(image)
image_label = ctk.CTkLabel(master = frame_right, image = img, text ='')
image_label.pack(expand = True)


#Executar
app.mainloop()
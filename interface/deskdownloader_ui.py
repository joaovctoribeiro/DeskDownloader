import tkinter as tk
import webbrowser
from tkinter import ttk, filedialog, messagebox
from app.downloader import download_video, download_audio

def create_ui():

    """
    Função pra criar a UI.
    """

    def yt_download_video():

        """
        Obtem a URL e o caminho para onde vai o download.
        E chama a função de downlaod do vídeo.
        """

        # Obtém a URL inserida pelo usuário.
        # Abre a janela para escolher onde o download vai ficar.
        url = url_entry.get() 
        download_path = filedialog.askdirectory()

        # Chama a função de download e mostra a mensagem de erro ou sucesso.
        if download_path:
            message = download_video(url, download_path)
            messagebox.showinfo("Resultado", message)

    def yt_download_audio():

        """
        Obtem a URL e o caminho para onde vai o download.
        E chama a função de downlaod do áudio.
        """

        # Obtém a URL inserida pelo usuário.
        # Abre a janela para escolher onde o download vai ficar.
        url = url_entry.get()
        download_path = filedialog.askdirectory()

        # Chama a função de download e mostra a mensagem de erro ou sucesso.
        if download_path:
            message = download_audio(url, download_path)
            messagebox.showinfo("Resultado", message)

    # Função pra abrir o link no navegador.
    def open_link(event):
        webbrowser.open_new(r"https://github.com/joaovctoribeiro")

    # Função pra iniciar o sistema no centro da tela.
    def center_window(window, width=500, height=250):
        screen_width = window.winfo_screenwidth() 
        screen_height = window.winfo_screenheight() 
        x = (screen_width // 2) - (width // 2) # Calcula a posição x pra centralizar.
        y = (screen_height // 2) - (height // 2) # Calcula a posição y pra centralizar.
        window.geometry(f"{width}x{height}+{x}+{y}")

    # Criando janela do app.
    app = tk.Tk()

    app.title("DeskDownloader - Download de Vídeos e Áudios do YouTube")
    app.geometry("500x220")
    app.resizable(False, False)

    # Centraliza a janela.
    center_window(app, 500, 260)

    style = ttk.Style()

    style.configure("TLabel", font=("Arial", 12))
    style.configure("TButton", font=("Arial", 10))
    style.configure("TEntry", font=("Arial", 12))

    main_frame = ttk.Frame(app, padding="10")
    main_frame.pack(fill=tk.BOTH, expand=True)

    ttk.Label(main_frame, text="URL do Vídeo do YouTube:", font=("Arial", 15, "bold")).pack(pady=5)

    # Campo para a url.
    url_entry = ttk.Entry(main_frame, width=50)
    url_entry.pack(pady=5)

    button_frame = ttk.Frame(main_frame, padding="10")
    button_frame.pack(pady=10)

    icon_path = "icon.png"  # Caminho para o ícone
    app.iconphoto(False, tk.PhotoImage(file=icon_path))  # Define o ícone

    # Botão para download do vídeo.
    ttk.Button(button_frame, text="Download do Vídeo", command=yt_download_video).grid(row=0, column=0, padx=5)

    # Botão para download o áudio.
    ttk.Button(button_frame, text="Download do Áudio", command=yt_download_audio).grid(row=0, column=1, padx=5)

    ttk.Label(main_frame, text="Desenvolvido por João Ribeiro.").pack(pady=5)

    # Label link para acessar no navegador.
    link_label = tk.Label(main_frame, text="Perfil do Github", font=("Arial", 10), fg="blue", cursor="hand2")
    link_label.pack(pady=10)
    link_label.bind("<Button-1>", open_link)

    ttk.Label(main_frame, text="v0.0.1").pack(pady=5)

    app.mainloop()
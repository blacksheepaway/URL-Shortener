import pyshorteners
import tkinter as tk

# Função para encurtar o URL longo usando o pyshorteners
def shorten_url():
    long_url = entry.get()
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)
    result_label.config(text=short_url)

    # Habilita o botão "Copiar URL" e passa a short_url para a função copy_url
    copy_button.config(state=tk.NORMAL, command=lambda: copy_url(short_url))

# Função para copiar a URL encurtado para a área de transferência
def copy_url(short_url):
    # Limpa a area de transferência
    root.clipboard_clear()
    root.clipboard_append(short_url)
    tk.messagebox.showinfo("Sucesso", "URL copiado para a área de transferência")

# Crie a janela principal com o tkinter
root = tk.Tk()
root.title("Encurtador de URL")
root.configure(background="#f7fafc")

title_label = tk.Label(root, text="Encurtador de URL", bg="#f7fafc", fg="#1d3557", font=("Helvetica", 14, "bold"))
title_label.grid(row=0, column=0, padx=20, pady=20)

url_label = tk.Label(root, text="URL Longo:", bg="#f7fafc", fg="#1d3557", font=("Helvetica", 10))
url_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry = tk.Entry(root, width=50)
entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

button = tk.Button(root, text="URL Encurtado", command=shorten_url)
button.grid(row=1, column=2, padx=10, pady=10, sticky="e")

result_label = tk.Label(root, text="", bg="#f7fafc", fg="#1d3557", font=("Helvetica", 10))
result_label.grid(row=2, column=1, padx=10, pady=10)

# Crie um botão para copiar a URL abreviada para a área de transferência - que estava inicialmente desativado
copy_button = tk.Button(root, text="Copiar URL", state=tk.DISABLED)
copy_button.grid(row=2, column=2, padx=10, pady=10)

# Inicia o loop principal
root.mainloop()

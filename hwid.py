import tkinter as tk
import sys
import hashlib
import platform
import pyperclip


def obter_hwid():

    system_info = platform.uname()
    hwid_data = f"{system_info.node}{system_info.processor}{system_info.system}"
    return hashlib.sha256(hwid_data.encode()).hexdigest()

def copiar_hwid():

    hwid_atual = obter_hwid()
    pyperclip.copy(hwid_atual)

root = tk.Tk()
root.withdraw()

janela_alerta = tk.Toplevel(root)
janela_alerta.title("HWID")
janela_alerta.geometry("400x150")
#janela_alerta.iconbitmap("fotos/icon.ico")
janela_alerta.resizable(False, False)

hwid_atual = obter_hwid()
mensagem = f"Seu HWID:\n\n{hwid_atual}"


lbl_mensagem = tk.Label(janela_alerta, text=mensagem)
lbl_mensagem.pack(pady=10)


copiar_botao = tk.Button(janela_alerta, text="Copiar HWID", command=copiar_hwid)
copiar_botao.pack(pady=5)

janela_alerta.protocol("WM_DELETE_WINDOW", lambda: [janela_alerta.destroy(), root.quit()])

root.mainloop()
sys.exit(1)
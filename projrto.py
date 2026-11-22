import tkinter as tk
from tkinter import messagebox

# Lista para armazenar todas as atividades cadastradas durante a execução
atividades = []


def cadastrar_atividade():
    """Coleta os dados dos campos, valida, salva na lista e atualiza a exibição."""
    nome = entry_nome.get().strip()
    materia = entry_materia.get().strip()
    atividade = entry_atividade.get().strip()
    data = entry_data.get().strip()
    horario = entry_horario.get().strip()
    obs = text_obs.get("1.0", tk.END).strip()
    status = "Concluída" if var_concluida.get() else "Pendente"

    # Validação básica dos campos principais
    if not materia or not atividade:
        messagebox.showwarning(
            "Campos obrigatórios",
            "Por favor, preencha pelo menos a Matéria e a Atividade / Projeto."
        )
        return

    # Estrutura em dicionário para armazenar os dados de cada compromisso
    lembrete = {
        "materia": materia,
        "atividade": atividade,
        "data": data if data else "Não informada",
        "horario": horario if horario else "Não informado",
        "observacao": obs if obs else "Sem observações",
        "status": status
    }

    atividades.append(lembrete)

    # Limpa os campos da atividade para facilitar o próximo cadastro
    entry_materia.delete(0, tk.END)
    entry_atividade.delete(0, tk.END)
    entry_data.delete(0, tk.END)
    entry_horario.delete(0, tk.END)
    text_obs.delete("1.0", tk.END)
    var_concluida.set(False)

    atualizar_resumo(nome)
    messagebox.showinfo("Sucesso", "Atividade cadastrada com sucesso!")


def atualizar_resumo(nome):
    """Atualiza a área de texto inferior com todas as atividades registradas."""
    texto_resumo.config(state="normal")
    texto_resumo.delete("1.0", tk.END)

    estudante = nome if nome else "Não informado"
    texto_resumo.insert(tk.END, f"Estudante: {estudante} | Total de atividades: {len(atividades)}\n")
    texto_resumo.insert(tk.END, "-" * 58 + "\n")

    for item in atividades:
        linha = (
            f"[Data: {item['data']} - Hora: {item['horario']}] - "
            f"Matéria: {item['materia']} - "
            f"Atividade: {item['atividade']}. "
            f"Status: {item['status']}.\n"
            f"Obs: {item['observacao']}\n\n"
        )
        texto_resumo.insert(tk.END, linha)

    texto_resumo.config(state="disabled")


# Configuração da janela principal
janela = tk.Tk()
janela.title("MY ORGANIZER - Organizador Acadêmico")
janela.geometry("520x620")
janela.resizable(False, False)

# Cabeçalho
tk.Label(
    janela,
    text="Novo Registro de Atividade",
    font=("Arial", 13, "bold")
).pack(anchor="w", padx=16, pady=(12, 8))

# Formulário de entrada
frame_form = tk.Frame(janela)
frame_form.pack(fill="x", padx=16)

tk.Label(frame_form, text="Seu nome:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=4)
entry_nome = tk.Entry(frame_form, width=42, font=("Arial", 10))
entry_nome.grid(row=0, column=1, sticky="w", pady=4)

tk.Label(frame_form, text="Matéria:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=4)
entry_materia = tk.Entry(frame_form, width=42, font=("Arial", 10))
entry_materia.grid(row=1, column=1, sticky="w", pady=4)

tk.Label(frame_form, text="Atividade / Projeto:", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=4)
entry_atividade = tk.Entry(frame_form, width=42, font=("Arial", 10))
entry_atividade.grid(row=2, column=1, sticky="w", pady=4)

tk.Label(frame_form, text="Data de entrega:", font=("Arial", 10)).grid(row=3, column=0, sticky="w", pady=4)
entry_data = tk.Entry(frame_form, width=18, font=("Arial", 10))
entry_data.grid(row=3, column=1, sticky="w", pady=4)

tk.Label(frame_form, text="Horário de entrega:", font=("Arial", 10)).grid(row=4, column=0, sticky="w", pady=4)
entry_horario = tk.Entry(frame_form, width=18, font=("Arial", 10))
entry_horario.grid(row=4, column=1, sticky="w", pady=4)

tk.Label(frame_form, text="Observação:", font=("Arial", 10)).grid(row=5, column=0, sticky="nw", pady=4)
text_obs = tk.Text(frame_form, width=42, height=4, font=("Arial", 10))
text_obs.grid(row=5, column=1, sticky="w", pady=4)

# Caixa de seleção de status
var_concluida = tk.BooleanVar()
tk.Checkbutton(
    frame_form,
    text="Atividade já foi concluída",
    variable=var_concluida,
    font=("Arial", 10)
).grid(row=6, column=1, sticky="w", pady=6)

# Botão principal de ação
btn_cadastrar = tk.Button(
    janela,
    text="Cadastrar Atividade",
    command=cadastrar_atividade,
    bg="#1e73be",
    fg="white",
    font=("Arial", 11, "bold"),
    cursor="hand2",
    relief="flat",
    pady=8
)
btn_cadastrar.pack(fill="x", padx=16, pady=(6, 12))

# Área de exibição do resumo
tk.Label(
    janela,
    text="Resumo das Atividades Cadastradas:",
    font=("Arial", 10, "bold")
).pack(anchor="w", padx=16)

texto_resumo = tk.Text(janela, height=13, width=60, font=("Arial", 9), state="disabled")
texto_resumo.pack(fill="both", expand=True, padx=16, pady=(4, 14))

# Inicia o loop da interface gráfica
janela.mainloop()

from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import google.generativeai as genai
import markdown

load_dotenv()

app = Flask(__name__)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('models/gemini-2.0-flash')

def formatar_anotacoes(anotacoes_brutas):
    """
    Formata e organiza anotações brutas usando a IA do Gemini em Markdown (compacto).
    """
    prompt = f"""Por favor, formate e organize as seguintes anotações bagunçadas usando a sintaxe Markdown de forma concisa e com mínimo espaçamento.

    {anotacoes_brutas}

    Apresente as anotações de forma clara, com títulos em Markdown (usando #),
    subtítulos (usando ##), listas (usando * ou -). Evite espaços excessivos entre os elementos.
    Liste os principais pontos de cada tópico usando listas Markdown de forma direta.
    Use ênfase (com **) quando necessário, mas mantenha a saída compacta.

    A saída deve ser diretamente em Markdown formatado, sem envolver o texto em blocos de código.
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip() if response.text else "Não foi possível formatar as anotações."
    except Exception as e:
        return f"Ocorreu um erro ao formatar as anotações: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    anotacoes_formatadas_md = None

    if request.method == "POST" and "anotacoes_brutas" in request.form:
        anotacoes_brutas = request.form["anotacoes_brutas"]
        anotacoes_formatadas_md = formatar_anotacoes(anotacoes_brutas)

    anotacoes_formatadas_html = markdown.markdown(anotacoes_formatadas_md) if anotacoes_formatadas_md else None

    return render_template("index.html", anotacoes_formatadas=anotacoes_formatadas_html)

if __name__ == "__main__":
    app.run(debug=True)
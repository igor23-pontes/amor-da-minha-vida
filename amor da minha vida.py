import streamlit as st
import time

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Feliz Aniversário, Amor!",
    page_icon="❤️",
    layout="centered"
)

# --- ESTILO (CSS) PARA FICAR COM CARA DE SITE PROFISSIONAL ---
st.markdown("""
    <style>
    .stApp {
        background-color: #FAFAFA;
    }
    .main-title {
        color: #E63946; /* Vermelho bonito */
        font-family: 'Helvetica', sans-serif;
        text-align: center;
        font-size: 3.5em;
        font-weight: 800;
        margin-bottom: 0px;
    }
    .sub-title {
        color: #1D3557; /* Azul escuro */
        text-align: center;
        font-size: 1.2em;
        margin-bottom: 30px;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        text-align: center;
    }
    .highlight {
        color: #E63946;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- CONTROLE DE FASES ---
if 'fase' not in st.session_state:
    st.session_state.fase = 0

def proxima_fase():
    st.session_state.fase += 1
    st.balloons()
    time.sleep(1)
    st.rerun()

# =========================================================
# TELA INICIAL
# =========================================================
if st.session_state.fase == 0:
    st.markdown("<h1 class='main-title'>Parabéns, Amor! ❤️</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Um pequeno site feito só para a minha Pitucha.</p>", unsafe_allow_html=True)
    
    st.image("https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif", use_container_width=True)
    
    st.write("---")
    st.markdown("""
    <div style="text-align: center;">
        <h3>Oi, meu amor!</h3>
        <p>Hoje é seu dia e eu queria fazer algo diferente.</p>
        <p>Para descobrir qual é o seu presente, você precisa provar que nossa história está gravada no coração.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("COMEÇAR O DESAFIO ✨", use_container_width=True):
            proxima_fase()

# =========================================================
# FASE 1: O DESTINO
# =========================================================
elif st.session_state.fase == 1:
    st.progress(33)
    st.markdown("<div class='card'><h3>📍 Fase 1: A Linha do Tempo</h3></div>", unsafe_allow_html=True)
    
    st.write("Tudo começou lá atrás, em **2017**, no **Colégio Santo Inácio**.")
    st.write("Eu já te achava a menina mais linda do 6º ano, mas a vida nos afastou por 4 anos...")
    st.write("Até que o destino agiu.")
    
    st.info("Onde foi nosso reencontro mágico, onde eu te vi e falei pra mim mesmo: **'Vou casar com ela'**?")
    
    resposta = st.radio("", ["Na fila do mercado", "Numa Festa Universitária", "No Tinder", "Na academia"])
    
    if st.button("Confirmar"):
        if resposta == "Numa Festa Universitária":
            st.success("Exato! Você estava linda demais. Ali eu tive certeza.")
            time.sleep(2)
            proxima_fase()
        else:
            st.error("Eita! Tenta de novo, Amor! 😂")

# =========================================================
# FASE 2: A ROTINA
# =========================================================
elif st.session_state.fase == 2:
    st.progress(66)
    st.markdown("<div class='card'><h3>😂 Fase 2: Coisas de Pitucha</h3></div>", unsafe_allow_html=True)
    
    st.write("A gente se diverte muito juntos, mas tem uma coisa específica que você faz que eu AMO ver.")
    st.info("Qual é a mania da Iza que faz o Pitucho rir junto?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Mandar Reels e rir sozinha"):
            st.toast("Isso é 100% você! 😂❤️")
            time.sleep(1.5)
            proxima_fase()
    with col2:
        if st.button("Dormir no meio do filme"):
            st.error("Isso acontece também... mas não é a resposta certa kkk")

# =========================================================
# FASE 3: O FUTURO (SONHO)
# =========================================================
elif st.session_state.fase == 3:
    st.progress(90)
    st.markdown("<div class='card'><h3>👩‍⚕️ Fase Final: O Orgulho</h3></div>", unsafe_allow_html=True)
    
    st.write("Eu admiro muito a mulher que você está se tornando.")
    st.write("Essa pergunta é sobre o futuro brilhante que te espera.")
    
    st.text_input("Qual é o maior sonho profissional da Iza?", key="sonho_iza")
    
    if st.button("Responder"):
        texto = st.session_state.sonho_iza.lower()
        # Aceita variações da resposta
        if "neuro" in texto or "médica" in texto or "medica" in texto:
            st.success("SIM! E você será a melhor Neurologista desse mundo.")
            st.write("Eu vou estar lá na primeira fila te aplaudindo.")
            time.sleep(3)
            proxima_fase()
        else:
            st.warning("Dica: Tem a ver com medicina e ser a melhor especialista em cérebros! Tente 'Neurologista'.")

# =========================================================
# FINAL: O CONVITE
# =========================================================
elif st.session_state.fase == 4:
    st.progress(100)
    st.balloons()
    
    st.markdown("<h1 class='main-title'>PARABÉNS, AMOR! 🎉</h1>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif", width=250)
    
    st.markdown("""
    <div class='card'>
        <p>Você acertou tudo. Você é a mulher da minha vida.</p>
        <p>Como presente, quero te levar para uma experiência especial.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    
    # --- CARTÃO DO CONVITE ---
    st.markdown("""
    <div style="background-color: #fff3cd; padding: 20px; border-radius: 10px; border: 2px dashed #dba900;">
        <h2 style="color: #856404; text-align: center;">☕ CONVITE ESPECIAL</h2>
        <p><strong>Onde:</strong> [Holandesa]</p>
        <p><strong>Quando:</strong> Sexta-feira (Seu Aniversário)</p>
        <p><strong>Traje:</strong> Linda como sempre</p>
        <p><strong>Missão:</strong> Tomar o melhor café da cidade com seu Pitucho.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    # BOTÃO DO MAPA
    # Substitua o link abaixo pelo link real do Google Maps ou Instagram
    st.link_button("📍 Ver Localização", "https://www.instagram.com/holandesapanificadora?igsh=MTl0NmNibXlkMWV3eQ==") 
    
    st.write("")
    st.markdown("<h3 style='text-align: center;'>Te amo muito! ❤️</h3>", unsafe_allow_html=True)

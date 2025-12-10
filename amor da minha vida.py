import streamlit as st
import time

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Feliz Aniversário, Amor!",
    page_icon="❤️",
    layout="centered"
)

# --- CSS ANTI-BUG (CORRIGE O MODO ESCURO E BOTÕES) ---
st.markdown("""
    <style>
    /* 1. Força o fundo BRANCO */
    .stApp {
        background-color: #FFFFFF !important;
    }
    
    /* 2. Força TODO texto a ser PRETO (Corrige o sumiço no iPhone) */
    h1, h2, h3, h4, h5, h6, p, div, span, label {
        color: #000000 !important;
    }
    
    /* 3. Estilo dos Cards (As caixinhas brancas) */
    .card {
        background-color: #F0F2F6; /* Cinza clarinho pra destacar do fundo */
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        text-align: center;
        border: 1px solid #E0E0E0;
    }
    
    /* 4. Título Principal Ajustado */
    .main-title {
        color: #E63946 !important; /* Vermelho */
        font-family: 'Helvetica', sans-serif;
        text-align: center;
        font-size: 2.2em; 
        font-weight: 800;
        margin-bottom: 15px;
    }
    
    /* 5. Botões Grandes e Fáceis de Clicar */
    .stButton button {
        width: 100%;
        height: 3.5em;
        border-radius: 12px;
        font-weight: bold;
        font-size: 18px;
        border: 1px solid #ddd;
        color: #333 !important; /* Texto do botão escuro */
    }
    /* Cor quando passa o mouse ou clica */
    .stButton button:hover, .stButton button:active {
        border-color: #E63946;
        color: #E63946 !important;
        background-color: #FFF5F5;
    }
    </style>
""", unsafe_allow_html=True)

# --- CONTROLE DE FASES ---
if 'fase' not in st.session_state:
    st.session_state.fase = 0

def proxima_fase():
    st.session_state.fase += 1
    st.balloons()
    time.sleep(0.5)
    st.rerun()

# =========================================================
# TELA INICIAL
# =========================================================
if st.session_state.fase == 0:
    st.markdown("<h1 class='main-title'>Parabéns, Amor! ❤️</h1>", unsafe_allow_html=True)
    
    # Imagem menorzinha para não ocupar a tela toda do celular
    st.image("https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif", use_container_width=True)
    
    st.markdown("""
    <div class='card'>
        <p><strong>Oi, minha Pitucha!</strong></p>
        <p>Preparei esse site especial para o seu dia.</p>
        <p>Vamos ver se você está com a memória boa?</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("COMEÇAR O DESAFIO ✨"):
        proxima_fase()

# =========================================================
# FASE 1: O DESTINO
# =========================================================
elif st.session_state.fase == 1:
    st.progress(33)
    st.markdown("<div class='card'><h3>📍 Onde a mágica aconteceu?</h3></div>", unsafe_allow_html=True)
    
    st.write("Começamos no **Santo Inácio (2017)**, ficamos 4 anos longe e nos reencontramos...")
    st.info("Onde foi que eu te vi e decidi: **'Vou casar com ela'**?")
    
    # BOTÕES NO LUGAR DE RADIO (Muito melhor pro celular)
    if st.button("Na fila do mercado"):
        st.error("Não... 😂")
    
    if st.button("Numa Festa Universitária"):
        st.success("SIM! Ali eu tive certeza.")
        time.sleep(1.5)
        proxima_fase()
        
    if st.button("No Tinder"):
        st.error("Errou! Tenta de novo.")

# =========================================================
# FASE 2: A MANIA
# =========================================================
elif st.session_state.fase == 2:
    st.progress(66)
    st.markdown("<div class='card'><h3>😂 Coisas de Iza</h3></div>", unsafe_allow_html=True)
    
    st.write("Qual é a sua mania que eu mais amo e acho engraçada?")
    
    if st.button("Mandar Reels e rir sozinha"):
        st.toast("Isso é muito você! 😂❤️")
        time.sleep(1.5)
        proxima_fase()
        
    if st.button("Dormir assistindo filme"):
        st.error("Acontece, mas não é essa! kkk")

# =========================================================
# FASE 3: O SONHO (TEXTO)
# =========================================================
elif st.session_state.fase == 3:
    st.progress(90)
    st.markdown("<div class='card'><h3>👩‍⚕️ O Orgulho</h3></div>", unsafe_allow_html=True)
    
    st.write("Qual é o maior sonho profissional da Iza?")
    
    # Input de texto continua igual
    sonho = st.text_input("Escreva aqui:", key="sonho_iza")
    
    if st.button("ENVIAR RESPOSTA"):
        texto = sonho.lower()
        if "neuro" in texto or "médica" in texto or "medica" in texto:
            st.success("A Melhor Neurologista do Mundo! 🧠")
            time.sleep(2)
            proxima_fase()
        else:
            st.warning("Dica: Tem a ver com medicina e cérebros! Tente 'Neurologista'.")

# =========================================================
# FINAL: O CONVITE
# =========================================================
elif st.session_state.fase == 4:
    st.progress(100)
    st.balloons()
    
    st.markdown("<h1 class='main-title'>PARABÉNS! 🎉</h1>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif", use_container_width=True)
    
    st.markdown("""
    <div class='card'>
        <p>Você acertou tudo. Te amo!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # CONVITE
    st.markdown("""
    <div style="background-color: #fff3cd; padding: 15px; border-radius: 10px; border: 2px dashed #dba900; color: #000;">
        <h3 style="color: #856404; margin:0;">☕ CONVITE OFICIAL</h3>
        <hr>
        <p><strong>Local:</strong> [HOLANDESA]</p>
        <p><strong>Dia:</strong> Sexta-feira</p>
        <p><strong>Missão:</strong> Café especial com o Pitucho</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    # Substitua o link aqui
    st.link_button("📍 VER LOCALIZAÇÃO", "https://www.instagram.com/holandesapanificadora?igsh=MTl0NmNibXlkMWV3eQ==", use_container_width=True)
    
    st.write("")
    st.markdown("<h4 style='text-align: center; color: #E63946;'>Seu Pitucho ❤️</h4>", unsafe_allow_html=True)

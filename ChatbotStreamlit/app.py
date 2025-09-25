import streamlit as st
import random
import time

st.title("Nnao AI")


# chat memory
if "pesan" not in st.session_state:
    st.session_state.pesan = []

# input
pesanUser = st.chat_input("Hello")

# efek ketik
def typing_effect(text):
    for char in text:        # kirim per karakter
        yield char
        time.sleep(0.04)     # atur delay (0.03 lebih halus)


# KNOWLEDGE PER KATEGORI
sapaan = {
    "hai": random.choice(["Hai juga, gimana kabarnya Ryan?", "Halo Ryan, gimana hari ini?", "Halo Ryan, butuh sesuatu?",]),
    "hello": random.choice(["Hai juga, gimana kabarnya Ryan?", "Halo Ryan, gimana hari ini?", "Halo Ryan, butuh sesuatu?",]),
    "halo": random.choice(["Hai juga, gimana kabarnya Ryan?", "Halo Ryan, gimana hari ini?", "Halo Ryan, butuh sesuatu?",])
}
data_diri = {
    "nisn": "NISN kamu adalah 000000000",
    "nomor hp": "Nomor hp kamu adalah 09999999"
}



# knowledge
knowledgeBase = {
    "sapaan": sapaan,
    "data": data_diri
}

# riwayat
for pesan in st.session_state.pesan:
    with st.chat_message(pesan["role"]):
        st.markdown(pesan["content"])

if pesanUser:
    #  simpan pesan
    st.session_state.pesan.append({"role": "user", "content": pesanUser})
    # cari jawaban
    respon = None
    for kategori, data in knowledgeBase.items():
        if pesanUser.lower() in data:
            respon = data[pesanUser.lower()]
            break
    if not respon:
        respon = "Maaf aku gak ngerti😊"
    
    with st.chat_message("user"):
        st.markdown(pesanUser)

    # Simpan respon bot pakai efek ketik
    with st.chat_message("assistant"):
        response_text = st.write_stream(typing_effect(respon))

    # simpan respon
    st.session_state.pesan.append({"role": "assistant", "content": respon})



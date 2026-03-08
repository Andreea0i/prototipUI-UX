import streamlit as st

#titlu aplicatie
st.title("Prototip: Sistem digital de Depunere Declaratii Fiscale")
st.subheader("Monotorizare Servicii")

#Sectiune date personale
st.header("1. Identificare Contribuabil")
nume = st.text_input("Nume si Prenume")
cnp = st.text_input("CNP(Cod Numeric Personal)", max_chars=13)

if cnp and (not cnp.isdigit() or len(cnp) !=13):
    st.error("Eroare: CNP invalid.")

#Detalii venit
st.header("2. Detalii Venituri")
tip_venit = st.selectbox("Sursa venitului",
                         ["Activitati independente", "Chirii", "Dividente", "Alte surse"])
suma_bruta = st.number_input("Suma de bruta incasata(RON)", min_value=0.0)

#Calculare impozit
impozit = suma_bruta * 0.10
st.write(f"**Impozit calculat automat (10%):** {impozit} RON")

#Incarcare documente
st.header("3. Documente Justificative")
document = st.file_uploader("Incarca adeverinta de venit(PDF/JPG)")

#final
if st.button("Trimite Declaratia"):
    if nume and cnp and len(cnp) == 13:
        st.success(f"Declaratie trimisa cu succes pentru {nume}!")
        #st.balloons()
    else:
        st.warning("Va rugam sa completati toate campurile corect.")
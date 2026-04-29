import streamlit as st
import subprocess

st.title("🥷 HackingTool Web Panel")

# Isang sidebar para sa navigation
menu = ["Home", "System Info", "Run Tool"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.write("Welcome sa iyong Web Interface! Piliin ang tool sa sidebar.")

elif choice == "System Info":
    st.subheader("Files in Repository")
    # Ito yung ginawa mo kanina pero mas malinis na listahan
    files = subprocess.check_output(["ls"]).decode("utf-8")
    st.code(files)

elif choice == "Run Tool":
    st.subheader("Execute Hacking Tool")
    command = st.text_input("I-type ang command (halimbawa: python3 hackingtool.py --help)")
    
    if st.button("Run"):
        if command:
            # Dito natin papataktbuhin ang script at kukunin ang output
            try:
                result = subprocess.check_output(command.split(), stderr=subprocess.STDOUT).decode("utf-8")
                st.code(result)
            except Exception as e:
                st.error(f"Error: {e}")

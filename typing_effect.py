import streamlit as st
import asyncio

async def type_text(text, speed=0.05):
    placeholder = st.empty()
    typed_text = ""
    for char in text:
        typed_text += char
        placeholder.markdown(f"**{typed_text}**")
        await asyncio.sleep(speed)

def main():
    st.title("Typing Effect Example (Efficient)")
    user_message = st.text_input("Enter your message:")

    if st.button("Show Typing Effect"):
        if user_message:
            asyncio.run(type_text(user_message))

if __name__ == "__main__":
    main()

import streamlit as st
import qrcode
from io import BytesIO
import re
import email_validator

st.markdown("""<style>.st-emotion-cache-sh2krr p{font-size: 20px;}</style>""", unsafe_allow_html=True)

#Define tab names
tabs = ["URL", "Text", "Email", "Phone"]

#Create tabs
selected_tab = st.sidebar.selectbox("Select QR Code Type", tabs, index=0)

#Title
st.markdown("<h1 style='text-align: center;'>QR Code Generator</h1>", unsafe_allow_html=True)

#Function to validate email format
def is_valid_email(email):
    try:
        email_validator.validate_email(email)
        return True
    except email_validator.EmailNotValidError as e:
        return False

#Function to validate phone number format
def is_valid_phone(phone):
    pattern = r'^[0-9]{10}$'
    if re.match(pattern, phone):
        return True
    else:
        return False

if selected_tab == "URL":
    url = st.text_input("Enter URL :")
    if st.button("Generate QR Code"):
        if url:
            qr = qrcode.make(url)
            img = BytesIO()
            qr.save(img, format='PNG')
            img.seek(0)
            st.image(img, caption='Generated QR Code', use_column_width=True)
            st.download_button(
                label="Download QR Code",
                data=img,
                file_name="myqr.png",
                mime="image/png"
            )

elif selected_tab == "Text":
    text = st.text_area("Enter Text :")
    if st.button("Generate QR Code"):
        if text:
            qr = qrcode.make(text)
            img = BytesIO()
            qr.save(img, format='PNG')
            img.seek(0)
            st.image(img, caption='Generated QR Code', use_column_width=True)
            st.download_button(
                label="Download QR Code",
                data=img,
                file_name="myqr.png",
                mime="image/png"
            )

elif selected_tab == "Email":
    email = st.text_input("Enter Email :")
    if st.button("Generate QR Code"):
        if email and is_valid_email(email):
            qr = qrcode.make(f"mailto:{email}")
            img = BytesIO()
            qr.save(img, format='PNG')
            img.seek(0)
            st.image(img, caption='Generated QR Code', use_column_width=True)
            st.download_button(
                label="Download QR Code",
                data=img,
                file_name="myqr.png",
                mime="image/png"
            )
        elif email:
            st.error("Please Enter Valid Email Address.")

elif selected_tab == "Phone":
    phone = st.text_input("Enter Phone Number :")
    if st.button("Generate QR Code"):
        if phone and is_valid_phone(phone):
            qr = qrcode.make(f"tel:{phone}")
            img = BytesIO()
            qr.save(img, format='PNG')
            img.seek(0)
            st.image(img, caption='Generated QR Code', use_column_width=True)
            st.download_button(
                label="Download QR Code",
                data=img,
                file_name="myqr.png",
                mime="image/png"
            )
        elif phone:
            st.error("Please Enter Valid 10-digit Phone Number.")
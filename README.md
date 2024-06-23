# QR Code Generator

This Streamlit application allows users to generate QR codes for URLs, text, email addresses, and phone numbers. The generated QR codes can be displayed within the app and downloaded as PNG files.

## Features

- **URL QR Code Generation:** Enter a URL to generate a QR code that directs to the given URL.
- **Text QR Code Generation:** Enter any text to generate a QR code that contains the text.
- **Email QR Code Generation:** Enter an email address to generate a QR code that creates an email message to the given address.
- **Phone QR Code Generation:** Enter a phone number to generate a QR code that initiates a phone call to the given number.

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/qrcode-generator.git
   ```
2. **Navigate to the project directory:**
   ```sh
   cd qrcode-generator
   ```
3. **Install the required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit app:**
   ```sh
   streamlit run app.py
   ```
2. **Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).**

3. **Select the type of QR code you want to generate from the sidebar:**
   - URL
   - Text
   - Email
   - Phone

4. **Input the required information and click on the "Generate QR Code" button.**

5. **View the generated QR code and download it using the "Download QR Code" button.**

## Code Explanation

### Libraries Used

- **streamlit:** For creating the web interface.
- **qrcode:** For generating QR codes.
- **BytesIO:** For handling image data in memory.
- **re:** For validating phone numbers.
- **email_validator:** For validating email addresses.

### Functions

- **is_valid_email(email):** Validates the email format using the `email_validator` library.
- **is_valid_phone(phone):** Validates the phone number format using a regular expression (expects a 10-digit number).

### Tabs

- **URL Tab:**
  - Takes a URL input from the user.
  - Generates and displays the QR code.
  - Provides an option to download the QR code.

- **Text Tab:**
  - Takes text input from the user.
  - Generates and displays the QR code.
  - Provides an option to download the QR code.

- **Email Tab:**
  - Takes an email address input from the user.
  - Validates the email address.
  - Generates and displays the QR code if the email is valid.
  - Provides an option to download the QR code.
  - Displays an error message if the email is invalid.

- **Phone Tab:**
  - Takes a phone number input from the user.
  - Validates the phone number (expects a 10-digit number).
  - Generates and displays the QR code if the phone number is valid.
  - Provides an option to download the QR code.
  - Displays an error message if the phone number is invalid.

Feel free to contribute to this project by opening issues and submitting pull requests. Happy coding!

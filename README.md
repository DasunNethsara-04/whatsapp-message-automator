# WhatApp Message Automator
WhatApp Message Automator is a simple Python program that automates the process of sending messages to multiple WhatsApp numbers using WhatsApp Web. It reads phone numbers from a text file (phoneNums.txt) and sends a predefined message to each of those numbers.


## Prerequisites
Before using AutoWhatsAppSender, ensure you have the following:
* Python installed on your system (version 3.10 or higher)
* Web browser with WhatsApp Web logged in


## Installation
1. Clone the Repository:
   ```bash
   git clone https://github.com/DasunNethsara-04/whatsapp-message-automator.git
   ```
2. Navigate to the Directory:
   ```bash
   cd whatsapp-message-automator
   ```
3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```


## Usage
1. Prepare Phone Numbers:
   - Open `phoneNums.txt`.
   - Delete the dummy content.
   - Enter the WhatsApp numbers line by line.<br/>
![image](https://github.com/DasunNethsara-04/whatsapp-message-automator/assets/99202052/327fdc77-20a5-41fb-a6c8-93eb070c1a51)

2. Run the Program:
   ```bash
   python auto_whatsapp_sender.py
   ```
3. Follow Instructions:
   - Make sure your browser is open and logged in to WhatsApp Web.
   - The program will automatically open WhatsApp Web in your default browser.
   - It will send the predefined message to each phone number sequentially.
4. Note:
   - Ensure a stable internet connection throughout the process.
   - Avoid interfering with the browser window while the program is running.


## Configuration
   - Message: You can customize the message to be sent by modifying the `message` variable in `app.py`.

## Browser Requirements
   - *Logged In:* Make sure you are logged into your WhatsApp account from the web browser.
   - *Default Browser:* Ensure that the browser being used is your default browser.

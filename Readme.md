# 🔐 Caesar Cipher Encryption & Decryption Tool

A simple Python-based tool that encrypts and decrypts messages using the **Caesar Cipher**, one of the earliest and most well-known encryption techniques.  
This project is perfect for beginners learning cybersecurity, cryptography fundamentals, and Python programming.



## 📌 Features

✔ Encrypt any text using a shift (key)  
✔ Decrypt encrypted text back to original  
✔ Preserves uppercase, lowercase, spaces, and punctuation  
✔ Beginner-friendly code  
✔ Great for cybersecurity portfolio projects



## 🧠 Understanding the Caesar Cipher

The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted by a fixed number.

Example with a shift of **3**:  
- A → D  
- B → E  
- X → A  
- HELLO → KHOOR  

Although it is not used in modern cryptography, it is extremely useful for learning:

- How encryption works  
- Character manipulation  
- How to reverse an encryption operation  
- Basic cryptography principles  


## ▶️ How to Run the Program

1. Install Python on your computer.
2. Open your terminal or command prompt.
3. Navigate to the project directory:
    Run the script:
        Copy code
        python cipher.py
        Enter your message and the shift value (1–25).

        🧪 Example Usage
        Input:
        Message:
            Attack At Dawn!
        
        Output:
            pgsql
        Encrypted: Exxego Ex Hear!
        Decrypted Back: Attack At Dawn!
        🧩 How It Works
            ord() converts characters to ASCII codes.

        Characters are shifted within their alphabet ranges (A–Z or a–z).
        26 ensures wrap-around so Z becomes A.
        Decryption simply reverses the shift.

🤝 Contributing
This is a beginner-friendly project — feel free to fork it, improve it, and open pull requests.





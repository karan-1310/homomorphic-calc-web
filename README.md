# 🔐 Homomorphic Encryption Calculator (CKKS-based)

This project is a Streamlit-powered calculator that demonstrates **privacy-preserving arithmetic computation** using **Homomorphic Encryption (HE)**. It allows users to input arithmetic expressions, **encrypts the entire computation process**, and only decrypts the final result — all without revealing any intermediate values.

The calculator is built using the **CKKS scheme from TenSEAL**, suitable for approximate real-number arithmetic, and supports BODMAS operations on encrypted inputs.

---

## 📌 Introduction

**Homomorphic Encryption (HE)** is a modern cryptographic technique that allows computation on encrypted data without ever decrypting it. Think of it like assembling a ring inside a **locked glovebox** — workers (i.e., computers) can perform operations **without ever opening the box**, and only the key owner can unlock the final result.

- ✅ Data stays encrypted throughout computation.
- ✅ Operations are performed on encrypted values.
- ✅ Only the final result is decrypted by the key holder.

---

## 🧠 Conceptual Analogy

| Step     | What It Means                    | Analogy                          |
|----------|----------------------------------|----------------------------------|
| KeyGen   | Generates a public/private key   | Making a lock and key            |
| Enc      | Encrypts data with public key    | Dropping material into glovebox  |
| Eval     | Operates on encrypted data       | Assembling ring inside glovebox  |
| Dec      | Decrypts using private key       | Unlocking glovebox to see result |

---

## 🔍 Use Case Example

Let’s say you're storing sensitive emails in the cloud and want to search only those with “homomorphic” in the subject.

- 🔒 Normally: All data must be decrypted to perform the search — breaking privacy.
- 🛡 With HE: 
  - Query is encrypted and sent.
  - Search is performed on encrypted content.
  - Results are returned encrypted.
  - Only **you** decrypt them.

This is the power of **privacy-preserving computation**.

---

## 🛠️ Technologies Used

- **Language:** Python 3
- **UI Framework:** Streamlit
- **Encryption Library:** [TenSEAL](https://github.com/OpenMined/TenSEAL) (CKKS Scheme)
- **Libraries:** 
  - `tenseal` for encryption
  - `ast` and `operator` for expression parsing
  - `streamlit` for web interface

---

## 📋 Features

- 🔢 Supports arithmetic expressions with `+`, `-`, `*`, `/`
- 🔒 All values are encrypted using CKKS vectors
- 🔁 Operates fully on ciphertexts
- 🔓 Only the final result is decrypted for the user
- ⚠️ Handles division-by-zero errors and invalid inputs

---

## 💻 Code Architecture

### ➤ Expression Evaluation (`eval_expr()`)

- Recursively parses arithmetic expressions using Python’s `ast` module.
- Applies BODMAS logic while preserving homomorphic context.
- Handles encrypted addition, subtraction, multiplication, and secure division.

### ➤ UI with Streamlit

- Accepts a user-friendly expression input.
- Encrypts operands and evaluates securely.
- Displays only the final decrypted result on the screen.

---

## 🧪 Example Input/Output

#### ✅ Input:

```

(5 + 4) \* (2 - 1) / 3

```

#### 🔐 Internally:
- All numbers are encrypted using CKKS.
- Computation performed entirely on ciphertexts.
- Decryption reveals final output only.

#### ✅ Output:

```

✅ Encrypted Calculation Result: 3.0000

````

---

## 🧬 Real Homomorphic Schemes Overview

| Scheme         | Supported Operations                       |
|----------------|--------------------------------------------|
| RSA            | Multiplication (mod N)                     |
| ElGamal        | Multiplication                             |
| Paillier       | Addition, XOR                              |
| BGN05          | Limited quadratic formulas                 |
| **CKKS**       | Approximate real number arithmetic (✅ Used)|
| BFV            | Integer arithmetic                         |
| Gentry (2009)  | First fully homomorphic scheme             |

---

## 🚀 How to Run the Project

### 🧰 Prerequisites

Install required libraries:

```bash
pip install streamlit tenseal
````

### ▶️ Run the App

```bash
streamlit run your_script_name.py
```

*(Replace `your_script_name.py` with your actual filename, e.g., `homomorphic_calculator.py`)*

---

## 📌 Notes on CKKS Scheme

* CKKS is suitable for **real-number arithmetic** but supports only **approximate** results.
* Precision may slightly vary due to floating-point representation.
* Ideal for **ML**, **signal processing**, and **privacy-preserving computation**.

---

## 📷 Dashboard Preview

*(Add a screenshot here if available)*

---

## ✅ Future Enhancements

* Add support for **BFV scheme** (exact integer operations).
* Visualize encryption/decryption steps for educational clarity.
* Extend to **multi-client encrypted computation**.

---

## 🙏 Acknowledgements

* OpenMined’s [TenSEAL](https://github.com/OpenMined/TenSEAL) for making encrypted computing accessible.
* [Streamlit](https://streamlit.io/) for rapid app development.
* Homomorphic encryption research and academic community.

---

## ⚠️ Disclaimer

This project is built **strictly for educational purposes** and academic experimentation. Do not use it for secure production applications unless professionally audited and tested.

---

```

---

✅ You can **copy the entire block above** into your `README.md` file and push it directly to your GitHub repository.  
Let me know if you’d like to include a screenshot, deployment guide (e.g., Streamlit Cloud), or even a YouTube demo link!
```

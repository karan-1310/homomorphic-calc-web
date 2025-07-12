import streamlit as st
import tenseal as ts

# Page Title
st.title("🔐 Homomorphic Encryption Calculator")

# User Inputs
num1 = st.number_input("Enter first number:", value=0.0)
num2 = st.number_input("Enter second number:", value=0.0)

if st.button("Encrypt, Add & Show Results"):
    # Step 1: Create encryption context
    context = ts.context(
        ts.SCHEME_TYPE.CKKS,
        poly_modulus_degree=8192,
        coeff_mod_bit_sizes=[60, 40, 40, 60]
    )
    context.global_scale = 2**40
    context.generate_galois_keys()

    # Step 2: Encrypt inputs
    enc_num1 = ts.ckks_vector(context, [num1])
    enc_num2 = ts.ckks_vector(context, [num2])

    # Step 3: Show size of encrypted numbers
    serialized1 = enc_num1.serialize()
    serialized2 = enc_num2.serialize()

    st.write(f"🔒 Encrypted {num1} size: {len(serialized1)} bytes")
    st.write(f"🔒 Encrypted {num2} size: {len(serialized2)} bytes")

    # Step 4: Perform addition on encrypted numbers
    enc_result = enc_num1 + enc_num2

    # Step 5: Decrypt result
    result = enc_result.decrypt()

    # Step 6: Display result
    st.success(f"✅ Encrypted Addition Result: {result[0]:.4f}")

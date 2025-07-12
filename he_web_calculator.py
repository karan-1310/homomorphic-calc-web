import streamlit as st
import tenseal as ts
import ast
import operator

# Supported operators mapping for easy lookup
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}

def eval_expr(node, context):
    if isinstance(node, ast.Num):  # number literal
        return ts.ckks_vector(context, [node.n])

    elif isinstance(node, ast.BinOp):
        left = eval_expr(node.left, context)
        right = eval_expr(node.right, context)

        if isinstance(node.op, ast.Add):
            return left + right
        elif isinstance(node.op, ast.Sub):
            return left - right
        elif isinstance(node.op, ast.Mult):
            return left * right
        elif isinstance(node.op, ast.Div):
            decrypted_right = right.decrypt()[0]
            if decrypted_right == 0:
                raise ZeroDivisionError("Division by zero detected.")
            return left / decrypted_right
        else:
            raise TypeError(f"Unsupported operation: {type(node.op)}")
    else:
        raise TypeError(f"Unsupported expression element: {type(node)}")

# Streamlit Page Title
st.title("🔐 Encrypted Expression Calculator (with BODMAS)")

# Input expression from user
expression = st.text_input("Enter your arithmetic expression (e.g., (5+4)*(2-1)/3):")

if st.button("Encrypt, Calculate & Show Result"):

    try:
        # Parse the expression safely
        parsed_expr = ast.parse(expression, mode='eval').body

        # Create encryption context
        context = ts.context(
            ts.SCHEME_TYPE.CKKS,
            poly_modulus_degree=8192,
            coeff_mod_bit_sizes=[60, 40, 40, 60]
        )
        context.global_scale = 2**40
        context.generate_galois_keys()

        # Evaluate encrypted expression
        enc_result = eval_expr(parsed_expr, context)

        # Decrypt final result
        final_result = enc_result.decrypt()[0]

        st.success(f"✅ Encrypted Calculation Result: {final_result:.4f}")

    except ZeroDivisionError as zde:
        st.error(f"❌ Error: {zde}")

    except Exception as e:
        st.error(f"❌ Invalid expression or unsupported operation.\nDetails: {e}")

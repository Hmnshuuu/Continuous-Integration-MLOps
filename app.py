import streamlit as st
import math

# Streamlit UI
st.title("Root & Logarithm Calculator")
st.write("Enter a positive number to calculate its square root, cube root, natural log (ln), and base-10 log.")

# Get user input
x = st.number_input("Enter a positive number", value=1.0, step=0.1, min_value=0.0001)

# Calculate results
square_root = math.sqrt(x)
cube_root = x ** (1/3)
ln_x = math.log(x)
log10_x = math.log10(x)

# Display results
st.write(f"Square root of {x} is: {square_root:.4f}")
st.write(f"Cube root of {x} is: {cube_root:.4f}")
st.write(f"Natural logarithm (ln) of {x} is: {ln_x:.4f}")
st.write(f"Base-10 logarithm (log₁₀) of {x} is: {log10_x:.4f}")
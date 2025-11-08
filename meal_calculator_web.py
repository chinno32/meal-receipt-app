import streamlit as st

st.set_page_config(page_title="Meal Receipt Generator", page_icon="🍽️")

st.title("🍽️ Meal Receipt Generator")

# Inputs
child_price = st.number_input("Child Meal Price ($)", min_value=0.0, step=0.5)
adult_price = st.number_input("Adult Meal Price ($)", min_value=0.0, step=0.5)
children = st.number_input("# of Children", min_value=0, step=1)
adults = st.number_input("# of Adults", min_value=0, step=1)
drink_price = st.number_input("Drink Price ($)", min_value=0.0, step=0.5)
drinks = st.number_input("# of Drinks", min_value=0, step=1)
appetizer_price = st.number_input("Appetizer Price ($)", min_value=0.0, step=0.5)
appetizers = st.number_input("# of Appetizers", min_value=0, step=1)
tax_rate = st.number_input("Tax Rate (%)", min_value=0.0, step=0.5)
tip_rate = st.number_input("Tip Rate (%)", min_value=0.0, step=0.5)
payment = st.number_input("Payment Amount ($)", min_value=0.0, step=0.5)

if st.button("Generate Receipt"):
    subtotal = (children * child_price) + (adults * adult_price) + (drinks * drink_price) + (appetizers * appetizer_price)
    tax = subtotal * (tax_rate / 100)
    total = subtotal + tax
    tip = total * (tip_rate / 100)
    grand_total = total + tip
    change = payment - grand_total

    st.subheader("🧾 Receipt")
    st.text(f"Child Meals   x{children} @ ${child_price:.2f} = ${children * child_price:.2f}")
    st.text(f"Adult Meals   x{adults} @ ${adult_price:.2f} = ${adults * adult_price:.2f}")
    st.text(f"Drinks        x{drinks} @ ${drink_price:.2f} = ${drinks * drink_price:.2f}")
    st.text(f"Appetizers    x{appetizers} @ ${appetizer_price:.2f} = ${appetizers * appetizer_price:.2f}")
    st.text("------------------------------")
    st.text(f"Subtotal:     ${subtotal:.2f}")
    st.text(f"Tax:          ${tax:.2f}")
    st.text(f"Tip:          ${tip:.2f}")
    st.text(f"Grand Total:  ${grand_total:.2f}")
    st.text(f"Payment:      ${payment:.2f}")
    st.text(f"Change:       ${change:.2f}")
    st.text("------------------------------")
    st.text("Thank you for dining with us!")

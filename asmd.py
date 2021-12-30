from numpy import subtract
import streamlit as st


st.title("Welcome to this page")
st.header("This page will help you to perform Addition Subtraction Multipllication and Division on two number")
c=st.selectbox("Choose what you want to perform",["Addition","Subtraction","Multiplication","Division"])
a=st.number_input("Enter first number")
b=st.number_input("Enter second number")
if (st.button("SUBMIT")):
    if c=="Addition":
        d=a+b
        st.text(d)

    elif c=="Subtraction":
        d=a-b
        st.text(d)
    elif c=="Multiplication":
        d=a*b
        st.text(d)
    else:
        d=a/b
        st.text(d)
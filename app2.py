import streamlit as st
import nltk
nltk.download('stopwords')

if "users" not in st.session_state:
    st.session_state["users"] = {"testuser": "password123"}

def register_user():
    st.subheader("User Registration")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type='password')
    confirm_password = st.text_input("Confirm Password", type='password')

    if st.button("Register"):
        if new_user in st.session_state["users"]:
            st.error("Username already exists. Try another one.")
        elif new_password != confirm_password:
            st.error("Passwords do not match.")
        else:
            st.session_state["users"][new_user] = new_password 
            st.success("Registration Successful! You can now log in.")

def user_login():
    st.subheader("User Login")
    st.success("If you are a new user then move to the registration page")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        if username in st.session_state["users"] and st.session_state["users"][username] == password:
            st.success(f"Welcome {username}!")
        else:
            st.error("Invalid Username or Password")

def admin_login():
    st.subheader("Admin Login")
    ad_user = st.text_input("Admin Username")
    ad_password = st.text_input("Admin Password", type='password')

    if st.button('Login'):
        if ad_user == 'admin' and ad_password == 'admin123':
            st.success("Welcome Dear Admin!")
        else:
            st.error("Wrong ID & Password Provided")

def run():
    st.title("AI Resume Analyser")
    st.sidebar.markdown("# Choose User")
    activities = ["User", "Admin", "Register"]
    choice = st.sidebar.selectbox("Choose among the given options:", activities)

    if choice == "User":
        user_login()
    elif choice == "Admin":
        admin_login()
    elif choice == "Register":
        register_user()

    links = [
        '[©Developed by Shanvi](https://www.linkedin.com/in/shanvi-agarwal-93b38928b)',
        '[©Developed by Anshika](https://www.linkedin.com/in/anshika-agrawal-417305293)',
        '[©Developed by Swati](https://www.linkedin.com/in/swati-chaudhary-636039290)',
        '[©Developed by Sumit](https://www.linkedin.com/in/sumit-pilaniya-1b663828a)'
    ]
    for link in links:
        st.sidebar.markdown(link, unsafe_allow_html=True)

run()

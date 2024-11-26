import streamlit as st  
import datetime
from PIL import Image

st.set_page_config(page_title="My Biography", layout='wide')


# ---- HEADER SECTION ----
st.title("BIOGRAPHY")
st.subheader("Hi, I am Dimple")
st.write("A 1st Year Computer Engineering student")
# ---- Personal Info (Left Side) ----
# ---- ID (Right Side) ----
with st.container():
    left_column, right_column=st.columns(2)
#allignment
    with left_column: #similar to if-else statement
        st.subheader("Personal Information")
#medium font size
        name= st.text_input("Name", "Dimple D. Cubillan")

        #age
        age=st.selectbox(
            "Age",
            ("18", "19", "20",
             "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", 
             "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", 
             "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", 
             "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", 
             "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", 
             "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", 
             "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", 
             "91", "92", "93", "94", "95", "96", "97", "98", "99", "100")
        )

        #bday
        bday=st.date_input("Birthday",datetime.date(2006,6,17))

        #gender
        options=["Male","Female"]
        gender=st.pills("Gender",options,selection_mode="single")

        #Family Bcakground
        #Mother
        st.subheader("Family Background")
        mother=st.text_input("Mother's name","Marisa D. Cubillan")
        mbday=st.date_input("Birthday",datetime.date(1979,4,22))

        #Father
        father=st.text_input("Father's Name","Rommel A. Cubillan")
        mbday=st.date_input("Birthday",datetime.date(1970,6,6))

        st.subheader("Educational Background")
#medium font size
        elem=st.text_area("Elementary","Numancia Central Elementary School ")
        hs=st.text_area("Junior High School","Surigao del Norte State University-Del Carmen Campus ")
        shs=st.text_area("Senior High School","Northeastern Mindanao Colleges ")
        college=st.text_area("College","Surigao del Norte State University ")
        st.write("---")
       
        with right_column: #similar to if-else statement
            #picture
            #button to change picture
            st.write(" ")
            st.subheader("Social Media Accounts")
            fb=st.text_input("Facebook","Dimple Cubillan")
            instagram=st.text_input("Instagram"," ")

        with right_column: #similar to if-else statement
            st.subheader("My Accomplishments")
#medium font size
            st.write("- I am the one of the Heads of Membership Committe of Del Carmen Youth Initiative",
                     "at the age also of 15 I worked as a Youth Animator for Community and Family Services International (CFSI)",
                     "as well as demonstrating Psychological First Aid to children as a facilitator for UNICEF and UNILAB")
            st.write("- Former SSC Auditor during my senior high school days")

import streamlit as st
import random
import secrets
import string

# Create slider and checkboxes for user decision
length_range = st.slider("Choose the length range for your password:", 4, 24, (8,16))
lowercase = st.checkbox("Include lowercase letters?")
uppercase = st.checkbox("Include uppercase letters?")
numbers = st.checkbox("Include numbers?")
specials = st.checkbox("Include special characters? (!,@,#,etc.)")

# Password generator function
def generate_password(min_length, max_length, upper, nums, spec):
    # Set bools & length vals
    upper = uppercase
    nums = numbers
    spec = specials
    min_length = length_range[0]
    max_length = length_range[1]
    leng = 0
    pw = ""
    if min_length==max_length:
        leng=min_length 
    else:
        leng = min_length + secrets.randbelow(max_length+1 - min_length)
    
    # Set our character lists
    lowerchars = string.ascii_lowercase
    upperchars = string.ascii_uppercase
    numchars = string.digits
    specchars = string.punctuation
    char_options = [string.ascii_lowercase]

    # Add one of each selected character to password
    pw+=lowerchars[secrets.randbelow(len(lowerchars))]
    if upper:
        pw+=upperchars[secrets.randbelow(len(upperchars))]
        char_options.append(upperchars)
    if nums:
        pw+=numchars[secrets.randbelow(len(numchars))]
        char_options.append(numchars)
    if spec:
        pw+=specchars[secrets.randbelow(len(specchars))]
        char_options.append(specchars)

    # Add the remaining characters (if any) to the list randomly
    for i in range(len(pw),leng):
        choice = secrets.choice(char_options)
        pw+=choice[secrets.randbelow(len(choice))]

    # Scramble password
    pw_list = list(pw)
    random.shuffle(pw_list)
    scrambled="".join(pw_list)
    
    return scrambled

is_disabled = not (lowercase or uppercase or numbers or specials)

st.write("**Select at least one option and then click the button below!**")
if st.button("Generate your password", disabled=is_disabled):
    final_password = generate_password(length_range[0],length_range[1],uppercase,numbers,specials)
    st.write("Password:")
    st.text(final_password)

import streamlit as st
import random
import string

# Create slider and checkboxes for user decision
length_range = st.slider("Choose the length range for your password:", 4, 24, (8,16))
lowercase = st.checkbox("Include lowercase letters?", value=True, disabled=True, help="Lower case letters are required by default")
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
        leng = random.randrange(min_length, max_length+1)
    
    # Set our character lists
    lowerchars = string.ascii_lowercase
    upperchars = string.ascii_uppercase
    numchars = string.digits
    specchars = string.punctuation
    char_options = [string.ascii_lowercase]

    # Add one of each selected character to password
    pw+=lowerchars[random.randrange(0,len(lowerchars))]
    if upper:
        pw+=upperchars[random.randrange(0,len(upperchars))]
        char_options.append(upperchars)
    if nums:
        pw+=numchars[random.randrange(0,len(numchars))]
        char_options.append(numchars)
    if spec:
        pw+=specchars[random.randrange(0,len(specchars))]
        char_options.append(specchars)

    # Add the remaining characters (if any) to the list randomly
    for i in range(len(pw),leng):
        choice = random.choice(char_options)
        pw+=choice[random.randrange(0,len(choice))]

    # Scramble password
    pw_list = list(pw)
    random.shuffle(pw_list)
    scrambled="".join(pw_list)
    
    return scrambled

if st.button("Generate your password"):
    final_password = generate_password(length_range[0],length_range[1],uppercase,numbers,specials)
    st.write("Password:")
    st.text(final_password)

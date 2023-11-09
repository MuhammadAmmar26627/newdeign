
import streamlit as st
######## Client Data ###########
# form=st.sidebar.form("Calculate Material and Labour")

# Input fields
st.sidebar.header("Packaging Estimation Sheet")
st.sidebar.header("Client Bio")
col1,col2=st.sidebar.columns(2)
client_name=col1._text_input("Client Name")
CSR=col2._text_input("CSR Name")
col1,col2=st.sidebar.columns(2)
client_email=col1._text_input("Client Email")
Phone=col2._text_input("Phone Number")


########### Sheet Data (Size) #############
col1, col2 = st.sidebar.columns(2)
Sheet_size=["23x36","25x36","22x28",'20x30','25x30',"27x34"]
Sheet = col1.selectbox(
    "Sheet Size",
    Sheet_size
)
Packets_size=[("9x7.66","11.5x7.2","12x7.66","9x11.5","11.5x12","12x23","18x23"),
  ("9x8.33","12.5x7.5","12x8.33","9x12.5","12.5x12","12x25","18x25"),
  ('9.33x7.33',"11x14","14x22"),("10x7.5","10x15",'10x20','15x20'),
  ("10x8.33","10x12.5",'12.5x15','15x25'),('9x11.33','13.5x17','17x27')]
packet_index=Sheet_size.index(Sheet)
Packet = col2.selectbox(
    "Packet Size",
    Packets_size[packet_index]
)
st.sidebar.header("Sheet Size")
col1, col2 = st.sidebar.columns(2)
W_S=col1.number_input("W_Sheet", min_value=0.0)

# st.write(W_S)

L_S=col2.number_input("L_Sheet", min_value=0.0)
# st.sidebar.header("Material")
col1, col2 = st.sidebar.columns(2)
Material = col1.selectbox(
    "Material",
    ["Bleach Card","Bux Board", "Art Card", "Kraft",]
)
gsm = col2.number_input("GSM", min_value=0,value=300)
col1, col2 = st.sidebar.columns(2)
up = col1.number_input("Box Uping", min_value=1)
Req_Q = col2.number_input("Required Quantity", min_value=1)


agree = st.sidebar.checkbox('Print Size Same as Sheet Size')
col1, col2 = st.sidebar.columns(2)
W_P=col1.number_input("W_Print", min_value=0.0)
L_P=col2.number_input("L_Print", min_value=0.0)
# submitted = st.sidebar.form_submit_button("Submit")
################################################

st.sidebar.header("Corrugation")
col1, col2 = st.sidebar.columns(2)
stock = col1.selectbox(
    "Corrugation Material",
    ["L1", "E Flute", "B Flute"]
)

pasting = col2.selectbox(
    "Corrugation Pasting",
    ["None","Single Side", "Double Side",]
)

st.sidebar.header("Printing Colors")
col1, col2, col3 = st.sidebar.columns(3)
process_color = col1.selectbox(
    "Process Color",
    [0,1,2,3,4,5,6,7,8,]
)
pantone_color=col2.number_input("Pantone Color", min_value=0)
matallic_color=col3.number_input("Matallic Color", min_value=0)


st.sidebar.header("Add-Ons")
col1, col2, col3 = st.sidebar.columns(3)
Foil = col1.selectbox(
    "Foiling",
    ["None","Cupper","Brass","Zinc"],
     index=0
)
f_l=col2.number_input("Foiling_L", min_value=0.0)

# st.write(W_S)

f_w=col3.number_input("Foiling_W", min_value=0.0)
col1, col2 = st.sidebar.columns(2)

d_l=col1.number_input("Deboss_L", min_value=0.0)

# st.write(W_S)

d_w=col2.number_input("Deboss_W", min_value=0.0)
col1, col2 = st.sidebar.columns(2)

E_l=col1.number_input("Emboss_L", min_value=0.0)

# st.write(W_S)

E_w=col2.number_input("Emboss_W", min_value=0.0)
col1, col2 = st.sidebar.columns(2)

Uv_l=col1.number_input("UV_L", min_value=0.0)

# st.write(W_S)

Uv_w=col2.number_input("UV_W", min_value=0.0)
col1, col2,col3 = st.sidebar.columns(3)
window_die_cut=col1.selectbox(
    "Window Diecut",

     ["None","With PVC","Without PVC",])
win_l=col2.number_input("Window_L", min_value=0.0)

# st.write(W_S)

win_w=col3.number_input("Window_W", min_value=0.0)
############ Lamination ##########
st.sidebar.header("Lamination")
col1,col2=st.sidebar.columns(2)
inside=col1.selectbox(
    "Inside Lamination",
     ["None","Matte","Gloss","Soft Touch","Varnish",])
outside=col2.selectbox(
    "Outside Lamination",
     ["None","Matte","Gloss","Soft Touch","Varnish",])

############ Additional Expense ##########

st.sidebar.header("Additional Expense")
col1, col2 = st.sidebar.columns(2)
Mics = col1.number_input("Micsellneus", min_value=0)
Profit_margin = col2.number_input("Profit Margin", min_value=0)
# project_difficulty = col3.number_input("Project Difficulty", min_value=0)


### disply Machine size
# submitted = st.sidebar.form_submit_button("Submit")

# if submitted:
#     if agree:
#         W_P=W_S
#         L_P=L_S
#     else:
#         pass

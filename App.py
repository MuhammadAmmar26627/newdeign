import streamlit as st
import os
import pandas as pd
from function_file import *
# st.set_page_config(layout="wide")
with open ('custom.css') as f:
			st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

if "material_df" not in st.session_state:
    st.session_state["material_df"]=pd.read_csv("Material.csv")
if "lab_df" not in st.session_state:
    st.session_state["lab_df"]=pd.read_csv("Labour.csv")
if "df" not in st.session_state:
  if os.path.exists("Rate.csv"):
      st.session_state["df"]=pd.read_csv("Rate.csv")
  else:
      st.session_state["df"]=pd.read_csv("rate_.csv")
      st.session_state["df"].to_csv("Rate.csv",index=False)
df=st.session_state["df"]
lab_df=st.session_state["lab_df"]
#####################################
col1,col2,col3=st.sidebar.columns(3)
  
rigid=col1.checkbox("Rigid")

custom=col2.checkbox("Custom_S")
custom_p = col3.checkbox('Custom_P')
#####################################
# with st.sidebar.form("my_form"):
#     ######## Client Data ###########
#     st.header("Packaging Estimation Sheet")
#     st.header("Client Bio")
#     col1,col2=st.columns(2)
#     client_name=col1._text_input("Client Name")
#     CSR=col2._text_input("CSR Name")
#     col1,col2=st.columns(2)
#     client_email=col1._text_input("Client Email")
#     Phone=col2._text_input("Phone Number")

#     # checkbox_val = st.checkbox("Form checkbox")

#     # Every form must have a submit button.
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#           st.write("slider", 0, "checkbox", rigid)
#####################################
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

st.sidebar.header("Sheet Size")
if rigid:
    col1, col2 = st.sidebar.columns(2)
    Material_Rigid = col1.selectbox(
    "Material_Rigid",
    ["Grey Board",
"Bux Board",]
)
    gsm_rigid = col2.selectbox("GSM_Rigid",[900,1000,1200,1400,1600,1800,])

col1, col2 = st.sidebar.columns(2)
Material = col1.selectbox(
    "Material",
    ["Bleached Card",
"Bleached Card Pasted",
"Bux Board",
"Bux Board Pasted",
"Art Card",
"Grey Board",
"Bux Board",
"Kraft Local",
"Kraft Imported",
"Morocco",
"Art Paper",
"Rigid Box",]
)
gsm_list=[210,230,250,270,300,350,420,460,500,540,600,700,]
if Material=="Art Paper":
    gsm_list=[128,150,]
gsm = col2.selectbox("GSM",gsm_list)
if custom:
    col1, col2 = st.sidebar.columns(2)
    W_S=col1.number_input("W_Sheet", min_value=0.0)
    L_S=col2.number_input("L_Sheet", min_value=0.0)
else:
    col1, col2 = st.sidebar.columns(2)
    Sheet_size=["23x36","25x36","22x28",'20x30','25x30',"27x34"]
    Sheet = col1.selectbox( 
        "Sheet Size",
        Sheet_size)
    Packets_size=[("9x7.66","11.5x7.2","12x7.66","9x11.5","11.5x12","12x23","18x23"),
    ("9x8.33","12.5x7.5","12x8.33","9x12.5","12.5x12","12x25","18x25"),
    ('9.33x7.33',"11x14","14x22"),("10x7.5","10x15",'10x20','15x20'),
    ("10x8.33","10x12.5",'12.5x15','15x25'),('9x11.33','13.5x17','17x27')]

    packet_index=Sheet_size.index(Sheet)
    Packet = col2.selectbox(
        "Packet Size",
        Packets_size[packet_index])
    pack=Packet.split("x")
    W_S,L_S=float(pack[0]),float(pack[1])
if custom_p:
    col1, col2 = st.sidebar.columns(2)
    W_P=col1.number_input("W_Print", min_value=0.0)
    L_P=col2.number_input("L_Print", min_value=0.0)
else:
    W_P=W_S
    L_P=L_S

col1, col2 = st.sidebar.columns(2)
up = col1.number_input("Box Uping", min_value=1)
Req_Q = col2.number_input("Required Quantity", min_value=1)








# submitted = st.sidebar.form_submit_button("Submit")
################################################

st.sidebar.header("Corrugation")
col1, col2 = st.sidebar.columns(2)
pasting = col1.selectbox(
    "Corrugation Pasting",
    ["None","Single Side", "Double Side",]
)
stock = col2.selectbox(
    "Corrugation Material",
    ["L1", "E Flute", "B Flute"]
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
    ["None","Copper","Brass","Zinc"],
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
     ["None","Matte","Gloss","Soft Touch","Aqueous Coating",])
outside=col2.selectbox(
    "Outside Lamination",
     ["None","Matte","Gloss","Soft Touch","Aqueous Coating",])

############ Additional Expense ##########

st.sidebar.header("Additional Expense")
col1, col2 = st.sidebar.columns(2)
Mics = col1.number_input("Micsellneus", min_value=0)
Profit_margin = col2.number_input("Profit Margin", min_value=0)
submitted = st.sidebar.button("Submit")


############ Calculation  #####################
if submitted:
    machine_rate=find_machine_size(W_S,L_S,st.session_state["df"])
    Sheets=Req_Q/up
    print_sheet=Print_Sheet_calculator(Sheets)
    laminate_sheet=Lamination_sheets_calculator(Sheets)
    process_color_rate,pantone_color_rate,matallic_color_rate=Printing_Calculator(machine_rate,process_color,pantone_color,matallic_color,print_sheet)
    lamination_price=Lamination_price_calculator(W_P,L_P,laminate_sheet,inside,outside,machine_rate)
    die_cut_price=Die_cut_price(print_sheet,machine_rate)
    pasting_material=Pasting_Calculator(machine_rate,Req_Q)
    UV_coating=UV_price(Uv_l,Uv_w,print_sheet,machine_rate)
    foiling=foil_price(f_l,f_w,Foil,laminate_sheet,machine_rate)
    Debosing=debosing_price(d_l,d_l,machine_rate,print_sheet)
    Embosing=embosing_price(E_l,E_w,machine_rate,print_sheet)
    carrug_lab=corgation_price(W_S,L_S,pasting,laminate_sheet,machine_rate)
    st.dataframe(machine_rate,hide_index=True)

    ################### Table Update ################
    # print(st.session_state["lab_df"].columns)
    lab_df.set_index('index',inplace=True)
    # st.write(st.session_state["lab_df"].loc["Lam"])
    lab_df.loc["Printing"]=(process_color_rate,pantone_color_rate,matallic_color_rate,process_color_rate+pantone_color_rate+matallic_color_rate)
    lab_df.loc["Lam"]=(lamination_price[0],lamination_price[1],0,lamination_price[0]+lamination_price[1])
    lab_df.loc["Die cut"]=(die_cut_price,0,0,die_cut_price)
    lab_df.loc["Pasting"]=(pasting_material,0,0,pasting_material)
    lab_df.loc["Uv Coating"]=(UV_coating,0,0,UV_coating)
    lab_df.loc["Foiling"]=(foiling,0,0,foiling)
    lab_df.loc["Debossing"]=(Debosing,0,0,Debosing)
    lab_df.loc["Embossing"]=(Embosing,0,0,Embosing)
    lab_df.loc["Carrug Lab"]=(carrug_lab,0,0,carrug_lab)
    lab_df.loc["Lab Total"]=(0,0,0,lab_df.iloc[:-1,3].sum())
    lab_df.reset_index(inplace=True)


    #######################################################
    ctp=CTP_Plates_price(machine_rate,process_color,pantone_color,matallic_color)
    paper_price=paper_material(W_S,L_S,gsm,print_sheet,Material,machine_rate)
    die_making_price=Die_making_price(machine_rate)
    foil_block=foil_block_price(Foil,f_l,f_w,machine_rate)
    # deboss_price_Material=DebossBlock_price(W_P,L_P)   ###############  Function should be updated
    # # emboss_price_Material=EmbossBlock_price(Emboss,W_P,L_P)   ###############  Function should be updated
    # Carrugation_price_Material=carrugation_price_Material(stock,W_S,L_S,laminate_sheet) ### Editing

    #########################################################
    st.session_state["material_df"].set_index('index',inplace=True)
    st.session_state["material_df"].loc["CTP Plates"]=(0,0,0,ctp)
    st.session_state["material_df"].loc["Paper"]=(0,paper_price,0,paper_price)
    st.session_state["material_df"].loc["Die Making"]=(0,0,0,die_making_price)
    st.session_state["material_df"].loc["Foil Block"]=(0,0,0,foil_block)
    # # st.session_state["material_df"].loc["DebossBlock"]=(0,0,0,deboss_price_Material)
    # # st.session_state["material_df"].loc["EmbossBlock"]=(0,0,0,emboss_price_Material)
    # st.session_state["material_df"].loc["Carrugation"]=(0,0,0,Carrugation_price_Material)
    st.session_state["material_df"].loc["Material"]=(0,0,0,st.session_state["material_df"].iloc[:-1,3].sum())

    st.session_state["material_df"].reset_index(inplace=True)
    # print(st.session_state["material_df"].iloc[:-1,4].sum())
    total=st.session_state["material_df"].iloc[:-1,4].sum()+lab_df.iloc[:-1,4].sum()
    Profit_margin=1+Profit_margin/100
    total=total*Profit_margin
    cost_per_piece=total/Req_Q
    #############################################
else:
     print_sheet=laminate_sheet=total=cost_per_piece=0
# total=st.session_state["material_df"].iloc[:-1,3].sum()+lab_df.iloc[:-1,3].sum()
# Profit_margin=1+Profit_margin/100
# total=total*Profit_margin
# cost_per_piece=total/Req_Q
##########################################################
col1, col2, col3 = st.columns(3)
col1.metric("Sheet",print_sheet, laminate_sheet)
col2.metric("Total",total, "")
col3.metric("cost per Unit", cost_per_piece, "")
col1, col2, col3 = st.columns(3)
col1.metric("Material Cost",st.session_state["material_df"].iloc[:-1,4].sum(), "")
col2.metric("Labour Cost",lab_df.iloc[:-1,4].sum(), "")
col3.metric("Mics", Mics, "")
# print(Mics)
col1,col2=st.columns(2)
n_rows=13
height = int(35.2*(n_rows+1))
col1.header("Material Cost")
col1.dataframe(st.session_state["material_df"], width=700, height=410,hide_index=True)
col2.header("Labour Cost")
col2.dataframe(lab_df, width=700, height=height,hide_index=True)

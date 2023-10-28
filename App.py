# import streamlit_authenticator as stauth
import streamlit as st
# import pandas as pd
# import math
# from function_file import find_machine_size
# from function_file import *
# # st.set_page_config(layout="wide")
# rate_df=load_data("rate_database.xlsx",sheet_name="Sheet1")
# material_df=load_data("rate_database.xlsx",sheet_name="Sheet2")
# lab_df=load_data("rate_database.xlsx",sheet_name="Sheet3")

######## Client Data ###########
form=st.sidebar.form("Calculate Material and Labour")

# Input fields
form.header("Packaging Estimation Sheet")
form.header("Client Bio")
col1,col2=form.columns(2)
client_name=col1._text_input("Client Name")
CSR=col2._text_input("CSR Name")
col1,col2=form.columns(2)
client_email=col1._text_input("Client Email")
Phone=col2._text_input("Phone Number")


########### Sheet Data (Size) #############

form.header("Sheet Size")
col1, col2 = form.columns(2)
W_S=col1.number_input("W_Sheet", min_value=0.0)

# st.write(W_S)

L_S=col2.number_input("L_Sheet", min_value=0.0)
# st.sidebar.header("Material")
col1, col2 = form.columns(2)
Material = col1.selectbox(
    "Material",
    ["Bleach Card","Bux Board", "Art Card", "Kraft",]
)
gsm = col2.number_input("GSM", min_value=0,value=300)
col1, col2 = form.columns(2)
up = col1.number_input("Box Uping", min_value=1)
Req_Q = col2.number_input("Required Quantity", min_value=0)


agree = form.checkbox('Print Size Same as Sheet Size')
col1, col2 = form.columns(2)
W_P=col1.number_input("W_Print", min_value=0.0)
L_P=col2.number_input("L_Print", min_value=0.0)
# submitted = form.form_submit_button("Submit")
################################################

form.header("Corrugation")
col1, col2 = form.columns(2)
stock = col1.selectbox(
    "Corrugation Material",
    ["L1", "E Flute", "B Flute"]
)

pasting = col2.selectbox(
    "Corrugation Pasting",
    ["None","Single Side", "Double Side",]
)

form.header("Printing Colors")
col1, col2, col3 = form.columns(3)
process_color = col1.selectbox(
    "Process Color",
    [0,1,2,3,4,5,6,7,8,]
)
pantone_color=col2.number_input("Pantone Color", min_value=0)
matallic_color=col3.number_input("Matallic Color", min_value=0)


form.header("Add-Ons")
col1, col2, col3 = form.columns(3)
Foil = col1.selectbox(
    "Foiling",
    ["No","Yes","Cupper","Brass","Zinc"],
     index=0
)
f_l=col2.number_input("Foiling_L", min_value=0.0)

# st.write(W_S)

f_w=col3.number_input("Foiling_W", min_value=0.0)
col1, col2 = form.columns(2)

d_l=col1.number_input("Deboss_L", min_value=0.0)

# st.write(W_S)

d_w=col2.number_input("Deboss_W", min_value=0.0)
col1, col2 = form.columns(2)

E_l=col1.number_input("Emboss_L", min_value=0.0)

# st.write(W_S)

E_w=col2.number_input("Emboss_W", min_value=0.0)
col1, col2 = form.columns(2)

Uv_l=col1.number_input("UV_L", min_value=0.0)

# st.write(W_S)

Uv_w=col2.number_input("UV_W", min_value=0.0)
col1, col2,col3 = form.columns(3)
window_die_cut=col1.selectbox(
    "Window Diecut",

     ["None","With PVC","Without PVC",])
win_l=col2.number_input("Window_L", min_value=0.0)

# st.write(W_S)

win_w=col3.number_input("Window_W", min_value=0.0)
############ Lamination ##########
form.header("Lamination")
col1,col2=form.columns(2)
inside=col1.selectbox(
    "Inside Lamination",
     ["None","Matte","Gloss","Soft Touch","Varnish",])
outside=col2.selectbox(
    "Outside Lamination",
     ["None","Matte","Gloss","Soft Touch","Varnish",])

############ Additional Expense ##########

form.header("Additional Expense")
col1, col2 = form.columns(2)
Mics = col1.number_input("Micsellneus", min_value=0)
Profit_margin = col2.number_input("Profit Margin", min_value=0)
# project_difficulty = col3.number_input("Project Difficulty", min_value=0)


### disply Machine size
submitted = form.form_submit_button("Submit")

# if submitted:
#     if agree:
#         W_P=W_S
#         L_P=L_S
#     else:
#         pass
#     machine_rate=find_machine_size(W_S,L_S,rate_df)
#     st.dataframe(machine_rate.loc[:,machine_rate.columns[:14]],hide_index=True)
#     st.dataframe(machine_rate.loc[:,machine_rate.columns[14:]],hide_index=True)
#     Sheets=Req_Q/up
#     print_sheet=Print_Sheet_calculator(Sheets)
#     st.write(f'print_sheet: {print_sheet}')
#     laminate_sheet=Lamination_sheets_calculator(Sheets)
#     st.write(f'laminate_sheet: {laminate_sheet}')
#     process_color_rate,pantone_color_rate,matallic_color_rate=Printing_Calculator(machine_rate,process_color,pantone_color,matallic_color,print_sheet)
#     # st.write("Printing Rate")
#     # st.write(process_color_rate,pantone_color_rate,matallic_color_rate)
#     # st.write("Lamination Rate")
#     lamination_price=Lamination_price_calculator(W_P,L_P,laminate_sheet,inside,outside,rate_df)
#     # st.write(lamination_price)

#     # st.write("Die Cut")
#     die_cut_price=Die_cut_price(machine_rate)
#     # st.write(die_cut_price)

#     # st.write("Pasting")
#     pasting_material=Pasting_Calculator(machine_rate,Req_Q)
#     # st.write(pasting_material)
#     # st.write("UV")
#     UV_coating=UV_price(W_S,L_S,UV,print_sheet)
#     # st.write(UV_coating)

#     # st.write("Foil")
#     foiling=foil_price(W_P,L_P,Foil,laminate_sheet)
#     # st.write(foiling)
#     # st.write("Debosing")
#     Debosing=debosing_price(W_P,L_P,Deboss,machine_rate,print_sheet)
#     # st.write(Debosing)
#     # st.write("Embosing")
#     Embosing=embosing_price(W_P,L_P,Emboss,machine_rate,print_sheet)
#     # st.write(Embosing)

#     # st.write("Carrugation")
#     carrug_lab=corgation_price(W_S,L_S,pasting,laminate_sheet)
#     # st.write(carrug_lab)
#     lab_df.set_index('index',inplace=True)
#     lab_df.loc["Printing"]=(process_color_rate,pantone_color_rate,matallic_color_rate,process_color_rate+pantone_color_rate+matallic_color_rate)
#     lab_df.loc["Lam"]=(lamination_price[0],lamination_price[1],0,lamination_price[0]+lamination_price[1])
#     lab_df.loc["Die cut"]=(die_cut_price,0,0,die_cut_price)
#     lab_df.loc["Pasting"]=(pasting_material,0,0,pasting_material)
#     lab_df.loc["Uv Coating"]=(UV_coating,0,0,UV_coating)
#     lab_df.loc["Foiling"]=(foiling,0,0,foiling)
#     lab_df.loc["Debossing"]=(Debosing,0,0,Debosing)
#     lab_df.loc["Embossing"]=(Embosing,0,0,Embosing)
#     lab_df.loc["Carrug Lab"]=(carrug_lab,0,0,carrug_lab)
#     lab_df.loc["Lab Total"]=(0,0,0,lab_df.iloc[:-1,3].sum())

#     lab_df.reset_index(inplace=True)
#     # corgation_price(10,12.5,"Double Side",3467)

#     ##################################
#     ############ Material Calculation #############
#     material_df.set_index('index',inplace=True)
#     ctp=CTP_Plates_price(machine_rate,process_color,pantone_color,matallic_color)
#     material_df.loc["CTP Plates"]=(0,0,0,ctp)
#     paper_price=paper_material(W_S,L_S,gsm,print_sheet,Material,)
#     material_df.loc["Paper"]=(0,paper_price,0,paper_price)
#     die_making_price=Die_making_price(machine_rate)
#     material_df.loc["Die Making"]=(0,0,0,die_making_price)
#     foil_block=foil_block_price(Foil,W_P,L_P)
#     material_df.loc["Foil Block"]=(0,0,0,foil_block)
#     deboss_price_Material=DebossBlock_price(Deboss,W_P,L_P)
#     material_df.loc["DebossBlock"]=(0,0,0,deboss_price_Material)
#     emboss_price_Material=EmbossBlock_price(Emboss,W_P,L_P)
#     material_df.loc["EmbossBlock"]=(0,0,0,emboss_price_Material)
#     Carrugation_price_Material=carrugation_price_Material(stock,W_S,L_S,laminate_sheet) ### Editing
#     material_df.loc["Carrugation"]=(0,0,0,Carrugation_price_Material)
#     material_df.loc["Material"]=(0,0,0,material_df.iloc[:-1,3].sum())

#     material_df.reset_index(inplace=True)





# ###############################################
# col1, col2, col3 = st.columns(3)
# col1.metric("Total Amount", material_df.iloc[:-1,4].sum()+lab_df.iloc[:-1,4].sum(), "Misc Profit Marig Difficulty")
# # col2.metric("Wind", "9 mph", "-8%")
# if Req_Q==0:
#     cost_per_piece=0
# else:
#     cost_per_piece=(material_df.iloc[:-1,4].sum()+lab_df.iloc[:-1,4].sum())/Req_Q
# col3.metric("Cost Per Piece", cost_per_piece, "")

# col1, col2, col3 = st.columns(3)
# col1.metric("Material Cost", material_df.iloc[:-1,4].sum(), "")
# col2.metric("Labour Cost", lab_df.iloc[:-1,4].sum(), "")
# col3.metric("Material + Labour Cost", material_df.iloc[:-1,4].sum()+lab_df.iloc[:-1,4].sum(), "")



# col1,col2=st.columns(2)
# n_rows=13
# height = int(35.2*(n_rows+1))
# col1.header("Material Cost")
# col1.dataframe(material_df, width=700, height=410,hide_index=True)
# col2.header("Labour Cost")
# col2.dataframe(lab_df, width=700, height=height,hide_index=True)
# # st.cache_data.clear()
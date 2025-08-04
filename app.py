import requests
from pathlib import Path
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import os
import json

# Directories and file paths
THIS_DIR = Path(__file__).parent
ASSETS = THIS_DIR / "images"
LOTTIE_ANIMATION = ASSETS / "Animation - 1708211828248.json"


# Function to load and display the Lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Main Reporting", page_icon=":📂:", layout="wide")


# ---- LOAD ASSETS ----
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
digest = Image.open("images/digest.png")
payments = Image.open("images/Payments.png")
som = Image.open("images/som.png")
av = Image.open("images/av.png")
bonds = Image.open("images/bonds.png")
avd = Image.open("images/avd.png")
dailyims = Image.open("images/imsdaily.png")
ds = Image.open("images/ds.png")
wo = Image.open("images/wo.png")
terminal = Image.open("images/Terminal.png")
ka = Image.open("images/ka.png")
KAGTW = Image.open("images/KAGTW.png")

# ---- SUBHEADER----
with st.container():
    #st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Reporting 📂")
        st.write("##")      
        st.write(
            """
           Below you might find main links:
            """
        )    
        st.write("[Ukraine_Global_BI_PRD >](https://app.powerbi.com/groups/48aaa182-efc4-40eb-8e6f-ac264bdaea3e/list?openReportSource=ReportInvitation&ctid=8b86a65e-3c3a-4406-8ac3-19a6b5cc52bc&bookmarkGuid=Bookmark64ec64b10eb90492f0fb&experience=power-bi)")
        st.write("[CIP portal >](https://commercialintelligenceportal-pmicloud.msappproxy.net/welcome)")
    with right_column:
        st.write("##")
        st_lottie(lottie_animation, key="lottie-holiday", height=300)
        
        
        
# ---- Reports ----
with st.container():
    st.write("---")
    st.header("Power BI & Excel reports")
    st.write("##")
    image_column, text_column = st.columns((1, 2 ))
    with image_column:
        st.image(digest)
    with text_column:
        st.subheader("Digest")
        st.write(
            """
            Weekly IMS and SoM Dynamics by Area, Region, main customer group : NKA, SWH and oth. 
            \nIncludes Device offtakes and Brand Retail performance. 
            """
        )
        st.write("##")
        st.write('Weekly updating')
        st.markdown("[Digest>](https://app.powerbi.com/groups/48aaa182-efc4-40eb-8e6f-ac264bdaea3e/reports/416c1745-f13f-4dad-832c-fafa88a9c70d/ReportSection98cbde60b6649ede16a2?openReportSource=ReportInvitation&ctid=8b86a65e-3c3a-4406-8ac3-19a6b5cc52bc&experience=power-bi)")


with st.container():
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(ka)
    with text_column:
        st.subheader("KA Cockpit")
        st.write(
            """
            Offtakes by Customers 
            \nSource: Offtakes and Shipments (ATB)
            
            """
        )
        st.write("##")
        st.write('Weekly updating')
        st.markdown("[KA Cokpits>](https://app.powerbi.com/links/vFK1K7BClH?ctid=8b86a65e-3c3a-4406-8ac3-19a6b5cc52bc&pbi_source=linkShare&bookmarkGuid=fbf4af0d-1e33-4efb-b294-2fe3c0ab38d4)")    


with st.container():
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(KAGTW)
    with text_column:
        st.subheader("Weekly detailed IMS & Shipments")
        st.write(
            """
            Detailed sales info by Customers. 
            \nSource: Weekly Shipments, IMS 
            
            """
        )
        st.write("##")
        st.write('Weekly updating')
        st.markdown("[Weekly Report>](https://pmicloud.sharepoint.com/:x:/r/teams/Reporting-Commercial-Ukraine/Shared%20Documents/General/Reporting/Sales/02_PMU_sales_weekly.xlsx?d=w7585c493c2894b2ca3445ea0657e0caf&csf=1&web=1&e=A94a5j)")    
 
with st.container():
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(bonds)
    with text_column:
        st.subheader("RRP Orders")
        st.write(
            """
            Source: Orders
            
            """
        )
        st.write("##")
        st.write('Daily updating')
        st.markdown("[RRP Orders>](https://pmicloud.sharepoint.com/:x:/r/teams/Reporting-Commercial-Ukraine/Shared%20Documents/General/Reporting/SFP/ILUMA%20%26%20Terea.xlsx?d=w4e5061ea673f4edab9bc196bb5dd299a&csf=1&web=1&e=EfkOfU)")
   

with st.container():
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(dailyims)
    with text_column:
        st.subheader("Daily Shipments & IMS")
        st.write(
            """
            \nSource: Daily Shipments, IMS 
            
            """
        )
        st.write("##")
        st.write('Daily updating')
        st.markdown("[Daily Shipments & IMS>](https://pmicloud.sharepoint.com/:x:/r/teams/Reporting-Commercial-Ukraine/Shared%20Documents/General/Reporting/Sales/Daily%20Shipments%20%26%20IMS.xlsx?d=w08e06db63c29460ba1e89d264dd62995&csf=1&web=1&e=hRk9ws)")
      
 
with st.container():
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(som)
    with text_column:
        st.subheader("SoM By Clients")
        st.write(
            """   
            Source: IMS & Shipment
            """
        )
        st.write("##")
        st.write('Weekly updating')
        st.markdown("[SoM By Clients>](https://pmicloud.sharepoint.com/:x:/r/teams/Reporting-Commercial-Ukraine/Shared%20Documents/General/Reporting/Sales/01_SoM%20By%20Clients.xlsx?d=wf6b532d0a80347329757d152f5339edd&csf=1&web=1&e=bqQr8R)")
 
with st.container():
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(ds)
    with text_column:
        st.subheader("SFP Offtakes")
        st.write(
            """   
            Source: Offtakes
            """
        )
        st.write("##")
        st.write('Weekly updating')
        st.markdown("[SFP Offtakes>](https://pmicloud.sharepoint.com/:x:/r/teams/Reporting-Commercial-Ukraine/Shared%20Documents/General/Reporting/SFP/SFP%20Offtakes.xlsx?d=w273a49326a2148b0bdfc71ad6969ae25&csf=1&web=1&e=pGf8sR)")
 
with st.container():
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(wo)
    with text_column:
        st.subheader("Weekly Offtakes")
        st.write(
            """   
            """
        )
        st.write("##")
        st.write('Weekly updating')
        st.markdown("[Weekly Offtakes>](https://pmicloud-my.sharepoint.com/:x:/r/personal/aradchuk_pmintl_net/Documents/Tasks/Reporting/Weekly%20Offtakes.xlsx?d=wfd4d36b41fc14832b6ab1995809b5278&csf=1&web=1&e=qf4J9b)")
 
                
with st.container():
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(av)
    with text_column:
        st.subheader("Availability")
        st.write(
            """
            
            
            """
        )
        st.write("##")
        st.write('Weekly updating')
        st.markdown("[Availability>](https://pmicloud.sharepoint.com/:x:/r/teams/Reporting-Commercial-Ukraine/Shared%20Documents/General/Reporting/Sales/AvailabilityReport.xlsx?d=wf1204fd50eaa4a75b207c846b761c0fb&csf=1&web=1&e=bLq3Pz)")
   
   
##with st.container():
##    st.write("##")
##    image_column, text_column = st.columns((1, 2))
##    with image_column:
##        st.image(avd)
##    with text_column:
##        st.subheader("Availability with Distributor")
##        st.write(
##            """
##            
##            
##            """
##        )
##        st.write("##")
##        st.write('Daily updating')
##        st.markdown("[Availability with Distributor>](https://pmicloud-my.sharepoint.com/:x:/r/personal/vmarchuk_pmintl_net/Documents/Desktop/Availability/Availability_with_Distr.xlsx?d=w8d4ed320a1274e26bf59c4841b603949&csf=1&web=1&e=8mzrAR)")
   

 
 
##python -m streamlit run app.py

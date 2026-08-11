
import streamlit as st
import requests

st.title("Hadiths web app")
st.write("Read and explore hadiths")


hadithsData= requests.get("https://hadithapi.com/public/api/hadiths?apiKey=$2y$10$Wwe4yeMZRnOyHtwHWAt7luC4aOLUijvgbBHzBTE7DKtj2qvrcc2")


hadiths =hadithsData.json()["hadiths"]["data"]

bookdata= requests.get("https://hadithapi.com/api/books?apiKey=$2y$10$Wwe4yeMZRnOyHtwHWAt7luC4aOLUijvgbBHzBTE7DKtj2qvrcc2")
books= bookdata.json()["books"]

bookOptions = []

for book in books:
    bookOptions.append(f"{book["bookName"]} | {book["bookSlug"]}")
    
    
selectBook= st.selectbox("Select your hadiths book", bookOptions)

bookSlug= selectBook.split(" | ")[1]
st.write(bookSlug)

st.info(f"You selected: {selectBook}")

        

allChapterData=requests.get(f"https://hadithapi.com/api/{bookSlug}/chapters?apiKey=$2y$10$lUEWfNTE8oxTk9DA0ueVOwzNvzf3WA14VPw9LHSwNgm07qGxS")
chapters=allChapterData.json()["chapters"]

chapterOptions= []

for c in chapters:
    chapterOptions.append(f"{c["chapterNumber"]} | {c["chapterArabic"]} | {c["chapterUrdu"]}")

selectChapter= st.selectbox("Select book chapter", chapterOptions)



for h in hadiths:
    st.success(f"Hadith no. {h['hadithNumber']}")
    st.write(h["hadithArabic"])
    st.write(h["hadithUrdu"])
    st.write(h["hadithEnglish"])
    st.divider()


from tkinter import *
import nltk
from newspaper import Article
from textblob import TextBlob
from fpdf import FPDF
pdf=FPDF()

nltk.download('punkt')

def summarize():
    url = urltext.get()

    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    
    art = Article(url)
    art.download()
    art.parse()
    art.nlp()

    title.config(state="normal")
    author.config(state="normal")
    date.config(state="normal")
    summary.config(state="normal")
    sentiment.config(state="normal")

    title.delete('1.0', 'end')
    title.insert(END, article.title)

    authors = ", ".join(article.authors)
    author.delete('1.0', 'end')
    author.insert(END, authors if authors else "Unknown")

    date.delete('1.0', 'end')
    date.insert(END, article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert(END, article.summary)
    
    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    n=analysis.polarity*100
    sentiment.insert(END, f'Sentiment: {"Very positive " if n > 50 else "Moderate positive" if n>0 else " very negative" if n < -60 else "Moderate negative" if n<0 else "neutral"}')

    title.config(state="disabled")
    author.config(state="disabled")
    date.config(state="disabled")
    summary.config(state="disabled")
    sentiment.config(state="disabled")
       
    
root = Tk()
root.geometry("1000x600")
root.minsize(1000, 600)
root.maxsize(1000, 600)
root.title("News Summarizer")

f1 = Frame(root, bg="orange")
f1.pack(side=TOP)

l = Label(f1, text="News Summarizer", font="comicsansms 19 bold", relief=SUNKEN, bg="orange")
l.pack(padx=12, pady=12)

content_frame = Frame(root)
content_frame.pack(expand=True, fill=BOTH)

ulable = Label(content_frame, text="Enter URL:", font="comicsansms 16 bold")
ulable.pack()
urltext = Entry(content_frame, width=120)
urltext.pack()

frame = Frame(root, borderwidth=5, bg="pink")
frame.pack()
b1 = Button(frame, fg="green", text="Summarize", font="comicsanms 14 bold", command=summarize)
b1.pack(side=BOTTOM, padx=4, pady=4)

output_frame = Frame(content_frame)
output_frame.pack(expand=True, fill=BOTH, pady=10)

tlable = Label(output_frame, text="Title", font="comicsanms 16 bold", fg="blue")
tlable.pack()
title = Text(output_frame, height=1, width=120)
title.config(state="disabled", bg="light grey")
title.pack()

alable = Label(output_frame, text="Author", font="comicsanms 16 bold", fg="blue")
alable.pack()
author = Text(output_frame, height=1, width=120)
author.config(state="disabled", bg="light grey")
author.pack()

plable = Label(output_frame, text="Publishing Date", font="comicsanms 16 bold", fg="blue")
plable.pack()
date = Text(output_frame, height=1, width=120)
date.config(state="disabled", bg="light grey")
date.pack()

slable = Label(output_frame, text="Summary", font="comicsanms 16 bold", fg="blue")
slable.pack()
summary = Text(output_frame, height=11, width=120)
summary.config(state="disabled", bg="light grey")
summary.pack()

selable = Label(output_frame, text="Sentiment Analysis", font="comicsanms 16 bold", fg="blue")
selable.pack()
sentiment = Text(output_frame, height=1, width=120)
sentiment.config(state="disabled", bg="light grey")
sentiment.pack()

root.mainloop()

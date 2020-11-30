#As there are several issues installing tkinter so use command "sudo apt-get install python3-tk" for linux based system
import tkinter as tk
import engine_supporter as eg
from textblob import TextBlob
from newspaper import Article


#Function which we will be calling using button
def analyze():

    # We will read it from textbox(Getting the url of the article)--Starting index(1.0) ending index("end")
    url = url_text.get("1.0", "end").strip()

    # Creating an article object
    article = Article(url)

    # Downloading the article data and parsing it
    article.download()
    article.parse()

    article.nlp()

    title.config(state="normal")
    author.config(state="normal")
    Publish.config(state="normal")
    Summary.config(state="normal")
    Sentiment.config(state="normal")
    frnews.config(state="normal")

    #Deleting whatever was there earlier(in textboxes)
    #As now all the text boxes are in normal state so we can delete

    if article.title is not None:
        title.delete("1.0", "end")
        title.insert(tk.END, article.title)

    if article.authors is not None:
        author.delete("1.0", "end")
        author.insert(tk.END, article.authors)
    
    
    if article.publish_date is not None:
        Publish.delete("1.0", "end")
        Publish.insert(tk.END, article.publish_date)
        
    if article.summary is not None:
        Summary.delete("1.0", "end")
        Summary.insert(tk.END, article.summary)

    analysis = TextBlob(article.text)
    
    if analysis is not None:
        Sentiment.delete("1.0", "end")
        Sentiment.insert(tk.END, f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')
    
    if article.summary is not None:
        frnews.delete("1.0", "end")
        a = eg.fnews(str(article.summary))
        if a == 1:
            frnews.insert(tk.END,"Fake News")
        else:
            frnews.insert(tk.END,"Real News")


    title.config(state="disabled")
    author.config(state="disabled")
    Publish.config(state="disabled")
    Summary.config(state="disabled")
    Sentiment.config(state="disabled")
    frnews.config(state="disabled")



base = tk.Tk()
base.title("News Analyser")
base.geometry('1200x690')

tlabel = tk.Label(base, text="Title")
tlabel.pack()
#Adding title textbox
title = tk.Text(base, height=1, width=140)
title.config(state="disabled", bg="#dddddd")
title.pack()

alabel = tk.Label(base, text="Author")
alabel.pack()
#Adding author textbox
author = tk.Text(base, height=1, width=140)
author.config(state="disabled", bg="#dddddd")
author.pack()

plabel = tk.Label(base, text="Publish Date")
plabel.pack()
#Adding publish textbox
Publish = tk.Text(base, height=1, width=140)
Publish.config(state="disabled", bg="#dddddd")
Publish.pack()

slabel = tk.Label(base, text="Summary")
slabel.pack()
#Adding summary textbox
Summary = tk.Text(base, height=20, width=140)
Summary.config(state="disabled", bg="#dddddd")
Summary.pack()

sslabel = tk.Label(base, text="Sentiment")
sslabel.pack()
#Adding sentiment textbox
Sentiment = tk.Text(base, height=1, width=140)
Sentiment.config(state="disabled", bg="#dddddd")
Sentiment.pack()

fnlabel = tk.Label(base, text="Fake or real news")
fnlabel.pack()
#Adding fake or real news textbox
frnews = tk.Text(base, height=1, width=140)
frnews.config(state="disabled", bg="#dddddd")
frnews.pack()



urllabel = tk.Label(base, text="URL")
urllabel.pack()
#Adding url textbox
url_text = tk.Text(base, height=1, width=140)
url_text.config(state="normal", bg="#dddddd")
url_text.pack()

btn = tk.Button(base, text="Analyze", command=analyze)
btn.pack()
base.mainloop()

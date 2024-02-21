import requests
import json
import tkinter as tk


class Link:
    def display(self):

        self.id = self.data["_id"]
        self.content = self.data["content"]
        self.author = self.data["author"]
        self.tags = self.data["tags"]
        self.authorSlug = self.data["authorSlug"]
        self.length = self.data["length"]
        self.dateAdded = self.data["dateAdded"]
        self.dateModified = self.data["dateModified"]


        self.display.config(text=("ID: {}".format(self.id))
                            + "\n" + ("CONTENT: {}".format(self.content))
                            + "\n" + ("AUTHOR: {}".format(self.author))
                            + "\n" + ("TAGS: {}".format(self.tags))
                            + "\n" + ("AUTHOR SLUG: {}".format(self.authorSlug))
                            + "\n" + ("LENGTH: {}".format(self.length))
                            + "\n" + ("DATE ADDED: {}".format(self.dateAdded))
                            + "\n" + ("DATE MODIFIED: {}".format(self.dateModified)),
                            bg="light yellow", font=('Times new roman',15,'bold'), width=100, height=50)

    def __init__(self):
        self.url = "https://api.quotable.io/random"
        self.response = requests.get(self.url)
        self.data = json.loads(self.response.content)

        self.window = tk.Tk()
        self.window.geometry("500x600")
        self.window.configure(bg="lightblue")

        self.button = tk.Button(text="CLICK HERE", command=self.display)
        self.button.pack(pady=20)

        self.display = tk.Label(width=100, height=50)
        self.display.pack()
        self.window.mainloop()


obj = Link()

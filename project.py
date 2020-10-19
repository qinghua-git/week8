from tkinter import *
from tkinter.messagebox import showerror
import csv
import pandas as pd
from datetime import datetime
import tkinter as tk

def channel_id(channelid): 
        channelid_1 = channelid.get()
        print (channelid_1)
        df2 = df[df['channel Id'] == channelid_1]
        df2.to_csv('select_videos_by_channel_id.csv', index = False)

if __name__ == "__main__" :
    df = pd.read_csv ('youtube10-5to10-11_header.csv')
    df.columns = ["videoId", "title", "channel Id", "channel title", "likeCount","dislikeCount", "viewCount", "publishedAt"]
    df['publishedAt'] = pd.to_datetime(df['publishedAt'])
    df[["channel Id", "channel title"]] = df[["channel Id", "channel title"]].astype(str)
    #print (df)
    
    window = tk.Tk()
    window.title('Search Videos')
    window.geometry('500x500') 
    
    channelid = tk.Entry(window, show = None)
    channelid.pack()
    
    def channel_id(): 
        channelid_1 = channelid.get()
        print (channelid_1)
        df2 = df[df['channel Id'] == channelid_1]
        df2.to_csv('select_videos_by_channel_id.csv', index = False)
        
    b2 = tk.Button(window, text='channel id', width=10,
               height=2, command=channel_id)
    b2.pack()
    
    channeltitle = tk.Entry(window, show = None)
    channeltitle.pack()
    
    def channel_title(): 
        channeltitle_1 = channeltitle.get()
        print (channeltitle_1)
        df3 = df[df['channel title'] == channeltitle_1]
        df3.to_csv('select_videos_by_channel_title.csv', index = False)
        
    b3 = tk.Button(window, text='channel title', width=10, height=2, command=channel_title)
    b3.pack()
    
    
    time1 = tk.Entry(window, show = None)
    time1.pack()
    time2 = tk.Entry(window, show = None)
    time2.pack()
    
    def time(): 
        time_1 = time1.get()
        time_2 = time2.get()
        time_1 = datetime.strptime(time_1, '%Y-%m-%d %H:%M:%S')
        time_2 = datetime.strptime(time_2, '%Y-%m-%d %H:%M:%S')
        df1 = df[(df['publishedAt'] > time_1) & (df['publishedAt'] < time_2)]
        df1.to_csv('select_videos_by_time.csv', index = False)
        
    b1 = tk.Button(window, text='time period', width=10, height=2, command=time)
    b1.pack()

    
    window.mainloop()
import pandas as pd
import sqlite3 

#1. Customer Purchases Analysis

with sqlite3.connect('chinhook.db') as connection:
    invoices=pd.read_sql_query('select * from invoices',connection)
    customers=pd.read_sql_query('select * from customers',connection)

invoices['FullName']=invoices['FirstName']+' '+invoices['LastName']
name=customers[['CustomerID','FullName']]
total_spent=invoices[['CustomerID','FullName','Total']].groupby(['CustomerID','FullName']).sum()
top5=pd.concat((name,total_spent),axis=1).sort_values(['Total'],ascending=False).head(5)

#2.Album vs. Individual Track Purchases
 
with sqlite3.connect('chinhook.db') as connection:
    invoices = pd.read_sql_query("SELECT InvoiceId, CustomerId FROM invoices", connection)
    invoice_lines = pd.read_sql_query("SELECT InvoiceId, TrackId, InvoiceLineId, UnitPrice FROM invoice_lines", connection)
    tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM tracks", connection)
    albums = pd.read_sql_query("SELECT AlbumId, COUNT(TrackId) AS total_tracks FROM tracks GROUP BY AlbumId", connection)

dataframe=invoices.merge(tracks, on='TrackID').merge(albums,on='AlbumID').merge(invoices,on='InvoiceID')
cust_album = (dataframe.groupby(["CustomerId", "AlbumId"])
                .agg(tracks_bought=('TrackId', 'nunique'), total_tracks=('total_tracks', 'first'))
                .reset_index())
cust_album['prefers_tracks']=cust_album['tracks_bought']<cust_album['total_tracks']
cust_album['prefers_albums']=cust_album['tracks_bought']==cust_album['total_tracks']
cust_pref = cust_album.groupby('CustomerId').agg(
    any_subsets=('prefers_tracks', 'any'),
    all_full=('prefers_album', 'all')
).reset_index()
    
cust_pref['category'] = cust_pref.apply(
    lambda r: 'Track-preferrer' if r['any_subsets'] else 'Album-preferrer',
    axis=1
)

summary = (
    cust_pref['category']
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
    .reset_index()
    .rename(columns={'index': 'category', 'category': 'percentage'})
)

print(summary)


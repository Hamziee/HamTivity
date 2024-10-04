from pypresence import Presence
import time
import config

last_author = None
last_song = None
RPCconnection = False

timeFormat = time.strftime("[%H:%M:%S - %d/%m/%Y]")

RPC = Presence(config.clientid)

def changeRPC(author, song, cover, url):
    global last_author, last_song

    if author == last_author and song == last_song:
        pass
    else:
        if cover == None:
            cover = "https://avatars.githubusercontent.com/u/91210085"
            big_text = "Cover is not available, this is a placeholder image"
        else:
            big_text = f"Cover of {song}"
        try:
            RPC.update(state=f"By: {author}", details=f"Listening to {song}", large_image=cover, large_text=big_text, small_image="https://cdn.discordapp.com/app-assets/1291800023666790472/1291827724863672422.png", small_text="Scrobelled from LastFM", buttons=[{"label": "View on LastFM", "url": url}, {"label": "HamTivity Github", "url": "https://github.com/Hamziee/HamTivity/"}])
            print(f"{timeFormat} Changed Discord RPC successfully. ~ Author: {author} | Song: {song}")

            last_author = author
            last_song = song
        except:
            print(f"{timeFormat} Discord RPC Change Failed.")

def connectRPC():
    global RPCconnection
    if RPCconnection == False:
        RPC.connect()
        RPCconnection = True
        print(f"{timeFormat} Connected Discord RPC.")
    elif RPCconnection == True:
        pass
    else:
        print(f"{timeFormat} An error occured which shouldn't be possible. (RPCconnection var has no value)")

def disconnectRPC():
    global RPCconnection
    if RPCconnection == True:
        RPC.close()
        RPCconnection = False
        print(f"{timeFormat} Disconnected Discord RPC.")
    elif RPCconnection == False:
        pass
    else:
        print(f"{timeFormat} An error occured which shouldn't be possible. (RPCconnection var has no value)")
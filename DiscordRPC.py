scriptDiscordRPC = "DiscordRPC"
versionDiscordRPC = "v0.2.0"

from pypresence import Presence
import time
import config

def logFormat():
    return f"{time.strftime('[%H:%M:%S - %d/%m/%Y]')} | {scriptDiscordRPC} {versionDiscordRPC}"

last_author = None
last_song = None
RPCconnection = False

RPC = Presence(config.clientid)

def changeRPC(reqScript, author, song, cover, url):
    global last_author, last_song

    if author == last_author and song == last_song:
        pass
    else:
        if cover is None:
            cover = "https://avatars.githubusercontent.com/u/91210085"
            big_text = "Cover is not available, this is a placeholder image"
        else:
            big_text = f"Cover of {song}"
        if reqScript == "LastFM":
            method_small_image="https://cdn.discordapp.com/app-assets/1291800023666790472/1291827724863672422.png"
            method_small_text="Scrobelled from LastFM"
        else:
            print(f"{logFormat()} An error occured which shouldn't be possible. (method var has no value)")
        try:
            RPC.update(state=f"By: {author}", details=f"Listening to: {song}", large_image=cover, large_text=big_text, small_image=method_small_image, small_text=method_small_text, buttons=[{"label": "View on LastFM", "url": url}, {"label": "HamTivity Github", "url": "https://github.com/Hamziee/HamTivity/"}])
            print(f"{logFormat()} Changed Discord RPC successfully. ~ Method: {reqScript} | Author: {author} | Song: {song}")

            last_author = author
            last_song = song
        except:
            print(f"{logFormat()} Discord RPC Change Failed, requested by [{reqScript}] script.")

def connectRPC(reqScript):
    global RPCconnection
    if RPCconnection == False:
        RPC.connect()
        RPCconnection = True
        print(f"{logFormat()} Connected Discord RPC, requested by [{reqScript}] script.")
    elif RPCconnection == True:
        pass
    else:
        print(f"{logFormat()} An error occured which shouldn't be possible. (RPCconnection var has no value)")

def disconnectRPC(reqScript):
    global RPCconnection
    if RPCconnection == True:
        RPC.close()
        RPCconnection = False
        global last_author, last_song
        last_song, last_author = None, None
        print(f"{logFormat()} Disconnected Discord RPC, requested by [{reqScript}] script.")
    elif RPCconnection == False:
        pass
    else:
        print(f"{logFormat()} An error occured which shouldn't be possible. (RPCconnection var has no value)")
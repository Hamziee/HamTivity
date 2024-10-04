import pylast
import time
import DiscordRPC
import config

timeFormat = time.strftime("[%H:%M:%S - %d/%m/%Y]")

network = pylast.LastFMNetwork(api_key=config.API_Key, api_secret=config.API_Secret)

def loop():
    while True:
        username = config.username
        user = network.get_user(username)
        playing_song = None
        try:
            playing_song = user.get_now_playing()
            pass
        except:
            print(f"{timeFormat} Failed to get information from LastFM, retrying...")
            pass

        if playing_song is not None:
            try:
                song = playing_song.get_title()
                artist = playing_song.get_artist()
                cover = playing_song.get_cover_image()
                url = playing_song.get_url()
            except:
                print(f"{timeFormat} Failed to get information from LastFM, retrying...")
                pass
            DiscordRPC.connectRPC()
            DiscordRPC.changeRPC(str(artist), str(song), cover, url)
            time.sleep(15)
        else:
            print(f"{timeFormat} No song playing at the moment.")
            DiscordRPC.disconnectRPC()
        time.sleep(15) # Set to 15 seconds, because you can only change the RPC every 15 seconds
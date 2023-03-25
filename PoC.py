# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

from pyyoutube import Api

# Read API_key
with open("api_key.txt", 'r') as file:
    key = file.read()

# Create an instance of the client class
api = Api(api_key = key)

# Get info about the channel by channel_id
info = api.get_channel_info(channel_id="UCgpSieplNxXxLXYAzJLLpng")

info.items[0].to_dict()

# Get all playlist items
playlists_by_id = api.get_playlist_items(playlist_id="UUgpSieplNxXxLXYAzJLLpng", count=None)

playlists_by_id.items[0].to_dict()





import os
import glob
import random


def main():
    # Get the root folder for where we start our search from the user
    music_path = input("Enter path to the root Music folder [~/Music]: ")
    if music_path == "":
        music_path = "~/Music"

    # convert user relative path to full path (if required)
    dir = os.path.expanduser(music_path)

    # Get the output file for our playlist
    playlist_out = input(f"Enter the path to where I will write the playlist [{dir}/playlist.m3u]: ")
    if playlist_out == "":
        playlist_out = f"{dir}/playlist.m3u"

    # Ask if we want to randomize our playlist
    randomize = input("Would you like the list order randomized? [y/N]")
    if randomize.lower() != "y":
        randomize = False

    playlist = []
    for (path, subdirs, files) in os.walk(dir):
        os.chdir(path)

        for ext in ["*.mp3", "*.m4a"]:
            for song in glob.iglob(ext):
                _path = path.replace(dir, ".")
                playlist.append(f"{_path}/{song}\n")

    if randomize:
        random.shuffle(playlist)

    # Write our playlist file
    _m3u = open( playlist_out , "w" )
    _m3u.writelines(playlist)
    _m3u.close()




if __name__ == "__main__":
    main()
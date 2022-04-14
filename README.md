# Blender_Dev_Tools
 A simple script that makes it easy to work with repositories when develping Blender add-ons. I created this to make it easier to commit to GitHub while developing Blen_My_NFTs. 
 
# Setup:
In Blender_Dev_Tools.py set `BLNEDER_DEV_DIR` to the directory of the Blender addons folder located in `(Blender.app or Blender.exe)/Contents/Resources/3.1/scripts/addons` on your system. 

Then in `GIT_REPOS` add an item to the dict where the key is how you want to refer to your repo, and the value is the directory to that repo. You can add as many as you want. 

# Commands: 
- `pull_from_repo` Pulls code from a specified repository to the BLNEDER_DEV_DIR in the Blender addons folder. If the Blender repo is already located there, it will be deleted and replaced with the GitHub repo. 
- `push_to_repo` Pushes code from a specified Blender repo to the GitHub repsoitory. The GitHub repo is first deleted, then replaced with the contents of the Blender repo. 
- `delete_blender_repo` Deletes the Blender repo of a specified repository. Does not affect the GitHub repo. 

# To run in terminal:
It's recommended to place Blender_Dev_Tools.py in Desktop so that you can just cd into Desktop.
## Commands:
$ cd <path/to/Blender_Dev_Tools> 
$ python3 Blender_Dev_Tools.py `<Command>` <`Key from GIT_REPOS dict`>

import os
import fire
import shutil

"""
To run in terminal: 
$ cd <path/to/Blender_Development_Tools>
$ python3 Blender_Dev_Tools.py <Dev Tool Function> <Repo name>

"""

# Paths to local repositories:
GIT_REPOS = {  # Schema: "<Command Name>": "<Path to Repo>"
    "BMNFTs_Public": "/Users/torrinleonard/Desktop/Repositories/Blend_My_NFTs",
    "BMNFTs_Confidential": "/Users/torrinleonard/Desktop/Repositories/Blend_My_NFTs Confidential",
}  # The keys in this dict will be used to identify which repo you want from the command line

# Path to Blender addons folder:
BLNEDER_DEV_DIR = "/Applications/Blender.app/Contents/Resources/3.1/scripts/addons"

# Coloured messages:
class bcolors:
   """
   The colour of console messages.
   """
   OK = '\033[92m'  # GREEN
   WARNING = '\033[93m'  # YELLOW
   ERROR = '\033[91m'  # RED
   RESET = '\033[0m'  # RESET COLOR

# Main class:
class Blender_Dev_Tools(object):
    """Main class"""

    def pull_from_repo(self, repo):
        """
        Pulls code from a local GitHub repo and updates the Blender repo in BLNEDER_DEV_DIR.
        WARNING: If repo found at BLENDER_DEV_DIR, the existing repo will be deleted and replaced with the new.
        """
        check = False
        for i in list(GIT_REPOS.keys()):
            if i == str(repo):
                check = True
                repo_path = GIT_REPOS[i]
                repo_name = os.path.basename(repo_path)
                blender_repo_path = os.path.join(BLNEDER_DEV_DIR, repo_name)

                def copy_paste_repo():
                    if os.path.isdir(blender_repo_path):  # Check if repo already exists, remove if True.
                        shutil.rmtree(blender_repo_path)

                    shutil.copytree(repo_path, blender_repo_path)
                    print(f"\n{bcolors.OK}{repo_path} has been pulled successfully!{bcolors.RESET}\n")

                if os.path.isdir(blender_repo_path):
                    print(f"\n{bcolors.ERROR}The Repository '{i}' already exists at '{blender_repo_path}'. Proceeding will delete the existing repository and all its changes.{bcolors.RESET}")
                    confirmation = input(f"\nWould you like to proceed? (y/n) ")
                    if confirmation == "y" or "Y" or "yes" or "Yes" or "YES":
                        copy_paste_repo()
                    elif confirmation == "n" or "N" or "no" or "No" or "NO":
                        print(f"\nNo changes were made.")
                        return
                    else:
                        print("\nInvalid Input. Retry command.")
                        return
                else:
                    copy_paste_repo()
        if not check:
            print(f"{repo} not found in Blender_Dev_Tools GIT_REPOS dict. Add this repository to Blender_Dev_Tools.")

    def push_to_repo(self, repo):
        """
        Pushes code from Blender repo to a local GitHub repo.
        WARNING: Deletes repo and replaces it with Blender repo.
        """
        check = False
        for i in list(GIT_REPOS.keys()):
            if i == str(repo):
                check = True
                repo_path = GIT_REPOS[i]
                repo_name = os.path.basename(repo_path)
                blender_repo_path = os.path.join(BLNEDER_DEV_DIR, repo_name)

                def copy_paste_repo():
                    if os.path.isdir(repo_path):  # Check if repo already exists, remove if True.
                        shutil.rmtree(repo_path)

                    shutil.copytree(blender_repo_path, repo_path)
                    print(f"\n{bcolors.OK}{blender_repo_path} has been pushed to {i} successfully!{bcolors.RESET}\n")

                if os.path.isdir(blender_repo_path):
                    print(f"\n{bcolors.ERROR}The Repository '{i}' will be deleted and replaced with the blender repo at '{blender_repo_path}'.{bcolors.RESET}")
                    confirmation = input(f"\nWould you like to proceed? (y/n) ")
                    if confirmation == "y" or "Y" or "yes" or "Yes" or "YES":
                        copy_paste_repo()
                    elif confirmation == "n" or "N" or "no" or "No" or "NO":
                        print(f"\nNo changes were made.")
                        return
                    else:
                        print("\nInvalid Input. Retry command.")
                        return
                else:
                    copy_paste_repo()
        if not check:
            print(f"{repo} not found in Blender_Dev_Tools GIT_REPOS dict. Add this repository to Blender_Dev_Tools.")

    def delete_blender_repo(self, repo):
        """
        Deletes specified repo from BLNEDER_DEV_DIR.
        WARNING: Deletes entire specified Blender repo
        """
        check = False
        for i in list(GIT_REPOS.keys()):
            if i == str(repo):
                check = True
                repo_path = GIT_REPOS[i]
                repo_name = os.path.basename(repo_path)
                blender_repo_path = os.path.join(BLNEDER_DEV_DIR, repo_name)

                def delete_repo():
                    if os.path.isdir(blender_repo_path):  # Check if repo already exists, remove if True.
                        shutil.rmtree(blender_repo_path)

                    print(f"\n{bcolors.OK}{blender_repo_path} has been successfully deleted!{bcolors.RESET}\n")

                if os.path.isdir(blender_repo_path):
                    print(
                        f"\n{bcolors.ERROR}If you proceed, the blender repo '{blender_repo_path}' will be deleted.{bcolors.RESET}")
                    confirmation = input(f"\nWould you like to proceed? (y/n) ")
                    if confirmation == "y" or "Y" or "yes" or "Yes" or "YES":
                        delete_repo()
                    elif confirmation == "n" or "N" or "no" or "No" or "NO":
                        print(f"\nNo changes were made.")
                        return
                    else:
                        print("\nInvalid Input. Retry command.")
                        return
                else:
                    delete_repo()
        if not check:
            print(f"{repo} not found in Blender_Dev_Tools GIT_REPOS dict. Add this repository to Blender_Dev_Tools.")

    # Doesn't work:
    # def delete_pycache_files(self, repo):
    #     """Deletes pycache files from Blender repo."""
    #
    #     for i in list(GIT_REPOS.keys()):
    #         if i == str(repo):
    #             repo_path = GIT_REPOS[i]
    #             repo_name = os.path.basename(repo_path)
    #             blender_repo_path = os.path.join(BLNEDER_DEV_DIR, repo_name)
    #
    #             if os.path.isdir(blender_repo_path):
    #                 for root, dirs, files in os.walk(blender_repo_path):
    #                     for name, directory in zip(dirs, root):
    #                         print(directory)
    #                         if name == "__pycache__":
    #                             print(f"\nDeleting {name}")
    #                             shutil.rmtree(directory)  # Fails here due to OSError Read Only
    #         else:
    #             print(f"{repo} not found in Blender_Dev_Tools GIT_REPOS dict. Add this repository to Blender_Dev_Tools.")


if __name__ == '__main__':
  fire.Fire(Blender_Dev_Tools)

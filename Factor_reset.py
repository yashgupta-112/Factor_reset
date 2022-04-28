import os
import tqdm 
from time import sleep
"""
Path definded for the directories
"""

path = os.getcwd() #homex/username
apps_path = path + '/.apps'
config_path = path + '/.config'
files_path = path + '/files'
downloads_path = path + '/downloads'
music_path = path + '/media/Music'
Movie_path = path + '/media/Movies'
tv_path = path + '/media/"TV Shows"'
book_path = path + '/media/Books'
backup_path = path + '/.apps/backup/*'
rutorrent_plugin = path + '/www/rutorrent'
bin_path = path + '/bin'


"""
clean up class
"""
class FactorReset():
    
    def unmount_rclone(self):
        grep_path = os.popen("mount | grep $USER").read()
        if grep_path == "":
            print("No rclone on your service....")
        else:
            rclone_path = grep_path.split()
            rclone_path = rclone_path[2]
            print("All rclone service has been stopped.")
            os.system("systemctl --user stop rclone-vfs")
            print("Your mergerfs is stopped now..")
            os.system("systemctl --user stop mergerfs")
            os.system("fusermount -zu {}".format(rclone_path))
            print("Rclone unmounted...")
            os.system("killall rclone")
            print("Rclone unmounted succesfully...")

    def Remove_Extra_directory(self,path):
        main_dir = []
        second_round = []
        remove_dir = ['media','files','downloads','.bashrc', '.bash_history', 'watch', '.wget-hsts', '.config',
                      'factor_reset.py','.profile', '.python_history', 'www', 'bin', '.bash_logout', 
                      '.nano', '.apps', '.rtorrent.rc',".viminfo",'.ssh'] #these directories will not get removed
        listed_dir = os.listdir(path)
        for lis in listed_dir:
            main_dir.append(lis)
        final_dir = list(set(main_dir).difference(remove_dir))
        print("Removing Extra directories#########")
        for i in final_dir:
            os.system("rm -rf {}".format(i))
        listed_dir = os.listdir(path)
        for lis in listed_dir:
            second_round.append(lis)
        second_round_dir = list(set(second_round).difference(remove_dir))
        for i in second_round_dir:
            os.system("rm -rf '{}'".format(i))
        print("All extra directories and files has been deleted moving forward")
    
    def uninstall_apps_directory(self,path):
        remove_apps = ['backup','nginx']
        all_apps = os.listdir(path)
        delete_apps = list(set(all_apps).difference(remove_apps))
        for i in delete_apps:
            os.system("rm -rf"+ " " + apps_path + "/" + i)
        for i in delete_apps:
            #print("Uninstallation of {} has been started.....".format(i))
            os.system("app-{} uninstall ".format(i))
            print("{} succesfully uninstalled".format(i))
    
    
    def delete_config(self,path):
        remove_config = ['systemd']
        all_configs = os.listdir(path)
        delete_config = list(set(all_configs).difference(remove_config))
        os.system("app-rtorrent uninstall")
        os.system("app-deluge uninstall")
        os.system("app-transmission uninstall")
        os.system("app-qbittorrent uninstall")
        os.system("rm -rf .ssh/authorized_keys")
        os.system("rm -rf www/rutorrent")
        #os.system("rm -rf {}".format(backup_path))
        os.system("rm -rf {}".format(rutorrent_plugin))
        for i in delete_config:
            os.system("rm -rf"+ " " + config_path + "/" + i)
        print("All torrent clients has been uninstalled and config files has been deleted")

    def delete_Data_from_maindirectory(self,path1,path2,path3,path4,files_path,downloads_path):
        print("Main directory cleanup started..")
        os.system("rm -rf {}".format(path1 + "/*"))
        #print("media/Movie directory cleanup done..")
        #print("media/Tv Show directory cleanup started..")
        os.system("rm -rf {}".format(path2 + "/*"))
        #print("media/Tv Show directory cleanup done..")
        #print("media/Music directory cleanup started..")
        os.system("rm -rf {}".format(path3 + "/*"))
        #print("media/Music directory cleanup done")
        #print("media/Books directory cleanup started..")
        os.system("rm -rf {}".format(path4 + "/*"))
        #print("media/Books directory cleanup done")
        #print("Files directory cleanup started..")
        os.system("rm -rf {}".format(files_path + "/*"))
        #print("Files directory cleanup started..")
        os.system("rm -rf {}".format(downloads_path + "/*"))
        #print("Files directory cleanup done")
    
    def ClearBin(self, files_path):
        avoid = ['nginx']
        all_bin_dir = os.listdir(files_path)
        delete_bin_dir = list(set(all_bin_dir).difference(avoid))
        for i in delete_bin_dir:
             os.system("rm -rf"+ " " + files_path + "/" + i)
    
    def Finalfix(self):
        os.system("app-nginx uninstall && app-nginx install && app-nginx restart")
        os.system("clear")
    
        
    
reset = FactorReset()

if __name__ == '__main__':
    os.system("pip3 install tqdm")
    pbar = tqdm(range(100))
    print("\033[91m"+ "Disclaimer: This script is unofficial and USB staff will not support any issues with it" + "\033[0m")
    s = input("Are you sure you want to delete all your data and applications config ? (yes/no)")
    confirmation = input("Please type 'confirm' to run the script:")
    if s == "yes" or s == "Yes" or s =="YES" and confirmation == "confirm":
        print("Choose the option from the list below.\n")
        print("1. Complete reset delete all data and config. \n")
        print("2. Delete all extra folders and files. \n")
        print("3. Uninstall all applications and their config but don't delete data. \n")
        print("4. Delete data from default directories. \n")
        choice = input("Please enter your choice: ")
        if choice == "1":
            os.system("pip3 install tqdm")
            os.system("clear")
            pbar.update(0)
            sleep(0.2)
            reset.Remove_Extra_directory(path)
            pbar.update(25)
            sleep(0.2)
            reset.uninstall_apps_directory(apps_path)
            pbar.update(50)
            sleep(0.2)
            reset.delete_config(config_path)
            pbar.update(75)
            sleep(0.2)
            reset.delete_Data_from_maindirectory(Movie_path,tv_path,music_path,book_path,files_path,downloads_path)
            pbar.update(95)
            sleep(0.2)
            reset.unmount_rclone()
            reset.ClearBin(bin_path)
            pbar.update(100)
            sleep(0.2)
            os.system("pip3 tqdm uninstall")
            reset.Finalfix()
            
        if choice == "3":
            pbar.update(0)
            sleep(0.2)
            reset.uninstall_apps_directory(apps_path)
            pbar.update(60)
            sleep(0.2)
            reset.delete_config(config_path)
            pbar.update(90)
            sleep(0.2)
            reset.ClearBin(bin_path)
            pbar.update(100)
            sleep(0.2)
            os.system("pip3 tqdm uninstall")
            reset.Finalfix()
            
        if choice == "2":
            pbar.update(0)
            sleep(0.2)
            reset.Remove_Extra_directory(path)
            pbar.update(50)
            sleep(0.2)
            pbar.update(100)
            sleep(0.2)
            os.system("pip3 tqdm uninstall")
            reset.Finalfix()
            
        if choice == "4":
            pbar.update(0)
            sleep(0.2)
            reset.delete_Data_from_maindirectory(Movie_path,tv_path,music_path,book_path,files_path,downloads_path)
            pbar.update(80)
            sleep(0.2)
            pbar.update(100)
            sleep(0.2)
            os.system("pip3 tqdm uninstall")
            reset.Finalfix()
                        
        else:
            print("Choose correct option and please run the script again.. :)")
    elif s == "no" or s == "NO" or s == "No":
        print("Factor Reset has been stopped.... All your data is safe")
    else :
        print("Please run the script again and choose valid option.")
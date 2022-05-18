import os
from subprocess import check_output
"""
Path definded for the directories
"""

path = os.getcwd()  # homex/username
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
systemd_app = config_path + '/systemd/user/'





class FactorReset():

    def unmount_rclone(self):
        grep_path = os.popen("mount | grep $USER").read()
        if grep_path == "":
            print("No rclone on your service")
        else:
            rclone_path = grep_path.split()
            rclone_path = rclone_path[2]
            print("All rclone service has been stopped")
            os.system("systemctl --user stop rclone-vfs")
            print("Your mergerfs is stopped now")
            os.system("systemctl --user stop mergerfs")
            os.system("fusermount -zu {}".format(rclone_path))
            print("Rclone unmounted...")
            os.system("killall rclone")
            print("Rclone unmounted succesfully")

    def Remove_Extra_directory(self, path):
        main_dir = []
        second_round = []
        remove_dir = ['media', 'files', 'downloads', '.bashrc', '.bash_history', '.bash_logout', 'watch', '.wget-hsts', '.config',
                      '.profile', 'www', 'bin', '.apps', '.ssh']  # these directories will not get removed
        listed_dir = os.listdir(path)
        for lis in listed_dir:
            main_dir.append(lis)
        final_dir = list(set(main_dir).difference(remove_dir))
        print("Removing Extra directories")
        for i in final_dir:
            os.system("rm -rf {}".format(i))
        listed_dir = os.listdir(path)
        for lis in listed_dir:
            second_round.append(lis)
        second_round_dir = list(set(second_round).difference(remove_dir))
        for i in second_round_dir:
            os.system("rm -rf '{}'".format(i))
        print("All extra directories and files has been deleted moving forward")

    def uninstall_apps_directory(self, path):
        remove_apps = ['backup', 'nginx']
        all_apps = os.listdir(path)
        delete_apps = list(set(all_apps).difference(remove_apps))
        for i in delete_apps:
            os.system("rm -rf" + " " + apps_path + "/" + i)
        for i in delete_apps:
            print("Uninstallation of {} has been started".format(i))
            os.system("app-{} uninstall ".format(i))
            print("{} succesfully uninstalled".format(i))

    def delete_config(self, path):
        remove_config = ['systemd']
        all_configs = os.listdir(path)
        delete_config = list(set(all_configs).difference(remove_config))
        os.system("app-rtorrent uninstall --full-delete")
        os.system("app-deluge uninstall --full-delete")
        os.system("app-transmission uninstall --full-delete")
        os.system("app-qbittorrent uninstall --full-delete")
        os.system("rm -rf www/rutorrent")
        #os.system("rm -rf {}".format(backup_path))
        os.system("rm -rf {}".format(rutorrent_plugin))
        for i in delete_config:
            os.system("rm -rf" + " " + config_path + "/" + i)
        print("All torrent clients has been uninstalled and config files has been deleted")

    def delete_Data_from_maindirectory(self, path1, path2, path3, path4, files_path, downloads_path):
        print("media/Movie directory cleanup started")
        os.system("rm -rf {}".format(path1 + "/*"))
        print("media/Movie directory cleanup done")
        print("media/Tv Show directory cleanup started")
        os.system("rm -rf {}".format(path2 + "/*"))
        print("media/Tv Show directory cleanup done")
        print("media/Music directory cleanup started")
        os.system("rm -rf {}".format(path3 + "/*"))
        print("media/Music directory cleanup done")
        print("media/Books directory cleanup started")
        os.system("rm -rf {}".format(path4 + "/*"))
        print("media/Books directory cleanup done")
        print("Files directory cleanup started..")
        os.system("rm -rf {}".format(files_path + "/*"))
        print("Files directory cleanup started..")
        os.system("rm -rf {}".format(downloads_path + "/*"))
        print("Files directory cleanup done")

    def ClearBin(self, files_path):
        avoid = ['nginx']
        all_bin_dir = os.listdir(files_path)
        delete_bin_dir = list(set(all_bin_dir).difference(avoid))
        for i in delete_bin_dir:
            os.system("rm -rf" + " " + files_path + "/" + i)

    def Stop_Systemd_app(self, path):
        dir_list = []
        not_remove_systemd_app = ['default.target.wants', 'nginx.service']
        list_dir = os.listdir(path)
        for i in list_dir:
            dir_list.append(i)
        final_list = list(set(dir_list).difference(not_remove_systemd_app))
        if len(final_list) == 0:
            pass
        else:
            for s in final_list:
                os.system("systemctl --user stop {}".format(s))
                os.system("rm -rf" + " " + path + "/" + i)
                print("{} service has been stopped and removed".format(s))
        os.system("systemctl --user daemon-reload")
        os.system("systemctl --user reset-failed")

    def Finalfix(self):
        os.system("app-nginx uninstall && app-nginx install && app-nginx restart")
        os.system("clear")

    def Fresh_Bash_install(self):
        print("Deleting your old .bashrc and .profile")
        os.system("rm -rf .bashrc")
        os.system("rm -rf .profile")
        os.system("cp /etc/skel/.profile ~/")
        os.system("cp /etc/skel/.bashrc ~/")
        check_output("source .bashrc",   shell=True, executable="/bin/bash")
        check_output("source .profile",   shell=True, executable="/bin/bash")
        print("Fresh .profile and .bashrc has been installed and loaded")

    def clear_corntab(self):
        os.system("crontab -r")


reset = FactorReset()

if __name__ == '__main__':
    print("\033[91m" + "Disclaimer: This script is unofficial and USB staff will not support any issues with it" + "\033[0m")
    s = input("Are you sure you want to delete all your data and applications config because once script is executed your data will be deleted forever we won't be able to get back your data ? (yes/no)")
    confirmation = input("Please type 'confirm' to run the script:")
    if s == "yes" or s == "Yes" or s == "YES" and confirmation == "confirm":
        print("Choose the option from the list below.\n")
        print("1. Complete reset delete all data and config. \n")
        print("2. Delete all extra folders and files. \n")
        print("3. Uninstall all applications and their config but don't delete data. \n")
        print("4. Delete data from default directories. \n")
        choice = input("Please enter your choice: ")
        if choice == "1":
            reset.Remove_Extra_directory(path)
            reset.uninstall_apps_directory(apps_path)
            reset.delete_config(config_path)
            reset.delete_Data_from_maindirectory(
                Movie_path, tv_path, music_path, book_path, files_path, downloads_path)
            reset.unmount_rclone()
            reset.ClearBin(bin_path)
            reset.Stop_Systemd_app(systemd_app)
            reset.Fresh_Bash_install()
            reset.clear_corntab()
            reset.Finalfix()

        if choice == "3":
            reset.uninstall_apps_directory(apps_path)
            reset.delete_config(config_path)
            reset.Stop_Systemd_app(systemd_app)
            reset.ClearBin(bin_path)
            reset.Fresh_Bash_install
            reset.clear_corntab()
            reset.Finalfix()
        if choice == "2":
            reset.Remove_Extra_directory(path)
            reset.Finalfix()
        if choice == "4":
            reset.delete_Data_from_maindirectory(
                Movie_path, tv_path, music_path, book_path, files_path, downloads_path)
            reset.Finalfix()
    elif s == "no" or s == "NO" or s == "No":
        print("Factor Reset has been stopped,All your data is safe")
    else:
        print("Please run the script again and choose valid option.")

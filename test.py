import os
path = os.getcwd() #homex/username
config_path = path + '/.config'
systemd_app = config_path + '/systemd/user/'
dir_list = []
not_remove_systemd_app = ['default.target.wants', 'nginx.service']
list_dir = os.listdir(systemd_app)
for i in list_dir:
   dir_list.append(i)
final_list = list(set(dir_list).difference(not_remove_systemd_app))
print(final_list)
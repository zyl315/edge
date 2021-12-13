def makedir(path):
    import os
    if not os.path.exists(path):
        os.makedirs(path)


fig_folder_path = "../../results/fig"
CMAB_folder_path = "../../results/URMB"
ENUR_folder_path = "../../results/ENUR"

if __name__ == '__main__':
    makedir(fig_folder_path)
    makedir(CMAB_folder_path)
    makedir(ENUR_folder_path)

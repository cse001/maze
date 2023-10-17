import os
from pathlib import Path
import string
import argparse
import shutil
maze_path = "/home/hacker/maze/"
def delete():
    for letter in string.ascii_lowercase:
        try:
            shutil.rmtree(letter)
        except:
            continue
    for letter in string.ascii_lowercase:
        try:
            # print(maze_path+letter+"_end")
            Path(maze_path+letter+"_end").unlink()
            # os.remove(maze_path+letter+"_end")
        except:
            continue

def create():
    dirs="1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35/36/37/38/39/40/41/42/43/44/45/46/47/48/49/50/51/52/53/54/55/56/57/58/59/60/61/62/63/64/65/66/67/68/69/70/71/72/73/74/75/76/77/78/79/80/81/82/83/84/85/86/87/88/89/90/91/92/93/94/95/96/97/98/99/"
    for letter in string.ascii_lowercase:
        dir_path = letter+"/"+dirs
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        os.symlink(maze_path,dir_path+"root")
        os.symlink(dir_path, maze_path+letter+"_end")

def print_path():
    p=""
    i=0
    for letter in string.ascii_lowercase:
        if i<20:
            p = p+"/"+letter+"_end"+"/root"
        else:
            break
        i+=1
    print(p)

def main():
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
    parser.add_argument('-c', '--create', action='store_true')
    parser.add_argument('-d', '--delete', action='store_true')
    args = parser.parse_args()
    if args.create:
        create()
    elif args.delete:
        delete()
    else:
        print_path()

if __name__ == "__main__":
    main()

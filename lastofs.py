#!/usr/bin/python3
from pprint import pprint;

def FS_DiskInit(letter):
  if (len(letter) > 1):
    print("\033[91mSystem error\033[0m, could not initialize disk");
    print("Error code: 0x00000103 Disk letter is more than 1 byte");
    exit(1);
  return {letter: {"type": "d", "name": letter, "files": dict()}};

def FS_DirCreate(disk, path):
  path = path.split("/");
  name = path[-1];
  path = path[:-1];
  dict_path = "['" + "']['files']['".join(path) + "']['files']";
  new_dir = str({"type": "d", "name": name, "files": dict()});
  exec(f"disk{dict_path}['{name}'] = {new_dir};");
  return disk;

def FS_FileCreate(disk, path):
  path = path.split("/");
  name = path[-1];
  path = path[:-1];
  dict_path = "['" + "']['files']['".join(path) + "']['files']";
  new_file = str({"type": "f", "name": name, "contents": bytearray([0])});
  exec(f"disk{dict_path}['{name}'] = {new_file};");
  return disk;

def FS_ListDirs(disk, cwd):
  path = cwd.split("/");
  name = path[-1];
  path = path[:-1];
  dict_path = "['" + "']['files']['".join(path) + "']['files']";
  exec(f"global files; files = disk{dict_path};");
  res = "";
  for i in files.values():
    if (i["type"] == "d"):
      res += f"\033[94m{i['name']}\033[0m ";
  return res;

def FS_ListFiles(disk, cwd):
  path = cwd.split("/");
  name = path[-1];
  path = path[:-1];
  dict_path = "['" + "']['files']['".join(path) + "']['files']";
  exec(f"global files; files = disk{dict_path};");
  res = "";
  for i in files.values():
    if (i["type"] == "f"):
      res += f"\033[92m{i['name']}\033[0m ";
  return res;

disk = FS_DiskInit("L");
disk = FS_DirCreate(disk, "L/Documents");
disk = FS_DirCreate(disk, "L/Downloads");
disk = FS_DirCreate(disk, "L/Photos");
disk = FS_DirCreate(disk, "L/Music");
disk = FS_FileCreate(disk, "L/file.txt");
disk = FS_FileCreate(disk, "L/Documents/file.txt");

print(FS_ListDirs(disk, "L/") + FS_ListFiles(disk, "L/"));


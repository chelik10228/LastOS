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

def FS_FileCreate(disk, path, fn):
  path = path.split("/");
  name = path[-1];
  path = path[:-1];
  dict_path = "['" + "']['files']['".join(path) + "']['files']";
  with open(fn, "rb") as s:
    f = s.read();
  new_file = str({"type": "f", "name": name, "contents": bytearray(f)});
  exec(f"disk{dict_path}['{name}'] = {new_file};");
  return disk;

def FS_FileRead(disk, path):
  path = path.split("/");
  name = path[-1];
  path = path[:-1];
  dict_path = "['" + "']['files']['".join(path) + "']['files']";
  exec(f"global s; s = disk{dict_path}['{name}']['contents'];");
  return s;

def FS_FileStream(disk, path, stream_fn):
  path = path.split("/");
  name = path[-1];
  path = path[:-1];
  dict_path = "['" + "']['files']['".join(path) + "']['files']";
  exec(f"global s; s = disk{dict_path}['{name}']['contents'];");
  with open(stream_fn, "wb") as fl:
    fl.write(s);

def FS_ListDirsRaw(disk, cwd):
  path = cwd.split("/");
  name = path[-1];
  path = path[:-1];
  dict_path = "['" + "']['files']['".join(path) + "']['files']";
  exec(f"global files; files = disk{dict_path};");
  res = "";
  for i in files.values():
    if (i["type"] == "d"):
      res += f"{i['name']} ";
  res = res[:-1];
  return res;

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
  res = res[:-1];
  return res;

def FS_ListFilesRaw(disk, cwd):
  path = cwd.split("/");
  name = path[-1];
  path = path[:-1];
  dict_path = "['" + "']['files']['".join(path) + "']['files']";
  exec(f"global files; files = disk{dict_path};");
  res = "";
  for i in files.values():
    if (i["type"] == "f"):
      res += f"{i['name']} ";
  res = res[:-1];
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
  res = res[:-1];
  return res;


import time;
import subprocess;

_timer_start = None;

def print_chars(msg, t):
  for i in msg:
    print(end=i, flush=True);
    time.sleep(t);

def printff(fn):
  with open(fn, "rb") as fl:
    print(fl.read().decode().replace("\\ESC", "\033"));

def readff(fn):
  with open(fn, "rb") as fl:
    return fl.read().decode().replace("\\ESC", "\033");

def printd(lines, d):
  for i in lines:
    print(i, flush=True);
    sleep(d);

def shell_call(command, shell=True, universal_newlines=True):
  try:
    result = subprocess.run(
      command,
      check=True,
      shell=shell,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE,
      universal_newlines=universal_newlines
    );
    return result.stdout;
  except subprocess.CalledProcessError as e:
    error_output = f"Command failed with exit code {e.returncode}\n";
    error_output += f"Error output:\n{e.stderr}";
    raise subprocess.CalledProcessError(
      e.returncode, e.cmd, error_output
    ) from e;

def start_timer():
  global _timer_start;
  _timer_start = time.time();

def cur_timer():
  if (_timer_start is None):
    return None;
  return time.time() - _timer_start;

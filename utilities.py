import pytz
import datetime
import os
import json
import yaml

# Terminal colors


class TerminalColors:
  PURPLE = "\033[95m"
  BLUE = "\033[94m"
  CYAN = "\033[96m"
  GREEN = "\033[92m"
  YELLOW = "\033[93m"
  RED = "\033[91m"
  RESET = "\033[0m"
  BOLD = "\033[1m"
  UNDERLINE = "\033[4m"


# Clear terminal
def clear_terminal():
  os.system("cls" if os.name == "nt" else "clear")


# Get time and date
def date_time(formatted: bool = False, date_class: bool = False):
  date_and_time = datetime.datetime.now(pytz.timezone("Asia/Ho_Chi_Minh"))
  if date_class:
    return date_and_time
  return (
    date_and_time.day, 
    date_and_time.month, 
    date_and_time.year,
    date_and_time.hour, 
    date_and_time.minute, 
    date_and_time.second
  ) if formatted else date_and_time.strftime("%m/%d/%Y, %H:%M:%S")

def time(formatted: bool = False) -> tuple or str:
  current_time = datetime.datetime.now(pytz.timezone("Asia/Ho_Chi_Minh"))
  return current_time.hour, current_time.minute, current_time.second if formatted else current_time.strftime("%H:%M:%S")


def date(formatted: bool = False) -> tuple or str:
  current_date = datetime.datetime.now(pytz.timezone("Asia/Ho_Chi_Minh"))
  return current_date.day, current_date.month, current_date.year if formatted else current_date.strftime("%m/%d/%Y")


# Get all files in a directory
def get_files(directory: str) -> list:
  # return os.listdir(directory) # This is the old way / deprecated
  return [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]


# Get all sub-directories in a directory
def get_sub_directories(directory: str) -> list:
  return [sub_directory for sub_directory in os.listdir(directory) if os.path.isdir(os.path.join(directory, sub_directory))]


# JSON handler
def get_json_data(directory: str) -> dict or list or tuple or set:
  with open(directory, "r", encoding="utf-8") as file:
    return json.load(file)


def save_json_data(directory: str, data: dict) -> None:
  with open(directory, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

# Yaml handler


def get_yaml_data(directory: str) -> dict or list or tuple or set:
  with open(directory, "r", encoding="utf-8") as file:
    return yaml.load(file)


def save_yaml_data(directory: str, data: dict) -> None:
  with open(directory, "w", encoding="utf-8") as file:
    yaml.dump(data, file, indent=2)


# Remove file
def delete_file(directory: str) -> None:
  os.remove(directory)

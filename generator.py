from typing import *
from utilities import *
import abc
import os
import re
import time
import zipfile

def create_sub_path_if_not_exists(directory: str) -> None:
  for i in range(len(directory.split("/"))):
    sub_path = "/".join(directory.split("/")[:i + 1])
    if not os.path.exists(sub_path):
      os.mkdir(sub_path)

def calculate_time(func) -> Callable:
  def inner(*args, **kwargs) -> Any:
    begin = time.time()
    data = func(*args, **kwargs)
    end = time.time()
    print("Total time taken in:", func.__name__, f"{end - begin:.5f}s!")

    return data

  return inner

class TestGenerator:
  def __init__(
    self,
    name: str = "default",
    number_of_testcases: int = 10,
    syntax: list = [
      "%1_id_1%.in",
      "%1_id_1%.out"
    ]
  ) -> None:
    self.name = name
    self.syntax = syntax
    self.number_of_testcases = number_of_testcases

  @abc.abstractmethod
  def algorithm(self, input_: str) -> str:
    pass

  @abc.abstractmethod
  def set_input(self, index: int) -> str:
    pass

  @calculate_time
  def generate(self, zip_all_file: bool = False) -> None:
    path = f"problems/{self.name}/testcase"
    create_sub_path_if_not_exists(path)

    regex_id_syntax = r"%[0-9]+_id_[0-9]+%"
    start_input, zero_fill_input = re.findall(regex_id_syntax, self.syntax[0])[0].strip("%").split("_id_")
    start_output, zero_fill_output = re.findall(regex_id_syntax, self.syntax[1])[0].strip("%").split("_id_")

    if (start_input == start_output != "0"):
      testcase_range = range(int(start_input), int(start_input) + self.number_of_testcases)
    else:
      testcase_range = range(self.number_of_testcases)

    for i in testcase_range:
      input_file_name = re.sub(regex_id_syntax, str(i).zfill(int(zero_fill_input)), self.syntax[0])
      output_file_name = re.sub(regex_id_syntax, str(i).zfill(int(zero_fill_output)), self.syntax[1])
      with (
        open(f"./problems/{self.name}/testcase/{input_file_name}", "w", encoding="utf-8") as input_file,
        open(f"./problems/{self.name}/testcase/{output_file_name}", "w", encoding="utf-8") as output_file
      ):
        input_data = self.set_input(i)
        input_file.write(str(input_data))
        output_file.write(str(self.algorithm(input_data)))

    if zip_all_file:
      self.zip()

  @calculate_time
  def zip(self) -> None:
    with zipfile.ZipFile(f"problems/{self.name}/{self.name}.zip", "w") as zip:
      for file in get_files(f"problems/{self.name}/testcase"):
        zip.write(
          filename=f"problems/{self.name}/testcase/{file}",
          arcname=file
        )

# A sample of the TestGenerator for Sum of 2 integers 
if __name__ == "__main__":
  from random import (
    randint as r,
    choice as c
  )

  class aplusb(TestGenerator):
    def __init__(self) -> None:
      super().__init__(
        "aplusb", 
        100
      )

    @calculate_time
    def algorithm(self, input_) -> Any:
      return sum(map(int, input_.split()))

    def set_input(self, index) -> Any:
      s = f"{r(10**4, 10**5)} {r(10**4, 10**5)}"
      return s

  class dinhcao_viethoangpopping(TestGenerator):
    def __init__(self) -> None:
      super().__init__(
        "dinhcao_viethoangpopping", 
        100
      )

    @calculate_time
    def algorithm(self, input_) -> Any:
      input_ = input_.split("\n")
      n = int(input_[0])
      data = input_[1:]
      return len([1 for i in range(n) if data[i].count("1") >= 3])

    def set_input(self, index) -> Any:
      s = ""
      n = r(10**4, 10**5)
      s += str(n) + "\n"
      for _ in range(n):
        s += f"{c([0, 1])} {c([0, 1])} {c([0, 1])} {c([0, 1])} {c([0, 1])}" + "\n"
      return s

  class cses1635(TestGenerator):
    def __init__(self) -> None:
      super().__init__(
        "cses1635", 
        100
      )

    @calculate_time
    def algorithm(self, input_) -> Any:
      input_ = input_.split("\n")
      n = int(input_[0])
      data = input_[1:]
      return len([1 for i in range(n) if data[i].count("1") >= 3])

    def set_input(self, index) -> Any:
      n = r(1, 100)
      x = r(1, 10**6)
      s = f"{n} {x}\n"
      contain = [0] * 10**6
      for _ in range(n):
        coin = r(1, 10**6 - 1)
        while not contain[coin]:
          s += f"{coin} "
          contain[coin] = True
          break
      return s.rstrip()

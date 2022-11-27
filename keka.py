import subprocess

while True:
  command = input("$ ").split(" ")
  subprocess.run(command)

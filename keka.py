import subprocess

while True:
  try: 
    command = input("$ ").split(" ")
    subprocess.run(command)
  except Exception as e:
    print(e)

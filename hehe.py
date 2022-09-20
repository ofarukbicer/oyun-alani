from time import sleep, time
from datetime import datetime


def readme_text():
    leave_date = datetime(2022, 9, 30)
    now_date = datetime.now()
    delta = leave_date - now_date
    if delta.days <= 0:
        return "# :(, coktan gittim"
    return str(f"""# ofarukbicer'in gidisine son {delta.days} gun {delta.seconds//3600} saat {(delta.seconds//60) % 60} dakika {str(delta).split(":")[-1].split(".")[0]} saniye kaldi

## Gidis tarihi: 30.09.2022 :(""")

def hehe():
    with open("README.md", "w") as f:
        f.write(readme_text())

while True:
    hehe()
    sleep(5)
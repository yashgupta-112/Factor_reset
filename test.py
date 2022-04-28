# python3 <(wget -qO- https://raw.githubusercontent.com/yashgupta-112/Factor_reset/master/Factor_reset.py)

pbar = ProgressBar().start()
def job():
   total_steps = 7
    # script 1
    pbar.update((1/7)*100)  # current step/total steps * 100
    # script 2
    pbar.update((2/7)*100)  # current step/total steps * 100
    # ....
    pbar.finish()pip in
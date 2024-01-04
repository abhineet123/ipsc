# virtualenv
mkvirtualenv -p python3.10 dproc
alias dproc='workon dproc'
alias ac='workon dproc'

## pycharm       @ virtualenv-->dproc_setup
Add interpreter > On WSL

# packages
python -m pip install imagesize paramparse numpy opencv-python matplotlib pandas tqdm prettytable tabulate scikit-learn pycocotools pyperclip

sudo apt-get install python3.10-tk



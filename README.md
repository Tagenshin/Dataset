# Collecting Dashboard

## Setup Install Library - Terminal (pip - Virtual Environment Opsional)

### (Opsional) Buat Virtual Environment (disarankan agar tidak mengganggu sistem utama):

python -m venv myenv
source myenv/bin/activate # Mac/Linux
myenv\Scripts\activate # Windows

### Install Library

pip install pandas
pip install matplotlib
pip install seaborn
pip install numpy
pip install streamlit

## Setup Install Library - Terminal (Conda - Anaconda Prompt)

### Buat dan Aktifkan Conda Environment

conda create --name myenv python=3.9
conda activate myenv

### Install Library Satu per Satu dengan Conda:

conda install pandas
conda install matplotlib
conda install seaborn
conda install numpy
conda install -c conda-forge streamlit

## Run steamlit app

streamlit run dashboard.py

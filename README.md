# Collecting Dashboard

## Setup Install Library - Terminal (pip - Virtual Environment Opsional)

### (Opsional) Buat Virtual Environment (disarankan agar tidak mengganggu sistem utama):

python -m venv myenv<br>
source myenv/bin/activate # Mac/Linux<br>
myenv\Scripts\activate # Windows<br>

### Install Library

pip install pandas <br>
pip install matplotlib<br>
pip install seaborn<br>
pip install numpy<br>
pip install streamlit<br>

## Setup Install Library - Terminal (Conda - Anaconda Prompt)

### Buat dan Aktifkan Conda Environment

conda create --name myenv python=3.9<br>
conda activate myenv<br>

### Install Library Satu per Satu dengan Conda:

conda install pandas<br>
conda install matplotlib<br>
conda install seaborn<br>
conda install numpy<br>
conda install -c conda-forge streamlit<br>

## Run steamlit app

streamlit run dashboard.py

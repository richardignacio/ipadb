# Installation

**Prerequisite: Python 3 must already be installed for your platform!**
- Windows: https://docs.python.org/3/using/windows.html
- macOS  : https://docs.python.org/3/using/mac.html

## Instructions

1. Download or clone the code from this github repository

    a. Option 1: Download the zip file and unzip into a new directory

    - https://github.com/richardignacio/ipadb/archive/refs/heads/main.zip
    
    b. Option 2: If you have git installed, clone the repo.
    
    - git clone https://github.com/richardignacio/ipadb.git

2. Change (cd) into the repo's root directory (it should have a __requirements.txt__ file)

3. Create a virtual environment

    a. Windows: `py -m venv .venv`
    
    b. macOS: `python3 -m venv .venv`

4. Activate the virtual environment

    a. Windows: `.venv\Scripts\activate`
    
    b. macOS: `source .venv/bin/activate`

5. Install and upgrade pip

    a. Windows: `py -m pip install --upgrade pip`

    b. macOS: `python3 -m pip install --upgrade pip`

6. Install the depdencies

    a. Windows: `py -m pip install -r requirements.txt`

    b. macOS: `python3 -m pip install -r requirements.txt`

## Running the demo scripts

In the root of the repository, do the following.

1. Ensure the virual environment is activated.  See Step 4 above.

2. Add your API Key to the environment variables. This allows the script to access your API_KEY with it being hard-coded into the script.

    - Windows: `set API_KEY=<insert_your_API_key_here>`

    - macOS: `export API_KEY=<insert_your_API_key_here>`

2. If it is a python script, run it like this:

    - Windows: `py ipadb.py <insert_argument_here>`

    - macOS: `python3 ipadb.py <insert_argument_here>`

3. If it is a bash script, run it like this:

    - `./ipadb.sh <insert_argument_here>`


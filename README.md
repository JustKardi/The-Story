# The Story

## What is it?
The Story is a simple AI driven app that will predict your life. It uses fine-tuned models trained on custom data in order to predict your future, and show in a riddle-like way that is up to you to decode. It uses two fine-tuned models that work together to make everything work. **THE MODELS ARE NOT HOSTED ON THE WEB -- IF YOU ARE RUNNING LOCALLY, YOU NEED TO TRAIN THE MODELS** *See training section*

# Locally Running the App
In order to locally run the app, you need to do the following
* Ensure you have Git installed
* Run `git clone https://github.com/JustKardi/The-Story` in your desired directory
* Navigate to `The Story/thestory/ai`
* Activate the venv using:
    * CMD: `venv_directml\Scripts\activate.bat`
    * PowerShell: `.\venv_directml\Scripts\activate.ps1`
    * Bash: `source venv/scripts/activate`
* Once the virtual environment is active, ensure you have Python installed
    * **IMPORTANT**: Release 0.0 has limited support for local running. It requires Python 3.10 or below and AMD Radeon Graphics
* Install the necessary dependencies using `pip install -y torch_directml transformers`
* Run `python train.py`
* Run `python train_predictor.py`
* Navigate to root and install NodeJS dependencies using:
    * `npm i express`
    * `npm i nodemon`
* Ensure `package.json` has `"dev": "nodemon app.js"` in `Scriptd`



## NOTE: THIS APP IS NOT COMPLETE IS UNDER MAJOR DEVELOPMENT FOR CROSS PLATFORM SUPPORT
# Note: If on Windows, run
# git clone -c core.symlinks=true https://github.com/plaid/quickstart
# instead to ensure correct symlink behavior

git clone https://github.com/plaid/quickstart.git
cd quickstart/python

# Copy the .env.example file to .env, then fill
# out PLAID_CLIENT_ID and PLAID_SECRET in .env
cp .env.example .env

# Note: must use python 3

# For virtualenv users:
# virtualenv venv
# source venv/bin/activate
pip3 install -r requirements.txt

# Start the backend app
./start.sh
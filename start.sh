#Dont change anything without informing us
if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/shakir04/AutoFilter.git /AutoFilter
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /AutoFilter
fi
cd /Lucy
pip3 install -U -r requirements.txt
echo "sᴛᴀʀᴛɪɴɢ ʟᴜᴄʏ ʙᴏᴛ...."
python3 bot.py

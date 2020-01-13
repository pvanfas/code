Install Visual Studio Code and install following extensions
 ```
sudo apt update
sudo apt install software-properties-common apt-transport-https wget
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
sudo apt update
sudo apt install code
 ```
  Launch VS Code Quick Open (Ctrl+P), paste the following command, and press enter.
  
 ```
 ext install burkeholland.simple-react-snippets
 ext install esbenp.prettier-vscode
 ext install kelset.rn-full-pack
 
 ```
Open settings (ctrl + comma) and add the following to the json file

 ```
 "editor.formatOnSave": true,
 ```

# LoL-Valorant-Offline-Mode
LoL - Valorant Offline Mode

You can play Valorant or LoL without chat!

[![](https://cdn.discordapp.com/attachments/452001720055234581/912693098201632798/ss.png)](https://cdn.discordapp.com/attachments/452001720055234581/912693098201632798/ss.png)

[Click here to download compiled version (You must start as a administrator)](https://github.com/Dekares/LoL-Valorant-Offline-Mode/releases/tag/compiled "Click here to download compiled version (You must start as a administrator)")

Manuel:

for offline = `netsh advfirewall firewall add rule name="lolchat" dir=out remoteip={serverip} protocol=TCP action=block`         
for online = `netsh advfirewall firewall delete rule name="lolchat"`

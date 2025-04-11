# TP-Link-HS100-Sysinfo
Retrieves device information from the TP-Link HS100 smart plug by sending encrypted JSON payloads over TCP


##How it works:
The script creates a raw TCP socket connection to the plug on port 9999.
A get_sysinfo JSON payload is encrypted using TP-Link’s XOR algorithm (key: 171).
The encrypted payload is sent, and the plug responds with an encrypted message.
The response is decrypted and printed in JSON format for analysis.

##Disclaimer:
This script was created for educational and research purposes only.

# PixelverseXYZ Clicker Bot
[![App Screenshot](https://raw.githubusercontent.com/katzura1/Pixelversexyz-Bot/main/SCR-20240508-ste.png)](https://raw.githubusercontent.com/katzura1/Pixelversexyz-Bot/main/SCR-20240508-ste.png)


This script automates clicks in the PixelverseXYZ app. It uses the developer console to identify and extract necessary tokens and modifies the script to automate the clicker functionality.

## Step-by-Step Instructions

- `git clone https://github.com/Zlkcyber/pixelversexyz.git`
- `cd pixelversexyz`

1. **Open the Developer Console**
   - In your web browser, open the developer tools (usually accessed with `F12` or `Ctrl+Shift+I`).
   - Go to the "Network" tab to inspect network requests.

2. **Open the PixelverseXYZ App**
   - Navigate to the PixelverseXYZ app or website in your browser to start capturing network traffic.

3. **Extract Initdata, TGID and Secret**
   - Look for `user` on the `network`
   - Identify the request that contains the `tgid` ,`secret` `initdata` and `username`.
   - These values may be present in the request headers or the URL itself.
[![App Screenshot](https://raw.githubusercontent.com/Zlkcyber/pixelversexyz/main/pixel3.png)](https://raw.githubusercontent.com/Zlkcyber/pixelversexyz/main/pixel3.png)
5. **Edit the Script**
   - Open the script file `main.py`.
   - Update the placeholders for `tgid` ,`secret` `initdata` and `username` with the extracted information from step 3.

6. **Run the Script**
   - Ensure Python is installed on your system.
   - Open a terminal or command prompt in the directory where `main.py` is located.
   - Execute the script with the following command:
     ```bash
     python3 main.py
     ```

## Troubleshooting

- **Incorrect TGID or Secret:** Double-check the extracted values to ensure they are accurate and placed in the correct locations within the script.
- **Python Not Found:** Confirm that Python is installed on your system and properly added to the PATH.
- **Script Errors:** If the script encounters issues, refer to the error messages for clues, and ensure all required information is correctly entered.

## Disclaimer

This script is for educational and personal use only. Ensure you have permission to use any tools or applications involved. Unauthorized use or accessing services without authorization may violate terms of service or laws. Use this script responsibly and at your own risk.

## License

This script is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute it, but must provide attribution to the original author.

source https://github.com/katzura1/Pixelversexyz-Bot 

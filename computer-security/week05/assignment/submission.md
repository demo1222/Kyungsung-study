<style>h3 { color: #000; font-weight: bold; }</style>

Scenario: Fake software / update

### 1. Initial contact

Mina is a student working on her report on her own laptop. She opens a news website she reads often, but the site has been hacked and has a hidden script on it. The script shows her a page that looks just like Chrome, saying her browser is out of date and needs a critical update. She clicks the button and a file called "Update.js" is downloaded. A real Chrome update would come through the browser itself, not from a web page.

### 2. Execution

Mina opens the file, thinking it is the update. It is actually a script, and it runs with her account's access. Nothing seems to happen, so she thinks the update finished and goes back to work. In the background, the script connects to the attacker's server and downloads more malware.

### 3. Privilege

A Windows prompt asks for permission to make changes. Mina uses an administrator account for everything, and she has clicked prompts like this many times before, so she clicks "Yes". Now the malware has admin rights. It can change system settings, turn off parts of the antivirus, and reach more data on the laptop. If she had used a standard account, the prompt would have asked for an admin password, and the damage would have stayed inside her own profile.

### 4. Persistence

The malware copies itself into the AppData folder with an ordinary-looking name. It adds a scheduled task and a startup entry so it runs again every time the laptop restarts. The laptop is now a bot that checks in with the attacker and waits for commands. Mina does not see any warning. She only notices that the laptop is slower, and sometimes unknown pages open in the browser.

### 5. Impact

First, the malware steals her saved browser passwords, login cookies, and what she types. With the stolen cookies, the attacker gets into her university email and sends fake "exam notes" to her classmates, with a link to the same fake update. A few days later, ransomware is installed. It encrypts her course files and the USB backup drive she always kept plugged in. A ransom note appears asking for payment, and the attacker also threatens to publish her documents.

### 6. Recovery

Mina stops using the laptop for anything important and reports the problem to the university IT support. She does not pay the ransom, because paying does not guarantee she gets her files back. Following IT's advice, she disconnects the laptop from Wi-Fi and unplugs the USB drive. From another device, she changes her email password, signs out of all sessions, changes the other passwords that were saved in the browser, turns on MFA, and warns her classmates about the fake email. The laptop is wiped and Windows is reinstalled. She restores her files from an older backup that was not connected to the laptop, and checks that they open correctly. To stop this from happening again, she creates a standard account for daily use, keeps automatic updates on, and keeps one backup offline. For the next few weeks she watches her accounts for strange logins.

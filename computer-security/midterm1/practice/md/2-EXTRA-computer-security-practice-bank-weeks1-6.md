# Computer Security — Extra Practice Bank

**EXTRA PRACTICE** · Weeks 1–6 · 343 questions · Answers at the end

> **How to use this bank.** This is extra practice on top of the main test. Do one week at a time, mark your answers in pencil, then check them with the key at the end. Re-do every question you missed two days later.
>
> | Part | What | Questions |
> |---|---|---|
> | A | Multiple choice, by week | 208 |
> | B | True / False | 50 |
> | C | Quick classification drills (CIA, malware, phishing labels, risk, P/D/R, access failures) | 59 |
> | D | Short answer (write 2–5 sentences) | 26 |

## Part A — Multiple Choice

### Week 1 — Introduction to Computer Security

1. Which CIA goal answers the question "Who is allowed to see it?"
     - A. Integrity
     - B. Confidentiality
     - C. Availability
     - D. Accountability

2. Which CIA goal answers "Is it correct, complete and trustworthy?"
     - A. Integrity
     - B. Confidentiality
     - C. Availability
     - D. Authorization

3. Which CIA goal answers "Can authorized people use it when needed?"
     - A. Confidentiality
     - B. Integrity
     - C. Availability
     - D. Authentication

4. The LMS is offline the night before a deadline. Which goal failed?
     - A. Confidentiality
     - B. Integrity
     - C. Non-repudiation
     - D. Availability

5. Someone changes a submitted assignment after the deadline. Which goal failed?
     - A. Confidentiality
     - B. Integrity
     - C. Availability
     - D. None of them

6. A shared file is corrupted and cannot be opened. Which is the best description?
     - A. Confidentiality only
     - B. Availability only, never integrity
     - C. Integrity, and as a result availability
     - D. It is not a security issue

7. Someone watches you type your password in the library (shoulder-surfing). This is a typical failure of:
     - A. Confidentiality
     - B. Integrity
     - C. Availability
     - D. Authorization

8. Which control mainly supports **availability**?
     - A. Screen lock
     - B. Sharing permissions
     - C. Redundancy and tested backups
     - D. Hashes

9. Which group lists typical **integrity** controls?
     - A. DoS protection only
     - B. Privacy screens
     - C. Public file sharing
     - D. Access control, validation, logs, version history and hashes

10. Which is a typical cause of an **availability** failure with no attacker?
     - A. A power or hardware failure
     - B. A phishing e-mail
     - C. A stolen password
     - D. A keylogger

11. MFA improves confidentiality but adds a login step. What is the course's answer to this trade-off?
     - A. Remove MFA to save time
     - B. Make protection usable instead of removing it
     - C. Use MFA only for administrators
     - D. Ignore user complaints

12. Which statement shows a **balanced** view of security?
     - A. "Nothing bad has happened, so we are safe."
     - B. "Everything is a disaster."
     - C. "Assess the real risks and choose usable controls."
     - D. "Security is only the IT department's job."

13. A tested backup supports which goals?
     - A. Only confidentiality
     - B. Only authorization
     - C. None of them
     - D. Availability, and it can restore integrity

14. In the five words, "a possible cause of harm" is a:
     - A. Threat
     - B. Vulnerability
     - C. Control
     - D. Asset

15. "A safeguard that reduces risk" is a:
     - A. Asset
     - B. Vulnerability
     - C. Control
     - D. Threat

16. "The possibility and consequence of harm" is:
     - A. Threat
     - B. Risk
     - C. Exploit
     - D. Asset

17. Mina's classmates and professor receive fake messages sent from her compromised account. What does this show?
     - A. Only Mina is affected
     - B. Only availability failed
     - C. The classmates are the attackers
     - D. One account compromise can also harm other people

18. In Mina's case, being locked out of her account before the deadline is a failure of:
     - A. Availability
     - B. Confidentiality
     - C. Integrity
     - D. Authentication strength

19. In "people, process, technology", **process** means:
     - A. Blocking and detecting attacks
     - B. The choices people make
     - C. The procedure that says what to do
     - D. Recording logs automatically

20. Why is technology alone never enough?
     - A. Technology is too expensive
     - B. A person can still give the password away
     - C. Technology never works
     - D. Laws forbid relying on technology

21. Which is a warning sign of a suspicious message?
     - A. Unexpected urgency and a request for credentials
     - B. A message you expected from a known teacher about a known task
     - C. A timetable update on the official portal
     - D. A library due-date reminder you signed up for

22. A message claims to be from your university and contains a link. How should you check it?
     - A. Click the link in the message
     - B. Reply and ask if it is real
     - C. Open the official site yourself through a route you choose
     - D. Forward it to classmates

23. According to week 1, "pressure is a signal to ______."
     - A. act quickly
     - B. slow down
     - C. reply immediately
     - D. delete everything

24. Two scans are technically identical. What makes one authorized and the other not?
     - A. The speed of the scan
     - B. The tool used
     - C. Permission, scope and how results are handled
     - D. The time of day

25. The scope of a lab exercise is unclear. What should you do?
     - A. Continue but be careful
     - B. Scan everything to be safe
     - C. Ask a classmate to do it
     - D. Stop and ask

### Week 2 — Assets, Threats and Risk

26. What are the four asset types?
     - A. Information, devices, people, services
     - B. Hardware, software, firmware, cloud
     - C. Money, buildings, cars, phones
     - D. Users, admins, guests, attackers

27. Patient records, grades and passwords are which asset type?
     - A. Devices
     - B. Information
     - C. Services
     - D. People

28. Online exams, messaging and payments are which asset type?
     - A. Information
     - B. People
     - C. Services
     - D. Devices

29. The Equifax 2017 breach mainly shows the loss of:
     - A. Availability
     - B. Integrity
     - C. Physical safety
     - D. Confidentiality

30. The NHS disruption in May 2017 (WannaCry) mainly shows the loss of:
     - A. Availability
     - B. Confidentiality
     - C. Integrity only
     - D. Authentication

31. GitLab 2017 (database data deleted) mainly shows the loss of:
     - A. Confidentiality
     - B. Integrity
     - C. Physical safety
     - D. Nothing

32. Which question is **not** one of the three questions that go beyond an asset list?
     - A. Value: why does it matter?
     - B. Dependency: what does it need to work?
     - C. Protection goals: what must be preserved?
     - D. Manufacturer: who built it?

33. What is a **threat**?
     - A. A weakness
     - B. A protective measure
     - C. A possible cause of harm
     - D. A way to use a weakness

34. What is an **exploit**?
     - A. A way to use a weakness
     - B. A possible cause of harm
     - C. A software update
     - D. A copy of data

35. What is a **control**?
     - A. A weakness
     - B. A possible cause of harm
     - C. An attacker
     - D. A protective measure

36. Which statement is correct?
     - A. A threat must always be a person with bad intentions
     - B. A threat does not have to be a person with bad intentions
     - C. Fires are not threats
     - D. Accidents are vulnerabilities

37. Which is an **incident**?
     - A. An unfixed flaw might be used next month
     - B. A weak backup could fail next term
     - C. The library computers were encrypted by ransomware this morning
     - D. Phishing might target staff in the future

38. "Checking records of unusual access" is which type of control?
     - A. Prevent
     - B. Detect
     - C. Recover
     - D. Exploit

39. "Restoring from a tested copy" is which type of control?
     - A. Recover
     - B. Detect
     - C. Prevent
     - D. Threat

40. "Fixing a known flaw" is which type of control?
     - A. Detect
     - B. Recover
     - C. Prevent
     - D. Exploit

41. What is a **patch**?
     - A. A copy of data
     - B. A fake website
     - C. An attack
     - D. A software update that fixes a problem

42. What is the Equifax lesson about patches?
     - A. A patch instruction is enough
     - B. The patch must be applied and checked on the real system
     - C. Patches cause breaches
     - D. Only antivirus matters

43. Which pair is correct?
     - A. Backup = make a separate copy; restore = use the copy to recover
     - B. Backup = use a copy to recover; restore = make a copy
     - C. Backup and restore mean the same thing
     - D. Backup = encrypt data; restore = decrypt data

44. What are **credentials**?
     - A. A software update
     - B. A list of assets
     - C. Evidence used to prove identity, such as login details
     - D. A firewall rule

45. What is **authentication** (week 2 definition)?
     - A. Giving permissions
     - B. The process of checking a claimed identity
     - C. Encrypting a disk
     - D. Making a backup

46. Why did the attacker get into Uber in September 2022?
     - A. A contractor approved a login after repeated requests
     - B. The servers were unpatched
     - C. A data center caught fire
     - D. A USB stick was found in the car park

47. Which word best describes the security keys that protected Cloudflare?
     - A. Reusable SMS codes
     - B. Password-based
     - C. Shared between staff
     - D. Origin-bound

48. Before rating a risk, what must you define first?
     - A. The attacker's name
     - B. The price of the asset
     - C. The event, the period and the current controls
     - D. Only the impact

49. In risk assessment, a statement "supported by evidence" is a:
     - A. Fact
     - B. Assumption
     - C. Unknown
     - D. Risk

50. "Missing evidence" is called an:
     - A. Fact
     - B. Unknown
     - C. Assumption
     - D. Exploit

51. Likelihood score 3 means:
     - A. Unlikely
     - B. Possible
     - C. Likely: expected, or strongly supported by evidence
     - D. Severe

52. Impact score 2 ("Serious") means:
     - A. Small disruption, routine recovery
     - B. Essential service lost
     - C. No effect at all
     - D. Important work or privacy affected; extra help needed

53. L = 1 and I = 3. Score and level?
     - A. 3, Medium
     - B. 3, Low
     - C. 4, Medium
     - D. 3, High

54. L = 3 and I = 1. Score and level?
     - A. 3, Low
     - B. 4, Medium
     - C. 3, Medium
     - D. 3, High

55. A verified patch mainly reduces:
     - A. Impact
     - B. Likelihood
     - C. Value
     - D. Dependency

56. A GitLab-like deletion happens, but a recent restore works. Which rating did the slides give?
     - A. 9, High
     - B. 6, High
     - C. 4, Medium
     - D. 2, Low

57. Week 2 assignment: a public exam system has an unfixed flaw and an untested backup; the exam is in 30 days. The model rating is:
     - A. 3 × 3 = 9, High
     - B. 1 × 1 = 1, Low
     - C. 2 × 2 = 4, Medium
     - D. 1 × 3 = 3, Medium

58. What does MFA require?
     - A. Two passwords
     - B. More than one **kind** of identity evidence
     - C. A very long password
     - D. Only an e-mail confirmation

59. Why was Uber's MFA weak against this attack?
     - A. The security key was stolen
     - B. MFA was not enabled
     - C. It depended on a person's judgment under pressure
     - D. The password was too strong

60. In week 2, **phishing** is defined as:
     - A. A deceptive message or website that tries to trick someone
     - B. A worm that spreads by itself
     - C. A data-center fire
     - D. A software patch

### Week 3 — Social Engineering and Phishing

61. Through which channels can social engineering arrive?
     - A. Only e-mail
     - B. Phone, text, e-mail, social media or in person
     - C. Only websites
     - D. Only USB sticks

62. Which three reasons explain why social engineering works?
     - A. Trust, pressure, attention
     - B. Speed, cost, size
     - C. Encryption, hashing, salting
     - D. Patching, backups, logging

63. "You won a tuition grant! Claim it today." Which lever is this mainly?
     - A. Fear
     - B. Authority
     - C. Reward
     - D. Familiarity

64. "Someone posted your photo. Click to see it." Which lever?
     - A. Urgency
     - B. Reward
     - C. Authority
     - D. Curiosity

65. "It's me. I changed my number." Which lever?
     - A. Authority
     - B. Reward
     - C. Familiarity
     - D. Curiosity

66. "Your account is involved in a crime." Which lever?
     - A. Fear
     - B. Reward
     - C. Curiosity
     - D. Familiarity

67. Why is "Keep this private until approval" dangerous?
     - A. It makes the message shorter
     - B. It proves the request is official
     - C. It removes the person who would notice that something looks odd
     - D. It is illegal to keep secrets

68. You find a USB stick labelled "Exam answers" in the hallway. What is the best action?
     - A. Plug it into your laptop to find the owner
     - B. Plug it into a lab computer that is not yours
     - C. Keep it and check it at home
     - D. Do not plug it in; hand it to IT

69. What is **baiting**?
     - A. Following someone through a secure door
     - B. An attractive item or offer that invites a risky action
     - C. A phishing phone call
     - D. A phishing text message

70. What is the polite, safe response to tailgating?
     - A. Push the person out
     - B. Point them to reception or call the person they are visiting
     - C. Let them in if they look friendly
     - D. Ignore them

71. Which control is better than "be more careful" against MFA fatigue?
     - A. Approve prompts quickly so they stop
     - B. Turn off MFA
     - C. Phishing-resistant MFA, limits and alerts on repeated prompts, and a rule to report prompts you did not start
     - D. Use SMS codes only

72. What does **verified contact** mean?
     - A. The message says it is from the university
     - B. The logo matches the real one
     - C. The profile picture looks right
     - D. You reach the person through a route you already trust and confirm the exact request

73. Which of these can be copied easily by an attacker?
     - A. A hardware security key
     - B. A phone number you saved earlier
     - C. An agreed approval process
     - D. Names, logos and profile pictures

74. Spear phishing describes which feature of an attack?
     - A. Targeting
     - B. Channel
     - C. Claimed identity
     - D. Malware type

75. Vishing describes which feature?
     - A. The voice-call channel
     - B. The text channel
     - C. Targeting
     - D. Malware

76. Impersonation describes which feature?
     - A. The channel
     - B. Targeting
     - C. The reward lever
     - D. Claimed identity

77. A generic e-mail sent to all students asks them to "sign in again". Best label?
     - A. Spear phishing + vishing
     - B. Smishing
     - C. Broad phishing
     - D. Impersonation + tailgating

78. A caller pretending to be your bank asks for the code you just received. Labels?
     - A. Smishing + spear phishing
     - B. Vishing + impersonation
     - C. Baiting
     - D. Tailgating

79. A copied friend profile on social media asks for urgent money. Best label?
     - A. Vishing
     - B. Impersonation
     - C. Smishing
     - D. Worm

80. What was the best control in the Korean "daughter" call case (reported July 2018)?
     - A. Pay quickly to help
     - B. Ask the caller to send a photo as proof
     - C. Stay on the line until the caller hangs up
     - D. Call back on a known number, or use a family code word

81. What is the lesson of the Twilio case (August 2022)?
     - A. Text messages cannot be phishing
     - B. A familiar name does not prove the destination, and an account's reach should be limited
     - C. Only managers are targeted
     - D. HTTPS stops all phishing

82. The Changwon District Court warning (8 July 2025) described "court mail was returned" messages. What should you do?
     - A. Find the court's number yourself and call it
     - B. Use the link in the message
     - C. Install the app the message asks for
     - D. Give the information requested

83. In the Hong Kong deepfake meeting case, about how much was transferred?
     - A. HK$2 million
     - B. HK$20 million
     - C. HK$200 million
     - D. HK$2 billion

84. What is a **deepfake**?
     - A. A fake Wi-Fi network
     - B. AI used to imitate a person's appearance or voice
     - C. A kind of worm
     - D. A fake domain name

85. The warning pattern **U + P + S** stands for:
     - A. Unknown, Private, Secure
     - B. Urgent, Personal, Simple
     - C. Update, Patch, Scan
     - D. Unexpected, Pressure, Sensitive action

86. Which request deserves a pause?
     - A. A lecture reminder you expected
     - B. A request to change the bank account for a payment
     - C. A newsletter you subscribed to
     - D. A timetable posted on the portal

87. A hostname is read from the:
     - A. Left
     - B. Path after the slash
     - C. Right
     - D. Protocol part

88. You get an urgent tuition notice with a QR code. What is the strongest action?
     - A. Scan it now before the deadline
     - B. Open the usual portal yourself
     - C. Ask the sender if it is real
     - D. Forward it to friends

89. A verification route is **independent** when:
     - A. It appears in the message signature
     - B. The sender gave it to you in the same call
     - C. You obtained it separately from the suspicious contact
     - D. It is printed on a QR code

90. You entered your password on a fake page. What should you do?
     - A. Reset access and end sessions through a trusted route, and contact IT
     - B. Do nothing if nothing happens
     - C. Delete the e-mail only
     - D. Wait a week to see

91. You installed an app or allowed remote access after a scam call. What should you do?
     - A. Continue online banking on the same device
     - B. Reinstall the app later
     - C. Stop using the device for sensitive tasks and get help from another device
     - D. Post about it on social media first

92. Why respond supportively ("Thank you for telling me") when someone reports a mistake?
     - A. Shame makes people hide information and delay help
     - B. It is only about being polite
     - C. It is legally required
     - D. It avoids paperwork

### Week 4 — Identity, Authentication and Access Control

93. What is **authorization**?
     - A. An account claim
     - B. Proof for the account
     - C. Permission for that action
     - D. Logging the event

94. What does a successful authentication show?
     - A. That the proof matched the account, not that the real owner typed it
     - B. That the real owner is at the keyboard
     - C. That the user may do any action
     - D. That the device is free of malware

95. Should Mina's student account be able to change grades?
     - A. Yes, if the password is correct
     - B. Yes, if MFA is complete
     - C. Only during exam week
     - D. No; the student role cannot edit grades, whoever is signed in

96. A stranger signed in as Mina. What is the best evidence to collect?
     - A. Mina's handwriting
     - B. The access log: sign-in time, account, events, decisions, and active sessions
     - C. The Wi-Fi name
     - D. The password itself

97. What does the **account record** store?
     - A. Role, status and scope
     - B. Only the password
     - C. The web pages visited
     - D. The device's IP address

98. What is the purpose of a **session**?
     - A. To store the password
     - B. To decide permissions for the whole day
     - C. To recognize later requests after sign-in
     - D. To encrypt the disk

99. A former TA's account stays active after they leave. Which item failed?
     - A. The session
     - B. The permission check
     - C. The hash
     - D. The account record (its status)

100. Which statement is correct?
     - A. A successful sign-in settles every later request
     - B. Each request still needs its own permission check
     - C. Sessions can never be stolen
     - D. Permissions are only checked at login

101. Which defense fits **credential stuffing**?
     - A. A unique password for each service
     - B. A bigger screen
     - C. A shared account
     - D. Turning off logs

102. Which defense fits online **password guessing**?
     - A. Longer usernames
     - B. Shared accounts
     - C. Attempt limits and strong passwords
     - D. Disabling logs

103. Which defense fits **phishing** for credentials?
     - A. Longer usernames
     - B. Phishing-resistant authentication such as passkeys or FIDO keys
     - C. A weaker recovery process
     - D. A shared login

104. How many possible values does a four-digit PIN have?
     - A. 9,999
     - B. 1,000
     - C. 10,000
     - D. 40

105. How many possible values does a six-digit PIN have?
     - A. 100,000
     - B. 600,000
     - C. 999,999
     - D. 1,000,000

106. Besides the number of possibilities, the time to guess also depends on:
     - A. The guessing rate and the defenses
     - B. The colour of the login page
     - C. The length of the username only
     - D. The time zone

107. In **offline** guessing, where do the guesses go?
     - A. To the login service
     - B. To a copied hash on the attacker's own device
     - C. To the user's phone
     - D. To the firewall

108. Does login MFA prevent offline hash testing?
     - A. Yes, always
     - B. Yes, if the codes are sent by SMS
     - C. Only for administrators
     - D. No; it can block account entry, but it does not stop hash testing

109. What slows offline guessing?
     - A. A costly password-hashing scheme such as Argon2id
     - B. A login attempt limit
     - C. A longer username
     - D. A faster hash such as SHA-256 alone

110. A short candidate list fails to match a hash. What does that prove?
     - A. SHA-256 is broken
     - B. The salt is secret
     - C. Only that those few words were wrong, not that the password is safe
     - D. The hash was decrypted

111. Why is `Campus2026!` a weak password?
     - A. It follows a recognizable pattern: word + year + symbol
     - B. It is too long
     - C. It has no letters
     - D. It contains a capital letter

112. NIST SP 800-63B-4: minimum length of a password used **within MFA**?
     - A. 4
     - B. 6
     - C. 8
     - D. 15

113. NIST SP 800-63B-4: minimum length for **password-only** sign-in?
     - A. 8
     - B. 10
     - C. 12
     - D. 15

114. What is the main job of a password manager?
     - A. Reuse one strong password everywhere
     - B. Generate and store a different random password for each login in a protected vault
     - C. Share passwords with friends
     - D. Remove the need for MFA

115. Which statement about a **salt** is correct?
     - A. It is stored with the hash and does not have to be secret
     - B. It must be kept secret
     - C. It makes hashing slower by itself
     - D. It is the same for every user

116. Where does the **slowness** in good password storage come from?
     - A. The salt
     - B. The password-hashing scheme, such as Argon2id
     - C. Fast SHA-256 alone
     - D. The username

117. Using fast SHA-256 alone for passwords:
     - A. Is best practice
     - B. Is unbreakable
     - C. Uses a lot of memory per guess
     - D. Allows rapid guesses, which the demo used to illustrate the weakness

118. The forum password leaks. You reused it on the LMS, but used a generated password for e-mail. Which accounts are at risk?
     - A. E-mail only
     - B. All three
     - C. The forum and the LMS
     - D. None

119. A fingerprint is which factor type?
     - A. Something you are
     - B. Something you know
     - C. Something you have
     - D. Something you do

120. A hardware security key is which factor type?
     - A. Something you know
     - B. Something you have
     - C. Something you are
     - D. Not a factor

121. A security key activated with its PIN is:
     - A. Know + know, not MFA
     - B. Have + have
     - C. Are + know
     - D. Have + know, so it is MFA

122. What is the risk of a **typed one-time code**?
     - A. A deceptive site may relay it to the real service
     - B. It cannot be typed on phones
     - C. It is always longer than 15 characters
     - D. It lasts forever

123. You get an unexpected MFA approval prompt. What should you do?
     - A. Approve it so the notifications stop
     - B. Deny it and investigate through the official service
     - C. Ignore it forever
     - D. Reply to the text message

124. Why do passkeys and FIDO keys resist phishing?
     - A. They are just longer passwords
     - B. They are sent by SMS
     - C. Their cryptographic proof binds authentication to the real service
     - D. They are stored in browser history

125. Password accepted, MFA still pending. What should the protected account page do?
     - A. Allow the request
     - B. Allow read-only access
     - C. Delete the account
     - D. Require the second factor

126. Access to your account looks wrong. What should you do?
     - A. Use the official service to change exposed credentials and revoke unfamiliar sessions
     - B. Click the link in the alert e-mail
     - C. Create a second account
     - D. Wait for the attacker to leave

127. Before an incident, what protects account recovery?
     - A. Sharing backup codes with friends
     - B. Protecting the recovery e-mail and storing backup codes securely
     - C. Disabling recovery completely
     - D. Writing backup codes on your screen

128. Which question should be asked for **every** request?
     - A. Is the password long?
     - B. Is the user friendly?
     - C. Does the policy allow this subject to perform this action on this resource?
     - D. Is the network fast?

129. "Roles grant ______. Scope limits ______."
     - A. actions; resources
     - B. resources; actions
     - C. passwords; sessions
     - D. logs; users

130. A student changes course grades. Which failure?
     - A. Horizontal
     - B. Vertical
     - C. Authentication
     - D. Not a failure

131. In the role table, what can a **disabled account** do?
     - A. Read its own grades
     - B. Edit one section
     - C. Nothing: no reading and no editing
     - D. Read all grades

132. PortSwigger lab: signed in as `wiener`, you change the user ID to `carlos` and see carlos's API key. Which failure?
     - A. Vertical
     - B. Phishing
     - C. Availability
     - D. Horizontal: the ownership of the requested resource was not checked

133. Join – Change – Leave: when a person leaves, what should happen?
     - A. Remove access and revoke applicable sessions
     - B. Keep the account in case they return
     - C. Give the account to a new person
     - D. Only change the password

134. Why is a **shared login** a problem?
     - A. It is too fast
     - B. It always requires MFA
     - C. The log shows the account, not which person used it, so accountability is harder
     - D. It uses a salt

135. Access log row: "10:03 mina.student — Read Joon's grade — **Allow**". What does it show?
     - A. Correct behaviour
     - B. A horizontal failure: it should have been denied
     - C. A vertical failure
     - D. An authentication failure

136. What can an access log **not** prove?
     - A. Which account acted
     - B. When it happened
     - C. What the system decided
     - D. That the person was really Mina

137. Row "10:04 mina.student — Edit Joon's grade — **Deny**" shows:
     - A. The vertical boundary held
     - B. A horizontal failure
     - C. An authentication failure
     - D. A broken log

### Week 5 — Malware and Endpoint Security

138. What is **malware**?
     - A. Any software bug
     - B. Software intentionally designed to cause harm
     - C. A hardware failure
     - D. A slow computer

139. A virus activates when:
     - A. An infected file or program is executed
     - B. The computer is turned off
     - C. The network cable is unplugged
     - D. A backup is restored

140. Sality is the slide example of a:
     - A. Virus
     - B. Worm
     - C. Bot
     - D. Spyware

141. Conficker is the slide example of a:
     - A. Trojan
     - B. Spyware
     - C. Virus
     - D. Worm

142. SocGholish (a fake browser update) is the slide example of a:
     - A. Trojan
     - B. Worm
     - C. Bot
     - D. Virus

143. What does a bot such as Neutrino Bot allow?
     - A. It encrypts files for ransom
     - B. An external operator to use the device for spam, fraud or attacks
     - C. It only records keystrokes
     - D. It spreads only by USB

144. Course files no longer open and a screen demands payment. Type?
     - A. Ransomware
     - B. Spyware
     - C. Bot
     - D. Worm

145. Paying the ransom:
     - A. Guarantees recovery
     - B. Is required by law
     - C. Removes the malware
     - D. Does not guarantee recovery

146. An infected program is shared on USB, and other executables become infected. Type?
     - A. Virus
     - B. Worm
     - C. Spyware
     - D. Bot

147. A device sends attack traffic whenever a remote operator says so. Type?
     - A. Worm
     - B. Virus
     - C. Trojan
     - D. Bot

148. A laptop is slow, but there is no scan, process or network evidence. Best conclusion?
     - A. Ransomware
     - B. Worm
     - C. Unknown, possibly not malware
     - D. Spyware

149. A fake update steals information and then downloads ransomware. Types involved?
     - A. Only a virus
     - B. Only a worm
     - C. Only a bot
     - D. Trojan + spyware + ransomware

150. Which statement is true?
     - A. A computer always shows a warning when infected
     - B. Only ransomware counts as malware
     - C. A computer can be infected with no warning window
     - D. Symptoms alone prove infection

151. Which evidence separates malware from an ordinary fault?
     - A. Screen brightness
     - B. Running processes, network connections, recent changes and scan results
     - C. Keyboard colour
     - D. Battery percentage

152. Why can an attachment from a **known contact** still be dangerous?
     - A. Known contacts never send malware
     - B. Attachments are always safe
     - C. The account may be compromised, the address spoofed, or the contact forwarding it unknowingly
     - D. Only ZIP files can be dangerous

153. Which control fits the **untrusted downloads** path?
     - A. Download from any site
     - B. Use approved sources; check the publisher and the update path
     - C. Disable antivirus
     - D. Use an administrator account

154. Which list describes **weak configuration**?
     - A. Using standard accounts
     - B. Applying patches quickly
     - C. Tested backups
     - D. Auto-run, exposed services, default credentials, disabled protections

155. What is the **supply chain** infection path?
     - A. Phishing e-mails
     - B. Legitimate updates or vendors are compromised
     - C. Found USB sticks
     - D. Weak passwords

156. Which control fits the supply-chain path?
     - A. Trusted signed sources; track dependencies and supplier notices
     - B. Disable all updates forever
     - C. Use pirated software
     - D. Use an administrator account

157. Which control fits **unpatched vulnerabilities**?
     - A. Wait until next year
     - B. Disable updates
     - C. Only patch printers
     - D. Prioritize internet-facing and critical systems; replace unsupported software

158. In the network-worm story, what is the **execution** stage?
     - A. The user opens an attachment
     - B. The user runs an installer
     - C. No user action: the worm exploits an unpatched service
     - D. The user plugs in a USB stick

159. Which is an example of **persistence**?
     - A. Opening the e-mail
     - B. A startup entry or scheduled task
     - C. Restoring a backup
     - D. Patching the system

160. Which statement about endpoint protection is correct?
     - A. It detects every threat
     - B. It replaces backups
     - C. It blocks known threats and flags suspicious files; alerts need investigation
     - D. It only works offline

161. What should **updates** cover?
     - A. Only the operating system
     - B. Only games
     - C. OS, browsers, applications, firmware and security tools, while tracking devices that cannot update
     - D. Only antivirus

162. "Defaults prioritize ______." Fill the gap.
     - A. security
     - B. convenience
     - C. privacy
     - D. logging

163. Backups should be:
     - A. Connected at all times
     - B. Protected, separated and tested
     - C. Shared publicly
     - D. Never tested, to save time

164. You suspect an infection. What should you do?
     - A. Keep experimenting on the device
     - B. Reinstall everything without telling anyone
     - C. Stop sensitive work, avoid unnecessary changes, report quickly
     - D. Ignore it

165. Why "follow guidance before disconnecting critical systems"?
     - A. Disconnecting is illegal
     - B. It breaks the whole Internet
     - C. Antivirus needs the Internet
     - D. Staff may need to preserve evidence

166. Which sequence describes **trusted-state recovery**?
     - A. Restore files only
     - B. Pay the ransom
     - C. Reinstall games
     - D. Clean system → weakness fixed → credentials safe → data restored → monitored afterwards

167. Why is antivirus not enough?
     - A. No tool detects every threat; protection also depends on configuration, updates, privilege, backups and users
     - B. Antivirus is illegal
     - C. Antivirus always slows computers to a stop
     - D. Antivirus only works on servers

168. Library computer activity: which accounts should be reset first, and how?
     - A. Accounts used last year, from the same computer
     - B. None
     - C. Accounts used after the fake update was installed, starting with e-mail, from a different trusted device
     - D. All accounts, from the infected computer

169. What is the **first** of the six questions before recommending anything?
     - A. Recovery evidence
     - B. Safe first action
     - C. Affected data
     - D. Symptom

### Week 6 — Networking Fundamentals for Security

170. What is a **network**?
     - A. Devices connected so they can exchange data
     - B. A single computer
     - C. A type of malware
     - D. A password policy

171. Which is a **LAN**?
     - A. A university linking two cities
     - B. Computers and a printer in one lab
     - C. The whole Internet
     - D. A cloud provider's data centers worldwide

172. What is a **WAN**?
     - A. One room's network
     - B. A printer cable
     - C. A network that links networks over larger distances
     - D. A single laptop

173. What is the **Internet**?
     - A. One LAN
     - B. One switch
     - C. One router
     - D. Many connected networks worldwide

174. Which is correct?
     - A. A client starts a request; a server provides a service
     - B. A server always starts the request
     - C. Clients and servers are the same thing
     - D. Only routers are clients

175. What is an **endpoint**?
     - A. A switch
     - B. A cable
     - C. A device at an end of a communication
     - D. A DNS record

176. A switch learns which addresses?
     - A. IP addresses
     - B. MAC addresses
     - C. Domain names
     - D. Port numbers

177. What does an **access point** do?
     - A. Routes between networks
     - B. Translates names to addresses
     - C. Encrypts the disk
     - D. Lets wireless devices join a network

178. What is the **default gateway**?
     - A. The next router used to reach other networks
     - B. The DNS server
     - C. The printer
     - D. The LMS server

179. A home "Wi-Fi router" is usually:
     - A. Only a switch
     - B. Only an access point
     - C. Router + access point + switch in one box
     - D. Only a modem

180. The week 6 path is: Laptop → A → B → D (router/firewall) → C (Internet routers) → LMS server. What is **B**?
     - A. Router
     - B. Switch
     - C. Internet routers
     - D. DNS resolver

181. Wi-Fi connects you to:
     - A. A network, which is not necessarily the Internet
     - B. Always the Internet
     - C. Only the LMS
     - D. Only a printer

182. What is a security concern for a **switch**?
     - A. Fan noise
     - B. Port colour
     - C. Too many lights
     - D. An unused cable socket can be an entry point

183. What is the main concern for a **router**, and its control?
     - A. It is too heavy; mount it on a wall
     - B. An attacker can change its settings; use protected admin access and updates
     - C. It learns MAC addresses; turn it off
     - D. It has no concern

184. An unauthorized device joins through Wi-Fi or a cable socket. Which control fits?
     - A. Antivirus
     - B. DNS
     - C. Network access control
     - D. HTTPS

185. From the network side, how do you reduce WannaCry-style spread?
     - A. Install the fix and restrict unnecessary SMB traffic
     - B. Use a longer Wi-Fi name
     - C. Turn off DNS
     - D. Use HTTP instead of HTTPS

186. Laptop 192.168.10.24, LMS 198.51.100.20, public address 203.0.113.5. Which address is the **default gateway** in the classroom example?
     - A. 198.51.100.20
     - B. 192.168.10.24
     - C. 203.0.113.5
     - D. 192.168.10.1

187. A **port** answers which question?
     - A. Where is it?
     - B. Which service?
     - C. Which rules?
     - D. What address matches the name?

188. A **protocol** answers which question?
     - A. Where is it?
     - B. Which service?
     - C. Which rules?
     - D. What address matches the name?

189. What does **TCP** do?
     - A. Delivers data reliably and in order
     - B. Translates names to addresses
     - C. Defines web pages
     - D. Encrypts content

190. What does **TLS** do?
     - A. Delivers packets between networks
     - B. Defines web requests
     - C. Finds the IP address of a name
     - D. Protects a connection's data with encryption and certificate checks

191. What does **HTTP** do?
     - A. Encrypts connections
     - B. Defines web requests and responses
     - C. Delivers packets between networks
     - D. Learns MAC addresses

192. What does **IP** do?
     - A. Defines web pages
     - B. Provides encryption
     - C. Delivers packets between networks
     - D. Translates names

193. HTTPS is:
     - A. HTTP protected by TLS
     - B. A faster version of DNS
     - C. A firewall
     - D. A type of switch

194. What is a **certificate**?
     - A. A password
     - B. A firewall rule
     - C. An IP address
     - D. Digital evidence used to check the server's identity

195. In `https://lms.example.com/course/6`, the part `/course/6` is the:
     - A. Domain name
     - B. Protocol
     - C. Path to a resource
     - D. Port

196. Which port is used for HTTPS when none is written?
     - A. 80
     - B. 443
     - C. 22
     - D. 21

197. Can malware on your own device read data even when you use HTTPS?
     - A. Yes; endpoint security still matters
     - B. No, never
     - C. Only on Wi-Fi
     - D. Only with IPv6

198. Does HTTPS hide IP addresses and traffic timing?
     - A. Yes, always
     - B. Only on Wi-Fi
     - C. Only with DNS
     - D. No, they may remain visible

199. In browser DevTools, one row in the Network tab is:
     - A. One packet
     - B. A firewall rule
     - C. A resource request
     - D. A MAC address

200. A useful explanation of a network risk names:
     - A. The location, the weakness and the control
     - B. The attacker's name only
     - C. The colour of the cable
     - D. Only the protocol

201. "Excessive access": the request is encrypted, but the user gets more than they should. What fixes it?
     - A. TLS
     - B. Authentication and authorization
     - C. DNS
     - D. A faster switch

202. What is an **on-path attacker**?
     - A. A fake USB stick
     - B. A weak password
     - C. Ransomware
     - D. Someone positioned to intercept or influence traffic

203. "Too much exposure" on a public web server. Which firewall approach fits?
     - A. Allow everything
     - B. Deny 443
     - C. Allow 443 to the public, deny public SSH (22), allow an approved admin path
     - D. Allow public SSH from anywhere

204. What is a **firewall**?
     - A. Software or hardware that allows or blocks traffic using rules
     - B. A backup system
     - C. A DNS resolver
     - D. A password manager

205. The office printer's firmware is old. What should you do?
     - A. Ignore it
     - B. Move it to the guest network
     - C. Make it reachable from the Internet
     - D. Update it, or restrict it until it is replaced

206. Five locations: Device → Access → Boundary → Data in transit → Server. Which control belongs to **Boundary**?
     - A. TLS
     - B. Firewall rules
     - C. Server permissions
     - D. Endpoint protection

207. Which control belongs to **Data in transit**?
     - A. TLS
     - B. Firewall rules
     - C. Authenticated Wi-Fi
     - D. Updates

208. A café certificate warning could come from where?
     - A. Only the website
     - B. Only the browser theme
     - C. The device (wrong clock, malware), the network (fake hotspot) or the website (expired or wrong certificate)
     - D. Only the printer

<div class="pb"></div>

## Part B — True / False

Write **T** or **F**. If false, correct the statement.

1. Integrity and availability can fail by accident, with no attacker.
2. "Reachable" means "allowed".
3. A threat must be a person with bad intentions.
4. A backup you have never restored from is an assumption.
5. A verified patch mainly reduces impact.
6. A risk score of 5 is possible in the 3 × 3 matrix.
7. Password + security question counts as MFA.
8. HTTPS proves that a website is honest.
9. One phishing attack can carry several labels at the same time.
10. Smishing is phishing by voice call.
11. A hostname is read from the right.
12. Shame helps people report incidents faster.
13. If money was already sent after a voice-phishing call in Korea, call 112 and the bank.
14. Authentication proves that the real owner typed the password.
15. Credential stuffing works only when the password was reused.
16. Login MFA prevents offline hash testing.
17. A salt must be kept secret.
18. Argon2id makes each guess cost configured time and memory.
19. A four-digit PIN has 10,000 possible values.
20. Showing a verification screen is enough to enforce MFA.
21. A horizontal failure means performing a more privileged action.
22. Least privilege gives each account only the access its assignment needs.
23. A shared login makes individual accountability easier.
24. An access log proves which person used an account.
25. A virus spreads across networks without any user action.
26. WannaCry was ransomware that also spread as a worm.
27. A computer always shows a warning window when it is infected.
28. Paying the ransom guarantees recovery.
29. A connected backup may also be encrypted by ransomware.
30. Restoring files alone always returns a system to a trusted state.
31. Default settings usually prioritize security over convenience.
32. Antivirus detects every threat.
33. A switch forwards IP packets between networks.
34. If the Internet fails, a printer on the same local switch can still print.
35. An IP address identifies a network interface, not a person.
36. Port 443 is SSH.
37. HTTPS hides IP addresses and traffic timing.
38. DNS spoofing automatically defeats TLS.
39. An SSID proves only the advertised network name.
40. Segmentation limits an incident's spread.
41. Social engineering hacks computer code.
42. In social engineering, the requested action is what causes harm, not the story.
43. Tailgating means following an authorized person into a restricted area.
44. Recognition is the same as authorization.
45. In risk assessment, an assumption is a statement supported by evidence.
46. In the Uber case, the attacker already had the password before the prompts.
47. Cloudflare staff never entered their details on the fake site.
48. Technology alone is enough if passwords are strong.
49. NAT lets many private addresses share one public address.
50. A firewall allows or blocks traffic using rules.

## Part C — Quick Classification Drills

### C1. Which CIA goal failed? (write C, I or A)

1. Someone reads a classmate's private messages.
2. The exam website crashes under a flood of traffic.
3. An attacker changes the prices in an online shop.
4. Ransomware encrypts files so nobody can use them.
5. An unencrypted laptop with patient records is stolen.
6. A software bug saves wrong values into the database.
7. A power outage stops the LMS.
8. A private file link is shared publicly.
9. An old version of an assignment is uploaded instead of the final one.
10. Someone shoulder-surfs your PIN at an ATM.
11. A hardware failure takes the e-mail server down for a day.
12. Someone sends messages as you from your account.
13. A bad update stops computers from starting.
14. Grades are leaked online.
15. A storage fault corrupts a file.

### C2. Name the malware type

1. Spreads to every unpatched computer on the network with no clicks.
2. Hidden inside a cracked copy of paid software.
3. Quietly records screenshots and passwords.
4. Locks files and shows a payment note.
5. Infects other executables when an infected program runs.
6. The device secretly joins a group that sends spam on command.
7. A fake browser update.
8. A keylogger.
9. Conficker.
10. Neutrino.

### C3. Name the phishing label(s)

1. Mass e-mail: "Your mailbox is full, log in here."
2. Phone call claiming to be the police, asking for a transfer.
3. Text message: "Your parcel is held, pay the fee here."
4. E-mail to the finance team using the CFO's name and the current project.
5. A fake profile of your friend asking for money.
6. SMS pretending to be university IT, quoting your student ID.
7. A call claiming to be your bank, asking for the OTP.
8. A generic "You won a prize" e-mail.

### C4. Risk score and level

1. L 1, I 1
2. L 1, I 2
3. L 2, I 2
4. L 3, I 2
5. L 3, I 3
6. L 2, I 1
7. L 1, I 3
8. L 3, I 1
9. L 2, I 3
10. Internet-facing exam server, flaw already being exploited elsewhere, essential exam next week, no tested backup.

### C5. Prevent, Detect or Recover?

1. Applying a patch
2. Reviewing sign-in logs
3. Restoring from a backup
4. Requiring MFA
5. An endpoint-protection alert
6. A firewall deny rule
7. Rebuilding a clean system
8. Monitoring repeated MFA prompts
9. Using standard user accounts
10. Resetting passwords and revoking sessions after a compromise

### C6. Horizontal or vertical access failure?

1. A student views another student's grade.
2. A student edits course grades.
3. A TA for section A edits grades in section B.
4. A normal user opens the admin panel and deletes users.
5. A user changes the ID in the request and sees another user's API key.
6. A student approves their own scholarship as if they were staff.

## Part D — Short Answer

1. Define computer security and show how its three parts map to C, I and A.
2. Using Equifax 2017, explain the difference between threat, vulnerability, exploit and control.
3. Explain why integrity can fail without an attacker. Give two examples.
4. Explain "reachable does not mean allowed". Name the five things authorized practice has.
5. Explain prevent, detect and recover with one example of each.
6. Why must a restore be tested? Use the GitLab case.
7. Compare Uber (Sep 2022) and Cloudflare (2022). Why did one fail and the other hold?
8. Write the four-sentence risk answer for the week 2 assignment (public exam system, unfixed flaw, untested backup, exam in 30 days).
9. Explain pretext versus requested action with your own example.
10. Name the six levers of social engineering and give one sentence that shows each.
11. Why can one attack have several phishing labels? Give an example.
12. Explain the U + P + S warning pattern.
13. What should you do if you entered your password on a phishing page?
14. Explain identification, authentication and authorization using Mina.
15. Explain online versus offline guessing and which defenses apply to each.
16. Explain what a salt does and what Argon2id adds.
17. Why is "password + security question" not MFA?
18. Explain horizontal and vertical access failures with one example each.
19. Read the access log (10:01 sign-in success; 10:02 read Mina's grade allow; 10:03 read Joon's grade allow; 10:04 edit Joon's grade deny). Which row conflicts with the policy, and what can the log prove?
20. Explain the difference between a virus and a worm.
21. Write an infection story for a fake software update, with one control placed at each stage.
22. Why is a connected backup not enough against ransomware?
23. Trace a print job and an LMS request on the classroom network. What happens if the Internet fails?
24. Give four things HTTPS does and does not protect.
25. A small office has three risks: guests can reach staff systems, administration is public, printer firmware is old. Give a control for each and why it helps.
26. What is an evil twin, and how should you respond?

<div class="pb"></div>

## Answer Key

<div class="key">

### Part A

**Week 1:** **1** B · **2** A · **3** C · **4** D · **5** B · **6** C · **7** A · **8** C · **9** D · **10** A · **11** B · **12** C · **13** D · **14** A · **15** C · **16** B · **17** D · **18** A · **19** C · **20** B · **21** A · **22** C · **23** B · **24** C · **25** D

**Week 2:** **26** A · **27** B · **28** C · **29** D · **30** A · **31** B · **32** D · **33** C · **34** A · **35** D · **36** B · **37** C · **38** B · **39** A · **40** C · **41** D · **42** B · **43** A · **44** C · **45** B · **46** A · **47** D · **48** C · **49** A · **50** B · **51** C · **52** D · **53** A · **54** C · **55** B · **56** D · **57** A · **58** B · **59** C · **60** A

**Week 3:** **61** B · **62** A · **63** C · **64** D · **65** C · **66** A · **67** C · **68** D · **69** B · **70** B · **71** C · **72** D · **73** D · **74** A · **75** A · **76** D · **77** C · **78** B · **79** B · **80** D · **81** B · **82** A · **83** C · **84** B · **85** D · **86** B · **87** C · **88** B · **89** C · **90** A · **91** C · **92** A

**Week 4:** **93** C · **94** A · **95** D · **96** B · **97** A · **98** C · **99** D · **100** B · **101** A · **102** C · **103** B · **104** C · **105** D · **106** A · **107** B · **108** D · **109** A · **110** C · **111** A · **112** C · **113** D · **114** B · **115** A · **116** B · **117** D · **118** C · **119** A · **120** B · **121** D · **122** A · **123** B · **124** C · **125** D · **126** A · **127** B · **128** C · **129** A · **130** B · **131** C · **132** D · **133** A · **134** C · **135** B · **136** D · **137** A

**Week 5:** **138** B · **139** A · **140** A · **141** D · **142** A · **143** B · **144** A · **145** D · **146** A · **147** D · **148** C · **149** D · **150** C · **151** B · **152** C · **153** B · **154** D · **155** B · **156** A · **157** D · **158** C · **159** B · **160** C · **161** C · **162** B · **163** B · **164** C · **165** D · **166** D · **167** A · **168** C · **169** D

**Week 6:** **170** A · **171** B · **172** C · **173** D · **174** A · **175** C · **176** B · **177** D · **178** A · **179** C · **180** B · **181** A · **182** D · **183** B · **184** C · **185** A · **186** D · **187** B · **188** C · **189** A · **190** D · **191** B · **192** C · **193** A · **194** D · **195** C · **196** B · **197** A · **198** D · **199** C · **200** A · **201** B · **202** D · **203** C · **204** A · **205** D · **206** B · **207** A · **208** C

### Part B — True / False

| # | | Correction / reason |
|---|---|---|
| 1 | T | Editing the wrong row, bugs, power failure. |
| 2 | F | Permission (owner, scope, time, method, purpose) defines what is allowed. |
| 3 | F | Threats can be accidental (GitLab) or physical (Kakao fire). |
| 4 | T | Only a tested restore proves it. |
| 5 | F | A patch reduces **likelihood**; a tested restore reduces impact. |
| 6 | F | 5 cannot be made from 1–3 × 1–3. |
| 7 | F | Know + know is one factor type. |
| 8 | F | A phishing site can also use HTTPS. |
| 9 | T | Each label describes a different feature (channel, targeting, claimed identity). |
| 10 | F | Smishing = text/SMS. Vishing = voice. |
| 11 | T | `campus.example.verify-now.test` belongs to `verify-now.test`. |
| 12 | F | Shame makes people hide information and delay help. |
| 13 | T | Request payment suspension urgently. |
| 14 | F | It only shows the proof matched the account. |
| 15 | T | It reuses a pair leaked from another site. |
| 16 | F | Offline guesses run against a copied hash, not the login. |
| 17 | F | A salt is stored with the hash and need not be secret. |
| 18 | T | That is the job of a password-hashing scheme. |
| 19 | T | 0000 to 9999. |
| 20 | F | The protected route itself must refuse access until MFA is complete. |
| 21 | F | That is **vertical**. Horizontal = another user's resource at the same level. |
| 22 | T | |
| 23 | F | It makes accountability **harder**. |
| 24 | F | It proves which **account**; the password may have been stolen. |
| 25 | F | That describes a **worm**; a virus needs a user to run an infected file. |
| 26 | T | It spread through vulnerable SMB. |
| 27 | F | Malware often hides; only ransomware wants to be seen. |
| 28 | F | Payment does not guarantee recovery. |
| 29 | T | Backups must be protected and separated. |
| 30 | F | Restoring files may restore the weakness; fix the cause. |
| 31 | F | Defaults prioritize **convenience**. |
| 32 | F | No tool detects every threat (defense in depth). |
| 33 | F | A **router** does; a switch forwards frames inside a LAN. |
| 34 | T | The print job stays local. |
| 35 | T | It does not prove identity. |
| 36 | F | 443 = HTTPS; 22 = SSH. |
| 37 | F | IP addresses and timing may remain visible. |
| 38 | F | The fake server still needs a valid certificate for that name. |
| 39 | T | Anyone can advertise the same name (evil twin). |
| 40 | T | It limits unnecessary paths. |
| 41 | F | It hacks the human factor. |
| 42 | T | Judge the action, not the story. |
| 43 | T | |
| 44 | F | Recognition ≠ authorization (Hong Kong deepfake). |
| 45 | F | A **fact** is supported by evidence; an assumption is accepted for the exercise. |
| 46 | T | MFA fatigue starts after the password is already known. |
| 47 | F | They did enter details; origin-bound keys blocked the login. |
| 48 | F | People can still give passwords away. |
| 49 | T | |
| 50 | T | |

### Part C

**C1:** 1 C · 2 A · 3 I · 4 A · 5 C · 6 I · 7 A · 8 C · 9 I · 10 C · 11 A · 12 I · 13 A · 14 C · 15 I (and as a result A)

**C2:** 1 Worm · 2 Trojan · 3 Spyware · 4 Ransomware · 5 Virus · 6 Bot · 7 Trojan · 8 Spyware · 9 Worm · 10 Bot

**C3:** 1 Broad phishing · 2 Vishing + impersonation · 3 Smishing · 4 Spear phishing + impersonation · 5 Impersonation · 6 Smishing + spear phishing + impersonation · 7 Vishing + impersonation · 8 Broad phishing (reward lever)

**C4:** 1 = 1 Low · 2 = 2 Low · 3 = 4 Medium · 4 = 6 High · 5 = 9 High · 6 = 2 Low · 7 = 3 Medium · 8 = 3 Medium · 9 = 6 High · 10 = L 3 × I 3 = 9 High

**C5:** 1 P · 2 D · 3 R · 4 P · 5 D · 6 P · 7 R · 8 D · 9 P · 10 R

**C6:** 1 Horizontal · 2 Vertical · 3 Horizontal (same role, resource outside its scope) · 4 Vertical · 5 Horizontal · 6 Vertical

### Part D — Model answers

1. Computer security is the ideas, practices and controls that reduce **unauthorized access** (confidentiality), **unwanted change** (integrity) and **harmful disruption** (availability).
2. The **threat** was the attackers; the **vulnerability** was the unfixed software flaw; the **exploit** was using that flaw to get in; the **control** was a verified patch. Vulnerability = the flaw, exploit = its use.
3. Integrity means data is correct and trustworthy, and that can break without anyone attacking. Examples: editing the wrong row of a grade sheet; a software bug or corrupted storage. It is still a security problem because the data can no longer be trusted.
4. Being able to reach a system is not permission to test it. Authorized practice has a clear **owner, scope, time, method and purpose**. The same scan can be ethical on a provided lab machine and unethical on a real university server; if the scope is unclear, stop and ask.
5. **Prevent**: patch a known flaw or require MFA. **Detect**: check records of unusual access. **Recover**: restore from a tested backup.
6. GitLab found its backups did not work when it needed them after data was deleted by mistake. A backup you never restored from is only an assumption, so the restore must be tested before an incident.
7. Uber: the attacker had the password and sent repeated prompts; a tired contractor approved one, so the control depended on a person's judgment under pressure. Cloudflare: staff typed details on a fake site, but **origin-bound security keys** checked which site was asking and refused, so the stolen details were not enough.
8. *The asset is the public exam system; it matters because students need it to take the exam in 30 days. The threat could use the unfixed flaw, which is the weakness. Likelihood is 3 (likely) and impact is 3 (severe) because it is public and the backup is untested, so 9 = High. Our controls are to patch and verify (reduces likelihood) and to test the restore (reduces impact).*
9. The **pretext** is the invented story ("your scholarship payment failed"); the **requested action** is what the attacker wants ("confirm your password here"). The story can be believable; the action causes the harm, so judge the action.
10. Authority ("I am from the court"), fear ("your account is involved in a crime"), urgency ("you have ten minutes"), familiarity ("it's me, I changed my number"), reward ("you won a tuition grant"), curiosity ("someone posted your photo"). Secrecy is an extra lever.
11. Each label describes a different feature: deception (phishing), targeting (spear), channel (smishing, vishing) and claimed identity (impersonation). An SMS using your project name and a fake tutor identity is smishing + spear phishing + impersonation.
12. **Unexpected** contact, **pressure** (deadline, threat, secrecy) and a **sensitive action** (credentials, money, device access). One sign alone may be innocent; all three together is the pattern to stop on.
13. Reset the password and end active sessions through the official service (a route you choose), then contact the university IT office. Check MFA and recovery settings afterwards.
14. **Identification** = Mina claims an account ("mina.student"). **Authentication** = proof for that account (password, MFA). **Authorization** = permission for the requested action (reading her own grade yes; editing grades no).
15. **Online**: guesses go to the login service; attempt limits, monitoring and MFA help. **Offline**: guesses run against a copied hash on the attacker's device; server limits and login MFA do not help, so a slow hashing scheme (Argon2id) with salts and long unique passwords matter.
16. A unique random **salt** makes identical passwords produce different hashes, so one hash cannot be reused across accounts; it is stored with the hash and is not secret. **Argon2id** makes every guess cost configured time and memory, which slows offline guessing.
17. Both are **something you know**. MFA needs different factor types (know, have, are), not just two screens.
18. **Horizontal**: access to another user's resource at the same level (Mina reads Joon's grade). **Vertical**: a more privileged action (a student edits course grades).
19. Row **10:03** conflicts: a student may read only their own record, so it should have been denied (horizontal failure). Row 10:04 correctly denied the vertical action. The log proves which account did what, when, and the decision; it does not prove the person was Mina.
20. A **virus** activates when an infected file or program is run and copies itself into other content, so it needs a user action. A **worm** spreads by itself across networks to reachable, unpatched systems with no user action.
21. **Initial contact:** user downloads a "free update" (control: approved sources). **Execution:** user runs the installer (control: restrict installation). **Privilege:** it runs as admin (control: standard accounts). **Persistence:** auto-start entry (control: endpoint protection, monitor configuration). **Impact:** steals data / encrypts files (control: protected, separated backups). **Recovery:** trusted state: clean, fix cause, reset credentials, restore, monitor.
22. Ransomware can reach and encrypt anything the infected device can reach, including a connected backup. Backups must be protected, separated and tested.
23. Print job: laptop → AP → switch → printer (stays local). LMS request: laptop → AP → switch → router/firewall → Internet routers → server. If the Internet fails, printing still works but the LMS does not.
24. **Protects**: page content from nearby observers in transit (when TLS works). **Does not**: prove a site is honest (phishing can use HTTPS); stop malware on your own device; hide IP addresses and traffic timing.
25. Guests reach staff systems → separate guest access and traffic rules (segmentation), limits access to private services. Public admin → allow only an approved admin path, reduces exposure. Old printer firmware → update it or restrict it until replaced, reduces exploitable weaknesses.
26. An **evil twin** is a fake access point using a trusted Wi-Fi name; an SSID proves only the advertised name. Verify the network, follow the approved setup and stop at certificate warnings.

</div>

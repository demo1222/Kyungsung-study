# Computer Security — Practice Midterm Test

**MAIN TEST** · Multiple choice · Weeks 1–6 · 60 questions × 1 mark = 60 marks · Suggested time: 60 minutes

<div class="box"><b>Name:</b> ______________________________ &nbsp;&nbsp;&nbsp; <b>Student ID:</b> ____________________ &nbsp;&nbsp;&nbsp; <b>Score:</b> ______ / 60</div>

> **Instructions.** Choose the **one best** answer for each question and circle the letter. The questions follow the lecture order (week 1 → week 6). The answer key with a one-line reason for every question is on the last pages. Try the whole test before you look.

## Week 1 — Introduction to Computer Security

1. Which statement best matches the course definition of **computer security**?
     - A. Software that removes viruses from a computer
     - B. Ideas, practices and controls that reduce unauthorized access, unwanted change and harmful disruption
     - C. Encrypting every file stored on a device
     - D. Rules that stop people from using the Internet

2. A student's grades are accidentally posted on a public notice board. Which security goal failed?
     - A. Integrity
     - B. Availability
     - C. Confidentiality
     - D. Authorization

3. A staff member edits the wrong row in a spreadsheet and replaces correct grades with wrong ones. No attacker was involved. Which statement is correct?
     - A. It is an integrity failure, even though it was an accident
     - B. It is not a security problem because there was no attacker
     - C. It is only a confidentiality failure
     - D. It is only an availability failure

4. In Mina's university-account case, a **reused password** is an example of which of the five words?
     - A. Asset
     - B. Threat
     - C. Control
     - D. Vulnerability

5. Which activity is **authorized** (ethical) practice?
     - A. Scanning a university server because it is reachable from the dorm network
     - B. Scanning an instructor-provided lab machine during the scheduled exercise, using approved steps, and reporting findings privately
     - C. Logging into a friend's account with their old password to prove it is weak
     - D. Posting a discovered weakness on social media to warn other students

6. What does **defense in depth** mean?
     - A. Buying the strongest firewall available and relying on it
     - B. Hiding the network so attackers cannot find it
     - C. Using several layers of protection, because any single control can fail
     - D. Training users instead of using technology

7. What is the correct safe response to a suspicious message?
     - A. Click, check, report
     - B. Report, pause, check
     - C. Check, reply, report
     - D. Pause, check, report

## Week 2 — Assets, Threats and Risk

8. Two identical computers cost the same. One shows public notices; the other supports urgent hospital care. What does this show?
     - A. Value comes from what the asset does, not from what it costs
     - B. Both computers have exactly the same value
     - C. The cheaper-looking computer is always less valuable
     - D. Computers are not assets; only information is

9. In the Facebook outage (4 October 2021) the computers were fine, but a network setting change made services fail. Which asset question does this illustrate?
     - A. Value
     - B. Dependency
     - C. Confidentiality
     - D. Exploit

10. In the Equifax 2017 case, the **unfixed software flaw** is the ______ and **using the flaw to get in** is the ______.
     - A. threat; control
     - B. exploit; vulnerability
     - C. vulnerability; exploit
     - D. control; threat

11. In GitLab 2017, database data was deleted by mistake. What kind of threat is this?
     - A. Malicious
     - B. Physical
     - C. Social engineering
     - D. Accidental

12. Which case is the course's example of a **physical** threat?
     - A. Kakao data-center fire, 2022
     - B. WannaCry, 2017
     - C. GitLab database deletion, 2017
     - D. Uber MFA fatigue, 2022

13. What is the main lesson of GitLab 2017 about backups?
     - A. Backups are unnecessary if staff are careful
     - B. Recovery must be tested; a backup you never restored from is an assumption
     - C. Backups should stay connected to the main system at all times
     - D. Backups prevent every integrity failure

14. Which statement describes a **risk**, not an incident?
     - A. Ransomware encrypted the lab computers last night
     - B. A student account was used to send spam yesterday
     - C. The exam system has an unfixed flaw that could be used before next month's exam
     - D. Staff entered their passwords on a fake site this morning

15. Likelihood = 2 (Possible) and Impact = 3 (Severe). What are the score and level?
     - A. 5, Medium
     - B. 6, High
     - C. 6, Medium
     - D. 9, High

16. Which score can **never** appear in the 3 × 3 risk matrix?
     - A. 4
     - B. 6
     - C. 9
     - D. 5

17. A tested restore mainly reduces which part of risk?
     - A. Impact
     - B. Likelihood
     - C. The number of attackers
     - D. The value of the asset

18. Staff at Cloudflare (2022) entered their details on a fake site, but the attacker still could not log in. Why?
     - A. Staff never actually typed their details
     - B. The company used SMS codes
     - C. Origin-bound security keys checked which website was asking
     - D. A firewall blocked the phishing e-mail

19. Which sign-in combination is real **MFA**?
     - A. Password + security question
     - B. PIN + password
     - C. Two different passwords on two screens
     - D. Password + authenticator-app code

## Week 3 — Social Engineering and Phishing

20. Social engineering mainly attacks:
     - A. The human factor: attention, emotion, habits and working situation
     - B. Bugs in operating-system code
     - C. Weak Wi-Fi encryption
     - D. Hardware failures

21. "Your scholarship payment failed" is the ______; "send me your password" is the ______.
     - A. requested action; pretext
     - B. pretext; requested action
     - C. lever; exploit
     - D. threat; control

22. "I am calling from the court. You have ten minutes to respond." Which two levers are used?
     - A. Reward and curiosity
     - B. Familiarity and secrecy
     - C. Authority and urgency
     - D. Fear and reward

23. A visitor asks you to hold a secure door so they can follow you into a restricted area. This is:
     - A. Baiting
     - B. Vishing
     - C. Smishing
     - D. Tailgating

24. An SMS uses your project name, claims to be your tutor and asks you to sign in through a link. Which labels fit best?
     - A. Smishing + spear phishing + impersonation
     - B. Vishing only
     - C. Broad phishing only
     - D. Baiting + tailgating

25. In the Uber MFA-fatigue case, what changed between the rejected prompts and the one that was accepted?
     - A. The request became more legitimate
     - B. The person's state: tired and under pressure
     - C. The attacker obtained a hardware security key
     - D. MFA was switched off by the company

26. What is the main lesson of the Hong Kong deepfake meeting (reported 2024)?
     - A. Video calls are always safe
     - B. Only e-mails can be faked
     - C. Recognition is not authorization
     - D. HTTPS prevents deepfakes

27. Which URL really belongs to `campus.example`?
     - A. `https://campus.example.verify-now.test/login`
     - B. `https://login-campus.example.net/login`
     - C. `https://campus-example.com/login`
     - D. `https://login.campus.example/student`

28. Why is the HTTPS padlock weak evidence that a website is legitimate?
     - A. A phishing site can also use HTTPS
     - B. HTTPS is not a form of encryption
     - C. Only government websites can use HTTPS
     - D. The padlock means the site contains malware

29. In South Korea, you already **sent money** after a fake "daughter had an accident" call. What should you do first?
     - A. Contact 118 (KISA) only
     - B. Call 112 and your bank's official contact to request payment suspension
     - C. E-mail the university IT office
     - D. Call the scammer back to ask for a refund

30. You received a suspicious SMS asking you to install an app. Which Korean route gives technical advice about the message or app?
     - A. 112
     - B. The university library
     - C. 118 (KISA)
     - D. The phone number given in the SMS

## Week 4 — Identity, Authentication and Access Control

31. Mina types the username `mina.student`. Which step is this?
     - A. Authorization
     - B. Authentication
     - C. Accounting
     - D. Identification

32. A stranger signs in with Mina's stolen password. Which security check accepted the stranger?
     - A. Authentication
     - B. Authorization
     - C. Segmentation
     - D. Firewall filtering

33. What is **credential stuffing**?
     - A. Trying likely passwords such as `123456`
     - B. Reusing a username and password pair that leaked from another site
     - C. Phishing someone by voice call
     - D. Writing passwords on sticky notes

34. Why can login rate limits **fail** to stop offline guessing?
     - A. Rate limits only apply to administrator accounts
     - B. Offline guessing uses MFA codes instead of passwords
     - C. The guesses are tested against a copied hash on the attacker's own device
     - D. Password hashes can be decrypted instantly

35. In the CyberChef activity, the candidate `campus123` produced the target SHA-256 value. What happened?
     - A. The hash was decrypted
     - B. The salt revealed the password
     - C. SHA-256 is reversible
     - D. Hashing the guessed word produced the same hash: the guess matched

36. What is the purpose of a unique random **salt** for each password?
     - A. Identical passwords do not produce the same stored hash
     - B. It keeps the password secret, so the salt must also be secret
     - C. It makes hashing faster
     - D. It replaces the need for MFA

37. Which password best follows NIST SP 800-63B-4 for **password-only** sign-in?
     - A. `Campus2026!`
     - B. `P@ssw0rd1`
     - C. A randomly generated 20-character password stored in a password manager
     - D. An 8-character password with one symbol

38. Mina (a student) can read Joon's grade record. Which access failure is this?
     - A. Vertical
     - B. Horizontal
     - C. Authentication
     - D. Availability

39. Under **least privilege**, a TA assigned to grade section A should:
     - A. Edit grades for section A only, with no access to section B
     - B. Edit grades for every section in the course
     - C. Only read grades, never edit them
     - D. Have the same access as the lecturer

40. In the PortSwigger "2FA simple bypass" lab, the account page opened without a verification code. What failed?
     - A. The password was too short
     - B. The SMS provider was offline
     - C. The user approved a push prompt
     - D. The application did not check that MFA was completed before serving the protected page

## Week 5 — Malware and Endpoint Security

41. Malware is identified mainly by:
     - A. Its file name
     - B. Its purpose and actions
     - C. Symptoms alone, such as a slow laptop
     - D. Its file size

42. Several unpatched computers become infected without any user opening a file. Most likely type?
     - A. Virus
     - B. Trojan
     - C. Worm
     - D. Spyware

43. A "free game" installs a hidden remote-control program. Most likely type?
     - A. Trojan
     - B. Worm
     - C. Ransomware
     - D. Bot

44. A program secretly records everything a student types. Most likely type?
     - A. Bot
     - B. Ransomware
     - C. Virus
     - D. Spyware (keylogger)

45. Why may a **connected** backup fail to protect you from ransomware?
     - A. Connected backups are slower
     - B. The ransomware can encrypt the connected backup too
     - C. Backups are not allowed on university computers
     - D. Backups only protect confidentiality

46. After an infection is cleaned, what can happen if you **only** restore the files?
     - A. The system is guaranteed to be in a trusted state
     - B. You no longer need to change any passwords
     - C. You may restore the original weakness if the cause was not fixed
     - D. All backups are deleted automatically

47. Which control best reduces the **excess privilege** infection path?
     - A. Using standard (non-administrator) accounts for daily work
     - B. Turning off the screen lock
     - C. Using the same password everywhere
     - D. Allowing auto-run for USB devices

48. What is the correct order of the infection story used in week 5?
     - A. Execution → Initial contact → Impact → Privilege → Persistence → Recovery
     - B. Impact → Execution → Recovery → Initial contact → Privilege → Persistence
     - C. Initial contact → Persistence → Recovery → Execution → Impact → Privilege
     - D. Initial contact → Execution → Privilege → Persistence → Impact → Recovery

49. WannaCry (2017) is best described as:
     - A. A virus that needed users to share infected files
     - B. Ransomware that also spread as a worm through a vulnerable SMB service
     - C. Spyware that only recorded keystrokes
     - D. A phishing e-mail campaign without malware

## Week 6 — Networking Fundamentals for Security

50. Which statement about switches and routers is correct?
     - A. A switch connects different networks; a router forwards frames inside a LAN
     - B. Switches and routers do exactly the same job
     - C. A router only provides Wi-Fi
     - D. A switch forwards frames inside a LAN using MAC addresses; a router forwards IP packets between networks

51. What does HTTPS protect?
     - A. The content in transit between the two TLS endpoints
     - B. Your data from malware already on your own device
     - C. Your IP address and traffic timing
     - D. It guarantees that the website is honest

52. Guests in a small office should reach the Internet but **not** the staff records server. Which control fits best?
     - A. Antivirus on guests' phones
     - B. Hiding the Wi-Fi name
     - C. Network segmentation with rules: guest → Internet allow, guest → staff server deny
     - D. Changing the DNS server

53. In `198.51.100.20:22`, the number `22` usually identifies which service?
     - A. HTTPS
     - B. SSH
     - C. DNS
     - D. The device number on the LAN

54. What does DNS do?
     - A. Encrypts web pages
     - B. Blocks unwanted traffic using rules
     - C. Forwards frames between switch ports
     - D. Finds the IP address that matches a domain name

55. What is an **evil twin**?
     - A. A fake access point imitating a trusted Wi-Fi name
     - B. A virus with two copies of itself
     - C. Two routers with the same public IP
     - D. A backup copy of a server

56. Which statement about an IP address is correct?
     - A. It proves who the person using the device is
     - B. It is the same as a MAC address
     - C. It identifies a network interface, not a person
     - D. It is only used inside one LAN

57. What does **NAT** allow?
     - A. Encrypting all traffic leaving a network
     - B. Many private addresses to share one public address
     - C. A switch to learn MAC addresses
     - D. A DNS resolver to answer faster

58. The campus Internet connection fails. Can you still print to the lab printer connected to the same switch?
     - A. No, nothing works without the Internet
     - B. No, printing always goes through the LMS server
     - C. Only if you use HTTPS
     - D. Yes, because the print job stays on the local network

59. At a café you see a certificate warning on a site you use every day. What is the best first reaction?
     - A. Stop: do not continue, because the problem could be the device, the network or the website
     - B. Click "continue anyway", because you know the site
     - C. Turn off the antivirus and try again
     - D. Type your password quickly before the connection closes

60. Why does **DNS spoofing** not automatically defeat a correct HTTPS connection?
     - A. DNS is encrypted by the switch
     - B. Browsers never use DNS for HTTPS sites
     - C. The fake server still needs a valid certificate for that name
     - D. DNS spoofing only affects printers

<div class="pb"></div>

## Answer Key

| Q | Ans | Why |
|---|---|---|
| 1 | B | Security reduces unauthorized access (C), unwanted change (I) and harmful disruption (A). |
| 2 | C | Private data was seen by people who should not see it. |
| 3 | A | Integrity can fail by accident; the data is no longer trustworthy. |
| 4 | D | A reused password is a weakness that could be used. |
| 5 | B | Clear owner, scope, time, method and purpose. "Reachable" ≠ "allowed". |
| 6 | C | Several layers, because any single control can fail. |
| 7 | D | Pause → check (via a route you choose) → report (official channel). |
| 8 | A | Same price, different value: value comes from what the asset does. |
| 9 | B | Services that share one dependency fail together. |
| 10 | C | Vulnerability = the flaw; exploit = its use. The attackers are the threat. |
| 11 | D | Unintended harm = accidental threat. |
| 12 | A | M / A / P: WannaCry = malicious, GitLab = accidental, Kakao fire = physical. |
| 13 | B | A backup is only proven by a tested restore. |
| 14 | C | A risk is possible future harm; the others already happened (incidents). |
| 15 | B | 2 × 3 = 6; bands are 1–2 Low, 3–4 Medium, 6–9 High. |
| 16 | D | 5 cannot be made from 1–3 × 1–3. |
| 17 | A | Restore lowers how much is lost (impact); a patch lowers likelihood. |
| 18 | C | Origin-bound keys check the website automatically, so stolen details were not enough. |
| 19 | D | Know + have. A, B, C are all "know + know". |
| 20 | A | Social engineering hacks the human factor, not code. |
| 21 | B | Pretext = invented story; requested action = what causes harm. |
| 22 | C | "From the court" = authority; "ten minutes" = urgency. |
| 23 | D | Following an authorized person into a restricted area. |
| 24 | A | Text channel (smishing) + targeted (spear) + claimed identity (impersonation). |
| 25 | B | The request stayed the same; the person's state changed. |
| 26 | C | Seeing a familiar face is not passing the approval process. |
| 27 | D | Read the hostname from the right: `…campus.example`. Option A belongs to `verify-now.test`. |
| 28 | A | HTTPS also protects a connection to a deceptive site. |
| 29 | B | Money sent → 112 + bank immediately for payment suspension. |
| 30 | C | 118 KISA = technical advice on suspicious SMS / malicious apps. |
| 31 | D | Identification = the account claim. |
| 32 | A | The stolen password was valid proof, so authentication passed. |
| 33 | B | Stuffing does not guess; it reuses a leaked pair. |
| 34 | C | Offline guesses never reach the login service. |
| 35 | D | A hash is one-way; the guess produced a match, nothing was decrypted. |
| 36 | A | A salt makes every hash different; it is stored with the hash and is not secret. |
| 37 | C | Minimum 15 characters for password-only; long, random and unique. |
| 38 | B | Another user's resource at the same level = horizontal. |
| 39 | A | Only the access the assignment needs. |
| 40 | D | A verification screen alone does not enforce the rule; the route must check MFA state. |
| 41 | B | Malware is defined by purpose and actions, not names or symptoms. |
| 42 | C | A worm spreads by itself through reachable, unpatched systems. |
| 43 | A | Disguised as something useful = Trojan. |
| 44 | D | Collects information; a keylogger captures keystrokes. |
| 45 | B | Backups must be protected, separated and tested. |
| 46 | C | Fix the cause too, or the weakness comes back. |
| 47 | A | Admin rights let malware change more and disable controls. |
| 48 | D | Contact → execution → privilege → persistence → impact → recovery. |
| 49 | B | Ransomware + worm via SMB on reachable, unpatched Windows systems. |
| 50 | D | Switches connect local devices; routers connect networks. |
| 51 | A | Only content in transit between TLS endpoints. |
| 52 | C | Segmentation limits unnecessary paths and an incident's spread. |
| 53 | B | 22 = SSH, 443 = HTTPS. |
| 54 | D | DNS: `lms.example.com` → `198.51.100.20`. |
| 55 | A | An SSID only proves the advertised name. |
| 56 | C | An IP address identifies an interface; it does not prove identity. |
| 57 | B | NAT: many private addresses share one public address. |
| 58 | D | Laptop → AP → switch → printer stays local. |
| 59 | A | Name the location first; stop at certificate warnings. |
| 60 | C | Without a valid certificate for that name, TLS shows a warning. |

**Scoring guide:** 54–60 excellent · 45–53 good, review the weeks you missed · below 45 re-read the study guide, then take the EXTRA practice bank.

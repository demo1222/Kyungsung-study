# MIDTERM STUDY GUIDE

**Computer Security** · Weeks 1–3, 5 and 6

*Condensed, comprehensive review for efficient midterm preparation*

`What is valuable? → What can harm it? → Why could it succeed? → How serious? → What do we do?`

> **Scope note**
>
> This guide covers every lecture in the repo: weeks 1, 2, 3, 5 and 6. **There are no week 4 slides in the folder.** If a week 4 lecture was given, get those slides before the exam, because nothing here covers it.

> **Important exam note**
>
> The slides never state the midterm format, so this guide prepares for the three things every lecture practised: (1) **define a term** in plain English, (2) **classify a scenario** (which CIA goal, which malware type, which phishing label, which risk level), and (3) **explain a real case** using asset / threat / vulnerability / control. The course teaches protection, not attack: no question will ask you how to perform an attack.

Prepared from the week 1–6 slides, my notes and the assignments.

## How to Use This Guide

This guide replaces re-reading five slide decks. It keeps the lecture order, the lecturer's own terms and every real case, and drops repeated examples.

### Study in three passes

| Pass | What to do |
|---|---|
| 1. Learn the chain | Asset → threat → vulnerability → exploit → control → risk. Every later week reuses these six words. |
| 2. Review each week | Definitions, the comparison tables, and what each real case teaches. |
| 3. Test yourself | Use the self-check section at the end. If you cannot answer in one or two sentences, go back to that week. |

### What "explain a case" means

- Name the **asset** that was harmed and which **CIA goal** it lost.
- Separate the **threat** (who or what caused harm) from the **vulnerability** (the weakness that let it work).
- Name one **control** and say whether it **prevents, detects or recovers**, and whether it lowers **likelihood** or **impact**.

> **Do not memorize dates only**
>
> A date with no lesson scores nothing. For every case know one sentence: *what happened* and *what it teaches*. The case table near the end has all of them.

## The Course as One System

`Asset → Threat → Vulnerability → Exploit → Control → Risk`

Each week answers a different question:

| Week | Main question | Core concepts |
|---|---|---|
| 1 | What does security protect? | Definition of security, CIA triad, five words, pause-check-report, permission, defense in depth |
| 2 | What matters, what can harm it, how serious is it? | Four asset types, threat / vulnerability / exploit / control, prevent-detect-recover, MFA, backup vs restore, risk matrix |
| 3 | How are people attacked? | Social engineering, pretext vs action, six levers, phishing family, warning signs, reporting routes |
| 4 | (no slides in the repo) | — |
| 5 | How is a device attacked? | Six malware categories, seven infection paths, endpoint controls, trusted-state recovery |
| 6 | Where does data travel, and where does security matter? | LAN/WAN, switch/AP/router, IP/port/protocol/DNS, HTTPS boundary, evil twin, firewall, segmentation |

> **Key distinction**
>
> Week 2 gives the **framework**. Week 3 applies it to **people**, week 5 to **devices**, week 6 to **networks**. The same answer pattern works everywhere: **location or asset → weakness → control**.

## Week 1 - Introduction to Computer Security

### Definition

**Computer security** is the set of ideas, practices and controls used to reduce **unauthorized access**, **unwanted change** and **harmful disruption**.

`Protect access → Protect accuracy → Protect use`

Those three map onto confidentiality, integrity and availability.

### What we protect

| Area | Examples |
|---|---|
| Information | Grades, messages, research, identity data, payment details |
| Devices + services | Phones, laptops, LMS, email, cloud storage, campus Wi-Fi |
| People + reputation | Time, trust, privacy, safety, the ability to study or work |

### The CIA triad

| Goal | Key question | School example | Typical failure | Typical controls |
|---|---|---|---|---|
| **Confidentiality** | Who is allowed to see it? | Only the student and authorized staff see a grade | Reading someone's email, public sharing of a private file, shoulder-surfing | Screen lock, unique password, MFA, sharing permissions |
| **Integrity** | Is it correct, complete, trustworthy? | An assignment arrives exactly as submitted | Altered grade, old file uploaded, corrupted storage | Access control, validation, logs and version history, hashes, backups |
| **Availability** | Can authorized people use it when needed? | LMS works before a deadline | DoS traffic, ransomware, power or hardware failure, bad update | Backups, redundancy, maintenance, monitoring, recovery plans |

> **Important**
>
> Integrity and availability can fail **by accident**, with no attacker: editing the wrong row, a software bug, a power failure. An accident is still a security problem because the data is no longer trustworthy or usable.

### Which CIA goal? (practise this)

| Situation | Goal |
|---|---|
| A student's grades are posted publicly | C |
| Someone changes a submitted assignment | I |
| The LMS is offline before a deadline | A |
| A shared file is corrupted and cannot open | I (and as a result A) |

### Balance

- More protection can add effort: MFA improves confidentiality but adds a login step. The answer is to make protection **usable**, not to remove it.
- One control can serve several goals: a **tested backup** supports availability and can restore integrity.
- Avoid both extremes: "nothing bad has happened, so we are safe" and "everything is a disaster".

## Week 1 - Five Words, Safe Response, Ethics

### Five words describe a security problem

| Term | Meaning | Mina's account |
|---|---|---|
| Asset | Something valuable | Her account, email, files, grades |
| Threat | A possible cause of harm | An attacker |
| Vulnerability | A weakness that could be used | A reused or phished password |
| Control | A safeguard that reduces risk | MFA, unique password, backups |
| Risk | The possibility and consequence of harm | Losing privacy, grades and reputation before a deadline |

### Case: Mina's university account

One account covers LMS, email, submissions, grades and files. One compromise hits **all three** goals: private email read (C), messages sent as her and assignment replaced (I), lockout before the deadline (A). It also harms **other people**: classmates and the professor receive the fake messages.

### People, process, technology

`People make choices → Process says what to do → Technology blocks, detects, records, recovers`

Technology alone is never enough: a strong password system fails if a person gives the password away.

### Pause, check, report

`PAUSE: do not click, reply, install, share → CHECK: verify sender, request, address, context → REPORT: use the official channel`

Warning signs: unexpected urgency, unfamiliar sender, mismatched address, request for credentials. **Pressure is a signal to slow down.** Verify through a route **you** choose (open the official site yourself), never through the link in the message.

### Permission defines ethical practice

Authorized practice has a clear **owner, scope, time, method and purpose**.

| Authorized | Unauthorized |
|---|---|
| Scanning an instructor-provided lab machine during the scheduled exercise, using approved steps, submitting findings privately | Scanning a university server because it is reachable, then sharing what you found |

> **Do not confuse**
>
> "Reachable" does not mean "allowed". The scan can be technically identical; **permission, scope and how results are handled** make the difference. When scope is unclear: **stop and ask**.

### Defense in depth

Several layers: attentive users, strong authentication, device protection, network controls, monitoring, backups. **Any single control can fail**, so another layer catches what one misses.

## Week 2 - Assets

### Four asset types

| Type | Meaning | Examples | Real case |
|---|---|---|---|
| Information | Useful facts we depend on | Patient records, grades, passwords | Equifax 2017 |
| Devices | Physical tools that support work | Laptops, phones, hospital computers | NHS, May 2017 |
| People | Knowledge, work and wellbeing | Staff, patients, students | NHS, May 2017 |
| Services | Functions people rely on | Online exams, messaging, payments | Facebook, 4 Oct 2021 |

### An asset list is only the beginning

| Question | Meaning | Example |
|---|---|---|
| Value | Why does it matter? | Two identical computers: one shows a public notice, one supports urgent care. **Same price, different value.** |
| Dependency | What does it need to work? | Facebook 2021: a network setting change cut communication between data centers. The computers were fine but the services failed. |
| Protection goals | What must be preserved? | Use C, I and A. |

> **Key idea**
>
> Value comes from what the asset **does**, not what it costs. Services that share one dependency **fail together**.

### What can an asset lose?

| Goal | Real case |
|---|---|
| Confidentiality | Equifax: private data was exposed |
| Integrity | GitLab: database data was deleted |
| Availability | NHS: healthcare work was disrupted |

## Week 2 - Harm and Protection

### Four roles

| Term | Meaning | Equifax 2017 |
|---|---|---|
| Threat | A possible cause of harm | The attackers |
| Vulnerability | A weakness | The unfixed software flaw |
| Exploit | A way to use a weakness | Using the flaw to get in |
| Control | A protective measure | A **verified** patch |

> **Do not confuse**
>
> The attackers are the threat. The flaw is the vulnerability. Using the flaw is the exploit. **Vulnerability = the flaw. Exploit = its use.**

### Three kinds of threat (M / A / P)

| Malicious | Accidental | Physical |
|---|---|---|
| Deliberate harm | Unintended harm | Physical damage |
| WannaCry 2017: ransomware disrupted NHS services | GitLab 2017: database data deleted by mistake | Kakao 2022: data-center fire |

A threat does not have to be a person with bad intentions.

### Incident vs risk

| Incident | Risk |
|---|---|
| Something **has happened** that harms or threatens security | **Possible future** harm, judged by chance and seriousness |

### Controls: prevent, detect, recover

`PREVENT: fix a known flaw → DETECT: check records of unusual access → RECOVER: restore from a tested copy`

- **Patch** = a software update that fixes a problem. Equifax lesson: a patch instruction is not enough; the patch must be **applied and checked** on the real system.
- **Backup** = make a separate copy. **Restore** = use the copy to recover. GitLab lesson: **recovery must be tested**. A backup you never restored from is an assumption.

### Account controls

| Term | Meaning |
|---|---|
| Phishing | A deceptive message or website that tries to trick someone |
| Credentials | Evidence used to prove identity, such as login details |
| Authentication | The process of checking a claimed identity |
| MFA | More than one **kind** of identity evidence: something you **know** (password) + something you **have** (security key) |

| Uber, Sep 2022 | Cloudflare, 2022 |
|---|---|
| After repeated requests, a contractor **approved** a login | Staff entered details on a fake site, but **security keys blocked** the login |
| Control depended on a person's judgment under pressure | **Origin-bound** key checks which website is asking, automatically |
| Attacker got in | Stolen login details were not enough |

## Week 2 - Assessing Risk

**Risk** = possible harm judged by **likelihood** and **impact**.

### Before you rate anything

| Define | Ask | Example |
|---|---|---|
| Event | What harmful event do we mean? | An attacker gains account access |
| Period | Over what period? | Before next month's exam |
| Current controls | What protection works now? | Security keys block one route |

Separate **facts** (supported by evidence), **assumptions** (accepted for the exercise) and **unknowns** (missing evidence).

### The two scales

| Score | Likelihood | Impact |
|---|---|---|
| 1 | **Unlikely**: not expected under stated conditions | **Minor**: small disruption, routine recovery |
| 2 | **Possible**: a believable route to harm exists | **Serious**: important work or privacy affected, extra help needed |
| 3 | **Likely**: expected, or strongly supported by evidence | **Severe**: essential service lost, or harm hard to reverse |

### Risk matrix: Score = Likelihood × Impact

| Likelihood ↓ / Impact → | 1 Minor | 2 Serious | 3 Severe |
|---|---|---|---|
| **3 Likely** | 3 Medium | 6 High | 9 High |
| **2 Possible** | 2 Low | 4 Medium | 6 High |
| **1 Unlikely** | 1 Low | 2 Low | 3 Medium |

> **High-yield: the bands**
>
> **1–2 = Low, 3–4 = Medium, 6–9 = High.** The score 5 cannot occur. Always write the working: "L = 2 (possible) × I = 3 (severe) = 6, High".

### Worked examples from the slides

| Scenario | L | I | Score | Level |
|---|---|---|---|---|
| WannaCry-like disruption, essential care stops | 3 | 3 | 9 | High |
| GitLab-like deletion, but a recent restore works | 2 | 1 | 2 | Low |
| Cloudflare-like route with strong key protection | 1 | 3 | 3 | Medium |
| Update failure interrupts essential work | 2 | 3 | 6 | High |

### What each control changes

| Control | Reduces | Because |
|---|---|---|
| Verified **patch** | **Likelihood** | That exploitation route is closed (other weaknesses may remain) |
| Tested **restore** | **Impact** | Less is lost after the event (some harm can remain) |

### The week 2 assignment pattern (exam in 30 days)

A public exam system has an unfixed flaw and an untested backup. Four sentences: *the asset is … it matters because … / the threat could use …, which is the weakness / likelihood is … and impact is … because … / our control is …; it reduces …*. Model answer: L 3 × I 3 = 9 High; **patch and verify** (likelihood) and **test the restore** (impact).

## Week 3 - Social Engineering

### Definition

**Social engineering** = deception that influences a person's action. It hacks the **human factor** (attention, emotion, habits, working situation), not the computer code. It can arrive by phone, text, email, social media or in person.

### Pretext vs requested action

| Pretext | Requested action |
|---|---|
| The situation the attacker invents | What the attacker wants you to do |
| "Your scholarship payment failed." | Send a password, approve a login, transfer money |

> **Key idea**
>
> The story may be believable. **The action is what causes harm**, so judge the action.

### Why it works

`Trust: we cooperate with familiar people → Pressure: fear or a deadline narrows attention → Attention: a busy moment interrupts checking`

### Six levers (plus secrecy)

| Lever | Sounds like |
|---|---|
| Authority | "I am from the court." |
| Fear | "Your account is involved in a crime." |
| Urgency | "You have ten minutes." |
| Familiarity | "It's me. I changed my number." |
| Reward | "You won a tuition grant." |
| Curiosity | "Someone posted your photo." |
| (Secrecy) | "Keep this private until approval." It removes the friend who would say "that looks odd". |

### In person

| Baiting | Tailgating |
|---|---|
| An attractive item or offer invites a risky action | Someone follows an authorized person into a restricted area |
| Unknown USB labelled "Exam answers" | A visitor asks you to hold a secure door |
| Do not plug it in; hand it to IT | Stay polite: point to reception or call the host |

### Uber: MFA fatigue

`Attacker has the password → Repeated approval prompts, first rejected → One accepted prompt gives access`

Nothing about the request changed; the **person's state** changed. A better control than "be more careful": phishing-resistant MFA (origin-bound key), limits and alerts on repeated prompts, and a rule that **a prompt you did not start is reported, never approved**.

### Verified contact vs claimed identity

| Verified contact | Claimed identity |
|---|---|
| You reach the person through a route you already trust, and confirm the exact request | The message *says* "university", "bank", "court" or "your friend" |
| | Names, logos and profile pictures can be copied |

## Week 3 - Phishing and Impersonation

**Phishing** = deceptive contact that seeks information or an unsafe action.

### Five labels, five different features

| Term | Feature it describes | Meaning |
|---|---|---|
| Phishing | Deception | The broad category |
| Spear phishing | **Targeting** | Personalized to a person, role or group |
| Smishing | **Text** channel | Phishing by SMS or text |
| Vishing | **Voice** channel | Phishing by call |
| Impersonation | **Claimed identity** | Pretending to be someone else |

> **High-yield**
>
> Each label describes a different feature, so **one attack can carry several labels**.

| Contact | Labels |
|---|---|
| Generic email requests a new sign-in | Broad phishing |
| SMS uses your project name and a fake tutor identity | Smishing + spear phishing + impersonation |
| A caller posing as a bank asks for a code | Vishing + impersonation |
| A copied friend profile requests urgent money | Impersonation |

### Cases

| Case | What happened | Lesson |
|---|---|---|
| Korean "daughter" call (reported Jul 2018) | Caller posed as a man's daughter, claimed an accident, asked for 20 million won. The real daughter was at home; no payment. | Fear + urgency + familiarity. Control: call back on a **known number**, or a family code word. |
| Twilio (Aug 2022) | Texts impersonated internal IT; staff used fake sign-in pages | A familiar name does not prove the destination. One account exposed **other people's** data, so limit what an account can reach. |
| Changwon District Court warning (8 Jul 2025) | "Court mail was returned": use a link, give information, install an app | Authority + unfamiliar legal language adds pressure. Find the court's number yourself. |
| Hong Kong deepfake meeting (reported 2024) | Fake CFO email, then a fabricated video meeting; about **HK$200 million** transferred | **Recognition is not authorization.** |

### Authorization vs recognition

| Authorization | Recognition |
|---|---|
| "This request passed our agreed verification and approval process." | "That looks like my manager." |

A **deepfake** uses AI to imitate a person's appearance or voice. Seeing a face raises confidence, but a sensitive request still needs an independent check.

## Week 3 - Warning Signs and Reporting

### U + P + S

`Unexpected: new contact, unusual login → Pressure: deadline, threat, secrecy → Sensitive action: credentials, money, device access`

One sign alone may be innocent. All three together is the pattern to stop on. Requests that deserve a pause: a **password or code**, a **payment change**, **device access** (install an app, enable remote access).

### Read the full hostname

```
https://login.campus.example/student           real: belongs to campus.example
https://campus.example.verify-now.test/student  fake: belongs to verify-now.test
```

A hostname is read **from the right**. Open the known portal yourself.

### Appearance is limited evidence

| Stronger checks | Easy to imitate |
|---|---|
| An expected task and a known contact route | Logo, display name, fluent grammar, familiar layout |
| Confirming the exact request through the official process | **HTTPS**: it also protects a connection to a deceptive site |

A QR code is a hidden link. For an urgent tuition QR notice the strongest action is **open the usual portal**, not "scan now" and not "ask the sender".

### Pause, verify, report

`PAUSE: stop the action, end the pressure → VERIFY: separate known route, confirm the exact request → REPORT: official channel, explain what happened`

A verification route is **independent** when you obtained it **separately** from the suspicious contact.

### Reporting routes in South Korea

| Situation | Route | Purpose |
|---|---|---|
| Money sent, or active voice-phishing fraud | **112** and your **bank's official contact** | Report urgently and request **payment suspension** |
| Suspicious SMS or possibly malicious app | **118 KISA** | Technical advice about the message or device |
| Campus account or university message | Known **university IT** office | Report and arrange an account response |

### If you already acted

| What happened | Immediate response |
|---|---|
| Opened a link only | Close it, report it, mention any downloads or permissions |
| Entered credentials or approved a login | Reset access and end sessions through a trusted route; contact IT |
| Installed an app or allowed remote access | Stop using the device for sensitive tasks; get help **from another device** |
| Sent money | 112 and the bank **immediately**; request payment suspension |

Respond supportively ("Thank you for telling me"). **Shame makes people hide information and delay help.**

## Week 5 - Malware Categories

**Malware** = software intentionally designed to cause harm: steal information, disrupt service, spy, gain control, or enable later attacks.

> **Key idea**
>
> Malware is identified by its **purpose and actions**, not by its name, appearance or symptoms. Some malware hides quietly, and **a symptom alone does not prove infection**.

### Six categories

| Category | Slide example | How it behaves | What helps |
|---|---|---|---|
| **Virus** | Sality | Activates when an infected file or program is **executed**; copies itself into other content | Do not share or run untrusted files |
| **Worm** | Conficker | **Propagates across networks** by exploiting weaknesses; no user needs to open a file | Fast patching, segmentation |
| **Trojan** | SocGholish (fake browser update) | **Disguised** as a game, update, document or pirated app | Trusted sources only; a filename proves nothing |
| **Ransomware** | WannaCry | **Encrypts or blocks** systems, may also steal data | Backups; **payment does not guarantee recovery** |
| **Spyware** | Spyware.KeyLogger | **Collects information**; a keylogger captures keystrokes | Monitoring, endpoint protection (often no visible sign) |
| **Bot** | Neutrino Bot | Lets an **external operator** use the device for spam, fraud, attacks | Monitoring for hidden activity |

> **Do not confuse**
>
> A **virus needs a user action** (running or sharing an infected file). A **worm spreads by itself** through reachable, unpatched systems. WannaCry was **ransomware that also spread as a worm**.

### Name the type (practise this)

| Observation | Most likely type |
|---|---|
| Infected program shared on USB; other executables become infected | Virus |
| Several unpatched computers infected without users opening a file | Worm |
| A "free game" installs an unwanted remote-control program | Trojan |
| Course files no longer open; a screen demands payment | Ransomware |
| A program secretly records what a student types | Spyware / keylogger |
| A device sends attack traffic when a remote operator says so | Bot |
| A laptop is slow, but no scan, process or network evidence exists | **Unknown, possibly not malware** |
| A fake update steals information and downloads ransomware | Trojan + spyware + ransomware |

Evidence that separates malware from an ordinary fault: running processes, network connections, recent changes, scan results, startup and configuration changes. A computer **can** be infected with no warning window; only ransomware wants to be seen.

## Week 5 - Infection Paths

Malware depends on unsafe content, weak configuration, excessive privilege or unpatched software.

### Seven paths and their controls

| Path | How it works | Control |
|---|---|---|
| Malicious messages | Attachments, links, fake login pages | Verify unexpected content; filtering; user reporting |
| Untrusted downloads | Pirated software, unofficial stores, fake updates | Approved sources; check publisher and update path |
| Unpatched vulnerabilities | Known flaws exploited when updates are delayed | Prioritize internet-facing and critical systems; replace unsupported software |
| Excess privilege | Admin access lets malware change more and disable controls | **Standard accounts** for daily work |
| Removable media | Unknown or infected USB devices | Media policy; do not connect found devices |
| Weak configuration | Auto-run, exposed services, default credentials, disabled protections | Secure baselines; monitor configuration changes |
| Supply chain | Legitimate updates or vendors are compromised | Trusted signed sources; track dependencies and supplier notices |

An attachment from a **known contact** can still be dangerous: the account may be compromised, the address spoofed, or the contact forwarding it without knowing.

### The infection story structure

`Initial contact → Execution → Privilege → Persistence → Impact → Recovery`

| Story | Contact | Execution | Persistence | Control |
|---|---|---|---|---|
| Email attachment | User receives an infected document | User **opens** it | Startup entry or scheduled task | Filtering, verify content, standard accounts |
| Fake software / update | User downloads a fake game or update | User **runs** the installer | Installed program, auto-start | Approved sources, restrict installation |
| Network worm | Vulnerable computer is **reachable** | Worm exploits an unpatched service, **no user action** | Service or system component | Patch quickly, segmentation |
| Infected USB | User connects the USB | User **runs** the infected file | Copies to other files and media | Media policy, disable auto-run |

> **High-yield**
>
> This six-stage path was the week 5 assignment. Be ready to write one story stage by stage, with a control placed against **each stage**, not all at the end.

## Week 5 - Protect and Respond at the Endpoint

### Four endpoint controls

| Control | Detail to remember |
|---|---|
| Updates | OS, browsers, applications, **firmware**, security tools. Automatic where appropriate; **track devices that cannot update**. |
| Endpoint protection | Blocks known threats, flags suspicious files and processes. Detection quality changes over time; **alerts need investigation**. |
| Secure configuration | Disable unnecessary services, restrict installation, lock screens, encrypt storage. **Defaults prioritize convenience.** Configuration should be repeatable and reviewable. |
| Backups | **Protected, separated and tested.** A **connected backup may also be encrypted** by ransomware. |

**Least privilege** limits what malicious code can change or access.

### If you suspect infection

`Stop sensitive work → Avoid unnecessary changes → Report quickly`

- **Do not keep experimenting** on the device.
- **Follow guidance before disconnecting critical systems**: staff may need to preserve evidence.

### Recovery = a trusted state

`Clean system → Weakness fixed → Credentials safe → Data restored → Monitored afterwards`

> **Trap**
>
> **Restoring files alone may restore the weakness.** Fix the cause, and document the cause and the improvement.

### Why antivirus is not enough

No tool detects every threat. Protection also depends on configuration, updates, privilege, backups and users. This is week 1's **defense in depth**.

### Six questions before recommending anything

`Symptom → Infection path → Privilege level → Affected data → Safe first action → Recovery evidence`

### Library computer activity (model answer)

A fake update was installed, the browser opens unknown pages, and a student used email afterwards. **Behavior:** Trojan from the fake update, possible spyware. **Containment:** stop sensitive use, do not experiment, report to university IT. **Affected accounts:** anything used **after** the installation, starting with email; reset from a **different trusted device**. **Prevention:** restrict installation, standard accounts, approved sources, monitored endpoint protection.

## Week 6 - Follow the Network Path

A **network** connects devices so they can exchange data.

`Laptop → Access point → Switch → Router / firewall → Internet routers → LMS server`

The shared printer hangs off the switch. In the labelled diagram: **A = access point, B = switch, C = Internet routers, D = router / firewall**.

### LAN, WAN, Internet

| Term | Meaning | Example |
|---|---|---|
| LAN | Network in a limited local area | Computers and a printer in one lab |
| WAN | Links networks over larger distances | A university links two distant sites |
| Internet | Many connected networks worldwide | Campus reaches a cloud LMS |

**Endpoint** = a device at an end of a communication. **Client** starts a request; **server** provides a service.

### The devices in between

| Device | What it does | Security concern |
|---|---|---|
| Switch | Forwards Ethernet **frames inside a LAN**; learns **MAC addresses** | An unused cable socket can be an entry point |
| Access point | Lets **wireless** devices join a network | Who can connect, and what can they reach? |
| Router | Forwards **IP packets between networks**; the **default gateway** is the next router | Settings can be changed by an attacker |

> **Key distinction**
>
> **Switches connect local devices. Routers connect networks.** A home "Wi-Fi router" is router + AP + switch in one box.

### Local vs remote

| Path | Route |
|---|---|
| Print job | Laptop → AP → switch → printer. **Stays local.** |
| LMS request | Laptop → AP → switch → router/firewall → Internet routers → server |

If the Internet connection fails, the local printer **still works**. Wi-Fi connects you to a network, which is not the same as the Internet.

### Where a risk can begin

| Location | What could go wrong | Control |
|---|---|---|
| Device | Malware uses the device's connections | Updates and endpoint protection |
| Wi-Fi or cable socket | An unauthorized device joins | Network access control |
| Router settings | An attacker changes settings | Protected admin access and updates |

**WannaCry from the network side:** it spread to **reachable, unpatched** Windows systems through a vulnerable **SMB** (file sharing) service. Reduce spread by installing the fix and restricting unnecessary SMB traffic.

## Week 6 - Read a Network Connection

### Four terms, four questions

| Question | Term | Classroom example |
|---|---|---|
| Where is it? | **IP address** | Laptop 192.168.10.24, gateway 192.168.10.1, LMS 198.51.100.20 |
| Which service? | **Port** | 443 = HTTPS, 22 = SSH |
| Which rules? | **Protocol** | IP, TCP, TLS, HTTP |
| What address matches the name? | **DNS** | lms.example.com → 198.51.100.20 |

- An IP address identifies a **network interface**. **It does not prove a person's identity.**
- **NAT** (Network Address Translation) changes address information as traffic passes, so many **private** addresses share one **public** address (203.0.113.5).

### Protocols

| Protocol | Plain English |
|---|---|
| IP | Delivers packets between networks |
| TCP | Delivers data reliably and in order |
| TLS | Protects a connection's data: encryption and certificate checks |
| HTTP | Defines web requests and responses |

**HTTPS = HTTP protected by TLS.** A **certificate** is digital evidence used to check the server's identity. **Encryption** makes content unreadable without the right keys.

### DNS and the URL

`Device asks: lms.example.com? → Resolver answers: 198.51.100.20 → Device connects to 198.51.100.20`

| URL part | Meaning |
|---|---|
| `https` | Use HTTP protected by TLS |
| `lms.example.com` | Domain name; DNS finds its address |
| `/course/6` | Path to a resource |
| (443) | Default HTTPS port when none is written |

### The HTTPS protection boundary

| Question | What HTTPS tells us |
|---|---|
| Can a nearby observer read the page content? | **Normally no**, when TLS works correctly |
| Is every website using HTTPS honest? | **No.** A phishing site can also use HTTPS |
| Can malware read data on my own device? | **Yes.** Endpoint security still matters |
| Is all network information hidden? | **No.** IP addresses and traffic timing may remain visible |

> **High-yield**
>
> HTTPS protects **content in transit between the TLS endpoints**, and nothing else. In browser DevTools a row is a **resource request, not one packet**, and the browser shows clear content because it **is** one endpoint.

## Week 6 - Locate and Reduce Risk

A useful explanation names the **location**, the **weakness** and the **control**.

### Five locations

`Device: endpoint protection, updates → Access: authenticated Wi-Fi → Boundary: firewall rules → Data in transit: TLS → Server: permissions`

### Named risks

| Risk | Where | What it is | Response |
|---|---|---|---|
| **Evil twin** | Access | A fake access point imitating a trusted Wi-Fi name. An SSID proves only the advertised name. | Verify the network, follow approved setup, **stop at certificate warnings** |
| **DNS spoofing** | DNS | False DNS information redirects traffic | It **does not automatically defeat TLS**: the fake server still needs a valid certificate for that name |
| **On-path attacker** | In transit | Someone positioned to intercept or influence traffic | HTTP is exposed; correct HTTPS protects content |
| **Too much exposure** | Service | A server reachable in more ways than needed | Firewall: allow 443 to the public, deny public SSH 22, allow an approved admin path |
| **Excessive access** | Server | Encrypted request, but the user gets more than they should | Authentication and authorization |

**Firewall** = software or hardware that allows or blocks traffic using rules.

### Authentication vs authorization

| Authentication | Authorization |
|---|---|
| *Who are you?* Checks **identity** | *What may you do?* Checks **permissions** |

### Segmentation

Divides a network into groups and controls communication between them. Guest devices → staff records server: **deny**. Guest devices → Internet: **allow**. It limits unnecessary paths and an incident's **spread**.

### Small office activity (model answer)

| Risk | Control | Why it helps |
|---|---|---|
| Guests can reach staff systems | Separate guest access, enforce traffic rules | Limits access to private services |
| Administration is public | Allow only an approved admin path | Reduces unnecessary exposure |
| Printer firmware is old | Update it, or restrict it until replaced | Reduces exploitable weaknesses |

### The café certificate warning

A warning does not say **where** the problem is. It could be the **device** (wrong clock, malware, intercepting software), the **network** (fake hotspot), or the **website** (expired or wrong certificate). Name the location first.

## Every Real Case in One Table

| Case | When | What happened | What it teaches | Week |
|---|---|---|---|---|
| **WannaCry / NHS** | May 2017 | Ransomware disrupted hospital services; spread as a worm through unpatched SMB | Malicious threat, availability, patching, reachability | 2, 5, 6 |
| **Equifax** | 2017 | Attackers used an unfixed software flaw to reach personal data | Vulnerability vs exploit; a patch must be applied **and verified**; confidentiality | 2 |
| **GitLab** | 2017 | Database data deleted by mistake; recovery was hard | Accidental threat; integrity; backup is not restore | 2 |
| **Facebook** | 4 Oct 2021 | Network setting change cut data centers off; services down | Dependency; availability | 2 |
| **Kakao** | 2022 | Data-center fire disrupted services | Physical threat | 2 |
| **Uber** | Sep 2022 | Contractor approved a login after repeated prompts | MFA fatigue; controls that rely on judgment under pressure are weak | 2, 3 |
| **Cloudflare** | 2022 | Staff typed details into a fake site; security keys blocked the login | Origin-bound, phishing-resistant MFA | 2 |
| **Korean "daughter" call** | Jul 2018 | Vishing with family impersonation, 20 million won requested | Emotion blocks the pause; verify by a known number | 3 |
| **Twilio** | Aug 2022 | Smishing impersonating internal IT; fake sign-in pages | A familiar name is not the destination; limit an account's reach | 3 |
| **Changwon District Court** | 8 Jul 2025 | Fake "returned court mail" calls and texts | Authority + unfamiliar legal language | 3 |
| **Hong Kong deepfake** | 2024 | Fake CFO email and fabricated video meeting, about HK$200M | Recognition is not authorization | 3 |
| **Sality, Conficker, SocGholish, Spyware.KeyLogger, Neutrino Bot** | — | Slide examples of virus, worm, Trojan, spyware, bot | One example per malware category | 5 |

## Commonly Confused Concepts

| Do not confuse | Correct distinction |
|---|---|
| Threat vs vulnerability | Threat = what could cause harm (the attackers). Vulnerability = the weakness that lets it work (the flaw). |
| Vulnerability vs exploit | The flaw vs the **use** of the flaw. |
| Incident vs risk | Has happened vs possible future harm. |
| Likelihood vs impact | Chance of the event vs seriousness of the consequences. |
| Patch vs restore | A patch lowers **likelihood**; a tested restore lowers **impact**. |
| Backup vs restore | Making a copy vs using it to recover. Only a **tested** restore counts. |
| Confidentiality vs integrity | Who may **see** it vs whether it is **correct**. |
| Integrity vs availability | Correct and complete vs usable when needed. A corrupted file can lose both. |
| Authentication vs authorization | Who are you vs what may you do. |
| Recognition vs authorization | "Looks like my manager" vs "passed our approval process". |
| Pretext vs requested action | The invented story vs what they want you to do. |
| Phishing vs spear phishing | General message to many vs tailored to a person or group. |
| Smishing vs vishing | Text channel vs voice channel. |
| Baiting vs tailgating | Tempting item or offer vs following someone through a secure door. |
| Virus vs worm | Needs a user to run or share it vs spreads by itself across the network. |
| Trojan vs virus | Trojan is **disguised** as something useful; a virus **infects other files**. |
| Spyware vs bot | Collects your information vs lets an outside operator use your device. |
| Symptom vs evidence | A slow laptop vs scan, process, network or configuration findings. |
| Switch vs router | Frames inside a LAN vs packets between networks. |
| Wi-Fi vs Internet | A local network connection vs the worldwide set of networks. |
| IP address vs port | Which destination vs which service there. |
| IP address vs identity | An address identifies an interface; it does not prove who the person is. |
| HTTP vs HTTPS | No protection in transit vs TLS-protected content. |
| HTTPS vs "safe site" | Encrypted connection vs honest owner. A phishing site can use HTTPS. |
| DNS spoofing vs broken TLS | A false address redirects traffic, but the certificate check still stands. |
| Evil twin vs on-path attacker | A fake access point vs anyone positioned to intercept traffic. |
| Firewall vs segmentation | Rules that allow or block traffic vs dividing the network into controlled groups. |
| Authorized vs reachable | Permission with owner, scope, time, method, purpose vs "I could connect to it". |

## How to Answer Scenario Questions

### 1. "Which CIA goal?"

`Seen by the wrong person = C → Changed or wrong = I → Cannot be used when needed = A`

Name the goal, then justify with the definition in half a sentence. If two apply, say which is **most** affected and why.

### 2. "Label this incident"

`Asset → Threat → Vulnerability → Exploit → Control`

Model: *Equifax. Asset: personal information. Threat: attackers. Vulnerability: the unfixed software flaw. Exploit: using it to gain access. Control: a verified patch.*

### 3. "Rate the risk"

`Define event, period, current controls → Likelihood 1–3 with reason → Impact 1–3 with reason → Multiply → Band → Control and what it lowers`

### 4. "Is this message safe?"

`Name the pretext → Name the levers → Name the requested action → Give the independent check → Give the reporting route`

### 5. "What malware is this?" / "Trace the infection"

`Behavior → Category → What evidence would confirm it → Path: contact, execution, privilege, persistence, impact → Control per stage → Trusted-state recovery`

### 6. "Where is the network risk?"

`Location → Weakness → Control that fits that location`

Model: *Wi-Fi access. Unknown network operator (evil twin). Verify the approved network and stop at certificate warnings.* Pick risks at **different** locations when asked for two.

## Self-Check Questions

Try to answer without looking back. These are review questions, not copies of the real midterm.

1. Define computer security in one sentence.
2. What do C, I and A stand for, and what question does each ask?
3. Which CIA goal is most affected when a grade is changed without permission?
4. Why can an accidental error still be a security problem?
5. Name the five words that describe a security problem.
6. What five things define authorized security practice?
7. Why do secure systems use several layers of defense?
8. Name the four asset types with one example each.
9. Two computers cost the same. Why might one be more valuable?
10. In Equifax, what was the threat, the vulnerability and the exploit?
11. Give one example each of a malicious, an accidental and a physical threat.
12. What is the difference between an incident and a risk?
13. Name the three things a control can do, with an example each.
14. Compare what happened at Uber and at Cloudflare in 2022.
15. Why are backup and restore different actions?
16. Likelihood 2 and impact 3: what is the score and the level?
17. Does a patch mainly reduce likelihood or impact? What about a tested restore?
18. What three things must you define before rating a risk?
19. Define social engineering.
20. What is the difference between a pretext and a requested action?
21. Name the six levers attackers use.
22. A caller posing as a bank asks for a code. Which labels apply?
23. Why is "recognition is not authorization" the lesson of the Hong Kong case?
24. Which address is fake and why: `login.campus.example` or `campus.example.verify-now.test`?
25. Which Korean reporting route fits: (a) money already sent, (b) a suspicious SMS, (c) a strange campus-account email?
26. What makes a verification route independent?
27. How is a worm different from a virus?
28. What is a Trojan? Give the slide example.
29. A laptop is slow and nothing else is known. What malware is it?
30. Name four of the seven infection paths.
31. Write the six stages of an infection story.
32. Why may a connected backup be useless against ransomware?
33. What five conditions make recovery complete?
34. Why is antivirus not enough?
35. What is the difference between a switch and a router?
36. The Internet is down. Can you still print to the lab printer? Why?
37. What do an IP address, a port, a protocol and DNS each answer?
38. Name two things HTTPS does **not** protect against.
39. What is an evil twin, and what should you do at a certificate warning?
40. Does DNS spoofing defeat TLS? Explain.
41. Authentication vs authorization?
42. How does segmentation reduce harm?

## Self-Check Answers

1. The ideas, practices and controls used to reduce unauthorized access, unwanted change and harmful disruption.
2. Confidentiality: who may see it? Integrity: is it correct, complete, trustworthy? Availability: can authorized people use it when needed?
3. Integrity: the information was changed improperly.
4. It can make data incorrect, expose information or stop a service even with no attacker.
5. Asset, threat, vulnerability, control, risk.
6. A clear owner, scope, time, method and purpose.
7. Any single control can fail; other layers reduce the chance that one mistake causes major harm.
8. Information (grades), devices (laptops), people (staff), services (online exam).
9. Value comes from what the asset does: one may support an urgent service, so interruption costs more.
10. Threat: the attackers. Vulnerability: the unfixed software flaw. Exploit: using that flaw to gain access.
11. Malicious: WannaCry. Accidental: GitLab deletion. Physical: Kakao data-center fire.
12. An incident has happened; a risk is possible future harm judged by likelihood and impact.
13. Prevent (fix a known flaw), detect (check records of unusual access), recover (restore from a tested copy).
14. Uber: a person approved a login after repeated prompts, so the attacker got in. Cloudflare: staff typed details into a fake site, but origin-bound security keys refused to work there.
15. Backup makes a copy; restore uses it to recover. An untested backup may not restore (GitLab).
16. 2 × 3 = 6, High.
17. A patch reduces likelihood. A tested restore reduces impact.
18. The event, the period and the current controls.
19. Deception that influences a person's action.
20. The pretext is the invented situation; the requested action is what the attacker wants you to do, and it is the action that causes harm.
21. Authority, fear, urgency, familiarity, reward, curiosity.
22. Vishing + impersonation.
23. The employee recognized faces in a video meeting, but the request never passed an independent approval process.
24. The second: reading from the right, it belongs to `verify-now.test`.
25. (a) 112 and the bank, request payment suspension. (b) 118 KISA. (c) University IT.
26. You obtained it separately from the suspicious contact.
27. A worm propagates through networks by itself; a virus depends on a user executing or sharing an infected file.
28. Malware disguised as legitimate or useful software. SocGholish, a fake browser update.
29. Unknown. A symptom is not evidence; you need scan, process, network or configuration findings.
30. Any four of: malicious messages, untrusted downloads, unpatched vulnerabilities, excess privilege, removable media, weak configuration, supply chain.
31. Initial contact, execution, privilege, persistence, impact, recovery.
32. Ransomware can encrypt it too. Backups must be protected, separated and tested.
33. Clean system, weakness fixed, credentials safe, data restored, monitored afterwards.
34. No tool detects every threat; protection also needs configuration, updates, least privilege, backups and users.
35. A switch forwards frames inside a LAN; a router forwards packets between networks.
36. Yes. The print path (laptop → AP → switch → printer) never leaves the LAN.
37. IP: where is it. Port: which service. Protocol: which rules. DNS: which address matches the name.
38. Any two of: a dishonest site owner (phishing sites use HTTPS), malware on your own device, visibility of IP addresses and traffic timing.
39. A fake access point imitating a trusted Wi-Fi name. Stop; do not click through the warning.
40. Not by itself. It can redirect traffic, but the fake server must still present a valid certificate for the name.
41. Authentication checks who you are; authorization checks what you may do.
42. It limits unnecessary communication between groups, so an incident cannot spread freely.

## Final 15-Minute Revision Checklist

| You should be able to... | Check |
|---|---|
| Define computer security and the three CIA goals, each with a school example. | ☐ |
| Classify a scenario as C, I or A and justify it. | ☐ |
| Define asset, threat, vulnerability, exploit, control, risk, incident. | ☐ |
| Explain pause-check-report, permission (owner, scope, time, method, purpose) and defense in depth. | ☐ |
| List the four asset types and explain value and dependency. | ☐ |
| Label the Equifax incident. | ☐ |
| Give malicious, accidental and physical threat examples. | ☐ |
| Explain prevent / detect / recover, patch, backup vs restore. | ☐ |
| Compare Uber and Cloudflare; explain MFA and origin-bound keys. | ☐ |
| Draw the 3 × 3 risk matrix with the bands 1–2, 3–4, 6–9. | ☐ |
| Say which control lowers likelihood and which lowers impact. | ☐ |
| Define social engineering, pretext, requested action and the six levers. | ☐ |
| Apply the five phishing labels to a contact, with multiple labels. | ☐ |
| Tell the Korean call, Twilio, Changwon and Hong Kong cases with one lesson each. | ☐ |
| Read a hostname from the right; explain why HTTPS and logos prove little. | ☐ |
| Give the Korean reporting routes (112 + bank, 118 KISA, university IT) and the "already acted" responses. | ☐ |
| Define the six malware categories with the slide example for each. | ☐ |
| Explain virus vs worm and why WannaCry is both ransomware and worm. | ☐ |
| List the seven infection paths with a control for each. | ☐ |
| Write an infection story: contact → execution → privilege → persistence → impact → recovery. | ☐ |
| List the endpoint controls and the five trusted-state conditions. | ☐ |
| Trace laptop → AP → switch → router/firewall → Internet → server; label A–D. | ☐ |
| Explain LAN/WAN/Internet, switch/AP/router, IP/port/protocol/DNS, NAT. | ☐ |
| Reproduce the HTTPS protection boundary table. | ☐ |
| Explain evil twin, DNS spoofing, on-path attacker, firewall, authentication vs authorization, segmentation. | ☐ |
| Explain any network risk as location → weakness → control. | ☐ |

> **Best final strategy**
>
> Do not memorize isolated definitions only. Pick one case (WannaCry is the best: it appears in weeks 2, 5 and 6) and practise telling it three ways: as a risk, as malware, and as a network path.

**End of Midterm Study Guide**

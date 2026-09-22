# Week 01 — Introduction to Computer Security

> Protect information, systems, and people through responsible decisions.
> Slides: [week01-introduction-to-computer-security.pdf](lecture/week01-introduction-to-computer-security.pdf)

**Contents**
1. Orientation and Security Basics
2. The CIA Triad
3. Everyday Security and Ethics

**Course goals.** By the end of the course you should be able to:
1. **Define security.** Describe what computer security protects, in plain language.
2. **Use the CIA triad.** Ask confidentiality, integrity and availability questions.
3. **Choose a safe response.** Act carefully, ethically, and only with permission.

---

## 1. Orientation and Security Basics

### This course teaches protection, not attack

| We will learn | We will not do |
|---|---|
| How security problems happen | Attack real systems |
| How controls reduce risk | Use real passwords |
| How to respond safely | Download real malware |
| How to think ethically | Scan university networks |
| How to explain decisions | Test without permission |

### Security begins with something valuable

Security always starts with the question *what are we protecting?* The lecture groups the answer into three areas:

| | What it is | Examples | Why it matters |
|---|---|---|---|
| **Information** | What we are trying to protect | Grades, messages, research, identity data, payment details | Loss, exposure or change hurts the owner |
| **Devices + services** | The things we depend on | Phones, laptops, LMS, email, cloud storage, campus Wi-Fi | Without them we can't reach the information |
| **People + reputation** | Why security ultimately matters | Time, trust, privacy, safety, the ability to study or work | Every technical failure lands on a person |

### Definition: computer security

> **Computer security** is the set of ideas, practices, and controls used to reduce **unauthorized access**, **unwanted change**, and **harmful disruption**.

A short version: **protect access → protect accuracy → protect use.** These three map directly onto the CIA triad in Part 2 (confidentiality, integrity, availability).

### Your day depends on connected systems

A single morning may involve unlocking a phone, opening university email, joining campus Wi-Fi, reading an LMS notice, paying online and saving work to the cloud.

Modern life feels simple because technology **hides complexity**. Part of cybersecurity is understanding those hidden dependencies and **what happens when one of them fails or is compromised**. For example, if campus Wi-Fi is down, you can't reach the LMS even though the LMS itself works fine.

### Good security avoids two unhelpful extremes

| Too little protection | Fear without judgment |
|---|---|
| "Nothing bad has happened, so we are safe." | "Every device and person is an immediate disaster." |
| **Result:** problems are ignored until an incident causes damage. | **Result:** useful systems become hard to use and attention is wasted. |

The goal is **reasonable, proportionate** protection: take real risks seriously without paralysing normal work.

### Security needs people, process, and technology

- **People** make choices and follow rules.
- **Process** defines what to do and when.
- **Technology** blocks, detects, records, or recovers.

Technology alone is never enough. A strong password system fails if a person gives the password away, or if there is no process for resetting a stolen account.

### Case 1: Meet Mina's university account

Mina uses **one account** for LMS lessons, university email, assignment submission, grades and shared files.

*If someone else gets access, what could happen?* Think about information being **seen**, information being **changed**, and Mina being **unable to use** the account.

The timeline of one morning:

| Time | What happens | Type of harm | CIA goal hit |
|---|---|---|---|
| 8:10 AM | Attacker reads years of private email and downloads personal documents | **Privacy** | Confidentiality |
| 8:25 AM | Messages sent from Mina's real email asking classmates and professors for money and files | **Impersonation** | Integrity (messages are not really from her) |
| 9:00 AM | Submitted assignment deleted or replaced; course files disappear | **Academic damage** | Integrity + Availability |
| 10:30 AM | Professor receives strange messages that appear to come from Mina | **Reputation** | Integrity (trust in her identity) |
| 11:00 AM | Mina can't access email, LMS or cloud files | **Lockout** | Availability |
| 11:59 PM | Assignment deadline | Pressure: the harm has a real cost | |

**Lesson:** one compromised account damages **all three** CIA goals and hurts people beyond Mina (classmates, the professor).

### Five words describe a security problem

| Term | Meaning |
|---|---|
| **Asset** | Something valuable |
| **Threat** | A possible cause of harm |
| **Vulnerability** | A weakness that could be used or triggered |
| **Control** | A safeguard that reduces risk |
| **Risk** | The possibility and consequence of harm |

Together they answer one chain of questions: **What do we value** (asset), **what could harm it** (threat), **why could that harm succeed** (vulnerability), **how serious would the result be** (risk), **and what can we do about it** (control)?

Applied to Mina: asset = her account and files; threat = an attacker; vulnerability = e.g. a reused or phished password; control = MFA, a unique password, backups; risk = losing privacy, grades and reputation before a deadline.

### Activity: identify the asset

> A student clicks on a false login link. An attacker may read university email and reset other accounts. **Which items are assets?**
> A. The link only  B. Email, account access, and identity  C. The attacker only

**Answer: B.** Email, account access and identity are valuable and need protection.
- The **link** is the *means* of attack (part of the threat), not something we value.
- The **attacker** is the *threat*.

---

## 2. The CIA Triad

Three questions explain almost every basic security goal.

| | Goal | Key question |
|---|---|---|
| **C** | **Confidentiality** | Who is allowed to see or access it? |
| **I** | **Integrity** | Is it correct, complete, and trustworthy? |
| **A** | **Availability** | Can authorized people use it when needed? |

### Confidentiality means authorized access

**Confidentiality** protects information from being seen or disclosed to people who are not allowed to have it.

- **School example:** only the student, the authorized instructor and approved staff should see a private grade.
- **Key question:** *Who is allowed to know?*

| Everyday controls | Confidentiality failures |
|---|---|
| Lock the screen | Reading another person's email |
| Use a strong, unique password | Publicly sharing a private file |
| Turn on multifactor authentication (MFA) | Sending data to the wrong person |
| Set sharing permissions | Shoulder-surfing a password |
| Avoid exposing private data | A stolen unlocked device |

### Integrity keeps information trustworthy

**Integrity** protects data and systems from **improper change or destruction**.

- **School example:** an assignment should arrive exactly as the student submitted it, and a grade should change only through an authorized process.
- **Key question:** *Can we trust that it is correct?*

**Integrity can fail by accident or by attack:**

| Accidental change | Intentional change |
|---|---|
| Editing the wrong row | Altering grades |
| Uploading an old file | Changing payment details |
| A software bug changes data | Modifying a message |
| Storage becomes corrupted | Planting false information |
| A user deletes content by mistake | Deleting evidence |

An accident still counts as a security problem, because the data is no longer trustworthy even though no one meant harm.

**Integrity controls:**
- **Access control** limits who can edit.
- **Validation** checks whether data follows expected rules (e.g. a grade must be 0–100).
- **Logs and version history** record what changed.
- **Hashes** can help detect whether a file changed.
- **Backups** help restore a known good copy.

### Availability means reliable access when needed

**Availability** keeps systems and information **usable for authorized users at the required time**.

- **School example:** the LMS must work when students need lessons, submit assignments or check announcements.
- **Key question:** *Can authorized users use it now?*

**Availability failures have many causes:**

| Intentional causes | Non-malicious causes |
|---|---|
| Denial-of-service (DoS) traffic | Power failure |
| Ransomware | Hardware failure |
| Deliberate deletion | Bad software update |
| Account lockout abuse | Network congestion |
| Sabotage | Fire, flood, or human error |

**Availability controls support recovery:**
- **Backups** preserve recoverable copies.
- **Redundancy** provides another component or path.
- **Maintenance** reduces preventable failures.
- **Monitoring** detects trouble early.
- **Recovery plans** explain how to restore service.

### CIA questions about the LMS

| Goal | Question | Good answer |
|---|---|---|
| C | Who may see each student's grade? | Only authorized people |
| I | Can assignments or grades change improperly? | Changes are controlled and traceable |
| A | Can students log in and submit on time? | The service remains usable or recovers |

### Security goals sometimes require balance

| More protection can add effort | One control can support several goals |
|---|---|
| **Example:** MFA improves confidentiality but adds a login step. | **Example:** a tested backup supports availability and may restore integrity after corruption. |
| The answer is **not** to remove protection; it is to make protection **usable**. | Good designs consider the **full system**. |

### Activity: which CIA goal is most affected?

| # | Situation | Answer | Why |
|---|---|---|---|
| 1 | A student's grades are posted publicly | **C** | Private information seen by people who shouldn't see it |
| 2 | Someone changes a submitted assignment | **I** | Data changed improperly |
| 3 | The LMS is offline before a deadline | **A** | Authorized users can't use the service when needed |
| 4 | A shared file is corrupted and cannot open | **I** (and **A**) | Corruption is improper change (integrity); as a result the file can't be used (availability) |

*(The slides don't give the answers; these follow from the definitions above.)*

### Explain CIA without using the letters

> *If you can explain it simply, you understand it.*

Sample completions:
- "**Confidentiality** matters when information is private, like my grades or messages, and only certain people should be allowed to see it."
- "**Integrity** matters when we need to trust that something is correct, like a submitted assignment arriving exactly as I sent it or a grade that nobody changed without permission."
- "**Availability** matters when I need a system at a specific time, like the LMS being up before an assignment deadline."

---

## 3. Everyday Security and Ethics

### Most security decisions happen before an alarm

Everyday moments are security decisions:
- A message asks you to act quickly.
- A device is left unlocked.
- A file-sharing setting looks too open.
- A friend asks for your account.
- A website requests unexpected information.

**The first decision is usually human: continue, pause, verify, or report?**

### Pause, check, report: a safe first response

| 1. **PAUSE** | 2. **CHECK** | 3. **REPORT** |
|---|---|---|
| Do not click, reply, install, or share. | Verify the sender, request, address, and context. | Use the official channel to report. |

### Urgency is designed to rush the decision

Example: a message says your account will close soon, provides a link, and asks you to sign in immediately.

**Warning signs:**
- unexpected urgency
- an unfamiliar sender
- a mismatched address
- a request for credentials

> **Pressure is a signal to slow down.**

### Safe response: stop and verify another way

1. Do **not** click the message link.
2. Do **not** enter a password or authentication code.
3. Open the **official** university site or app **yourself**.
4. Contact the help desk using a **known** address or number.
5. **Report** the suspicious message and follow guidance.

The key idea is **verifying through a route you choose**, not through the link or phone number in the message.

### Permission defines ethical security practice

**Authorized practice** has a clear **owner, scope, time, method, and purpose**. Without explicit permission, even a technically simple test may violate rules, privacy, law, or trust.

> **When scope is unclear: stop and ask.**

### Permission changes the ethical status

| Authorized | Unauthorized |
|---|---|
| A student scans an **instructor-provided lab machine** during the **scheduled exercise**, using the **approved steps**, then **submits findings privately**. | A student scans a **university server or public website because it is reachable**, then **shares discovered information with friends**. |

The action (a scan) can be technically the same in both. **Permission, scope, and how results are handled** make the difference. "Reachable" does not mean "allowed".

### Defense in depth limits one mistake

A safer system uses several **layers**:
- attentive users
- strong authentication
- device protection
- network controls
- monitoring
- backups and recovery

**No single layer is perfect.** Strong security **expects that individual controls can fail**, so another layer catches what one misses. For example, if Mina's password is phished, MFA can still stop the login, and if the file is deleted anyway, a backup restores it.

### Scenario activity: the urgent LMS message

> At 9:20 p.m., Mina receives: "Your university account will be disabled tonight. Confirm immediately." The sender address looks unusual. The link opens a login page that resembles the LMS.

1. **What assets are at risk?** Her university account and password, her email, LMS files, assignments and grades, her identity (it can be used to message others), and her time before the deadline.
2. **Which CIA goals could be affected?** **All three.** **C:** an attacker reads her email and files. **I:** the attacker sends messages as her or changes and deletes submissions. **A:** she could be locked out of her account.
3. **What should Mina do now?** **Pause.** Don't click. **Check** by opening the LMS herself through the usual address or app and seeing whether there is any real notice, or contact the university help desk through a known route. **Report** the message to university IT through the official channel.
4. **What must Mina avoid doing?** Clicking the link, entering her password or authentication code on that page, replying to the sender, installing anything, or forwarding the link to friends.

*Warning signs present:* urgency ("tonight", "immediately"), an unusual sender address, a look-alike login page, and a request for credentials.

---

## Q & A: check your understanding

**1. What does computer security protect?**
Systems, information, services, people, and other valuable assets.

**2. What do C, I, and A stand for?**
Confidentiality, integrity, and availability.

**3. Which CIA goal is most affected when a grade is changed without permission?**
Integrity, because the information was changed improperly.

**4. Why is explicit permission essential in security practice?**
Permission defines ownership, scope, and allowed actions. Without it, testing can become misuse.

**5. Give one control that supports confidentiality.**
Screen lock, a unique password, MFA, or correct sharing permissions.

**6. Why can an accidental error still be a security problem?**
An error can make data incorrect, expose information, or stop a service even without an attacker.

**7. What should you do first when an urgent message looks suspicious?**
Pause. Do not click, reply, install, or share. Then verify through a trusted route.

**8. Why do secure systems use several layers of defense?**
Any single control can fail. Complementary layers reduce the chance that one mistake causes major harm.

---

## Most important for exams

- **Definition:** computer security = ideas, practices, and controls that reduce **unauthorized access, unwanted change, and harmful disruption**.
- **CIA triad:** **C**onfidentiality (*who may see it?*), **I**ntegrity (*is it correct and trustworthy?*), **A**vailability (*can authorized users use it now?*). Be able to classify a scenario (e.g. grade changed = I, grades posted publicly = C, LMS offline = A).
- **Five words:** asset, threat, vulnerability, control, risk. Know each definition.
- **People + process + technology:** all three are needed.
- **Integrity can fail by accident**, not only by attack.
- **One control can serve several goals** (a backup helps A and I). Protection should be **usable**, not removed.
- **Safe response:** **Pause, check, report.** Verify through a route you choose, never the link in the message. **Pressure is a signal to slow down.**
- **Ethics:** authorized practice has an owner, scope, time, method, and purpose. *When scope is unclear, stop and ask.*
- **Defense in depth:** several layers, because any single control can fail.

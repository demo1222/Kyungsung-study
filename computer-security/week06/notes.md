# Week 06 — Networking Fundamentals for Security

> Where data travels and where security matters.
> Slides: [week06-networking-fundamentals-for-security.pdf](lecture/week06-networking-fundamentals-for-security.pdf)

**By the end you should be able to:**
1. Name the devices and follow a network path.
2. Explain IP addresses, ports, protocols, and DNS.
3. Locate a risk and choose a suitable control.

### Opening question

> A student opens the university LMS on café Wi-Fi. The browser shows a **certificate warning**. *Where could the problem be?* Discuss the **device**, the **network**, and the **website**.

The point of the question is that a warning doesn't tell you *where* the problem is. It could be:
- **the device** (wrong clock, malware, or software intercepting traffic),
- **the network** (a fake hotspot or a portal intercepting the connection),
- **the website** (an expired or wrong certificate on the real server).

The habit the whole lecture builds: **name the location first**, then the weakness, then the control.

---

## 1. Follow the network path

> A **network** connects devices so they can exchange data.

### One visit to the LMS

The laptop **sends a request**, the server **sends a response**. In the simple campus LAN used all lecture:

```
Student laptop --Wi-Fi--> Access point (AP) --cable--> Switch --> Router / firewall --> Internet routers
                                                         |                                    |
                                                   Shared printer                         LMS server
```

Real routes can include more devices.

### LAN, WAN, and the Internet

| Term | Meaning | Everyday example |
|---|---|---|
| **LAN** (Local Area Network) | A network in a limited local area | Computers and a printer in one lab |
| **WAN** (Wide Area Network) | Links networks over larger distances | A university links two distant sites |
| **Internet** | Many connected networks worldwide | Your campus reaches a cloud LMS |

A campus can contain **many separate LANs**.

### Endpoints send and receive data

An **endpoint** is a device at an end of a communication.

- **Client:** starts a request, such as a student's browser.
- **Server:** provides a service, such as course files.

Printers and cameras are also connected devices, so they are also part of the attack surface.

### The devices in between

| Device | What it does | Security concern |
|---|---|---|
| **Switch** | Forwards **Ethernet frames inside a LAN**. It learns local device addresses called **MAC addresses**. | An **unused cable socket** can be an entry point. |
| **Access point (AP)** | Lets **wireless** devices join a network. | **Who can connect, and which network do they reach?** |
| **Router** | Forwards **IP packets between networks**. Your **default gateway** is the next router for other networks. | Settings can be changed by an attacker. |

A home "Wi-Fi router" often combines **router + AP + switch** in one box, which is why people confuse the three.

> **Switches connect local devices. Routers connect networks.**

### Where can a network risk begin?

| Location | What could go wrong? | Useful control |
|---|---|---|
| **Device** | Malware uses the device's connections | Updates and endpoint protection |
| **Wi-Fi or cable socket** | An unauthorized device joins | Network access control |
| **Router settings** | An attacker changes settings | Protected admin access and updates |

A **control** is a measure that reduces a security risk (same meaning as in Week 2).

### Real example: WannaCry in 2017

- WannaCry spread to **reachable, unpatched** Windows systems.
- **Where was the weakness?** A vulnerable **SMB** service. SMB supports **file sharing**.
- **What could reduce spread?** **Install the fix**, and **restrict unnecessary SMB traffic**.

This is the Week 2 case seen from the network side: the same ransomware, but now the question is *how it reached the machines*. **Reachability is part of the risk.**

### Quick check

> The Internet connection fails. **Can a local printer still work?**

**Yes.** Printing is a **local** path (laptop → AP → switch → printer) and never leaves the LAN. Only paths that cross the router to other networks fail. This is why "Wi-Fi" and "the Internet" are different things.

### Activity: label the network

> Name A–D, then trace a print job and an LMS request. Add one risk beside a device or connection and explain why it belongs there.

**Answers:** A = **access point**, B = **switch**, C = **Internet routers**, D = **router / firewall**.

- **Print job:** laptop → AP → switch → printer. **Printing can stay local.**
- **LMS request:** laptop → AP → switch → router/firewall → Internet routers → LMS server. **The remote LMS path crosses other networks.**
- **Example risk:** an unknown device joins Wi-Fi. **Example control:** require approved network access.

---

## 2. Read a network connection

> An **address** identifies the destination. A **service** follows communication rules.

### An IP address helps deliver packets

An **Internet Protocol (IP) address** is a number for a **device's network connection (interface)**.

| Example item | Address in the classroom model |
|---|---|
| Student laptop | 192.168.10.24 |
| Default gateway | 192.168.10.1 |
| Remote LMS server | 198.51.100.20 |

> **An IP address does not prove a person's identity.** (Addresses are shared, reassigned and translated.)

### Private addresses and NAT

Inside the LAN, laptops have **private** addresses (192.168.10.24, 192.168.10.25). The router has a **public** side (203.0.113.5).

**NAT = Network Address Translation.** It **changes address information as traffic passes**, so many private devices share one public address. A result worth remembering: from the outside, those devices look like one address.

### A port identifies a service

One IP address can offer **several services**, so the port says which one:

| Port | Service |
|---|---|
| **443** | HTTPS website |
| **22** | SSH administration |

> **IP address: which network destination? Port number: which service at that destination?**

### Protocols define communication rules

| Protocol | Plain English | In the web example |
|---|---|---|
| **IP** | Delivers packets between networks | Destination address |
| **TCP** | Delivers data **reliably and in order** | Common transport for HTTP/1.1 and HTTP/2 |
| **TLS** (Transport Layer Security) | Protects a connection's data | Encryption and certificate checks |
| **HTTP** (Hypertext Transfer Protocol) | Defines web requests and responses | Request a course page |

- **HTTPS is HTTP protected by TLS.**
- **Certificate:** digital evidence used to **check the server's identity**.

### DNS looks up a name

**DNS = Domain Name System.** A **resolver** finds and returns DNS information.

1. Device asks: **lms.example.com?**
2. Resolver answers: **198.51.100.20**
3. Device connects to **198.51.100.20**

### The URL describes a web request

`https://lms.example.com/course/6`

| Part | Meaning |
|---|---|
| `https` | Use HTTP protected by TLS |
| `lms.example.com` | **Domain name.** DNS can find its address |
| `/course/6` | Path to a resource on the site |
| (port 443) | Default HTTPS port when no port is written |

> **Check the full domain name before signing in.** (Week 3's hostname lesson, now explained by DNS.)

### HTTP and HTTPS on the network

| HTTP | HTTPS |
|---|---|
| No TLS protection for the web content | TLS protects the web content **in transit** |
| Someone on the path **may read or change it** | Someone on the path **cannot normally read or change it** |
| Readable content, e.g. `course=6&student=demo` | A network observer sees **encrypted** content when TLS works correctly |

**Encryption** makes content unreadable without the right keys.

### HTTPS has a clear protection boundary

| Question | What HTTPS tells us |
|---|---|
| Can a nearby observer read the page content? | **Normally no**, when TLS works correctly |
| Is every website using HTTPS honest? | **No.** A phishing site can also use HTTPS |
| Can malware read data on my own device? | **Yes.** Endpoint security still matters |
| Is all network information hidden? | **No.** IP addresses and traffic timing may remain visible |

This table is the heart of the lecture: HTTPS protects **content in transit between the TLS endpoints**, and nothing else.

### Demo: a page makes network requests

Open DevTools → **Network** → reload the page. **A row is a resource request, not one network packet.** Clicking a request and choosing **Headers** shows the **Request URL** (the requested address) and **GET** (a request for content).

The browser can show clear content **because it is one endpoint** — decryption happens there.

### Quick check

> Which term answers each question?

| Question | Term |
|---|---|
| Where is it? | **IP address** |
| Which service? | **Port** |
| Which rules? | **Protocol** |
| What address matches the name? | **DNS** |

---

## 3. Locate and reduce risk

> A useful explanation names the **location**, the **weakness**, and the **control**.

### Security matters along the whole path

Five locations, each with its typical control:

| # | Location | Control that applies there |
|---|---|---|
| 1 | **Device** | Antivirus / endpoint protection, updates |
| 2 | **Access** (Wi-Fi, sockets) | Authenticated Wi-Fi, network access control |
| 3 | **Boundary** (router/firewall) | Firewall rules |
| 4 | **Data in transit** | TLS (HTTPS) |
| 5 | **Server** | Permissions, authentication and authorization |

> **Point to the location before naming the control.**

### Risk at access: a fake hotspot

Café scenario: two networks advertise the **same familiar name**.

| Wi-Fi name (SSID) | What the name proves |
|---|---|
| Campus_Guest | Only the advertised name |
| Campus_Guest | It could belong to another operator |

**Evil twin:** a fake access point that **imitates a trusted Wi-Fi network**.

**Response:** verify the network, follow approved setup instructions, and **stop at certificate warnings** — which answers the opening café question.

### Risk in DNS: a false destination

**DNS spoofing** supplies **false DNS information**.

| Question | Expected answer | False answer |
|---|---|---|
| lms.example.com? | 198.51.100.20 (intended service) | 198.51.100.50 (wrong service) |

A false DNS answer **can redirect traffic**, but **it does not automatically defeat TLS**: the fake server still has to present a certificate for that name, which is why the warning appears.

### Risk in transit: an on-path attacker

**On-path attacker:** someone positioned to **intercept or influence traffic** (browser → network intermediary → web server).

- **HTTP content can be exposed.**
- **Correct HTTPS protects content between its TLS endpoints.**

### Risk at a service: too much exposure

> A server should expose **only the access it needs**.

| Connection | Example rule | Reason |
|---|---|---|
| Public users to **HTTPS 443** | **Allow** required website traffic | Students need the LMS |
| Public users to **SSH 22** | **Deny** public administration | Limit admin access |
| Approved admin path to **SSH** | **Allow** authorized admins | Maintain the server securely |

**Firewall:** software or hardware that **allows or blocks traffic using rules**.

### Risk at the server: excessive access

The LMS receives an **encrypted** request. It must still decide **what the user may read**:

- **Authentication:** *Who are you?* The system checks your **identity**.
- **Authorization:** *What may you do?* The system checks your **permissions**.

Encryption in transit says nothing about permissions at the end. (Compare Week 3: **recognition is not authorization**.)

### Segmentation limits unnecessary paths

**Segmentation** divides a network into groups and controls communication between them.

- Guest devices → staff records server: **DENY**
- Guest devices → Internet access: **ALLOW**

### A risk explanation needs a location

| Location | Weakness or concern | Control that fits |
|---|---|---|
| Laptop | Unpatched software | Install supported updates |
| Wi-Fi access | Unknown network operator | Verify the approved connection |
| Web traffic | Sensitive data over HTTP | Use valid HTTPS |
| Private service | Access from unnecessary users | Limit reachability and permissions |

### Activity: a small office network

> A small office shares one network. (1) Guests connect to Wi-Fi for Internet access. (2) Staff use a payroll server; a printer runs old firmware. (3) The server allows administration from any Internet address.
> Draw the path, mark two risks, place two controls, and explain how each helps.

**One defensible answer:**

| Risk | Control | Why it helps |
|---|---|---|
| Guests can reach staff systems | **Separate guest access** and enforce traffic rules | Limits access to private services |
| Administration is public | Allow only an **approved admin path** | Reduces unnecessary exposure |
| Printer firmware is old | **Update it**, or restrict it while arranging replacement | Reduces exploitable weaknesses |

---

## Q&A: check your understanding

**1. What is the difference between a LAN and a WAN?**
A LAN covers a local area. A WAN links networks over larger distances.

**2. What does an access point do?**
An AP lets wireless devices join a network.

**3. How do a switch and a router differ?**
A basic switch forwards **within** a LAN. A router forwards **between** networks.

**4. What does an IP address identify?**
A network interface, for packet delivery.

**5. What does a port number identify?**
A logical port identifies an **application or service endpoint**.

**6. What does DNS do when you open a website?**
It can return an **address** for the website's **domain name**.

**7. What protection does HTTPS add?**
TLS protects web content **in transit** and **checks the server certificate**.

**8. Can a phishing website use HTTPS?**
**Yes.** HTTPS alone does not prove the site's owner is honest.

**9. Why does an exposed service need attention?**
A reachable service may allow access or expose a weakness. Limit and maintain it.

**10. How can segmentation reduce harm?**
It limits unnecessary communication and can **restrict an incident's spread**.

---

## Assignment: your own network path

> Choose one: opening a course page, making a video call, or using a shared printer.
> 1. Draw the endpoints and the network devices in between.
> 2. Explain where IP addresses, ports, or DNS help in your example.
> 3. Mark **two** possible risks and add a suitable control for each.
> Submit one PDF to LMS: **diagram + short explanations**.

How to approach it:
- Keep the diagram in the lecture's order: **device → AP → switch → router/firewall → Internet → server**. A printer job stops at the switch; that is a good contrast to show you understand local vs remote.
- For part 2, say which question each term answers: **IP = where, port = which service, DNS = which address matches the name**.
- For part 3, use the **location → weakness → control** pattern, and pick risks at **different** locations (e.g. evil-twin Wi-Fi at access, public SSH at the service) so the two controls aren't the same idea twice.

**Sources from the slides:** Cisco (switch vs router; network segmentation), Cloudflare (What is DNS?; What is HTTPS?), Microsoft (WannaCrypt, 12 May 2017), Google (Inspect network activity).

---

## Most important for exams

- **Five ideas the lecture ends on:** Wi-Fi connects you to a **network**, which is not the same as the Internet; **switches connect local devices, routers connect networks**; **IP, ports and protocols answer different questions**; **DNS finds an address, HTTPS protects content in transit**; controls are needed **at the device, on the path, and at the service**.
- **LAN / WAN / Internet** definitions with an example each.
- **Switch** = frames inside a LAN, learns **MAC addresses**. **AP** = wireless devices join. **Router** = IP packets between networks; **default gateway** = next router. A home box combines all three.
- **IP = which destination, port = which service** (443 HTTPS, 22 SSH), **protocol = which rules** (IP, TCP, TLS, HTTP). **HTTPS = HTTP + TLS.** **An IP address does not prove identity.**
- **NAT** translates private addresses to a public one.
- **DNS** maps a **name** to an **address**; **DNS spoofing** gives a false answer but **does not by itself defeat TLS**.
- **HTTPS boundary table** (very likely exam material): protects content in transit; does **not** make a site honest, does **not** stop malware on your device, does **not** hide IP addresses and timing.
- **Evil twin** = fake AP with a familiar SSID. **On-path attacker** = positioned to intercept or influence traffic.
- **Firewall** = allows/blocks traffic by rules; expose only what is needed. **Authentication (who are you)** vs **authorization (what may you do)**.
- **Segmentation** limits unnecessary paths and an incident's spread.
- **Explain any risk as location → weakness → control.** Expect to label the campus diagram (A = AP, B = switch, C = Internet routers, D = router/firewall).

<style>h3 { color: #000; font-weight: bold; }</style>

My example: opening a course page on the LMS from the library Wi-Fi

### 1. Diagram

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 250" width="100%" font-family="Arial" font-size="12" text-anchor="middle">
<g fill="none" stroke="#000">
<rect x="5" y="80" width="90" height="50"/>
<rect x="125" y="80" width="90" height="50"/>
<rect x="245" y="80" width="90" height="50"/>
<rect x="365" y="80" width="90" height="50"/>
<rect x="485" y="80" width="90" height="50"/>
<rect x="605" y="80" width="90" height="50"/>
<rect x="365" y="185" width="90" height="45"/>
<line x1="95" y1="105" x2="125" y2="105" stroke-dasharray="4"/>
<line x1="215" y1="105" x2="245" y2="105"/>
<line x1="335" y1="105" x2="365" y2="105"/>
<line x1="455" y1="105" x2="485" y2="105"/>
<line x1="575" y1="105" x2="605" y2="105"/>
<line x1="410" y1="130" x2="410" y2="185"/>
</g>
<text x="50" y="102">My laptop</text><text x="50" y="118">192.168.10.24</text>
<text x="170" y="102">Access point</text><text x="170" y="118">(Wi-Fi)</text>
<text x="290" y="109">Switch</text>
<text x="410" y="102">Router / firewall</text><text x="410" y="118">192.168.10.1</text>
<text x="530" y="102">Internet</text><text x="530" y="118">routers</text>
<text x="650" y="102">LMS server</text><text x="650" y="118">198.51.100.20</text>
<text x="410" y="204">DNS resolver</text><text x="410" y="220">(name to IP)</text>
<text x="110" y="72">Wi-Fi</text>
<text x="230" y="72">cable</text>
<text x="650" y="148">port 443 (HTTPS)</text>
<text x="50" y="30" font-weight="bold">Risk 1</text><text x="50" y="46">old software</text>
<text x="110" y="160" font-weight="bold">Risk 2</text><text x="110" y="176">fake hotspot</text>
<g stroke="#000"><line x1="50" y1="52" x2="50" y2="78"/><line x1="110" y1="146" x2="110" y2="108"/></g>
</svg>

Endpoints: my laptop (client) and the LMS server. Devices in between: access point, switch, router/firewall and the Internet routers.

### 2. IP addresses, ports and DNS

DNS: I type lms.example.com in the browser. My laptop asks the DNS resolver for this name and gets back the address 198.51.100.20. Without DNS I would have to remember the number.

IP addresses: my laptop has the private address 192.168.10.24. The LMS server is not in my network, so the laptop sends the packets to the default gateway 192.168.10.1 (the router). The router uses NAT to change my private address to its public one and forwards the packets to 198.51.100.20. The IP address tells the routers where to deliver the packets.

Ports: the server can run more than one service on the same IP address. The address starts with https, so the browser connects to port 443, which is the HTTPS website. The port tells the server which service I want.

### 3. Two risks and controls

Risk 1 (at the laptop): my laptop has old software that was not updated. Malware could use a known weakness and then read what I do on the LMS, even if the connection uses HTTPS.
Control: install updates and use endpoint protection. Updates fix the known weaknesses, so the malware has fewer ways to get in.

Risk 2 (at the Wi-Fi access): someone makes a fake hotspot with the same name as the library Wi-Fi (evil twin). If I connect to it, the attacker is on the path of my traffic and can try to send me to a fake login page.
Control: connect only to the approved network using the university setup instructions, and stop if the browser shows a certificate warning. HTTPS also keeps the page content unreadable for the person running the hotspot.

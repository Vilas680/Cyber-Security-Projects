keywords = {
    "threat": ["kill", "attack", "bomb", "hurt", "destroy", "injure", "weapon", "shoot", "violence"],
    "bullying": ["stupid", "loser", "ugly", "idiot", "dumb", "fat", "weirdo", "suck", "hate", "unwanted", "worthless"],
    "illegal": ["drugs", "fraud", "scam", "hack", "carding", "stolen", "illegal", "money laundering", "pirate", "phish", "exploit"],
    "privacy": ["password", "otp", "bank", "account", "aadhar", "ssn", "credit card", "personal info", "details"],
    "harassment": ["harass", "abuse", "blackmail", "stalk", "creep", "vulture", "extort", "porn", "sextortion", "shame"],
    "Authentication":["Authentication", "bypass1", "token", "session", "SSO", "SAML", "federated", "expired", "insecure-login", "brute-force"],
    "Network Security":["Firewall", "port", "router", "protocol", "scanning", "traffic", "IDS", "IPS", "packet", "network-config"],
    "Data Protection":["Encryption", "AES", "hashing", "plaintext", "cipher", "decryption", "unencrypted", "key-management", "custodian", "GDPR"],
    "Application Attacks":["SQL Injection", "XSS", "XSRF", "phishing-kit", "buffer-overflow", "remote-code", "API-key", "injection", "cross-site", "header"],
    "Data Breach":["Data-breach", "compromised", "exposed-data", "leaked", "notification", "reporting", "incident-response", "remediation", "audit-log", "PII"],
    "Regulatory Law":["GDPR", "CCPA", "HIPAA", "SOX", "PCI DSS", "FCRA", "Patriot Act", "IT Act", "compliance", "regulation"],
    "Legal/Jurisdiction":["Jurisdiction", "warrant", "subpoena", "liability", "consent", "waiver", "IPR", "copyright", "patent", "trademark"],
    "Digital Evidence":["Digital-Evidence", "chain-of-custody", "admissible", "forensic", "metadata", "hashing", "timestamp", "archive", "log-retention", "preservation"],
    "Policy/Controls":["Policy", "AUP", "terms-of-service", "privacy-notice", "acceptable-use", "due-diligence", "risk-assessment", "control", "governance", "framework"]
}

cyber_responses = {
    "what is cyber crime": "Cybercrime refers to illegal activities performed using computers or the internet.",
    "types of cyber crime": "Common types include phishing, identity theft, hacking, cyberbullying, ransomware, and online fraud.",
    "what is phishing": "Phishing is when attackers pretend to be trusted people or companies to steal your passwords or banking details.",
    "how to stay safe online": "Use strong passwords, enable 2FA, avoid unknown links, and never share OTP or banking details.",
    "what is cyber bullying": "Cyberbullying involves sending insulting, threatening, or harmful messages online.",
    "what is malware": "Malware is harmful software like viruses, spyware, or ransomware.",
    "what is ransomware": "Ransomware locks your files and demands money to unlock them.",
    "how to report cyber crime": "In India, report cybercrimes at https://cybercrime.gov.in or call 1930.",
    "what is identity theft": "Identity theft happens when someone steals your personal information to impersonate you.",
    "what is online fraud": "Online fraud involves cheating people on the internet to steal money or data.",
    "what is hacking": "Hacking means unauthorized access to systems, networks, or accounts.",
    "what is two-factor authentication": "2FA adds a second layer of security (like a code sent to your phone) beyond just a password.",
    "what is a vpn": "A VPN (Virtual Private Network) encrypts your internet connection, hiding your activity and location from others.",
    "what is encryption": "Encryption is the process of converting information into a code to prevent unauthorized access.",
    "how to create a strong password": "Use a mix of uppercase/lowercase letters, numbers, and symbols, and make it long—at least 12 characters.",
    "what is spyware": "Spyware is malware that secretly monitors and records a user's activity without their permission.",
    "what is adware": "Adware is software that automatically displays or downloads unwanted advertisements.",
    "what is a trojan": "A Trojan Horse is malicious software disguised as legitimate software.",
    "what is a virus": "A computer virus is a type of malware that self-replicates and spreads by inserting copies of itself into other computer programs.",
    "what is smishing": "Smishing is phishing conducted over text messages (SMS).",
    "what is vishing": "Vishing is phishing conducted over voice calls or VoIP.",
    "what is denial of service": "A Denial of Service (DoS) attack floods a server with traffic to overwhelm it, making the service unavailable.",
    "what is ddos": "DDoS (Distributed Denial of Service) is a DoS attack launched from multiple compromised computer systems.",
    "what is social engineering": "Social engineering is the psychological manipulation of people into performing actions or divulging confidential information.",
    "what is a botnet": "A botnet is a network of private computers infected with malware and controlled as a group without the owners' knowledge.",
    "what is a firewall": "A firewall is a network security system that monitors and controls incoming and outgoing network traffic.",
    "should i click on popups": "No. Avoid clicking on pop-up ads, especially those that warn you about a virus, as they are often malicious.",
    "what is blockchain": "Blockchain is a distributed, decentralized ledger that records transactions across many computers.",
    "what is cryptocurrency fraud": "This involves scams where criminals trick victims into investing in fake digital currencies.",
    "how to secure my wi-fi": "Use a strong password (WPA3 or WPA2), change the default router name, and disable remote management.",
    "what is data breach": "A data breach is a security incident where sensitive, protected, or confidential data is copied, transmitted, viewed, or stolen.",
    "what is ethical hacking": "Ethical hacking is legally penetrating a system with permission to find vulnerabilities and improve security.",
    "what is a zero-day exploit": "A zero-day exploit is an attack that exploits a software vulnerability unknown to the vendor, meaning they have 'zero days' to fix it.",
    "how do i check for a secure website": "Look for 'https://' at the start of the web address and a padlock icon in the browser bar.",
    "what is shoulder surfing": "Shoulder surfing is when attackers secretly observe a person's private information over their shoulder, like a PIN or password.",
    "what is scareware": "Scareware is malicious software that uses deceptive alerts to trick users into buying unnecessary software.",
    "what is catfishing": "Catfishing is the act of creating a false persona on social media to deceive someone.",
    "what is pharming": "Pharming redirects a user to a malicious website, even if they type the correct address.",
    "what is a public wi-fi risk": "Public Wi-Fi is often unsecured, making it easy for hackers to intercept your data.",
    "what is a keylogger": "A keylogger is software or hardware that records every keystroke made by a user.",
    "what is digital signature": "A digital signature is a mathematical technique used to validate the authenticity and integrity of a message or document.",
    "what is grooming": "Online grooming is when an adult builds a relationship with a child online for exploitative purposes.",
    "what is a strong password manager": "A password manager is an encrypted tool that stores and manages all your passwords securely.",
    "what is metadata": "Metadata is data that provides information about other data, such as the date a photo was taken or where a document was created.",
    "what is sim swapping": "SIM swapping is when a criminal convinces a phone carrier to switch a victim's phone number to a new SIM card they control.",
    "what is deepfake": "Deepfakes are synthetic media in which a person in an existing image or video is replaced with someone else's likeness using AI.",
    "what is two-step verification": "This is often used interchangeably with 2FA, but sometimes refers to simpler methods like a code sent to email after a password.",
    "what is security patch": "A security patch is a software update designed to fix security vulnerabilities in a program or operating system.",
    "what is phishing email look like": "Look for poor grammar, urgent language, and requests for private information or clicking an unfamiliar link.",
    "what is data minimization": "Data minimization is the principle that organizations should only collect, process, and store the minimum data necessary.",
    "what is gdpr": "GDPR (General Data Protection Regulation) is a European law focused on data protection and privacy.",
}

def analyze_text(text):
    text = text.lower()
    alerts = []

    for category, words in keywords.items():
        for w in words:
            if w in text:
                alerts.append((category, w))

    return alerts

def chatbot_answer(text):
    text = text.lower()
    for q in cyber_responses:
        if q in text:
            return cyber_responses[q]
    return None


print ("Chatbot Activated! Scanning for cybercrime indicators...\n")
print("Type 'Exit' to stop.\n")

while True:
    user_input = input("Enter text to scan: ")

    if user_input.lower() == "exit":
        print("Bot: Chatbot stopped. Stay safe online!")
        break


    answer = chatbot_answer(user_input)
    if answer:
        print("Bot:", answer)
        print()
        continue

    alerts = analyze_text(user_input)

    if alerts:
        print("Suspicious Content Found:")
        for c, w in alerts:
            print(f"- {w} ({c})")
        
        score = len(alerts) * 15
        if score >= 35:
            seven = "High Risk"
        elif score >= 25:
            seven = "Medium Risk"
        else:
            seven = "Low Risk"
        
        print(f"Severity Level → {seven}\n")
    else:
        print(" No cybercrime indicators detected.")
        print(" You can continue chatting safely.")
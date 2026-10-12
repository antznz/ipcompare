# IP Compare

A lightweight Python utility for comparing IP addresses across two files. Extracts IPv4 addresses from unstructured text, removes duplicates and identifies matches against an approved IP list.

Useful for penetration testing and external attack surface reconnaissance to identify discovered IP addresses that match explicitly authorised targets.

**Usage:**
```bash
python3 ip_compare.py discovered.txt approved_ips.txt
```

**Features:**
- Extracts IPv4 addresses from text files using regex.
- Automatically removes duplicates.
- Identifies IP addresses present in both files.
- Supports unstructured input containing additional text.
- Requires no third-party Python dependencies.

**Limitations:** Supports exact IPv4 matching only. CIDR ranges, IPv6 and strict IP address validation are not supported.

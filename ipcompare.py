import re
import sys

def read_ips_from_file(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    # Extract valid IP addresses using regex
    ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    ips = set()
    for line in data:
        ips.update(ip_pattern.findall(line))
    return ips

def main():
    # Ensure file paths are provided as arguments
    if len(sys.argv) != 3:
        print("Usage: python3 ip_compare.py <path_to_ip_data> <path_to_approved_ips>")
        sys.exit(1)

    data_file = sys.argv[1]
    approved_file = sys.argv[2]

    # Read IPs from both files
    data_ips = read_ips_from_file(data_file)
    approved_ips = read_ips_from_file(approved_file)

    # Find matching approved IPs
    matching_approved_ips = data_ips.intersection(approved_ips)

    # Output the results
    if matching_approved_ips:
        print("Matching IPs have been found:")
        for ip in matching_approved_ips:
            print(ip)
    else:
        print("No matching approved IPs found.")

if __name__ == "__main__":
    main()

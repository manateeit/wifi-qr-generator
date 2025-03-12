#!/usr/bin/env python3

import qrcode
import argparse

def generate_wifi_qr(ssid, password, security="WPA", output_file="wifi_qr.png"):
    """
    Generate a WiFi QR code with the given network details.
    
    Args:
        ssid (str): The WiFi network name
        password (str): The WiFi password
        security (str): Security type (default: WPA)
        output_file (str): Output file name (default: wifi_qr.png)
    """
    # Format the WiFi network string according to the standard
    # WIFI:S:<SSID>;T:<Security>;P:<Password>;;
    wifi_string = f"WIFI:S:{ssid};T:{security};P:{password};;"
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add the WiFi string data
    qr.add_data(wifi_string)
    qr.make(fit=True)
    
    # Create an image from the QR Code
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    qr_image.save(output_file)
    print(f"QR code has been generated and saved as '{output_file}'")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate a WiFi QR Code')
    parser.add_argument('--ssid', required=True, help='WiFi network name')
    parser.add_argument('--password', required=True, help='WiFi password')
    parser.add_argument('--output', default='wifi_qr.png', help='Output file name (default: wifi_qr.png)')
    parser.add_argument('--security', default='WPA', help='Security type (default: WPA)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Generate the QR code
    generate_wifi_qr(args.ssid, args.password, args.security, args.output)

if __name__ == "__main__":
    main() 
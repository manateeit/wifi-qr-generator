# WiFi QR Code Generator

A simple Python script that generates QR codes for WiFi network configuration. When scanned, these QR codes automatically configure WiFi settings on mobile devices.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/manateeit/wifi-qr-generator.git
cd wifi-qr-generator
```

2. Create a virtual environment (optional but recommended):
```bash
python3 -m venv wifi
source wifi/bin/activate  # On Unix/macOS
# or
.\wifi\Scripts\activate  # On Windows
```

3. Install required packages:
```bash
pip install qrcode pillow
```

## Usage

Basic usage:
```bash
./wifi_qr_generator.py --ssid "Your_WiFi_Name" --password "Your_WiFi_Password"
```

Options:
- `--ssid`: Your WiFi network name (required)
- `--password`: Your WiFi password (required)
- `--output`: Custom output filename (default: wifi_qr.png)
- `--security`: Security type (default: WPA)

Examples:
```bash
# Basic usage
./wifi_qr_generator.py --ssid "MyNetwork" --password "MyPassword123"

# Custom output filename
./wifi_qr_generator.py --ssid "MyNetwork" --password "MyPassword123" --output "custom_name.png"

# Different security type
./wifi_qr_generator.py --ssid "MyNetwork" --password "MyPassword123" --security "WEP"
```

## Features

- Generates QR codes that work with both iOS and Android devices
- Supports different security types (WPA, WEP)
- Customizable output filename
- Simple command-line interface

## Requirements

- Python 3.x
- qrcode
- pillow

## License

MIT License 
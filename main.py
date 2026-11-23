
import re
from datetime import datetime, timezone

import dns.resolver
import phonenumbers
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def check_email():
    email = input("\nEmail address: ").strip()

    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        print("Invalid email format.")
        return

    domain = email.split("@")[1]

    try:
        records = dns.resolver.resolve(domain, "MX")
        print(f"\nValid format: Yes")
        print(f"Domain: {domain}")
        print("Mail server records:")
        for record in records:
            print(f"- {record.exchange}")
    except Exception:
        print(f"\nEmail format: Valid")
        print(f"Domain: {domain}")
        print("MX records: Not found or unavailable")


def search_username():
    username = input("\nUsername: ").strip().lstrip("@")

    if not username or " " in username:
        print("Please enter a valid username.")
        return

    sites = {
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}/",
        "Instagram": f"https://www.instagram.com/{username}/",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "X": f"https://x.com/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
    }

    print("\nPublic profile links to check:")
    for site, url in sites.items():
        print(f"{site}: {url}")

    print("\nThese are candidate links, not confirmed accounts.")


def check_phone():
    number = input("\nPhone number (include country code): ").strip()

    try:
        parsed = phonenumbers.parse(number, None)

        print("\nPhone information:")
        print("Valid number:", phonenumbers.is_valid_number(parsed))
        print("Possible number:", phonenumbers.is_possible_number(parsed))
        print("International format:",
              phonenumbers.format_number(
                  parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL
              ))
        print("Country/region:",
              phonenumbers.region_code_for_number(parsed))

        print("\nThis does not identify the owner or locate the phone.")
    except phonenumbers.NumberParseException:
        print("Could not parse this number. Include its country code.")


def gps_to_decimal(degrees, minutes, seconds, direction):
    value = float(degrees) + float(minutes) / 60 + float(seconds) / 3600

    if direction in ("S", "W"):
        value = -value

    return value


def inspect_photo():
    path = input("\nPhoto file path: ").strip().strip('"')

    try:
        image = Image.open(path)
        exif = image.getexif()

        print("\nPhoto information:")
        print("File:", path)
        print("Image size:", image.size)
        print("Format:", image.format)

        if not exif:
            print("No EXIF metadata found.")
            return

        print("\nAvailable metadata:")
        for tag_id, value in exif.items():
            tag = TAGS.get(tag_id, str(tag_id))
            if tag != "GPSInfo":
                print(f"{tag}: {value}")

        gps = exif.get_ifd(34853)

        if gps:
            gps_data = {
                GPSTAGS.get(key, key): value
                for key, value in gps.items()
            }

            lat = gps_data.get("GPSLatitude")
            lat_ref = gps_data.get("GPSLatitudeRef")
            lon = gps_data.get("GPSLongitude")
            lon_ref = gps_data.get("GPSLongitudeRef")

            if lat and lat_ref and lon and lon_ref:
                latitude = gps_to_decimal(*lat, lat_ref)
                longitude = gps_to_decimal(*lon, lon_ref)

                print("\nGPS coordinates:")
                print("Latitude:", latitude)
                print("Longitude:", longitude)
                print("Note: These coordinates come from the photo's metadata.")
            else:
                print("\nNo complete GPS coordinates found.")
        else:
            print("\nNo GPS metadata found.")

    except FileNotFoundError:
        print("File not found.")
    except Exception as error:
        print("Could not inspect photo:", error)


def decode_discord_id():
    discord_id = input("\nDiscord ID: ").strip()

    if not discord_id.isdigit():
        print("Discord ID must contain only numbers.")
        return

    try:
        timestamp_ms = (int(discord_id) >> 22) + 1420070400000
        created = datetime.fromtimestamp(
            timestamp_ms / 1000, tz=timezone.utc
        )

        print("\nDiscord ID information:")
        print("Creation time (UTC):", created.strftime("%Y-%m-%d %H:%M:%S"))
        print("This does not reveal the account owner's identity.")

    except (ValueError, OverflowError, OSError):
        print("Could not decode this ID.")


def main():
    while True:
        print("""
================================
       GHOSTTRACE OSINT
================================
1. Check an email
2. Search a username
3. Check a phone number
4. Inspect a photo
5. Decode a Discord ID
6. Exit
================================
""")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            check_email()
        elif choice == "2":
            search_username()
        elif choice == "3":
            check_phone()
        elif choice == "4":
            inspect_photo()
        elif choice == "5":
            decode_discord_id()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose 1-6.")


if __name__ == "__main__":
    main()

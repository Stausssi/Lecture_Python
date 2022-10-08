def main():
    printChecksum(calculateChecksum(getUserInput()))


def getUserInput():
    # Prompt the user to enter their name and replace special chars
    return input("Enter your name: ") \
        .lower() \
        .replace("ä", "ae") \
        .replace("ö", "oe") \
        .replace("ü", "ue") \
        .replace("ß", "ss")


def calculateChecksum(name: str):
    # Calculate the checksum
    checksum = 0
    for char in name:
        num = ord(char)

        # Only consider regular letters
        if 97 <= num <= 122:
            checksum += num % 96

    return checksum


def printChecksum(checksum):
    # Print the given sum and divide it
    print(f"Your name has the checksum {checksum}.")
    print(f"Divided by 2: {str(checksum / 2).replace('.0', '')}")


if __name__ == "__main__":
    main()

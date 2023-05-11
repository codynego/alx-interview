#!/usr/bin/python3

"""
log parsing
"""
import re
import sys


def validate_input(inputs):
    pattern = (
        r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.+\] "GET /projects/260 '
        r'HTTP/1\.1" \d{3} \d+$'
    )
    match = re.match(pattern, inputs)
    if match:
        return True
    else:
        return False


def log_parser():
    line_count = 0
    total_size = 0
    codes = {}
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    try:
        for line in sys.stdin:
            if validate_input(line):
                line_count += 1
                input_list = line.split("/")
                filesize = input_list[-1].split(' ')[-1]
                status_code = input_list[-1].split(' ')[-2]
                total_size += int(filesize)
                if status_code in codes:
                    codes[status_code] += 1
                else:
                    codes[status_code] = 0
                    codes[status_code] += 1
                if line_count % 10 == 0:
                    print(f"File size: {total_size}")
                    codes = {key: codes[key] for key in sorted(codes)}
                    for k, v in codes.items():
                        print(f"{k}: {v}")
            else:
                continue
    
    except Exception as err:
        pass

    finally:
        print("File size:", total_size)
        codes = {key: codes[key] for key in sorted(codes)}
        for k, v in codes.items():
            print(f"{k}: {v}")


if __name__ == "__main__":
    log_parser()

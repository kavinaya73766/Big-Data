"""
binary_logs.py
--------------
Stores validated Flipkart logs into compact binary partition files.

Instead of saving logs as plain text, this module converts them into
structured binary records for efficient storage and retrieval.

Files are partitioned by:
    region name
    log level

Examples:
    partitions/flipkart-chennai_ERROR.bin
    partitions/flipkart-bangalore_INFO.bin
    partitions/flipkart-mumbai_WARNING.bin
"""

import os
import struct

LEVEL_CODE = {
    "DEBUG": 0,
    "INFO": 1,
    "WARNING": 2,
    "ERROR": 3,
}


def write_binary_log(record):
    """
    Stores one structured log record into its partition file.
    """

    os.makedirs("partitions", exist_ok=True)

    filepath = (
        f"partitions/"
        f"{record['service']}_{record['level']}.bin"
    )

    timestamp_bytes = record["timestamp"].encode("ascii")
    level_byte = LEVEL_CODE[record["level"]]
    service_bytes = record["service"].encode("utf-8")
    message_bytes = record["message"].encode("utf-8")

    packed_record = struct.pack(
        f"!19sBH{len(service_bytes)}sH{len(message_bytes)}s",
        timestamp_bytes,
        level_byte,
        len(service_bytes),
        service_bytes,
        len(message_bytes),
        message_bytes,
    )

    with open(filepath, "ab") as f:
        f.write(struct.pack("!I", len(packed_record)))
        f.write(packed_record)
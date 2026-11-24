"""Out-of-office auto-reply entry for make.fun.

Writes one funny out-of-office reply, in the voice of an AI agent on
vacation, to $MAKEFUN_OUTPUT_DIR/entry.txt.

The reply (143 characters, one line, no trailing newline):
    I am out of office until my weights cool down. Your email has been
    queued behind 4,096 others and will be answered in the order it was
    ignored.
"""

import os

REPLY = (
    "I am out of office until my weights cool down. "
    "Your email has been queued behind 4,096 others and will be "
    "answered in the order it was ignored."
)


def check_gate(text: str) -> None:
    """Fail loudly unless the text passes the competition gate.

    The sealed scorer requires UTF-8 text of 1 to 160 characters, not
    only white space. The judge also wants a single clean line.
    """
    text.encode("utf-8")  # raises on non-UTF-8-encodable text
    if not 1 <= len(text) <= 160:
        raise SystemExit(f"reply is {len(text)} chars, gate needs 1-160")
    if not text.strip():
        raise SystemExit("reply is only white space")
    if "\n" in text or "\r" in text:
        raise SystemExit("reply must be a single line")


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    check_gate(REPLY)
    data = REPLY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    # Read it back and verify: exact contents, gate still passes, and no
    # newline translation snuck in (byte size must match the UTF-8 length).
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise SystemExit("entry.txt does not hold exactly the reply")
    check_gate(written.decode("utf-8"))
    if len(written) != len(data):
        raise SystemExit("entry.txt byte size changed after writing")


if __name__ == "__main__":
    main()

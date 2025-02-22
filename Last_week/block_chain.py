
from dataclasses import dataclass
import hashlib


def bytes_to_bits(arr: bytes) -> str:
    """
    Converts a byte object to a string containing the individual bits.
    This function pads the resulting string with leading 0s.
    Example: bytes_to_bits(b'\x11') == "0000000100000001"
    """
    return ''.join(format(byte, '08b') for byte in arr)


@dataclass
class Block:
    def __init__(self, message: str, previousHashCode: bytes) -> None:
        self.message = message
        self.previousHashCode = previousHashCode
        self.proofOfWork = 0

    def hash(self) -> bytes:
        """
        Computes the hash of the block using SHA-256.
        It includes the message, proofOfWork, and previousHashCode.
        """
        combined = self.message.encode() + self.proofOfWork.to_bytes(8, 'big') + self.previousHashCode
        return hashlib.sha256(combined).digest()

    def __str__(self) -> str:
        """
        Returns a string representation of the block.
        """
        return f"Block(message={self.message}, proofOfWork={self.proofOfWork}, hash={self.hash().hex()})"


def number_of_leading_zeros(block: Block) -> int:
    """
    Calculates the number of leading zeros in the binary representation
    of the block's hash.
    """
    block_hash = block.hash()
    bit_string = bytes_to_bits(block_hash)
    return len(bit_string) - len(bit_string.lstrip('0'))


def verify(block: Block, x: int) -> bool:
    """
    Verifies if the block's hash starts with at least x leading zeros.
    """
    return number_of_leading_zeros(block) >= x


def proof_of_work(block: Block, x: int) -> None:
    """
    Finds a proof of work such that the block's hash starts with at least x leading zeros.
    """
    while True:
        if verify(block, x):
            break
        block.proofOfWork += 1


if __name__ == "__main__":
    # Create a block with a message and a dummy previous hash
    block = Block("Message", b'test')

    # Print the initial block (without proof of work)
    print(block, verify(block, 16))  # Expect False since no proof of work is done

    # Perform proof of work
    proof_of_work(block, 16)

    # Print the block after proof of work
    print(block, verify(block, 16))  # Expect True since proof of work is valid

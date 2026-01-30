Since you are modifying the **first block** specifically, this is the classic **IV Bit-Flipping** attack. It is the cleanest form of the attack because you don't have to sacrifice any data (unlike flipping bits in the ciphertext, which garbles the corresponding block).

Here is the theory and the exact process to calculate the new IV.

### The Theory

In AES-CBC mode, the first block of plaintext () is produced by XORing the decrypted intermediate state with the Initialization Vector ().

The formula for decryption is:


* : The Plaintext
* : The output of the block cipher decryption (The "Intermediate State")
* : The Initialization Vector

**The Vulnerability:**
Since you don't know the Key (), you cannot calculate or change . However, you *do not need to*. You know that  is a constant value as long as the ciphertext () remains untouched.

Because of the XOR operation, any change you make to the  propagates directly to  at the exact same bit position.

Therefore, you can mathematically force  to become whatever 16-byte value you want by adjusting the .

### The Process (The Calculation)

You need to construct a new IV () that, when XORed with the constant intermediate state, produces your target plaintext ().

The formula to generate your forged IV is:

#### Step-by-Step Implementation:

1. **Prepare your Data:** Ensure you have the 16 bytes of , 16 bytes of  (the original text), and define your 16 bytes of  (what you want the text to say).
2. **Calculate the XOR Difference:** Find the "difference" between the text you have and the text you want.


3. **Apply to IV:** XOR that difference into the original IV.



*(Note: You do this byte-by-byte for all 16 bytes).*
4. **Submit:** Send your **** and the **original ** to the server.

### Example Walkthrough (First Byte)

Imagine the first byte of the original plaintext is 'A' (0x41) and you want it to be 'Z' (0x5A).

1. **Plaintext XOR:**  (This is the flip required).
2. **Modify IV:** Take the first byte of the original IV (say it was 0x05) and XOR it with the flip.


3. **Result:** The first byte of your  is 0x1E. When the server decrypts, that byte will resolve to 'Z'.

Would you like a Python snippet to perform this byte-by-byte XOR calculation for you?
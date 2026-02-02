

public class BytecodeSolver {

    public static void main(String[] args) {
        // 1. Calculate the Target from the constants in the bytecode
        // Constant #3 (-889275714) XOR Constant #2 (525024598)
        int target = -889275714 ^ 525024598; 
        
        System.out.println("Target Value: " + target);

        // 2. Solve for 'input' bit by bit
        // Equation: input ^ (input << 3) = target
        int input = 0;

        for (int i = 0; i < 32; i++) {
            // Get the bit at position i from the target
            int targetBit = (target >> i) & 1;
            
            // Get the bit from (input << 3) at position i.
            // This is simply the input bit at position (i-3).
            // If i < 3, the shifted value contributes 0.
            int shiftedBit = (i >= 3) ? ((input >> (i - 3)) & 1) : 0;

            // Logic: targetBit = inputBit ^ shiftedBit
            // Therefore: inputBit = targetBit ^ shiftedBit
            int inputBit = targetBit ^ shiftedBit;

            // Set the calculated bit in our result 'input' variable
            if (inputBit == 1) {
                input |= (1 << i);
            }
        }

        System.out.println("Found Input: " + input);

        // 3. Verify the result using the original logic
        boolean check = checkNum(input);
        System.out.println("Verification Passed? " + check);
    }

    // This is the reconstructed original method for verification
    public static boolean checkNum(int input) {
        int v1 = input << 3;
        int v2 = input ^ 525024598;
        return (v1 ^ v2) == -889275714;
    }
}
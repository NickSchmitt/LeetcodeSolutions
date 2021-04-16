class Solution {
    public int minSwaps(int[] data) {
        
        /*
        The answer is equal to the number of zeroes in the window with the most ones, 
        where the window size being the number of ones.
        */
        
        // calculate window size
        int window = 0;
        for (int i : data){
            window += i;
        }
        
        int currentOnes = 0;
        int maxOnes = 0;
        
        
        for (int i = 0; i<data.length; i++){
            currentOnes += data[i];
            // Shift the window rightwards by removing data of the leftmost index.
            if (i >= window){
                currentOnes -= data[i-window];
            }
            // Compare window shifts and store the max
            maxOnes = Math.max(maxOnes, currentOnes);
        }
        // Return the number of zeroes
        return window - maxOnes;
    }
}
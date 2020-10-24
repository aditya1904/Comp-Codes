import java.util.Arrays;
//https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3506/

class BagOfTokens {
    public int bagOfTokensScore(int[] tokens, int P) {
        int head = 0;
        int tail = tokens.length - 1;
        int S = 0;
        int max_S = S;
        Arrays.sort(tokens);
        
        while (head <= tail){
            if ( P >= tokens[head] ) {
                P = P - tokens[head];
                S += 1;
                if (S > max_S) {
                    max_S = S;
                }
                head += 1;
            } else if (P < tokens[head] && S>=1) {
                P = P + tokens[tail];
                S -= 1;
                tail -= 1;
            } else {
                head +=1;
            }
        }
        return max_S;
        
    }
}
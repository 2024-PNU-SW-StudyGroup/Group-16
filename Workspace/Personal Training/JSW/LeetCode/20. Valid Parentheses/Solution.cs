public class Solution {
    public bool IsValid(string s) {
        char[] stack = new char[s.Length];
        int IDX = 0;
        foreach(char c in s) {
            if (c == '(' || c == '[' || c == '{') stack[IDX++] = c;
            else {
                if (IDX == 0) return false;
                if (!(c == ')' && stack[IDX-1] == '(' ||
                     c == ']' && stack[IDX-1] == '[' ||
                     c == '}' && stack[IDX-1] == '{')) return false;
                
                IDX--;
            }
        }

        return IDX == 0 ? true : false;
    }
}
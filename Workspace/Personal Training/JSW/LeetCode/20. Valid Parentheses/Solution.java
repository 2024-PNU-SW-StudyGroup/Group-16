class Solution {
    public boolean isValid(String s) {
        char[] charArray = s.toCharArray();
        char[] stack = new char[charArray.length];
        int index = 0;
        for(char c : charArray) {
            if (c == '(' || c == '[' || c == '{') {
                stack[index++] = c;
            }
            else {
                if (index == 0) return false;
                if (stack[index-1] == '(' && c == ')'
                || stack[index-1] == '[' && c == ']'
                || stack[index-1] == '{' && c == '}') {
                    index--;
                }
                else return false;
            }
        }

        return index == 0 ? true : false;
    }
}

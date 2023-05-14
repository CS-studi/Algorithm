class Solution {
    private static final int[] keys = new int[] {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    private static final String[] values = new String[] {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

    public String intToRoman(int num) {
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < 13; i++) {
            if (num >= keys[i]) {
                int count = num / keys[i];
                for (int j = 0; j < count; j++) {
                    builder.append(values[i]);
                }
                num -= count * keys[i];
            }
        }
        return builder.toString();
    }
}
class Solution {
    public String intToRoman(int num) {
        // 1 <= num <= 3999
        String ans = "";
        ArrayList<Integer> nums = new ArrayList<Integer>(Arrays.asList(1000,900, 500, 400, 100, 90 , 50, 40, 10, 9, 5, 4, 1));
        Map<Integer, String> roman = new HashMap<>();
        roman.put( 1000, "M");
        roman.put( 900, "CM" );
        roman.put(500, "D" );
        roman.put(400, "CD" );
        roman.put(100, "C" );
        roman.put(90, "XC");
        roman.put(50, "L");
        roman.put(40, "XL");
        roman.put(10, "X");
        roman.put(9, "IX");
        roman.put(5, "V");
        roman.put(4, "IV");
        roman.put(1, "I");
            
        
        
        for (int i = 0; i < 13; i++) {
            while (num >= nums.get(i)) {
                ans = ans.concat(roman.get(nums.get(i)));
                num -= nums.get(i);
            }
        }
        
        return ans;

        
    }
}
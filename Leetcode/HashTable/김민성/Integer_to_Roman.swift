class Solution {
    // 예외 6가지
    private let values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    private let symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    func intToRoman(_ num: Int) -> String {
        var roman: String = ""
        var num = num

         while num > 0 {
             for (i, d) in values.enumerated() where num - d >= 0 {
                 num -= d
                 roman += symbols[i]
                 break
             }
         }

         return roman
    }
}

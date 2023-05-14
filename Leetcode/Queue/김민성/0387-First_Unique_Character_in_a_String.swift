//
//  0387-First_Unique_Character_in_a_String.swift
//  algo
//
//  Created by MIN SEONG KIM on 2023/04/02.
//

import Foundation

class Solution {
    func firstUniqChar(_ s: String) -> Int {
        var dict = Dictionary(s.map { ($0, 1) }, uniquingKeysWith: +)
        for (index, char) in s.enumerated() {
            if dict[char] == 1 {
                return index
            }
        }
        return -1
    }
}


class Solution {
    func firstUniqChar(_ s: String) -> Int {
        var chars=[Character](s)
        for i in 0..<chars.count{
            var flag=true
            for j in 0..<chars.count where i != j{
                if chars[i]==chars[j]{
                    flag=false
                    break
                }
            }
            if flag {
                return i
            }
        }
        return -1
    }
}

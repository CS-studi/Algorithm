//
//  0144-binary-tree-preorder-traversal.swift
//  algo
//
//  Created by MIN SEONG KIM on 2023/03/26.
//

import Foundation


// Definition for a binary tree node.
public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil; }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}
 
class Solution {
   func preorderTraversal(_ root: TreeNode?) -> [Int] {
        guard let root = root else {
            return []
        }
        var preOrderOutput = [Int]()
        var stack = [TreeNode]()
        stack.append(root)
        
        while !stack.isEmpty {
            let node = stack.removeLast()
            preOrderOutput.append(node.val)
            if let rightNode = node.right {
                stack.append(rightNode)
            }
            if let leftNode = node.left {
                stack.append(leftNode)
            }
        }
        return preOrderOutput
    }
}

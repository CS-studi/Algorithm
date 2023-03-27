/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private List<Integer> lst = new ArrayList<>();

    public List<Integer> preorderTraversal(TreeNode root) {
        if(root == null)
            return lst;
        lst.add(root.val);
        preorderTraversal(root.left);
        preorderTraversal(root.right);
        return lst;
    }
}
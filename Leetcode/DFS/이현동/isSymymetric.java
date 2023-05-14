class Solution {
    private boolean isEquivalent(TreeNode left, TreeNode right) {
        if (left==null || right==null) return left == right; // 둘중에 하나 널이라면 둘다 널이어야 함. + null check
        else return left.val == right.val && isEquivalent(left.left, right.right) && isEquivalent(left.right, right.left); // 오른쪽 왼쪽 값이 같고, 왼쪽자식의 온쪽과 오른쪽의 오른쪽, 모두 대칭이어야하는 조건
    }

    public boolean isSymmetric(TreeNode root) {
        return isEquivalent(root.left, root.right);
    }
}
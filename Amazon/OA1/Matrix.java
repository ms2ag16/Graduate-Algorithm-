public class Matrix {
	
	public static int matrixSum(int[][] matrix)
    {
        int m = matrix.length;
        int n = matrix[0].length;
        int i = 0, j , sum =0;
        while ( i < m) {
            j = 0;
            while ( j < n) {
                sum += matrix[i][j];
                j++;
            }
            i++;
        }
        return sum;
    }
	
	public static void main(String[] args){
	    int[][] a = new int[][] {{1,2,3,4},{5,6,7,8}};
	    System.out.println(matrixSum(a));
	}

}

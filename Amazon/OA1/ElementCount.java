public class ElementCount {
	
	public static int countElement(int[] arr, int n)
    {
        int count = 0, len = arr.length;
        int doubleN = 2*n;
        // change the len and i, change the input type
        for (int i=0; i<len; ){
            if (arr[i]> doubleN){
                count +=1;
            }
            i++;
        }
        
        return count;
    }
	
	public static void main(String[] args){
	    int[] a = new int[] {1,2,3,5,84,56};
	    System.out.println(countElement(a, 50));
	}

}

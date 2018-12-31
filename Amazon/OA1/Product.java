public class Product {
	
	public static int countProduct(int size, int valueofK, int[] priceList)
    {
        if (size == 0)
            return 0;
        int j, count =0;
        // change from valueofK to size
        for (j=0; j < size ; ++j){
            System.out.println(j);
            if (priceList[j]<valueofK)
                count = count +1;
        }
        
        return count;
    }
	
	public static void main(String[] args){
	    int[] a = new int[] {1,2,3,5,84,56};
	    System.out.println(countProduct(6, 50, a));
	}

}

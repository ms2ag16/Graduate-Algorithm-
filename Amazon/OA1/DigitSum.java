public class DigitSum{
    public static int getDigitSumParity(int[] arr){
        int min = getMin(arr);
        //System.out.println(min);
        int result = getSum(min);
        //System.out.println(result);
        if (result == 0){
            // change here from 0 to 1
            return 1;
        }
        if (result % 2 ==0){
            return 1;
        }else {
            return 0;
        }
    }
    
    public static int getMin(int[] arr){
        if (arr == null || arr.length<=0){
            throw new IllegalArgumentException(
                "Input array should contain at least 1 element.");
        }
        int min = arr[0];
        for (int i=1, len=arr.length; i < len; i++){
            if (arr[i] < min){
                min = arr[i];
            }
        }
        
        return min;
    }
    
    public static int getSum(int num){
        int sum = 0;
        while (num != 0){
            int temp = num % 10;
            // change the order of the senquence
            num = num/10;
            sum = sum + temp;
        }
        
        return sum;
    }

    public static void main(String []args){
        int [] myIntArray = new int [] {123,45,46,23,97};
        System.out.println(getDigitSumParity(myIntArray));
    }
}

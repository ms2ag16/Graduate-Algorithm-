import java.util.Arrays;

public class Distinct{
    public static int sumDistinct(int size, int[] inputArray){
        int sum = inputArray[0];
        Arrays.sort(inputArray);
        int point = inputArray[0];
        // change the i < size to i < size -1
        for (int i=1; i < size-1; i++){
            if (point != inputArray[i]){
                sum += inputArray[i];
                point = inputArray[i];
            }
            System.out.println(sum);
            System.out.println(point);
        }
        
        return sum;
    }
    
    public static void main(String []args){
        int [] myIntArray = new int [] {123,45,46,23,97};
        int size = 5;
        System.out.println(sumDistinct(size, myIntArray));
    }
}

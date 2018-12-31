import java.util.Arrays;

public class Distinct{
    public static int sumDistinct(int size, int[] inputArray){
        int sum = inputArray[0];
        Arrays.sort(inputArray);
        int point = inputArray[0];
        if (size != inputArray.length){
            size = inputArray.length;
        }
        for (int i=1; i < size; i++){
            if (point != inputArray[i]){
                System.out.println(i);
                sum += inputArray[i];
                point = inputArray[i];
            }
            System.out.println(sum);
            System.out.println(point);
        }
        
        return sum;
    }
    
    public static void main(String []args){
        int [] myIntArray = new int [] {10,20,30,40,50};
        int size = 4;
        System.out.println(sumDistinct(size, myIntArray));
    }
}

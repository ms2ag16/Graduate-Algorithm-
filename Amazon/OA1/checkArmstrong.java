public class CheckArmstrong {
	
	public static int checkArmstrong(int num)
    {
        int digitCount=0, result=0; 
        // calculate number of digits
        int temp = num;  
        while (temp != 0)
        {      
            temp = temp/10;
            digitCount++;
        }
        // digitCount++;

        // sum digits to nth power
        temp = num;
        
        while (temp != 0)
        {
            int remainder = temp%10;
            result += Math.pow(remainder, digitCount);
            temp /= 10;
        }
        if(result == num)
            return 1;
        else
            return 0;
    }
	
	public static void main(String[] args) {
		System.out.println(checkArmstrong(371));
		System.out.println(checkArmstrong(153));
		System.out.println(checkArmstrong(1));
		System.out.println(checkArmstrong(2));
		System.out.println(checkArmstrong(154));
		System.out.println(checkArmstrong(360));

	}

}

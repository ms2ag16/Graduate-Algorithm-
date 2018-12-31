import java.util.Arrays;

public class Array {
	public static int[] sortArray(int arr[]) {
		int len = arr.length;
		int small, pos, i, j, temp;
		for (i = 0; i <= len - 1; i++) {
			for (j = i; j < len; j++) {
				temp = 0;
				if (arr[i] < arr[j]) {
					temp = arr[i];
					arr[i] = arr[j];
					arr[j] = temp;
				}
			}
		}
		return arr;
	}
	
	public static void main(String[] args) {
		int[] arr = new int[] {20, 2, 3, 5, 9, 6, 16};
		int[] sorted = sortArray(arr);
		System.out.println(Arrays.toString(sorted));

	}

}

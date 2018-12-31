public class ArraySort {
	
	public static int[] sortArray(int arr[]) {
		int i, max, location, j, temp, len = arr.length;
		for (i = 0; i < len; i++) {
			max = arr[i];
			location = i;
			for (j = i; j < len; j++) {
				if (max < arr[j]) {
					max = arr[j];
					location = j;
				}
			}
			temp = arr[i];
			arr[i] = arr[location];
			arr[location] = temp;
		}
		return arr;
	}
	
	public static void main(String[] args) {
		int[] arr = new int[] {20, 2, 3, 5, 9, 6, 16};
		int[] sorted = sortArray(arr);
		for (int x : sorted) {
			System.out.print(x + " ");
		}
		System.out.println();
	}
	
}

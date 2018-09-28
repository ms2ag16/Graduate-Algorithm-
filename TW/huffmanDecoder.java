import java.util.HashMap;
import java.util.Map;

public class HuffmanDecoder{
	
	private static String huffmanDecoder(String[] decoder, String str){
		if (str==null || str.length()==0) return null;
		
		Map<String, String> dMap = new HashMap<> ();
		for (int i =0; i < decoder.length; i++){
			String[] word=decoder[i].split(" ");
			if (word[0].equals("newline")) {
				 dMap.put(word[1], "\n");
			}else {
				dMap.put(word[1], word[0]);
			}
		}
		
		// initialize the result
		StringBuilder res = new StringBuilder();
		
		// loop the input string
		int start=0;
		int end=1;
		while (start< str.length() && end<=str.length()){
			String subString=str.substring(start, end);
			if (dMap.containsKey(subString)){
				// in the hashmap
				res.append(dMap.get(subString));
				start=end;
				end=start+1;
			} else {
				end++;
			}
		}
		
		return res.toString();
	}
	
	    public static void main(String[] args) {
        String[] dict = {"a 100100", "b 100101", "c 110001", "d 100000", "newline 1111111", "p 111110", "q 000001"};
        String input = "1111100000011001001111111100101110001100000";
        System.out.print(huffmanDecoder(dict, input));
    }

	
}

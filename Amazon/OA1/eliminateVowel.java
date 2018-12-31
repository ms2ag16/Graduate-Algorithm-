public class EliminateVowel {
	
	public static String eliminateVowel(String str)
    {
        String newString  = "";
        int i=0;
        char[] S = str.toCharArray();
        int len = str.length();
        if(len == 0)
        {
            return "";
        }
        
        
        while (i < S.length)
        {
            switch(S[i])
            {   case 'a':i++;
                    break;
                case 'e': i++;
                    break;
                case 'i': i++;
                    break;
                case 'o': i++;
                    break;
                case 'u': i++;
                    break;
                case 'A': i++;
                    break;
                case 'E': i++;
                    break;
                case 'U': i++;
                    break;
                case 'I': i++;
                    break;
                case 'O': i++;
                    break;
                default:
                    newString +=S[i];
                    i++;
            }
        }        
        return newString;
    }

	public static void main(String[] args) {
		System.out.println(eliminateVowel("absasewrb"));

	}

}

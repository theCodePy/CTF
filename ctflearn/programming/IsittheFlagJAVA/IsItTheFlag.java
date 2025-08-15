public class IsItTheFlag {

public static boolean isFlag(String str) {
	return str.hashCode() == 1471587914 && str.toLowerCase().hashCode() == 1472541258;
}

public static String bruteLowerCase(){
	String table = "abcdefghijklmnopqrstuvwxyz1234567890";
	String password ;

	for (int a=0; a<36; a++){
		for (int b=0; b<36; b++){
			for (int c=0; c<36; c++){
				for (int d=0; d<36; d++){
					for (int e=0; e<36; e++){
						for (int f=0; f<36; f++){
							password  = "" + table.charAt(a) + table.charAt(b) + table.charAt(c) + table.charAt(d) + table.charAt(e) + table.charAt(f);
							if (password.hashCode() == 1472541258){
								System.out.println("found password");
								System.out.println(password);
								return password;
							}
						}
					}
				}
			}
		}
	}
	return "not found";
}

public static String bruteUpperCase(){
	String table = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	String password;
	for (int a=0; a<2; a++){
		for (int b=0; b<2; b++){
			for (int c=0; c<2; c++){
				for (int d=0; d<2; d++){
					for (int e=0; e<2; e++){
						char A, B, C, D, E;
						if (a==0)
							A = 'G';
						else 
							A = 'g';
						if (b==0)
							B = 'H';
						else
							B = 'h';
						if (c==0)
							C = 'Z';
						else
							C = 'z';
						if (d==0)
							D = 'X';
						else
							D = 'x';
						if (e==0)
							E = 'Y';
						else
							E = 'y';
						password = "0" + A + B + C + D + E ;
						if (password.hashCode()==1471587914){
							System.out.println("found password : " + password);
							return password;
						}
					}
				}
			}
		}
	}
	return "not found";
}

public static void main(String[] args) {

	String flag = "------";
	// String lowerCaseFlag = bruteLowerCase();
	flag = "0ghzxy";
	flag = bruteUpperCase();

	if (isFlag(flag))
		System.out.println("You found it!");
	else
		System.out.println("Try again :(");
	

	}
}


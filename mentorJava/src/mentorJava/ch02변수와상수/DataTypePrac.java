package mentorJava.ch02변수와상수;

public class DataTypePrac {

	public static void main(String[] args) {
		byte a = 127; //byte가 가질 수 있는 최댓값
		
		int b = a; //자동형변환 : byte -> int
		System.out.println(b);
		
		float c = b; //자동형변환 : int -> float
		System.out.println(c);
		
		
		int d = 263;
		System.out.println(d);
		
		byte e = (byte)d; //명시적 형변환
		System.out.println(e);
	}
}
